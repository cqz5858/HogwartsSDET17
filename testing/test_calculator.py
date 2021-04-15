import sys
import pytest
import yaml

sys.path.append('..')
# print(sys.path)
from pythonencode.Calculator import Calculator

# def setup_module():
#     print("\n资源准备: setup_modle")
#
# def teardown_module():
#     print("\n释放资源: teardown_modle")
#
# def setup_function():
#     print("\n函数级前置: setup_function")
#
# def teardown_function():
#     print("\n函数级后置: teardown_function")
#
# def test_case1():
#     assert 1 == 1
#     print("test_case1")

def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'])

class TestCalculator:
    datas: list = get_datas()
    def setup_class(self):
        print("\n测试类前置")
        self.calc = Calculator()

    # def teardown_class(self):
    #     print("\n测试类后置")
    #
    # def setup(self):
    #     print("\n测试方法前置")
    #
    # def teardown(self):
    #     print("\n测试方法后置")

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    @pytest.mark.div
    def test_div(self):
        assert 1 == self.calc.div(1, 1)
