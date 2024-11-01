import flask
from flask import request, jsonify

server = flask.Flask(__name__)


# 定义API POST(text,num)
@server.route('/search', methods=['GET','POST'])
def api_search():
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


# 定义API GET(songmid)
@server.route('/getSongmid', methods=['GET'])
def api_get_songmid():
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


# 定义API GET(songmid)
@server.route('/getSongUrl', methods=['GET'])
def api_get_song_url():
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


server.config['JSON_AS_ASCII'] = False

server.run(host='0.0.0.0', port=5000)
