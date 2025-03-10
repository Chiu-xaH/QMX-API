# API

## @GET /search 检索
### 请求 query参数
st(搜索内容，必选)、num(一次请求数量，默认10，可选)
### 返回 JSON
    { 
        "status": String,
        "results": [
            {
                "song_id": Long,
                "song_name": String,
                "singer_name": String,
                "album_picture_id": Long
            }
        ]?
    }

## @GET /getSongmid 
### query参数
songid(必选，可从search接口中获取)
### 返回 JSON
    { 
        "status": String,
        "songmid": String?
    }

## @GET&POST /getSongUrl
### query参数
songmid(必选，可从getSongmid接口获取)
### 可附带Header Cookie(用于获取会员歌曲)
### 返回 JSON 
    { 
        "status": String,
        "songUrl": String?
    }

## @GET /getAlbumPicture 获取专辑封面
### query参数
id(必选，可从search接口获取)
### 返回 图片img

## @GET /getAlbumPicture2 获取专辑封面（方法2）
### query参数
albumMid(必选，可从search接口或者歌单中获取)
### 返回 图片img

## @GET /getLyrics 获取歌词
歌词解析，使用split分割时间与歌词，按照时间显示歌词即可
### 返回 JSON 
    { 
        "status": String,
        "songLyrics": String?
    }

## @GET /getMyInfo 获取个人信息(如果作为给外界用户使用应废除！)
### 返回 JSON 
    { 
        "name": String,
        "pictureUrl": String? (头像图片)
    }

## @GET /getMyLists 获取个人歌单(包括喜欢)(如果作为给外界用户使用应废除！)
### 返回 JSON 
    {
        "status" : "success",
        "list" : [ 
                    {
                        "id" : Long,
                        "title" : String,
                        "remark" : String,
                        "pictureUrl" : String
                    }
                ]?
    }

## @GET /getListInfo 获取歌单信息（歌单需要非隐私状态） （2.0）
### query参数
listId(必选，可从getMyLists接口中获取)、begin(可选，默认为0，代表从第begin+1首开始)、num(可选，默认为30，代表一次请求的数量)

获取listId方法，QQ音乐分享歌单到微信/QQ，复制链接，里面有id=XXX

如果要翻页，begin需要变为原num+原begin，建议直接传入0和5000，一网打尽
### 返回 JSON 
    {
        "result": {
            "info": {
                "host": {
                    "name": String?,
                    "pictureUrl": String?
                },
                "listenNum": Long 听歌次数,
                "pictureUrl":  String? ,
                "songNum": Long 歌单歌曲总数,
                "title": String?
            },
            "list": [
                {
                    "album": {
                        "id": Long?,
                        "mid": String?,
                        "name": String?
                    },
                    "id": Long?,
                    "mid": String?,
                    "name": String?,
                    "remark": String OST备注,
                    "singer": [
                        {
                            "id": Long?,
                            "mid": String?,
                            "title": String?
                        }
                    ]?
                }
            ]?
        }?,
        "status": "success"
    }
    