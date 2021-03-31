import time
import datetime
def import_data():
    method="post"
    url = "http://192.168.18.140:8120/bill/open/importBillByInterface"
    header = {"Accept": "application/json, text/plain,*/*", "Accept-Encoding": "gzip, deflate, br",
              "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive", "Content-Length": "61",
              "Content-Type": "application/json", "Host": "test.robotsh.com", "Origin": "https://test.robotsh.com",
              "Referer": "https://test.robotsh.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors",
              "Sec-Fetch-Site": "same-origin",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
              "session": "00000000-0000-0000-0000-000000000000", "operatorId": "1453396611397713920",
              "merchantId": "1453396611397713920", "account": "zhou3"}
    limitDate = time.strftime("%Y/%m/%d", time.localtime())
    num1 = time.strftime("%Y%m%d%H%M%S", time.localtime())

    now = datetime.datetime.now()
    starttime = str(now.strftime('%Y-%m-%d')) + " 00:00:00"
    dif = datetime.timedelta(days=0)
    tomorrow = now - dif
    endtime = tomorrow.strftime('%Y-%m-%d')
    endtime += " 23:59:59"
    startDate=now.strftime('%Y-%m-%d')
    code = num1
    packetName = "test委案" + str(num1)
    idNumber=int(str(3600)+str(code))
    taskname="任务"+str(num1)
    body = {
        "merchantId": 1453396611397713920,
        "operatorId": 1453396611397713920,
        "packetName": packetName,
        "productCode": "testnewcode",
        "valueHeadNameMap": {
            "0": "packetMerCode",
            "1": "overdueDay",
            "2": "commitMoney",
            "3": "commitDate",
            "4": "limitDate",
            "5": "currency",
            "6": "name",
            "7": "age",
            "8": "sex",
            "9": "idType",
            "10": "idNumber",
            "11": "firstPhone",
            "12": "secondPhone",
            "13": "homePhone",
            "14": "companyPhone",
            "15": "customerMerCode",
            "16": "registeredProvince",
            "17": "registeredCity",
            "18": "registeredAddress",
            "19": "marriageStatus",
            "20": "educationLevel",
            "21": "annualIncome",
            "22": "account",
            "23": "card",
            "24": "cashAmount",
            "25": "overdueDate",
            "26": "minRepaymentAmount",
            "27": "enterBillCode",
            "28": "limitRepayDate",
            "29": "thirdProductName"

        },
        "valueList": [
            {
                "0": code,
                "1": "10",
                "2": "1111",
                "3": "2021/3/10",
                "4": limitDate,
                "5": "人民币",
                "6": "周彦龙",
                "7": "24",
                "8": "男",
                "9": "身份证",
                "10": idNumber,
                "11": "13192293682",
                "12": "13192293682",
                "13": "13192293682",
                "14": "13192293682",
                "15": "7777",
                "16": "江西",
                "17": "鹰潭",
                "18": "余江区",
                "19": "未婚",
                "20": "本科",
                "21": "8888",
                "22": "147",
                "23": "258",
                "24": "111",
                "25": "2020/11/1",
                "26": "500",
                "27": "11",
                "28": "2020/11/12",
                "29": "产品111"
            }
        ]
    }
    print("进件号:"+code)
    print("逾期日期："+limitDate)
    billcode=str(code)+str(code)+"11"
    print("billcode:"+billcode)
    customercode="周彦龙"+str(idNumber)
    print("customercode:"+customercode)
    data = { "url": url, "headers": header, "method": method,"body": body,"code":code,"billcode":billcode,"idNumber":idNumber,"customercode":customercode,"packetName":packetName,"taskname":taskname,"starttime":starttime,"endtime":endtime,"startDate":startDate}
    print(data)
    return data
if __name__ == '__main__':
    import_data()
    # id = getattr(Import(), "idNumber")
    # print(id)
    # id1 = int(id) + 1
    # i=Import()
    # setattr(i, "idNumber", id1)
    # print(getattr(i, "idNumber"))
