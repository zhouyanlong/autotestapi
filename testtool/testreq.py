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
        data = {'url': 'https://test.robotsh.com/api/business/login',
                'headers': '{"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}',
                'method': 'post', 'body': '{"account":"zhou3","password":"Aa123456.","platform":"robot"}'}
        res = requests.request(url=data["url"], method=data["method"], headers=eval(data["headers"]), data=data["body"],verify=False)
        re = res.json()
        session_data = re["data"]["session"]
        session = {"session": session_data}
        print("商户端获取到的session为{}".format(session))

if __name__ == '__main__':
    url1 = "https://robotmeracd.zhilingsd.com/api/login"
    body1 = {"userAccount": "sclj02", "password": "Aa123456."}
    url2="https://robotmeracd.zhilingsd.com/api/robot/user/getSubUserList"
    body2={"currentPage":1,"pageSize":15}
    test1=Testacd2().test_getuser(url1,body1)
    #print(test1)
    test2=Testacd2().test_getuser(url2,body2)
    Testacd2().testlogin()















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