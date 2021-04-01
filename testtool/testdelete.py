import requests
import json
import pandas
import time
import datetime

"""url1 = "https://robotmeracd.zhilingsd.com/api/login"
body1 = {"userAccount": "sclj02", "password": "Aa123456."}
h1 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
s=requests.session()
res1 = s.request(url=url1, headers=h1, method="post", data=json.dumps(body1), verify=False)
print(res1.json(),res1.cookies)


url="https://robotmeracd.zhilingsd.com/api/robot/user/getSubUserList"
body={"currentPage":1,"pageSize":15}
h2 = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
res2 = s.request(url=url, headers=h2, method="post", data=json.dumps(body), verify=False)
print(res2.json(), res2.cookies)"""

"""url="https://ai.zhilingsd.com/api/business/login"
h={"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}
body={"account":"zhouyanlong","password":"Aa123456.","platform":"robot"}
s=requests.session()
res=s.request(url=url,headers=h,method="post",data=json.dumps(body),verify=False).json()
print(res)

url1="https://ai.zhilingsd.com/api/route/rest"
h1={"Content-Type": "application/json;charset=UTF-8","Accept": "application/json, text/plain, */*"}
body1={"method":"business_manager_batch_list","v":"1.0","timestamp":"2021-03-14 13:36:18","data":{"currentPage":1,"pageSize":15}}
res1=s.request(url=url1,headers=h1,method="post",data=json.dumps(body1),verify=False).json()
print(res1)"""

#pandas处理数据
df=pandas.read_excel("../config/apicase.xlsx",sheet_name="Sheet1")
#print(df.values)
#print(df.ix[1,1])
# num1=time.strftime("%Y%m%d%H%M%S", time.localtime())
# print(num1)
#
#
# def increase():
#     id = getattr(Import(),"idNumber")
#     print(id)
#     id1 = id + 1
#     setattr(Import(),"idNumber",id1)
#     return getattr(Import(),"idNumber")
#
#
# if __name__ == '__main__':
#     print(increase())


# data={'module': '委案批次', 'id': 7, 'usecase': '查询名称', 'url': 'https://test.robotsh.com/api/route/rest', 'headers': '{\n    "Accept": "application/json, text/plain,*/*",\n    "Accept-Encoding": "gzip, deflate, br",\n"Accept-Language": "zh-CN,zh;q=0.9",\n"Connection": "keep-alive",\n"Content-Length": "61",\n"Content-Type": "application/json",\n"Host": "test.robotsh.com",\n"Origin": "https://test.robotsh.com",\n"Referer": "https://test.robotsh.com/",\n"Sec-Fetch-Dest": "empty",\n"Sec-Fetch-Mode": "cors",\n"Sec-Fetch-Site": "same-origin",\n"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"\n}', 'method': 'post', 'body': '{\n    "method": "bill_manage_query_packet_page",\n    \n    "v": "1.0",\n    "timestamp": "2020-12-03 11:39:40",\n    "data": {\n        "currentPage": 1,\n        "pageSize": 15,\n        "packetName": "${packet_name}"\n    }\n}', 'code': '1', 'msg': None, 'checkdata': '["packetName","${packet_name}"]', 'sqldata': None, 'sqlassert': None}
# if data["body"].find("${packet_name}")!=-1:
#     print("1")
#     a=str(data["body"]).replace("${packet_name}","gggg")
#     print(a)
#
# now=datetime.datetime.now()
# starttime = str(now.strftime( '%Y-%m-%d' ))+" 00:00:00"
# dif = datetime.timedelta( days = 0 )
# tomorrow = now - dif
# endtime=tomorrow.strftime( '%Y-%m-%d' )
# endtime+= " 23:59:59"
# print(starttime)
# print(endtime)
# print(now.strftime('%Y-%m-%d'))


d=time.strftime("%Y%m%d%H%M%S", time.localtime())
print(type(d))