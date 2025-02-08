import requests

from main.api.getLyrics import save_lyrics
from main.api.getSong import get_songmid, get_song_url
from main.api.search import search, get_song_info


# 本地测试函数 如果部署在服务端，前端只需要用get_song_url拿到URL自己处理
def save_song(url, song_name):
    filename = "download/{}.m4a".format(song_name)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 以二进制写入的方式保存文件
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # 过滤掉保持活动的空块
                    file.write(chunk)
        print(f"音乐保存为 {filename}")
    else:
        print("音乐获取失败")


# 以下为搜索测试

search_text = str(input("输入搜索内容 "))
search_result = search(search_text, 15)

print("索引号 | 歌曲 | 歌手")
for index, item in enumerate(search_result):
    song_name = item["song_name"]
    singer_name = item["singer_name"]
    print("{} | {} | {}".format(str(index), song_name, singer_name))

index = int(input("输入要听的音乐索引号 "))
res = get_song_info(search_result, index)

song_id = res["song_id"]
song_name = res["song_name"]
singer_name = res["singer_name"]
filename = "{}-{}".format(song_name, singer_name)
songmid = get_songmid(song_id)

if songmid != None:
    url = get_song_url(songmid)
    if url != None:
        save_song(url, filename)
        save_lyrics(songmid, filename)
    else:
        print("获取URL失败")
else:
    print("获取songmid失败")
