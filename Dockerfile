# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录为/app
WORKDIR /app

# 复制当前目录下的所有文件到容器的/app目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 创建日志文件夹
RUN mkdir -p /app/log

# 暴露容器的端口（Flask 默认为 5000）
EXPOSE 5000

#CMD ["python", "./api/app.py"]
# 使用 gunicorn 启动 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api.app:app", "--access-logfile", "./log/access.log", "--error-logfile", "./log/error.log"]