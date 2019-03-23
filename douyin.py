##coding:utf-8
import base64
from dlib import *
from config import *
from settings  import *
from exception import *
from waiter import Waiter
from deco import force_type
from log import getLogger
from util.douyin import gen_device_data
from deco.douyin import choose

logger = getLogger(__name__)

class DouYinAPI:

    def __init__(self,proxy_api=PROXY_API,token_file=TOKEN_FILE,token=API_TOKEN):
        self.token = token
        self.proxy_api = proxy_api
        self.token_file = token_file
        self.waiter = Waiter()

    def init(self,db=False):
        self.waiter._check_token_files(self.token_file)
        if db:
            self.waiter._check_token_table()

    def get_tokens(self,count=1):
        tokens = self.waiter.tokens
        if tokens:
            try:
                return [tokens.pop() for _ in range(count)]
            except KeyError:
                raise TokenSetEmpty('No token in the token set.')
        raise NoTokensGenerated('No tokens found.You should generate some tokens before.')

    def get_token_info(self,token,proxy=None):
        try:
            data = api_service(route=ROUTE_INFO_TOKEN, method="get", token=token,proxy=proxy)
            return data
        except Exception as e:
            logger.error(f"{e.__class__.__name__}:{e}")

    def get_new_device_info(self,token, proxy=None):
        data,device_info = gen_device_data()
        try:
            data = api_service(route=ROUTE_CRYPT_DOUYIN, token=token, method="post",
                               data=json.dumps(data),content_type="application/json",
                               proxy=proxy)
            data = base64.b64decode(data['base64_data'])
            resp = requests.post(API_DEVICE_REGISTER,headers=HEADERS,data=data,proxies=proxy)
            content = resp.content.decode("utf-8")
            new_device = json.loads(content)
            new_device['openudid'] = device_info[0]
            new_device['android_id'] = device_info[1]
            new_device['uuid'] = device_info[2]
            new_device['iid'] = new_device['install_id']
            return new_device
        except Exception as e:
            logger.error(f'{e.__class__.__name__}:{e}')

    @force_type({1:dict})
    @choose('feed')
    def get_feed(self,params,token='',device_info={},proxy=None):
        return params

    @choose('user_info')
    def get_user_info(self,userId,token='',device_info={},proxy=None):
        params = {"user_id": userId}
        return params

    @choose('user_fans')
    def get_user_fans(self,userId,count=20,device_info={},proxy=None):
        params = {"user_id": userId, "count": count, "max_time": str(int(time()))}
        return params

    @choose('user_videos')
    def get_user_videos(self,userId,count=20,device_info={},proxy=None):
        params = {"user_id": userId, "max_cursor": 0, "count": count}
        return params

    @choose('user_like')
    def get_user_like(self,userId,count=20,device_info={},proxy=None):
        params = {"user_id": userId, "max_cursor": 0, "count": count}
        return params

    @choose('video_comments')
    def get_video_comments(self, aweme_id, count=20, device_info={}, proxy=None):
        params = {"aweme_id": aweme_id, "cursor": 0, "count": count}
        return params

    def generate_tokens(self,count=MAX_TOKEN_GETS,toDB=False,
                        tname=MongoDB['tokens'],path=None):
        self.waiter.generate_tokens(self.proxy_api,count,toDB,tname,path)