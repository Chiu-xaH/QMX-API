from api import api
import requests

headers = {
    "Referer" : "https://y.qq.com/portal/player.html"
}

# 获取歌词
def get_lyrics(songmid) :
    url = api["get_lyrics"].format(str(songmid))
    response = requests.get(url,headers=headers)
    if(response.status_code == 200) :
        data = response.json()["lyric"]
        return data
    else : 
        return None

# 保存歌词到文件
def save_lyrics(songmid,song_name) :
    filename = "download/{}.lrc".format(song_name)
    lyrics = get_lyrics(songmid)
    if lyrics:
        with open(filename,"w",encoding="utf-8") as file:
            file.write(lyrics)
        print(f"歌词保存为{filename}")
    else:
        print("歌词保存失败")