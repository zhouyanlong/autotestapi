import unittest
import ddt
from testtool.readexcel import Read_Excel
from testtool.sendrequest import Send_Request
from testtool.mylog import Log
from testtool.login import adminlogin

test_data = Read_Excel().read_data()
session = adminlogin()

@ddt.ddt
class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        Log().info("test start")

    @ddt.data(*test_data)
    def test_case(self, testdata):
        Log().info("用例{}正在执行".format(testdata["id"]))
        Log().info("用例{}的请求数据为{}".format(testdata["id"], testdata))
        res = Send_Request().send_req(testdata, session).json()
        if "error_response" in res.keys():
            res_code = int(res["error_response"]["code"])
            res_msg = res["error_response"]["msg"]
            Log().info("用例{}的响应code为{},响应msg为{}".format(testdata["id"], res_code, res_msg))
            if res_code == int(testdata["code"]) and res_msg == testdata["msg"]:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "成功")
                Log().info("用例{}：成功".format(testdata["id"]))
            else:
                Read_Excel().write_excel(int(testdata["id"]) + 1, "失败")
                Log().info("用例{}：失败".format(testdata["id"]))
            self.assertEqual(res_code, int(testdata["code"]),
                             "响应code为{0}，预期code为{1}".format(res_code, testdata["code"]))
            self.assertEqual(res_msg, testdata["msg"], "响应msg为{0}，预期msg为{1}".format(res_msg, testdata["msg"]))
        else:
            Read_Excel().write_excel(int(testdata["id"]) + 1, "成功")
            Log().info("用例{}：成功".format(testdata["id"]))

    def tearDown(self) -> None:
        Log().info("test ends")


if __name__ == '__main__':
    unittest.main()
    """suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApi))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)"""
    """suite = unittest.TestSuite()
    suite.addTest(TestApi("test_case"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)"""
    # unittest.main()

