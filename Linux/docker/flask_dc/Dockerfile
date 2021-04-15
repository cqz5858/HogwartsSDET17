# 基础镜像，首命令
FROM python:3.7-alpine

# 元数据标签信息
LABEL maintainer="hogwarts"

# 工作目录设定为 /code
WORKDIR /code

# 创建环境变量给Flask
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# 复制 app.py 到容器内 /code 目录
COPY app.py /code

# 安装 gcc 工具、python 的依赖
#RUN systemctl restart network
#RUN ping jd.com

RUN echo "127.0.0.1    localhost" >> /etc/hosts && cat /etc/hosts 
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install flask && pip install redis

#映射端口
EXPOSE 5000
 
STOPSIGNAL SIGTERM

#为容器设置默认启动命令
CMD ["flask", "run"]