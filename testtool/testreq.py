import requests
import json
import urllib3
urllib3.disable_warnings()
"""url="https://ai.zhilingsd.com/api/business/login"
h={"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}
body={"account":"zhouyanlong","password":"Aa123456.","platform":"robot"}
s=requests.session()
res=s.request(url=url,headers=h,method="post",data=json.dumps(body),verify=False).json()
print(res)
url1="https://ai.zhilingsd.com/api/route/rest"
h1={"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}
#"session":"user_session_cache:business:robot:1523372240188346368:5eb8b07a-e1a3-42f9-af7a-03975e371c82",
body1={"method":"business_manager_batch_list","v":"1.0","timestamp":"2021-03-14 13:36:18","data":{"currentPage":1,"pageSize":15}}
res1=s.request(url=url1,headers=h1,method="post",data=json.dumps(body1),verify=False).json()
print(res1)"""
#使用cookie
class Testacd2():
    """def test_login(self,url,data):

        h1 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
        res1 = requests.request(url=url, headers=h1, method="post", data=json.dumps(data), verify=False)
        #print(res1.json(), res1.cookies)
        return res1.cookies"""
    def test_getuser(self,url,data,cookie=None):
        h2 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
        res2 = requests.request(url=url, headers=h2, method="post", data=json.dumps(data), verify=False,cookies=cookie)
        if res2.cookies:
            cookie=res2.cookies
            print(cookie)
        #print(res2.json(), res2.cookies)
        return res2.cookies
    def testlogin(self):
        requests.packages.urllib3.disable_warnings()
        data = {'url': 'https://robotmeracd.zhilingsd.com/api/login','headers': '{"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}','method': 'post', 'body': '{"userAccount": "sclj02", "password": "Aa123456."}'}
        res = requests.request(url=data["url"], method=data["method"], headers=eval(data["headers"]), data=data["body"],verify=False)
        re = res.json()
        print(re)
        #session_data = re["data"]["session"]
        #session = {"session": session_data}
        #print("商户端获取到的session为{}".format(session))

if __name__ == '__main__':
    #url1 = "https://robotmeracd.zhilingsd.com/api/login"
    # body1 = {"userAccount": "sclj02", "password": "Aa123456."}
    # url2="https://robotmeracd.zhilingsd.com/api/robot/user/getSubUserList"
    # body2={"currentPage":1,"pageSize":15}
    # test1=Testacd2().test_getuser(url1,body1)
    # #print(test1)
    # test2=Testacd2().test_getuser(url2,body2)
    # Testacd2().testlogin()
    #url1="https://ai.zhilingsd.com/api/route/rest"
    url1="https://admintest.robot.com/api/route/rest"
    h1 = {"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "314",
"Content-Type": "application/json;charset=UTF-8",
"Host": "ai.zhilingsd.com",
"Origin": "https://ai.zhilingsd.com",
"Referer": "https://ai.zhilingsd.com/",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    # "session":"user_session_cache:business:robot:1523372240188346368:5eb8b07a-e1a3-42f9-af7a-03975e371c82",
    #body1 = {"method":"business_manager_task_edit_task","session":"user_session_cache:business:robot:1523372240188346368:513b6afb-68a5-40dc-9401-c4bd19be5e05","timestamp":"2021-04-21 18:01:52","data":{"id":"734","startDate":"2021-04-21","executeTime":[{"beginTime":"09:00","endTime":"21:00"}],"callLine":5}}
    # body1={"method":"merchant_query_platform_merchant_list","session":"user_session_cache:manage:17f02e8c-9b99-492d-92ea-5b863f662a71","v":"1.0","timestamp":"2021-04-22 17:46:51","data":{"platform":"robot"}}
    # res1 = requests.request(url=url1, headers=h1, method="post", data=json.dumps(body1), verify=False)
    # print(res1)
    # res2=res1.json()
    # print(res2)
    # print(type(res2["merchant_query_platform_merchant_list_response"]))
    # if str(type(a))=="<class 'dict'>":
    #     print("zidian")
    # if "" in res2.values():
    #     print("ttt")
    # else:
    #     print("没有")

    a=["list","phone","13192293666"]
    print(len(a))











#使用session
"""class Testacd2():
    def test_login(self,url,data):

        h1 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
        s=requests.session()
        res1 = s.request(url=url, headers=h1, method="post", data=json.dumps(data), verify=False)
        #print(res1.json(), res1.cookies)
        return s
    def test_getuser(self,url,data,s):
        h2 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
        res2 = s.request(url=url, headers=h2, method="post", data=json.dumps(data), verify=False)
        print(res2.json(), res2.cookies)
        return res2.json()
if __name__ == '__main__':
    url1 = "https://robotmeracd.zhilingsd.com/api/login"
    body1 = {"userAccount": "sclj02", "password": "Aa123456."}
    url2="https://robotmeracd.zhilingsd.com/api/robot/user/getSubUserList"
    body2={"currentPage":1,"pageSize":15}
    test1=Testacd2().test_login(url1,body1)
    print(test1)
    test2=Testacd2().test_getuser(url2,body2,test1)"""