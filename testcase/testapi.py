import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import ddt
from testtool.readexcel import Read_Excel
from testtool.sendrequest import Send_Request
from testtool.mylog import Log
from testtool.login import login
from testtool import setting
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
test_data=Read_Excel().read_data(setting.testcasedir)
#importdata=Read_Excel().read_importdata()
#Send_Request().send_import(importdata)
session=login()
@ddt.ddt
class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        Log().info("test starts")

        
    @ddt.data(*test_data)
    def test_case(self,testdata):
        Log().info("用例{}:{}正在执行".format(testdata["id"],testdata["usecase"]))
        Log().info("用例{}的请求数据为{}".format(testdata["id"],testdata))
        Log().info("session为{},类型为{}".format(session,type(session)))
        re=Send_Request().send_req(testdata,session)
        res=re.json()
        Log().info("响应结果为{}".format(res))
        body = eval(re.request.body)
        me = body["method"]
        method = str(me) + "_response"
        #返回报错
        if "error_response" in res.keys():
            res_code = int(res["error_response"]["code"])
            res_msg = res["error_response"]["msg"]
            Log().info("用例{}的响应code为{},响应msg为{}".format(testdata["id"], res_code, res_msg))
            if res_code == int(testdata["code"]) and res_msg == testdata["msg"]:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败",setting.testcasedir)
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(res_code, int(testdata["code"]),"响应code为{0}，预期code为{1}".format(res_code, testdata["code"]))
            self.assertEqual(res_msg, testdata["msg"], "响应msg为{0}，预期msg为{1}".format(res_msg, testdata["msg"]))
        #返回""，即引起表内数据变化
        elif "" in res.values():
            #需要将生成的id写入，作为传参传给其他接口
            if testdata["sqldata"] is not None:
                self.assertEqual(res_code, int(testdata["code"]),"响应code为{0}，预期code为{1}".format(res_code, testdata["code"]))
                self.assertEqual(res_msg, testdata["msg"], "响应msg为{0}，预期msg为{1}".format(res_msg, testdata["msg"]))
            #断言状态码，接口生成数据由查询去断言
            else:
                if re.status_code == 200:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "成功", setting.testcasedir)
                    Log().info("用例{}：成功".format(testdata["id"]))
                else:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "失败", setting.testcasedir)
                    Log().info("用例{}：失败".format(testdata["id"]))
                self.assertEqual(re.status_code, 200,"响应状态码为{0}，预期状态码为200".format(re.status_code))



        #响应结果返回字典
        #elif testdata["checkdata"] is not None and testdata["body"].find("pageSize")!=-1 and str(type(res[method]))=="<class 'dict'>":
        elif str(type(res[method])) == "<class 'dict'>":
            Log().info("请求包含分页，响应的字典数据为{}".format(res[method]))
            #判断checkdata是不是有三个值，用于断言list里的数据
            if len(testdata['checkdata'])==3:
                checkmenu = eval(testdata['checkdata'])[0]
                checkkey = eval(testdata['checkdata'])[1]
                checkvalue = eval(testdata['checkdata'])[2]
                res_list = Send_Request().get_list_data(checkmenu,testdata, session, checkkey)
                Log().info("响应中需要断言的数据为{},checkvalue为{}".format(res_list, checkvalue))
                if str(res_list) == checkvalue:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "成功", setting.testcasedir)
                    Log().info("用例{}：成功".format(testdata["id"]))
                else:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "失败", setting.testcasedir)
                    Log().info("用例{}：失败".format(testdata["id"]))
                self.assertEqual(str(res_list), checkvalue, "响应data为{0}，预期data为{1}".format(str(res_list), checkvalue))
            #判断checkdata是不是有两个值，用于断言部分接口比如报表
            elif len(testdata['checkdata'])==2:
                checkmenu=None
                checkkey = eval(testdata['checkdata'])[0]
                checkvalue = eval(testdata['checkdata'])[1]
                res_list = Send_Request().get_list_data(checkmenu,testdata, session, checkkey)
                Log().info("响应中需要断言的数据为{},checkvalue为{}".format(res_list, checkvalue))
                if str(res_list) == checkvalue:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "成功", setting.testcasedir)
                    Log().info("用例{}：成功".format(testdata["id"]))
                else:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "失败", setting.testcasedir)
                    Log().info("用例{}：失败".format(testdata["id"]))
                self.assertEqual(str(res_list), checkvalue, "响应data为{0}，预期data为{1}".format(str(res_list), checkvalue))

            #checkdata没有二或者三个值，则说明返回的list为空，断言total即可
            else:
                Log().info("响应结果预期应该为空，响应的total为{}".format(res[method]["total"]))
                if int(res[method]["total"]) == 0:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "成功", setting.testcasedir)
                    Log().info("用例{}：成功".format(testdata["id"]))
                else:
                    Read_Excel().write_excel(int(testdata["id"]) + 1, "失败", setting.testcasedir)
                    Log().info("用例{}：失败".format(testdata["id"]))
                self.assertEqual(int(res[method]["total"]), 0, "响应data为{0}".format(int(res[method]["total"])))


        #返回list
        elif str(type(res[method])) == "<class 'list'>":
            Log().info("响应的list数据为{}".format(res[method]))
            checkkey = eval(testdata['checkdata'])[0]
            checkvalue = eval(testdata['checkdata'])[1]
            res_list = Send_Request().get_res_data(testdata, session, checkkey)
            Log().info("响应中需要断言的数据为{},checkvalue为{}".format(res_list, checkvalue))
            if res_list == checkvalue:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败",setting.testcasedir)
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(res_list, checkvalue, "响应data为{0}，预期data为{1}".format(res_list, checkvalue))




    def tearDown(self) -> None:
        Log().info("test ends")

if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(TestApi("test_case"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)"""
    """suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApi))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)"""
    #unittest.main()

