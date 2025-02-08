import json


import requests

from main.apis import api,cookie_file_name

cookie_json = api.read_cookie()


def refresh_login():
    request_body = {
        "WXLoginByToken": {
            "method": "Login",
            "module": "music.login.LoginServer",
            "param": {
                "musicid": int(cookie_json["cookie"]["qqmusic_uin"]),
                "musickey": cookie_json["cookie"]["qqmusic_key"],
                "openid" : cookie_json["other"]["openid"],
                "refresh_token" : cookie_json["other"]["refresh_token"]
            }
        },
        "comm": {
            "guid" : cookie_json["other"]["qqmusic_guid"],
            "tmeLoginType": 1
        }
    }
    response = requests.post(api.api["get_lists"], headers=api.headers, json=request_body)
    if response.status_code == 200 and "data" in response.text:
        data_json = response.json()["WXLoginByToken"]["data"]
        new_music_key = data_json["musickey"]
        # 不为空则写入
        if new_music_key != "" or new_music_key is not None:
            file_json = api.read_cookie()
            file_json["cookie"]["qqmusic_key"] = new_music_key
            with open(cookie_file_name, "w", encoding="utf-8") as file:
                json.dump(file_json, file, ensure_ascii=False, indent=4)
            print("写入成功")
        else:
            print("KEY={}".format(new_music_key))
    else :
        print("失败 " + response.text)
        print("失败 " + str(api.headers))
        print("失败 " + str(request_body))

# 将此文件添加定时任务，刷新TOKEN
refresh_login()
