from api import api, headers
import requests
import re


def get_person_info():
    url = api["get_person_info"]
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return None


def get_person_name():
    json = get_person_info()["creator"]
    name = json["nick"]  # 昵称
    picture_url = json["headpic"]  # 头像
    return {
        "name": name,
        "pictureUrl": picture_url
    }


def get_lists():
    json = get_person_info()
    my_like = json["mymusic"][0]
    my_list = json["mydiss"]["list"]
    list = []

    # 喜欢的id与歌单获取有所不同："ADTAG=profile_h5&id=XXX"
    like_id = my_like["music_bykey"]["url_params"]
    match = re.search(r'id=(\d+)', like_id)
    if match:
        like_id = match.group(1)
    else:
        like_id = None

    like_picture_url = my_like["picurl"]
    like_title = my_like["title"]
    like_remark = my_like["subtitle"]
    list.append({
        "id": like_id,
        "title": like_picture_url,
        "remark": like_title,
        "pictureUrl": like_remark
    })
    # 遍历歌单
    for item in my_list:
        diss_id = item["dissid"]
        picture_url = item["picurl"]
        title = item["title"]
        remark = item["subtitle"]
        res = {
            "id": diss_id,
            "title": title,
            "remark": remark,
            "pictureUrl": picture_url
        }
        list.append(res)
    return list


# 插入歌单id到要POST的JSON中
def get_post_json(list_id, begin_num=0, num=30):
    data = {
        "comm": {
            "g_tk": 838510852,
            "uin": 3404728391,
            "format": "json",
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "platform": "h5",
            "needNewCode": 1
        },
        "req_0": {
            "module": "music.srfDissInfo.aiDissInfo",
            "method": "uniform_get_Dissinfo",
            "param": {
                "disstid": list_id,
                "enc_host_uin": "",
                "tag": 1,
                "userinfo": 1,
                "song_begin": begin_num,
                "song_num": num
            }
        }
    }
    return data


# 获取歌单 如果自己的歌单不对外公开，使用isOwn=true代表是自己查看 自动带上Cookie
def get_lists_songs(list_id, begin_num=0, num=30, isOwn=False):
    url = api["get_lists"]
    post_raw = get_post_json(list_id, begin_num, num)

    if isOwn:
        h = headers
    else:
        h = {}
    # 添加手机UA 否则收不到数据
    h["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/129.0.2792.84 Version/16.0 Mobile/15E148 Safari/604.1"

    response = requests.post(url=url, json=post_raw, headers=h)

    song_list = []

    if response.status_code == 200 and "req_0" in response.text:
        items = response.json().get("req_0", {}).get("data", {}).get("songlist", [])

        for item in items:
            song_id = item.get("id")
            song_mid = item.get("mid")
            song_name = item.get("title")
            song_remark = item.get("subtitle")

            # 解析歌手信息
            song_singers_list = item.get("singer", [])
            singer_list = [
                singer.get("title") if isinstance(singer, dict) else None
                for singer in song_singers_list
            ]

            # 解析专辑信息
            song_album = item.get("album", {})
            song_album_name = song_album.get("title") if isinstance(song_album, dict) else None

            # 构建歌曲信息字典
            res = {
                "id": song_id,
                "mid": song_mid,
                "name": song_name,
                "album": song_album_name,
                "remark": song_remark,
                "singer": singer_list
            }
            song_list.append(res)

    return song_list

# 本地测试
# l = get_person_name()["name"]
# get_person_info()
# l = get_lists()
# print(l)
#l = get_lists_songs(8409375066,0,30,isOwn=True)
#print(l)
