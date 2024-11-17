# 获取专辑图
import requests

from api import api


def get_album_picture(id):
    url = api["get_album_picture"].format(str(int(id) % 100), str(id))
    response = requests.get(url)
    if response.status_code == 200:
        # 用于测试是否成功获取图片
        # filename = os.path.basename(url)
        # with open(filename, "wb") as file:
        # file.write(response.content)
        return response.content
    else:
        return None

# 通过mid拿到专辑图片，适用于非搜索情况下
def get_album_picture_2(album_mid):
    url = api["get_album_picture_2"].format(album_mid)
    response = requests.get(url)
    if response.status_code == 200:
        # 用于测试是否成功获取图片
        # filename = os.path.basename(url)
        # with open(filename, "wb") as file:
        # file.write(response.content)
        return response.content
    else:
        return None