# QQ音乐接口
## 目前仅实现听歌 正在写...
## 食用方法
按src/requirements.txt安装所需软件包依赖

运行src/test.py，或者部署到服务器，运行src/server.py
## API
### @GET /search 检索
#### 请求 query参数
st(搜索内容，必选)、num(一次请求数量，默认10，可选)
#### 返回200 JSON
    { 
        status: String,
        results: [
            {
                "song_id": String,
                "song_name": String,
                "singer_name": String,
                "album_picture_id": String
            }
        ]?
    }
### @GET /getSongmid 
#### query参数
songid(必选，可从search接口中获取)
#### 返回200 JSON
    { 
        status: String,
        songmid: String?
    }
### @GET&POST /getSongUrl
#### query参数
songmid(必选，可从getSongmid接口获取)
#### 可附带Header Cookie(用于获取会员歌曲)
#### 返回200 JSON 
    { 
        status: String,
        songUrl: String?
    }
### @GET /getAlbumPicture 获取专辑封面
#### query参数
id(必选，可从search接口获取)
#### 返回200 图片img
### @GET /getLyrics 获取歌词
正在开发