# QQ音乐接口
## 目前仅实现基础功能 正在写...
## 食用方法
按src/requirements.txt安装所需软件包依赖

在src/config.txt添加Cookie，抓包获取(推荐抓QQ音乐客户端)(可选)

运行src/test.py，或者部署到服务器
(测试环境)
    
    cd ./src
    python server.py
(生产环境)
    
    cd ./src
    gunicorn -w 4 -b 127.0.0.1:5000 server:server
配置Nginx(略)



## API
### @GET /search 检索
#### 请求 query参数
st(搜索内容，必选)、num(一次请求数量，默认10，可选)
#### 返回 JSON
    { 
        "status": String,
        "results": [
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
#### 返回 JSON
    { 
        "status": String,
        "songmid": String?
    }
### @GET&POST /getSongUrl
#### query参数
songmid(必选，可从getSongmid接口获取)
#### 可附带Header Cookie(用于获取会员歌曲)
#### 返回 JSON 
    { 
        "status": String,
        "songUrl": String?
    }
### @GET /getAlbumPicture 获取专辑封面
#### query参数
id(必选，可从search接口获取)
#### 返回 图片img
### @GET /getLyrics 获取歌词
#### 返回 JSON 
    { 
        "status": String,
        "songLyrics": String?
    }
### @GET /getMyInfo 获取个人信息
#### 附带Header Cookie(必选)
#### 返回 JSON 
    { 
        "name": String,
        "pictureUrl": String? (头像图片)
    }
### @GET /getMyLists 获取个人歌单(包括喜欢)
#### 附带Header Cookie(必选)
#### 返回 JSON 
    [ 
        {
            "id" : String,
            "title" : String,
            "remark" : String,
            "pictureUrl" : String
        }
    ]?
### @GET /getListInfo 获取歌单信息 
#### query参数
listId(必选，可从getMyLists接口中获取)、begin(可选，默认为0，代表从第begin+1首开始)、num(可选，默认为30，代表一次请求的数量)

如果要翻页，begin需要变为原num+原begin
#### 附带Header Cookie(可选,如果自己的歌单不对外开放,需要带Cookie以自己的身份访问)
#### 返回 JSON 
    [ 
        {
                "id": String,
                "mid": String,
                "name": String,
                "album": Stringe,
                "remark": String,
                "singer": String
        }
    ]?