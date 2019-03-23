
import requests
from util.proxy import get_proxy
from settings import API_GET_TOKEN

def request_token(proxy_api,url=API_GET_TOKEN):
    while 1:
        proxy = get_proxy(proxy_api)
        res = requests.get(url,proxies=proxy)
        try:
            data = res.json()
        except Exception as e:
            print('Error:',res.content)
            continue
        if data:
            return data.get('token')