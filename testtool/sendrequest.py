import requests
import json
from testtool.readexcel import Read_Excel
from testtool.mylog import Log
from testtool.login import login
import urllib3
from testtool import setting
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class Send_Request():
    def send_req(self,data,session):
        try:
            if data["url"]:
                url=data["url"]
            else:
                url=None
            if data["method"].lower() == "post":
                method = "post"
            elif data["method"].lower() == "get":
                method = "get"
            else:
                method=None
            if data["headers"]:
                h=eval(data["headers"])
            else:
                h=None
            if data["body"]:
                a=data["body"]
                #替换body中的变量
                a=Send_Request().replace_data(a)
                body1=eval(a)
                body=dict(body1,**session)
                Log().info("合并后的data为{}".format(body))
            else:
                body=None
        except Exception as e:
            Log().error(e)
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(url=url, method=method, headers=h, data=json.dumps(body), verify=False)
        except Exception as e:
            Log().error(e)
        return res
    #获取response的特定menu数据
    def get_list_data(self,menu,data,session,key):
        try:
            if data["url"]:
                url=data["url"]
            else:
                url=None
            if data["method"].lower() == "post":
                method = "post"
            elif data["method"].lower() == "get":
                method = "get"
            else:
                method=None
            if data["headers"]:
                h=eval(data["headers"])
            else:
                h=None
            if data["body"]:
                a = data["body"]
                # 替换body中的变量
                a=Send_Request().replace_data(a)
                body1 = eval(a)
                body = dict(body1, **session)
                Log().info("合并后的data为{}".format(body))
            else:
                body = None
        except Exception as e:
            Log().error(e)
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(url=url, method=method, headers=h, data=json.dumps(body), verify=False)

            body = eval(res.request.body)
            me = body["method"]
            method = str(me) + "_response"
            if menu!=None:
                re = res.json()[method][menu]
                #如果是list，取第一条数据中的value
                if menu=="list":
                    value = re[0][key]
                    for r in re:
                        if r[key] == value:
                            Log().info("checkvalue=3时响应的value数据为{}".format(value))
                            return value
                        else:
                            return False
                #否则取menu中的value
                else:
                    value=res.json()[method][menu][key]
                    Log().info("checkvalue=3时非list的响应为{}".format(value))
                    return value
            else:
                value = res.json()[method][key]
                Log().info("checkvalue=2时响应的value数据为{}".format(value))
                return value
        except Exception as e:
            Log().error(e)
    #获取响应类型为list的数据
    def get_res_data(self,data,session,key):
        try:
            if data["url"]:
                url=data["url"]
            else:
                url=None
            if data["method"].lower() == "post":
                method = "post"
            elif data["method"].lower() == "get":
                method = "get"
            else:
                method=None
            if data["headers"]:
                h=eval(data["headers"])
            else:
                h=None
            if data["body"]:
                a = data["body"]
                # 替换body中的变量
                a = Send_Request().replace_data(a)
                body1=eval(a)
                body=dict(body1,**session)
            else:
                body=None
        except Exception as e:
            Log().error(e)
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(url=url, method=method, headers=h, data=json.dumps(body), verify=False)

            body = eval(res.request.body)
            me = body["method"]
            method = str(me) + "_response"
            re = res.json()[method][0]
            Log().info("响应列表的第一条数据为{}".format(re))
            value=re[key]
            return value
        except Exception as e:
            Log().error(e)
    #发送接口导案
    def send_import(self,data):

        try:
            if data["url"]:
                url = data["url"]
            else:
                url = None
            if data["method"].lower() == "post":
                method = "post"
            elif data["method"].lower() == "get":
                method = "get"
            else:
                method = None
            if data["headers"]:
                h = eval(data["headers"])
            else:
                h = None
            if data["body"]:
                body = eval(data["body"])
            else:
                body = None
        except Exception as e:
            Log().error(e)
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(url=url, method=method, headers=h, data=json.dumps(body), verify=False)
        except Exception as e:
            Log().error(e)
    def replace_data(self,a):
        # 商户端
        if a.find("${customerId}") != -1:
            number = Read_Excel().read_id(36, setting.testcasedir)
            Log().info("需要替换的customerid为{}".format(number))
            a = a.replace("${customerId}", number)
        if a.find("${taskid}") != -1:
            number = Read_Excel().read_id(55, setting.testcasedir)
            Log().info("需要替换的taskid为{}".format(number))
            a = a.replace("${taskid}", number)
        # 管理端
        if a.find("${templateid}") != -1:
            number = Read_Excel().read_id(36, setting.testcaseadmindir)
            Log().info("需要替换的templateid为{}".format(number))
            a = a.replace("${templateid}", number)
        if a.find("${repaytempid}") != -1:
            number = Read_Excel().read_id(41, setting.testcaseadmindir)
            Log().info("需要替换的repaytempid为{}".format(number))
            a = a.replace("${repaytempid}", number)
        if a.find("${backtempid}") != -1:
            number = Read_Excel().read_id(46, setting.testcaseadmindir)
            Log().info("需要替换的backtempid为{}".format(number))
            a = a.replace("${backtempid}", number)
        if a.find("${strategyid}") != -1:
            number = Read_Excel().read_id(110, setting.testcaseadmindir)
            Log().info("需要替换的strategyid为{}".format(number))
            a = a.replace("${strategyid}", number)
        if a.find("${strategycopyid}") != -1:
            number = Read_Excel().read_id(120, setting.testcaseadmindir)
            Log().info("需要替换的strategycopyid为{}".format(number))
            a = a.replace("${strategycopyid}", number)
        if a.find("${variableid}") != -1:
            number = Read_Excel().read_id(124, setting.testcaseadmindir)
            Log().info("需要替换的variableid为{}".format(number))
            a = a.replace("${variableid}", number)
        if a.find("${accessid}") != -1:
            number = Read_Excel().read_id(136, setting.testcaseadmindir)
            Log().info("需要替换的accessid为{}".format(number))
            a = a.replace("${accessid}", number)
        if a.find("${explicitnumber}") != -1:
            number = Read_Excel().read_id(157, setting.testcaseadmindir)
            Log().info("需要替换的explicitnumber为{}".format(number))
            a = a.replace("${explicitnumber}", number)
        if a.find("${linegroupid}") != -1:
            number = Read_Excel().read_id(168, setting.testcaseadmindir)
            Log().info("需要替换的linegroupid为{}".format(number))
            a = a.replace("${linegroupid}", number)
            print("替换后的a为"+a)
        if a.find("${linesupplierid}") != -1:
            number = Read_Excel().read_id(172, setting.testcaseadmindir)
            Log().info("需要替换的linesupplierid为{}".format(number))
            a = a.replace("${linesupplierid}", number)
        if a.find("${libraryid}") != -1:
            number = Read_Excel().read_id(176, setting.testcaseadmindir)
            Log().info("需要替换的libraryid为{}".format(number))
            a = a.replace("${libraryid}", number)
        if a.find("${soundid}") != -1:
            number = Read_Excel().read_id(184, setting.testcaseadmindir)
            Log().info("需要替换的soundid为{}".format(number))
            a = a.replace("${soundid}", number)
        if a.find("${stopblackid}") != -1:
            number = Read_Excel().read_id(229, setting.testcaseadmindir)
            Log().info("需要替换的stopblackid为{}".format(number))
            a = a.replace("${stopblackid}", number)

        return a
if __name__ == '__main__':
    r=Read_Excel().read_data(setting.testcasedir)
    r1=r[0]
    print(r1)
    # re=Send_Request().get_list_data(r1,login(),"upStatus")
    # print(re,type(re))
    #a=Read_Excel().read_importdata()
    #Send_Request().send_import(a)
    re=Send_Request().send_req(r1,login())
    #re.content.decode("utf-8")
    #print(re.text)
    print(re)
    print(re.json())
    # body=eval(re.request.body)
    # m=body["method"]
    # me=str(m)+"_response"
    # res=re.json()[me]["list"]
    # print(res)

