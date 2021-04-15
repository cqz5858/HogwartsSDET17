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

### docker - compose
