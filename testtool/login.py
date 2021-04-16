import sys,os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from testtool.mylog import Log
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def login():
    requests.packages.urllib3.disable_warnings()
    data={'url': 'https://test.robotsh.com/api/business/login', 'headers':{
    "Accept": "application/json, text/plain,*/*",
    "Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "61",
"Content-Type": "application/json",
"Host": "test.robotsh.com",
"Origin": "https://test.robotsh.com",
"Referer": "https://test.robotsh.com/",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-origin",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
}, 'method': 'post', 'body': '{"account":"zhou3","password":"Aa123456.","platform":"robot"}',"proxies":{"http":None,"https":None}}
    res=requests.request(url=data["url"],method=data["method"],headers=data["headers"],data=data["body"],verify=False,proxies=data["proxies"])
    re=res.json()
    session_data=re["data"]["session"]
    session={"session":session_data}
    Log().info("商户端获取到的session为{}".format(session))
    return session
def adminlogin():
    data = {'url': 'https://admintest.robot.com/api/manage/login',
            'headers': '{"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}',
            'method': 'post', 'body': '{"account":"zhouyanlong1","password":"Aa123456@"}',"proxies":{"http":None,"https":None}}
    res = requests.request(url=data["url"], method=data["method"], headers=eval(data["headers"]), data=data["body"],verify=False,proxies=data["proxies"])
    re = res.json()
    session_data = re["data"]["session"]
    session = {"session": session_data}
    Log().info("管理端获取到的session为{}".format(session))
    return session

if __name__ == '__main__':
    login()
    adminlogin()
