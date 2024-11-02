import re

api = {
    # 搜索 获取ID
    "search": "https://c.y.qq.com/soso/fcgi-bin/music_search_new_platform?format=json&w={}&n={}",
    # 获取专辑封面
    "get_album_picture": "http://imgcache.qq.com/music/photo/album_300/{}/300_albumpic_{}_0.jpg",
    # 获取songmid
    "get_songmid": "https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songid={}&tpl=yqq_song_detail&format=json",
    # 获取播放链接
    "get_song_url": "https://u6.y.qq.com/cgi-bin/musics.fcg?_=1730450550757&sign={}",
    # 用于播放链接前缀
    "play_on": "https://ws6.stream.qqmusic.qq.com/",
    # 获取歌词
    "get_lyrics" : "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?songmid={}&format=json&nobase64=1",
    # 获取个人歌单
    "get_person_info" : "https://c6.y.qq.com/rsc/fcgi-bin/fcg_get_profile_homepage.fcg?format=json&cid=205360838&reqfrom=1",
    # 获取某一个歌单里的歌曲
    "get_lists" : "https://u.y.qq.com/cgi-bin/musicu.fcg"
}

def read(filename):
    with open(filename, 'r',encoding="UTF-8") as file:
        string = file.read()
        return string

config_file_name = "config.txt"
content = read(config_file_name)
match = re.search(r'COOKIE\s*=\s*"([^"]+)"',content)
cookie = ""
if match :
    cookie = match.group(1)
else :
    print("cookie格式有误")

headers = {
    # 如果有绿钻，把Cookie放在这里，可以听VIP歌曲
    # SVIP可以听付费歌曲
    "Cookie": str(cookie).replace("\n", "").strip()
}
