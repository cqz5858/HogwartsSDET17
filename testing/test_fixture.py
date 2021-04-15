
# @pytest.mark.usefixtures("get_username")
# @pytest.mark.usefixtures("login")
# def test_buy(login, get_username):
def test_buy(login):
    print(login)
    print("购买商品")

def test_search():
    print("查找商品")