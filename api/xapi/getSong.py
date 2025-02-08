# 获取Songmid
import json
import os

import requests

from api.api.js.getSign import generate_request
from api.apis import api, headers


def get_songmid(songid):
    url = api["get_songmid"].format(str(songid))
    response = requests.get(url)
    if response.status_code == 200:
        body = response.json()
        mid = body["data"][0]["mid"]
        return mid
    else:
        return None




# 得到播放链接
def get_song_url(songmid):
    post_raw = generate_request(songmid)

    from api.api.js.getSign import get_sign
    sign = get_sign(post_raw)

    url = api["get_song_url"].format(sign)
    # 调试用
    print("url=" + url)

    response = requests.post(url, headers=headers, data=post_raw)

    print("code=" + str(response.status_code) + "body=" + response.text)

    if response.status_code == 200 and "data" in response.text:
        body = response.json()
        song_url = body["req_4"]["data"]["midurlinfo"][0]["purl"]
        # 拼接字符串
        return api["play_on"] + song_url
    else:
        return None




