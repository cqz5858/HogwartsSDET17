# import pytest
import allure


@allure.feature("登录模块")
class TestLogin:
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1: 打开应用"):
            print("打开应用")
        with allure.step("步骤2: 进入登录页面"):
            print("进入登录页面")
        with allure.step("步骤3: 输入用户名密码"):
            print("输入用户名密码")
        print("这是登录: 测试用例, 登录成功")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登录: 测试用例, 登录成功")

    @allure.story("用户名缺失")
    def test_login_failure_a(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败 ")

    @allure.story("登录失败")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_failure_b(self):
        print("这是登录: 测试用例, 登录失败")
        pass


@allure.feature("搜索模块")
@allure.severity(allure.severity_level.NORMAL)
class TestSearch:
    def test_case1(self):
        print("case1")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_case2(self):
        print("case2")
        assert 1 == 1

    def test_case3(self):
        print("case3")
