# 搜索 num一次搜索数量
import requests

from apis import api


def search(text, num=10):
    res = []
    url = api["search"].format(text, int(num))
    response = requests.get(url)

    if response.status_code == 200:
        body = response.json()
        list = body["data"]["song"]["list"]
        for item in list:
            f = item["f"]
            f_list = f.split("|")
            # 歌曲ID
            song_id = f_list[0]
            # 歌曲名
            song_name = f_list[1]
            # 歌手
            singer_name = f_list[3]
            # 专辑图片ID 用于获取图片
            album_picture_id = f_list[4]
            # 添加到Json
            res.append({
                "song_id": song_id,
                "song_name": song_name,
                "singer_name": singer_name,
                "album_picture_id": album_picture_id
            })
    return res


# 获取歌曲信息
def get_song_info(search_result_list, index):
    list = search_result_list
    return list[index]
