

def fun1(a, *b, **d):
    """
    不定参数实例
    :param a:
    :param b:
    :param d:
    :return:
    """
    print(type(a), a)
    print(type(b), b)
    print(type(d), d)


# fun1(1)
# fun1(1, 2, 3, 4)
# fun1(1, name='test', port=8080)
fun1(1, 2, 3, 4, name='test', port=8080)
#
# fun2 = lambda x: x*2
# print(fun2(3))
