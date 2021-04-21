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
    data={'url': 'https://ai.zhilingsd.com/api/business/login', 'headers':'{"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}','method': 'post', 'body': '{"account":"zhou3","password":"Aa123456.","platform":"robot"}'}
    res=requests.request(url=data["url"],method=data["method"],headers=eval(data["headers"]),data=data["body"],verify=False)
    re=res.json()
    session_data=re["data"]["session"]
    session={"session":session_data}
    Log().info("商户端获取到的session为{}".format(session))
    return session
def adminlogin():
    data = {'url': 'https://admintest.robot.com/api/manage/login',
            'headers': '{"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}',
            'method': 'post', 'body': '{"account":"zhouyanlong1","password":"Aa123456@"}'}
    res = requests.request(url=data["url"], method=data["method"], headers=eval(data["headers"]), data=data["body"],verify=False)
    re = res.json()
    session_data = re["data"]["session"]
    session = {"session": session_data}
    Log().info("管理端获取到的session为{}".format(session))
    return session

if __name__ == '__main__':
    login()
    adminlogin()
