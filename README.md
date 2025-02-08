# QQ音乐接口

## 声明
仅供个人学习用途，QMX-API利用Python将QQ音乐接口简单封装，可从中获取音乐、歌词、歌单等，目前仅实现基础功能 可按需求自行扩展
## 客户端实现案例
[婉婉动听](https://github.com/Chiu-xaH/WanwanDongting-Client)
## 食用方法
按requirements.txt安装所需软件包依赖
    
    pip(3) install -r ./src/requirements.txt

安装Node.js

在config.txt添加Cookie，抓包获取(推荐抓QQ音乐客户端)(可选)

运行test.py，或者部署到服务器
(测试环境)
    
    python server.py
(生产环境)
    
    gunicorn -w 4 -b 127.0.0.1:5000 server:server --access-logfile ./log/access.log --error-logfile ./log/error.log
    # 最好指定日志输出，方便分析问题
    pkill gunicorn(结束)
配置Nginx(略)
## 注意
如果不能获取歌曲URL(getSongURL) 应该是Cookie过期了，记得更新下
### Cookie自动更新配置
设置定时任务，执行
```
python refreshLogin.py
```
前端需注意：getSongURL不能频繁发送同一首歌的请求，否则对方服务器会返回封禁IP，待几小时后自动恢复

## [API文档](./main/src/API.md)
## [更新日志](./main/src/UPDATE.md)