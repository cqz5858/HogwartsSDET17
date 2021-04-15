import pytest
import requests


@pytest.fixture()
def login():
    data = {
        "account": "admin",
        "password": "123456",
        "referer": "http://127.0.0.1:8080/zentao/my/",
        "verifyRand": "1330477528"
    }
    r = requests.post(url="http://127.0.0.1:8080/zentao/user-login.html", data=data )
    print("登录操作")
    token:str = r.cookies.items()[0][1]
    # yield token # 相当于return
    # print("登录操作")
    return token

# fixture call fixture
@pytest.fixture
def get_username(login):
    print("获取用户")
    name = "张三"
    return name