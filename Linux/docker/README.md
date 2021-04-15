[通过容器化Python Web应用掌握Docker容器核心技能](https://ceshiren.com/t/topic/3708?u=cqz)
#### CentOS安装docker
1. 安装依赖：
yum install -y yum-utils device-mapper-persistent-data lvm2

2. 添加国内源阿里源，下载速度比较快：
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

3. 安装docker
yum install -y docker-ce

4. 配置镜像加速器 register: https://index.docker.io/v1/  修改为  register: https://index.docker.io/v1/

```
yum install -y yum-utils device-mapper-persistent-data lvm2 && yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo && yum install -y docker-ce
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://n1s5gkfw.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload && sudo systemctl restart docker


```

PS：
1、![vim /usr/libexec/urlgrabber-ext-down](https://images.gitee.com/uploads/images/2021/0407/150407_c727e791_1296031.png "屏幕截图.png")
vim /usr/libexec/urlgrabber-ext-down

2、![vim /usr/bin/yum-config-manager](https://images.gitee.com/uploads/images/2021/0407/150540_527a2144_1296031.png "屏幕截图.png")
vim /usr/bin/yum-config-manager

### docker - nginx

1. `docker run -d --name nginx -p 80:80 -v ${pwd}/nginx/html:/usr/share/nginx/html nginx:1.17.9` 
![输入图片说明](https://images.gitee.com/uploads/images/2021/0408/115329_62172464_1296031.png "屏幕截图.png")

PS:自动下载镜像nginx:1.17.9并运行在容器nginx中 

### docker - jenkins

1. `docker run -d --name jenkins -p 8080:8080 jenkins/jenkins`不挂载目录
2. `docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v ${PWD}/jenkins:/var/jenkins_home jenkins/jenkins`挂载目录
3. 查看密码 `docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword`

### docker-compose
docker-compose up -d
docker-compose up --build

### 4.08 （周四）20:00-21:30 docker实战常用测试平台搭建
###课堂笔记整理###
 - 面试问题：为什么没有IE？

        1. 你见过Linux上运行IE不，都是虚拟化技术，因为docker没有虚拟化自己的内核，直接用Linux内核，dockerd就是Linux的一个进程。
        2. docker使用宿主机Linux内核，容器也干不了，所以没有IE、不能做兼容性测试，部署测试要在虚拟机上做，同样的挑内核的事不要让docker来做
        3. 内核基本上等于操作系统，没有好的内核就没有操作系统
        docker与虚拟机的区别：
        1. 无法虚拟内核，依赖Linux内核，基于进程，轻量级，秒级启动，一台服务器能跑上百个，好的服务器能跑好几百个40核500G
        2. 部署比较方便，比如做微服务没有docker做不了，上百个各种服务，开发测试运维都要疯掉。

 - 技术点
  1. 容器的环境变量比较重要，相当于python的参数列表，namespace技术进程间可以传递参数，docker会使用很多宿主机的东西，比如网络、cpu
  2. CI持续集成：

 - 其它
  1. 全局fixture 数据准备（代码，文件，数据库）
  2. k8s所有大厂BAT都在用了，部分中厂也在用的,服务越来越多时，怎么才能把它部署越来，没有大厂不是996的，少只有少数特别的业务没有，比如银行
  3. 开发和测试用的是同一个代码和环境，很少说开发的和测试的不一样了。
  4. 测试开发就是要什么都会，编辑语言不会，你要多用啊，用于种场景
  5. 
 - 截图
![UI分布式自动化](https://images.gitee.com/uploads/images/2021/0410/104435_e218f930_1296031.png "屏幕截图.png")
![Dashboard](https://images.gitee.com/uploads/images/2021/0410/104533_f46dc1d9_1296031.png "屏幕截图.png")
![不能做兼容性测试](https://images.gitee.com/uploads/images/2021/0410/103438_92f332ca_1296031.png "屏幕截图.png")
![CI持续集成](https://images.gitee.com/uploads/images/2021/0410/104220_dd2bf936_1296031.png "屏幕截图.png")

###课后任务###
1. dockerfile自己搭建一个镜像

