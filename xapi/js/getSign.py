# 得到sign
import json
import os
import execjs


def get_sign(data):
    # 通过调用逆向得到的JS代码生成sign
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # print(current_dir)
    js_file_path = os.path.join(current_dir, "main.js")
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.get("Node").compile(js_code,cwd=current_dir)
    sign = ctx.call("get_sign",data)
    return sign

# def get_sign(data):
#     # 获取当前脚本所在目录
#     current_dir = os.path.dirname(__file__)
#     js_file_path = os.path.join(current_dir,'api.js')
#
#     # 读取 JS 代码
#     with open(js_file_path, 'r', encoding='utf-8') as f:
#         js_code = f.read()
#
#     # 执行 JS 代码并获取 sign
#     ctx = execjs.get("Node").compile(js_code)
#     sign = ctx.call("get_sign", data)
#     return sign
#

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



#
# #
# songmid = "0030kh511IGdpg"
# json_payload = generate_request(songmid)
#

# print(
#     get_sign('{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921505015329090","g_tk_new_20200303":946874042,"g_tk":946874042},"req_4":{"module":"music.vkey.GetVkey","method":"GetUrl","param":{"guid":"457218200","songmid":["0030kh511IGdpg"],"songtype":[0],"uin":"1152921505015329090","loginflag":1,"platform":"20"}}}')
# )
#
#
# print(
#     get_sign(json_payload)
# )
#
# print(
#     get_sign(get_post_raw(songmid))
# )