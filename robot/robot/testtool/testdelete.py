

import sys,os,time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from testtool.setconfig import Tool
T=Tool().get_config("tester","name")

class TestMethod():
    #初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #实例方法
    def method1(self):
        print("我是实例方法")
    #类方法
    @classmethod
    def method2(cls):
        print("我是类方法")
    #静态方法
    @staticmethod
    def method3():
        print("我是静态方法")

d=time.strftime("%Y%m%d%H%M%S", time.localtime())
print(type(d))