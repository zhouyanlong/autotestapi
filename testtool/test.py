from testtool.setconfig import Tool
from testtool.readexcel import Read_Excel
T=Tool().get_config("tester","name")
#print(T)

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

if __name__ == '__main__':
    #必须要用实例调用
    TestMethod("a",1).method1()
    #TestMethod.method1()
    #可以直接类名.方法名调用,无法调用类里的属性（如self.name）
    TestMethod.method2()
    TestMethod.method3()
    a=[1,2,3]
    for j in a:
        print(j)

    nameid = "449"
    name = "周彦龙" + nameid
    print(name)
    nameid=str(int(nameid)+1)
    name = "周彦龙" + nameid
    print(name)
    #print(len(a))
    """for i in range(len(a)):
        b=[1,3,4]
        if a[i] in b:
            print(a[i])"""





