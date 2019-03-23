from util.tools import date_to_time
from util.proxy import get_proxy


from douyin import DouYinAPI

if __name__ == '__main__':
    a = DouYinAPI()
    #API初始化
    a.init()
    #从数据库里检测是否有token
    # a.init(db=True)
    #要生成新的token必须使用代理，下面的表示将获取的新的token存进本地文件
    #a.generate_tokens(count=30,path=a.token_file)
    #生成的新的token保存进MongoDB数据库，可以在config中设置数据库
    #下面的表示同时存入数据库和保存进本地硬盘文件路径
    #a.generate_tokens(count=30,path=a.token_file,toDB=True)
    token = a.get_tokens(count=2)[0]
    print("内置token:",a.get_token_info(a.token))
    print('获取的token:',a.get_token_info(token))
    print(f'当前所有可用token {len(a.waiter.tokens)}个:',a.waiter.tokens)
    # 有代理时可以使用代理，在config中设置代理api
    # p = get_proxy()
    # print(p)
    d = a.get_new_device_info(a.token)
    print('新的设备信息:',d)
    c = a.get_feed({'count': 6, 'type': 0, 'max_cursor':date_to_time('2019-03-10 00:00:00'), 'min_cursor': date_to_time('2019-03-09 00:00:00'), 'pull_type':2},device_info=d)
    print('首页推荐:',c)
    # c = a.get_feed({'count': 6, 'type': 0, 'max_cursor': 0, 'min_cursor': -1, 'pull_type': 2},device_info=d)
    # print(len(c),c)
    print('用户ID-110725736365信息:',a.get_user_info('110725736365',device_info=d))
    print('用户ID-110725736365粉丝信息:',a.get_user_fans('110725736365',device_info=d))
    print('用户ID-110725736365发布视频信息:',a.get_user_videos('110725736365',device_info=d))
    print('用户ID-110725736365点赞视频信息:',a.get_user_like('110725736365', device_info=d))
    print('视频ID-6615981222587796743评论信息:',a.get_video_comments('6615981222587796743',device_info=d))