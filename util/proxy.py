#coding:utf-8
import re
import os
import random
import requests
from config import *
from w3lib.url import is_url

def  is_proxy_valid(proxy):
    """
    :usage:
    判断给定的代理ip是否符合格式要求:"<ip>:<port>"
    :param data:
    @proxy  : 要判断的代理ip
    :return:
    @result : 符合要求则返回 代理ip，否则为 []
    """
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b\:\d+',proxy)

def gen_proxy(proxy):
    proxy = proxy.strip('\n')
    return {
        'http':f'http://{proxy}',
        'https': f'https://{proxy}',
    }

def get_proxy(api=PROXY_API):
    if not is_url(api):
        if os.path.isfile(api):
            with open(api, 'r') as f:
                p_txt = f.readlines()
            return random.choice([gen_proxy(i) for i in p_txt])
        if isinstance(api, list):
            return random.choice([gen_proxy(i) for i in api])
        return gen_proxy(api)
    else:
        while 1:
            p = requests.get(api).text.strip('\r\n').strip()
            if not is_proxy_valid(p):
                continue
            return gen_proxy(p)

def pop_proxy(api=PROXY_API):
    a = requests.get(api)
    return a.text.strip()



