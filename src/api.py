import json
import re

api = {
    # 搜索 获取ID
    "search": "https://c.y.qq.com/soso/fcgi-bin/music_search_new_platform?format=json&w={}&n={}",
    # 获取专辑封面
    "get_album_picture": "http://imgcache.qq.com/music/photo/album_300/{}/300_albumpic_{}_0.jpg",
    # 获取专辑封面2
    "get_album_picture_2": "https://y.gtimg.cn/music/photo_new/T002R300x300M000{}.jpg",
    # 获取songmid
    "get_songmid": "https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songid={}&tpl=yqq_song_detail&format=json",
    # 获取播放链接req4 获取歌单歌曲及其歌单一些信息re15
    "get_song_url": "https://u6.y.qq.com/cgi-bin/musics.fcg?sign={}",
    # 用于播放链接前缀
    "play_on": "https://ws6.stream.qqmusic.qq.com/",
    # 获取歌词
    "get_lyrics": "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?songmid={}&format=json&nobase64=1",
    # 获取个人歌单
    "get_person_info": "https://c6.y.qq.com/rsc/fcgi-bin/fcg_get_profile_homepage.fcg?format=json&cid=205360838&reqfrom=1",
    # 获取某一个歌单里的歌曲 #刷新登录
    "get_lists": "https://u.y.qq.com/cgi-bin/musicu.fcg"
}


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        string = file.read()
        return string


config_file_name = "./config.txt"
content = read(config_file_name)
match = re.search(r'COOKIE\s*=\s*"([^"]+)"', content)
cookie = ""
if match:
    cookie = match.group(1)
else:
    print("cookie格式有误")

cookie = str(cookie).replace("\n", "").strip()


cookies = cookie.split("; ")

# 转换为字典
cookie_dict = {}
for item in cookies:
    if "=" in item:  # 检查是否是 key=value 格式
        key, value = item.split("=", 1)  # 按等号分割，最多分割一次
        cookie_dict[key] = value  # 保留最后一次出现的值


def read_cookie():
    with open("cookie.json", "r", encoding="utf-8") as file:
        file_json = json.load(file)
    return file_json


def init_cookie_json(cookie_dict):
    file_json = read_cookie()

    file_json["cookie"]["qqmusic_key"] = cookie_dict["qqmusic_key"]
    file_json["cookie"]["qqmusic_uin"] = cookie_dict.get("qqmusic_uin","0")
    file_json["cookie"]["qqmusic_uin"] = cookie_dict.get("uin","o0").lstrip("o")
    file_json["other"]["access_token"] = cookie_dict["psrf_qqaccess_token"]
    file_json["other"]["qqmusic_guid"] = cookie_dict.get("qqmusic_guid")
    file_json["other"]["qqmusic_guid"] = cookie_dict.get("guid")
    file_json["other"]["refresh_token"] = cookie_dict["wxrefresh_token"]
    file_json["other"]["openid"] = cookie_dict["wxopenid"]

    with open("cookie.json", "w", encoding="utf-8") as file:
        json.dump(file_json, file, ensure_ascii=False, indent=4)


init_cookie_json(cookie_dict)

file_json = read_cookie()["cookie"]

headers = {
    # 如果有绿钻，把Cookie放在这里，可以听VIP歌曲
    # SVIP可以听付费歌曲
    "Cookie": "qqmusic_key={}; qqmusic_uin={}".format(file_json["qqmusic_key"],file_json["qqmusic_uin"])
}
