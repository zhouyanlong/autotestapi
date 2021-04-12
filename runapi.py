from testtool import setting
import unittest
import time
from testtool.HTMLTestRunner import HTMLTestRunner
from testtool.newreport import new_report
from testtool.sendemail import send_mail
def add_case(file=setting.testpydir):
    #加载所有的测试用例
    discover=unittest.defaultTestLoader.discover(file,pattern="testapi.py")
    return discover
def add_admincase(file=setting.testpydir):
    #加载管理端的测试用例
    discover1=unittest.defaultTestLoader.discover(file,pattern="testadminapi.py")
    return discover1
def run_api(case,file=setting.reportdir):
    #按照testcase执行
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = file + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='python+requests+ddt+unittest接口自动化测试报告',
                            description='环境：windows 10 浏览器：chrome',
                            tester="周彦龙")
    runner.run(case)
    fp.close()
    # 调用模块生成最新的报告
    report = new_report()
    # 调用发送邮件模块
    #send_mail(report)
    

if __name__ == '__main__':
    case=add_case()
    admin_case=add_admincase()
    run_api(case)
    run_api(admin_case)

