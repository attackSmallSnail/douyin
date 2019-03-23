
from settings import *
from dlib import wrap_api

OPT_API = {
    'user_info':USER_INFO_OPT,
    'feed':FEED_OPT,
    'user_fans':USER_FANS_OPT,
    'user_videos':USER_POSTS_OPT,
    'user_like':USER_LIKE_OPT,
    'video_comments':VIDEO_COMMENTS_OPT

}

def choose(opt,produce=True):
    def outter(func):
        def wrapper(self,*args,**kwargs):
            if produce:
                params = func(self,*args,**kwargs)
                token = kwargs.get('token')
                if not token:
                    token = self.token
                if not kwargs.get('device_info'):
                    raise ValueError(f'device_info must not be None.')
                res = wrap_api(OPT_API.get(opt),
                                    params,
                                    device_info=kwargs.get('device_info'),
                                    token=token,
                                    proxy=kwargs.get('proxy')
                                    )
            else:
                return func(self,*args,**kwargs)
            return res
        return wrapper
    return outter
