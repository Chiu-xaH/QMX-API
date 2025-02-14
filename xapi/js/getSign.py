# 得到sign
import json
import os
import execjs
import requests

import api.apis


# def get_sign(data):
#     # 通过调用逆向得到的JS代码生成sign
#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     # print(current_dir)
#     js_file_path = os.path.join(current_dir, "main.js")
#     with open(js_file_path, 'r', encoding='utf-8') as f:
#         js_code = f.read()
#
#     ctx = execjs.get("Node").compile(js_code,cwd=current_dir)
#     sign = ctx.call("get_sign",data)
#     return sign


def get_sign_from_vercel(js):
    response = requests.get(url=api.apis.api["vercel_js"],params={
        "data" : js
    })
    if response.status_code == 200:
        return response.json()["sign"]
    else:
        raise Exception(f"Error executing JS: {response.json().get('error')}")


def generate_request(songmid):
    data = {
        "comm": {
            "cv": 4747474,
            "ct": 24,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "yqq.json",
            "needNewCode": 1,
            "uin": "1152921505015329090",
            "g_tk_new_20200303": 946874042,
            "g_tk": 946874042
        },
        "req_4": {
            "module": "music.vkey.GetVkey",
            "method": "GetUrl",
            "param": {
                "guid": "457218200",
                "songmid": [songmid],  # 动态替换 songmid
                "songtype": [0],
                "uin": "1152921505015329090",
                "loginflag": 1,
                "platform": "20"
            }
        }
    }

    # `separators=(',', ':')` 确保没有多余空格
    return json.dumps(data, separators=(',', ':'))

# 将songmid插入到要提交的json中
def get_post_raw(songmid):
    data = f'{{"comm":{{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505015329090","g_tk_new_20200303":946874042,"g_tk":946874042}},"req_4":{{"module":"music.vkey.GetVkey","method":"GetUrl","param":{{"guid":"457218200","songmid":["{songmid}"],"songtype":[0],"uin":"1152921505015329090","loginflag":1,"platform":"20"}}}}}}'
    return data
