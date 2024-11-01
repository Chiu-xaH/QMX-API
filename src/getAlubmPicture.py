# 获取专辑图
from io import BytesIO

import requests
from flask import send_file, jsonify

from api import api


def get_album_picture(id):
    url = api["get_album_picture"].format(str(id % 100), str(id))
    response = requests.get(url)
    if response.status_code == 200:
        # 用于测试是否成功获取图片
        # filename = os.path.basename(url)
        # with open(filename, "wb") as file:
        # file.write(response.content)
        # 将图片内容写入内存字节流
        img = BytesIO(response.content)
        img.seek(0)
        # 返回图片文件流，设置 mimetype 以确保客户端识别为图片
        return send_file(img, mimetype='image/jpg')
    else:
        # 返回错误信息
        return jsonify({"error": "图片获取失败"}), 404
