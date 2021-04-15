class Person:
    # 定义类变量,可变
    name = "default"
    age = 0
    gender = "default"
    weight = 0

    def __init__(self, name, age, gender, weight):
        # 定义实例变量,可变
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def act(self):
        print(f"{self.name} act")

    def sing(self):
        print(f"{self.name} sing")

    # 类方法
    @classmethod
    def think(cls):
        print(f"{cls.name} think")

# # 类型变量和实例变量区别:
# # 类变量classname.访问,实例变量要创建实例后才能访问,编写框架时使用,类不需要实例化的情况下使用
# # 类变量和实例变量的值可变
# print(Person.name)
# Person.name = '陈大'
# print(Person.name)
# zs = Person('张三', 33, '男', 133)
# print(zs.name)
# zs.name = '张山'
# print(zs.name)

# 类方法和实例方法区别:
# 类不能直接访问实例方法,需要加装饰器@classmethod
Person.think()
# zs = Person('张三', 33, '男', 133)
# zs.think()

# 类的实例化,创建一个实例
# zs = Person('张三', 33, '男', 133)
# print(zs.name, zs.age, zs.gender, zs.weight)
# print(f"名字：{zs.name}\n年龄：{zs.age}\n性别：{zs.gender}\n体重：{zs.weight}\n")
