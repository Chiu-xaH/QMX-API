# 获取Songmid
import requests

from api import api, headers


def get_songmid(songid):
    url = api["get_songmid"].format(str(songid))
    response = requests.get(url)
    if response.status_code == 200:
        body = response.json()
        mid = body["data"][0]["mid"]
        return mid
    else:
        return None


# 将songmid插入到要提交的json中
def get_post_raw(songmid):
    data = f'{{"comm":{{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505015329090","g_tk_new_20200303":1615368207,"g_tk":1615368207}},"req_4":{{"module":"music.vkey.GetVkey","method":"GetUrl","param":{{"guid":"8786979254","songmid":["{songmid}"],"songtype":[0],"uin":"1152921505015329090","loginflag":1,"platform":"20"}}}}}}'
    return data

# 得到播放链接
def get_song_url(songmid):
    from getSign import get_sign
    sign = get_sign(songmid)
    post_raw = get_post_raw(songmid)

    url = api["get_song_url"].format(sign)
    response = requests.post(url, headers=headers, data=post_raw)
    if response.status_code == 200 and "data" in response.text:
        body = response.json()
        song_url = body["req_4"]["data"]["midurlinfo"][0]["purl"]
        # 拼接字符串
        return api["play_on"] + song_url
    else:
        return None
