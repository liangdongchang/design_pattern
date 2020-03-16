# encoding: utf-8
'''
@contact: 1257309054@qq.com
@wechat: 1257309054
@Software: PyCharm
@file: 9、装饰模式.py
@time: 2020/3/14 14:09
@author:LDC
'''
"""
装饰模式
动态地给一个对象添加一些额外的职责。
就增加功能来说，Decorator 模式相比生成子类更为灵活。 
在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
"""

class Person(object):
    # 定义一个人类
    def __init__(self, name):
        self.name = name

    def show(self):
        print('{}穿着衣服'.format(self.name))


class Decorate(Person):
    # 定义一个装饰类
    component = None

    def __init__(self):
        pass

    def decorate(self, component):
        self.component = component

    def show(self):
        if self.component is not None:
            self.component.show()


class TShirts(Decorate):
    # 定义一个T恤类
    def __init__(self):
        pass

    def show(self):
        print('Big Tshirts')
        super(TShirts, self).show()


class BigTrouser(Decorate):
    # 定义一个裤子类
    def __init__(self):
        pass

    def show(self):
        print('Big Trouser')
        super(BigTrouser, self).show()


if __name__ == '__main__':
    ldc = Person('ldc')
    ts = TShirts()
    bt = BigTrouser()
    ts.decorate(ldc)
    bt.decorate(ldc)
    ts.show()
    bt.show()

"""
总结：
1.一般来说，通过继承可以获得父类的属性，还可以通过重载修改其方法。
2.装饰模式可以不以继承的方式而动态地修改类的方法。
3.装饰模式可以不以继承的方式而返回一个被修改的类。
"""
