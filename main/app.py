import os

import flask
from flask import request, jsonify, Response, Blueprint


app = flask.Flask(__name__)

# 创建一个蓝图，并添加前缀 '/qmx/main'
api = Blueprint('main', __name__, url_prefix='/qmx/main')


# 搜索API @GET(text,num)
@app.route('/search', methods=['GET', 'POST'])
def api_search():

    from main.api.search import search

    text = request.args.get("st")
    num = request.args.get("num", 10)

    if not text:
        return jsonify({
            "status": "缺少搜索文本",
            "results": None
        }), 400

    result = search(text, num)
    return jsonify({
        "status": "success",
        "results": result
    })


# 获取songmidAPI @GET(songmid)
@app.route('/getSongmid', methods=['GET'])
def api_get_songmid():
    from main.api.getSong import get_songmid

    songid = request.args.get("songid")

    if not songid:
        return jsonify({
            "status": "无songid",
            "songmid": None
        }), 400

    songmid = get_songmid(songid)
    if songmid is not None:
        return jsonify({
            "status": "success",
            "songmid": songmid
        })
    else:
        return jsonify({
            "status": "无songmid",
            "songmid": None
        }), 500


# 获取听歌链接API @GET(songmid)
@app.route('/getSongUrl', methods=['GET'])
def api_get_song_url():

    songmid = request.args.get("songmid")

    if not songmid:
        return jsonify({
            "status": "无songmid",
            "song_url": None
        }), 400

    from main.api.getSong import get_song_url
    song_url = get_song_url(songmid)
    if song_url is not None:
        return jsonify({
            "status": "success",
            "songUrl": song_url
        })
    else:
        return jsonify({
            "status": "无URL",
            "songUrl": None
        }), 500


# 获取歌词API @GET(songmid)
@app.route('/getLyrics', methods=['GET'])
def api_get_lyrics():
    from main.api.getLyrics import get_lyrics
    songmid = request.args.get("songmid")

    if not songmid:
        return jsonify({
            "status": "无songmid",
            "songLyrics": None
        }), 400

    song_lyrics = get_lyrics(songmid)
    if song_lyrics is not None:
        return jsonify({
            "status": "success",
            "songLyrics": song_lyrics
        })
    else:
        return jsonify({
            "status": "无歌词",
            "songLyrics": None
        }), 500


# 获取专辑封面 @GET(id)
@app.route('/getAlbumPicture', methods=['GET'])
def api_get_album_picture():
    id = request.args.get("id")
    if not id:
        return jsonify({
            "status": "无id",
        }), 400

    from main.api.getAlubmPicture import get_album_picture
    img = get_album_picture(id)
    if img is not None:
        return Response(img, content_type='image/jpeg')
    else:
        return jsonify({
            "status": "无图片",
        }), 500


# 获取专辑封面2 @GET(id)
@app.route('/getAlbumPicture2', methods=['GET'])
def api_get_album_picture_2():
    id = request.args.get("albumMid")
    if not id:
        return jsonify({
            "status": "无albumMid",
        }), 400

    from main.api.getAlubmPicture import get_album_picture_2
    img = get_album_picture_2(id)
    if img is not None:
        return Response(img, content_type='image/jpeg')
    else:
        return jsonify({
            "status": "无图片",
        }), 500


# 获取个人信息 @GET()  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@app.route('/getMyInfo', methods=['GET'])
def api_get_my_info():
    from main.api.getPersonInfo import get_person_name
    return get_person_name()


# 获取个人歌单 @GET()  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@app.route('/getMyLists', methods=['GET'])
def api_get_my_list():
    from main.api.getPersonInfo import get_lists
    return jsonify({
        "status": "success",
        "list": get_lists()
    })


# 获取歌单内容 @GET(listid)  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@app.route('/getListInfo', methods=['GET'])
def api_get_list_songs():
    list_id = request.args.get("listId")
    begin_num = request.args.get("begin", 0)
    num = request.args.get("num", 30)

    if not list_id:
        return jsonify({
            "error": "无id",
        }), 400

    from main.api.getPersonInfo import get_lists_songs

    return jsonify({
        "status": "success",
        "result": get_lists_songs(int(list_id), int(begin_num), int(num))
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
