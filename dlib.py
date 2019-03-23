#!/usr/bin/env python3
# encoding: utf-8
import json
import requests
import urllib3
from time import time
from urllib.parse import unquote_plus
from settings import API_EP_DOUYIN, ROUTE_SIGN_DOUYIN

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_original_url(action, args_dict, ts, device_info):
    install_id = device_info['install_id']
    device_id = device_info['device_id']
    uuid = device_info['uuid']
    openudid = device_info['openudid']
    args = ""
    # print(args_dict)
    for (idx, val) in args_dict.items():
        args += "&{0}={1}".format(idx, val)

    url = "https://aweme.snssdk.com/aweme/" + action + "/?" \
          + args \
          + "&retry_type=no_retry&" \
          + "iid=" + str(install_id) \
          + "&device_id=" + str(device_id) \
          + "&uuid=" + str(uuid) \
          + "&openudid=" + str(openudid) \
          + "&ts=" + str(ts) \
          + "&ac=wifi&channel=wandoujia_zhiwei&aid=1128&app_name=aweme&" \
            "version_code=290&version_name=2.9.0&device_platform=android&" \
            "ssmix=a&device_type=ONEPLUS+A5000&device_brand=OnePlus&language=zh&" \
            "os_api=28&os_version=9&manifest_version_code=290&resolution=1080*1920&" \
            "dpi=420&update_version_code=2902&_rticket=1548672388498"
    return url

def get_signed_url(action, args, ts, device_info, token=""):
    original_url = get_original_url(action, args, ts, device_info)
    return sign(original_url, token=token)

def sign(original_url, token=""):
    data = {"url": original_url}
    try:
        data = api_service(token=token, route=ROUTE_SIGN_DOUYIN, method="post", data=json.dumps(data))
        # cc = json.loads(data)
        # print(cc)
        return data.get("url")
    except Exception as e:
        print(e)

def api_douyin(action, args, ts, device_info, token="",proxy=None):
    try:
        url = get_signed_url(action, args, ts, device_info, token=token)
        resp = requests.get(url=url,
                            headers={
                                "User-Agent": "okhttp/3.10.0.1"},
                            verify=False,
                            cookies={'install_id': str(device_info['install_id'])},
                            proxies=proxy)
        content = resp.content.decode("utf-8")
        d = json.loads(content)
        return d
    except Exception as e:
        print(e)

def api_service(route, token="", method="get", data=None, content_type="application/json",proxy=None):
    resp = requests.request(method=method, url="{0}/{1}/{2}".format(API_EP_DOUYIN, route, token), data=data,
                            headers={"Content-Type": content_type}, verify=False,proxies=proxy)
    if token != "" and resp.headers.get("x-token") != token:
        raise Exception(resp.headers.get("x-token"))
    elif resp.headers.get("x-token-times") == "0":
        raise Exception(resp.content)
    data = resp.content.decode("utf-8")
    return json.loads(data)

def wrap_api(action, args, device_info={}, token="",proxy=None):
    try:
        ts = str(int(time()))
        data = api_douyin(action, args, ts, device_info, token=token,proxy=proxy)
        return data
    except Exception as e:
        print(e)

def request_dict(req):
    params = req.split("?")[1]
    lp = params.split('&')
    di = {}
    for e in lp:
        k, v = e.split('=')
        di[k] = unquote_plus(v)
    return dict(di)
