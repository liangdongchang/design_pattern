# encoding: utf-8
'''
@contact: 1257309054@qq.com
@wechat: 1257309054
@Software: PyCharm
@file: 10_2、桥接模式之多维度.py
@time: 2020/3/14 15:40
@author:LDC
'''

"""
多维度的桥接模式
结合上面的例子,增加一个维度"人",不同的人开着不同的汽车在不同的路上行驶(三个维度);
结合上面增加一个类"人",并重新调用.
"""


class AbstractRoad(object):
    # 路基类
    car = None


class AbstractCar(object):
    # 车辆基类

    def run(self):
        raise NotImplementedError


class People(object):
    # 定义一个人类
    road = None


class Street(AbstractRoad):
    # 市区街道
    def run(self):
        # 执行车辆对象的方法
        self.car.run()
        print("在市区街道上行驶")


class SpeedWay(AbstractRoad):
    # 高速公路
    def run(self):
        # 执行车辆对象的方法
        self.car.run()
        print("在高速公路上行驶")


class Car(AbstractCar):
    # 小汽车
    def run(self):
        # 被其它对象调用执行
        print("小汽车在")


class Bus(AbstractCar):
    # 公共汽车
    def run(self):
        # 被其它对象调用执行
        print("公共汽车在")


# 加上人
class Man(People):
    def drive(self):
        print("男人开着")
        self.road.run()  # 调用其它对象的执行方法


class Woman(People):
    def drive(self):
        print("女人开着")
        self.road.run()  # 调用其它对象的执行方法


if __name__ == '__main__':
    # 小汽车在高速公路上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()
    # 公共汽车在高速公路上行驶
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()
    # 人开车
    road3 = Street()
    road3.car = Bus()

    p1 = Man()
    p1.road = road3
    p1.drive()

    p2 = Woman()
    p2.road = road2
    p2.drive()


