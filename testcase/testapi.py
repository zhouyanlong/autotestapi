import unittest
import ddt
from testtool.readexcel import Read_Excel
from testtool.sendrequest import Send_Request
from testtool.mylog import Log
from testtool.login import login
from testtool.dbmysql import DB
from testtool import setting
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
test_data=Read_Excel().read_data(setting.testcasedir)
importdata=Read_Excel().read_importdata()
#Read_Excel().update_importdata()
Send_Request().send_import(importdata)
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
        #需要sql校验
        elif testdata["sqldata"] is not None:
            db=eval(testdata["sqldata"])[0]
            sql=eval(testdata["sqldata"])[1]
            sql_assert=testdata["sqlassert"]
            sql_res=DB().select(db,sql)
            Log().info("sql查询的结果为{}，预期结果为{}".format(str(sql_res),sql_assert))
            if str(sql_res)==sql_assert:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败",setting.testcasedir)
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(str(sql_res),sql_assert,"sql查询的结果为{}，预期结果为{}".format(str(sql_res),sql_assert))
        #返回字典
        elif testdata["checkdata"] is not None and testdata["body"].find("pageSize")!=-1:
            Log().info("请求包含分页，响应的字典数据为{}".format(res[method]))
            checkkey=eval(testdata['checkdata'])[0]
            checkvalue=eval(testdata['checkdata'])[1]
            res_list=Send_Request().get_list_data(testdata,session,checkkey)
            Log().info("响应中需要断言的数据为{},checkvalue为{}".format(res_list,checkvalue))
            if str(res_list)==checkvalue:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败",setting.testcasedir)
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(str(res_list),checkvalue,"响应data为{0}，预期data为{1}".format(str(res_list), checkvalue))
        #返回list
        elif testdata["checkdata"] is not None and testdata["body"].find("pageSize") == -1:
            Log().info("请求不包含分页，响应的list数据为{}".format(res[method]))
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

        #返回为空
        elif testdata["checkdata"] is None and "total" in res[method].keys():
            Log().info("响应结果应该为空，响应的total为{}".format(res[method]["total"]))
            if int(res[method]["total"]) == 0:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败",setting.testcasedir)
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(int(res[method]["total"]),0,"响应data为{0}".format(int(res[method]["total"])))
        else:
            Read_Excel().write_excel(int(testdata["id"]) + 1, "成功",setting.testcasedir)
            Log().info("用例{}：成功".format(testdata["id"]))







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

