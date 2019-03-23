
API_GET_TOKEN = 'http://sign.vsdouyin.com/api/token/gen/'
API_EP_DOUYIN = "https://sign.vsdouyin.com/api"
API_DEVICE_REGISTER = "https://log.snssdk.com/service/2/device_register/"

#生成签名服务器专用token
ROUTE_GEN_TOKEN = "token/gen"
ROUTE_INFO_TOKEN = "token/info"
# 抖音相关入口
ROUTE_SIGN_DOUYIN = "653d33c/sign"
ROUTE_CRYPT_DOUYIN = "653d33c/crypt"

#操作相关
FEED_OPT = "v1/feed"
USER_INFO_OPT = "v1/user"
USER_FANS_OPT = "v1/user/follower/list"
USER_POSTS_OPT = "v1/aweme/post"
USER_LIKE_OPT = "v1/aweme/favorite"
VIDEO_COMMENTS_OPT = "v1/comment/list"

HEADERS = {
    'Content-Type': 'application/octet-stream;tt-data=a',
    'sdk-version': '1',
    'user-agent': 'okhttp/3.10.0.1',
}