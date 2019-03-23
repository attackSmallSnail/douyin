#coding:utf-8
import re
import time

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

def together(*args,sep='-'):
    return sep.join([str(i) for i in args if i])

def from_pattern(pattern,text):
    res = re.findall(pattern,text)
    if res:
        return res[0]

def cookie_str_to_dict(cookie_str):
    seps = cookie_str.split(';')
    _dict = {i.split('=')[0]:i.split('=')[1] for i in seps}
    for i in _dict.items():
        yield {'name': i[0].strip(), 'value': i[1].strip()}

def time_to_date(timestamp):
    """
    时间戳转换为日期
    :param timestamp : 时间戳，int类型，如：1537535021
    :return:转换结果日期，格式： 年-月-日 时:分:秒
    """
    timearr = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return  otherStyleTime

def date_to_time(date):
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    _str = int(f'{timeStamp}000')
    return _str