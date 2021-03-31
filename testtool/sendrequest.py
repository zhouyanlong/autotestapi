import requests
import json
from testtool.readexcel import Read_Excel
from testtool.mylog import Log
from testtool.login import login
from testtool.apiimport import import_data
import urllib3
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
                body1=eval(data["body"])
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
    #获取response的list数据
    def get_list_data(self,data,session,key):
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
                body1=eval(data["body"])
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
            re = res.json()[method]["list"]
            Log().info("响应的list数据为{}".format(re))
            value=re[0][key]
            for r in re:
                if r[key]==value:
                    return value
                else:
                    return False
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
                body1=eval(data["body"])
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
                h = data["headers"]
            else:
                h = None
            if data["body"]:
                body = data["body"]
            else:
                body = None
        except Exception as e:
            Log().error(e)
        try:
            requests.packages.urllib3.disable_warnings()
            res = requests.request(url=url, method=method, headers=h, data=json.dumps(body), verify=False)
        except Exception as e:
            Log().error(e)


if __name__ == '__main__':
    # r=Read_Excel().read_data()
    # r1=r[0]
    # print(r1)
    # re=Send_Request().get_list_data(r1,login(),"upStatus")
    # print(re,type(re))


    # re=Send_Request().send_req(r1,login())
    # print(re.json())
    # body=eval(re.request.body)
    # m=body["method"]
    # me=str(m)+"_response"
    # res=re.json()[me]["list"]
    # print(res)

    da=import_data()
    Send_Request().send_import(da)
