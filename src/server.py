import flask
from flask import request, jsonify, Response,Blueprint

server = flask.Flask(__name__)

# 创建一个蓝图，并添加前缀 '/qmx/api'
api = Blueprint('api', __name__, url_prefix='/qmx/api')

# 搜索API @GET(text,num)
@server.route('/search', methods=['GET','POST'])
def api_search() :
    from search import search

    text = request.args.get("st")
    num = request.args.get("num",10)

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
@server.route('/getSongmid', methods=['GET'])
def api_get_songmid() :
    from getSong import get_songmid
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
@server.route('/getSongUrl', methods=['GET'])
def api_get_song_url() :
    from getSong import get_song_url
    songmid = request.args.get("songmid")

    if not songmid:
        return jsonify({
            "status": "无songmid",
            "song_url": None
        }), 400

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
@server.route('/getLyrics', methods=['GET'])
def api_get_lyrics() :
    from getLyrics import get_lyrics
    songmid = request.args.get("songmid")

    if not songmid:
        return jsonify({
            "status": "无songmid",
            "songLyrics": None
        }), 400
    
    song_lyrics = get_lyrics(songmid)
    if song_lyrics is not None :
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
@server.route('/getAlbumPicture', methods=['GET'])
def api_get_album_picture() :
    id = request.args.get("id")
    if not id:
        return jsonify({
            "status": "无id",
        }), 400
    
    from getAlubmPicture import get_album_picture
    img = get_album_picture(id)
    if img is not None :
        return Response(img, content_type='image/jpeg')
    else :
        return jsonify({
            "status": "无图片",
        }), 500

# 获取个人信息 @GET()  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@server.route('/getMyInfo', methods=['GET'])
def api_get_my_info() :
    from getPersonInfo import get_person_name
    return get_person_name()


# 获取个人歌单 @GET()  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@server.route('/getMyLists', methods=['GET'])
def api_get_my_list() :
    from getPersonInfo import get_lists
    return get_lists()


# 获取歌单内容 @GET(listid)  如果接口是面向对外使用，就需要重写方法 让用户自己提交Cookie，这里为了方便就用一斤发设定在config.txt的Cookie
@server.route('/getListInfo', methods=['GET'])
def api_get_list_songs() :
    list_id = request.args.get("listId")
    begin_num = request.args.get("begin",0)
    num = request.args.get("num",30)

    if not list_id:
        return jsonify({
            "error": "无id",
        }), 400

    from getPersonInfo import get_lists_songs

    return get_lists_songs(int(list_id),int(begin_num),int(num),True)


server.config['JSON_AS_ASCII'] = False
server.register_blueprint(api)

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)

