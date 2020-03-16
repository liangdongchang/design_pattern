# encoding: utf-8
'''
@contact: 1257309054@qq.com
@wechat: 1257309054
@Software: PyCharm
@file: 职责链模式.py
@time: 2020/3/15 17:33
@author:LDC
'''
"""
职责链模式
在调用时要定义好哪个实例是哪个实例的职责上一级，
请求沿着定义的链条传递给可以处理请求的对象
1、有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定；
2、在不明确指定接收者的情况下，向多个对象中的一个提交一个请求；
3、处理一个请求的对象集合应被动态指定。

比如费用报销找上级领导审批，不同的级别可以审批不同的金额。这时候就可以使用职责链模式。
"""


class HandlerBase(object):
    # 处理基类
    def successor(self, successor):  # 下一个处理者
        self._successor = successor


class RequestHandlerL1(HandlerBase):
    # 第一级请求处理者
    name = "TeamLeader"  # 小组领导

    def handle(self, request):
        if request < 500:
            print("审批者【{}】,处理请求金额【{}】元，审批结果【审批通过】".format(self.name, request))
        else:
            print("\033[31;1m【%s】无权审批,交给下一个审批者\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL2(HandlerBase):
    # 第一级请求处理者
    name = "DeptManager"  # 副经理

    def handle(self, request):
        if request < 5000:
            print("审批者【{}】,处理请求金额【{}】元，审批结果【审批通过】".format(self.name, request))
        else:
            print("\033[31;1m【%s】无权审批,交给下一个审批者\033[0m" % self.name)
            self._successor.handle(request)


class RequestHandlerL3(HandlerBase):
    # 第一级请求处理者
    name = "CEO"  # 首席执行官

    def handle(self, request):
        if request < 10000:
            print("审批者【{}】,处理请求金额【{}】元，审批结果【审批通过】".format(self.name, request))
        else:
            print("\033[31;1m【%s】钱太多了，不批\033[0m" % self.name)
            # self._successor.handle(request)


class RequestAPI(object):
    # 定义一个请求接口类
    h1 = RequestHandlerL1()
    h2 = RequestHandlerL2()
    h3 = RequestHandlerL3()

    h1.successor(h2)
    h2.successor(h3)

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def handle(self):
        # 统一请求接口
        self.h1.handle(self.amount)


if __name__ == '__main__':
    r1 = RequestAPI('ldc', 8000)
    r1.handle()
    print(r1.__dict__)


"""
总结：
接收者和发送者都没有对方的明确信息，且链中的对象自己并不知道链的结构，
职责链可简化对象的相互连接，他们仅需保持一个指向后继者的引用，
而不需要保持他所有候选接收者的引用，大大降低了耦合度，可以随时增加或修改处理一个请求的结构
"""