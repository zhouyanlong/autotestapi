import openpyxl
from testtool.setconfig import Tool
from testtool import setting
from testtool.mylog import Log
from testtool.apiimport import import_data
class Read_Excel():

    def read_data(self,file=setting.testcasedir):
        #wb=openpyxl.load_workbook("../config/apicase.xlsx")
        apidata = import_data()
        print(apidata["packetName"])
        wb = openpyxl.load_workbook(file)
        sheet=wb["Sheet1"]
        test_data=[]
        flag=Tool().get_config("casemanage","num")
        try:
            for i in range(2, sheet.max_row + 1):
                module = sheet.cell(i, 1).value
                id = sheet.cell(i, 2).value
                usecase = sheet.cell(i, 3).value
                url = sheet.cell(i, 4).value
                header = sheet.cell(i, 6).value
                method = sheet.cell(i, 5).value
                body = sheet.cell(i, 7).value
                if body is not None:
                    if body.find("${packet_name}") != -1:
                        body = body.replace("${packet_name}", apidata["packetName"])
                    if body.find("${billcode}") != -1:
                        body = body.replace("${billcode}", apidata["billcode"])
                    if body.find("${customercode}") != -1:
                        body = body.replace("${customercode}", str(apidata["customercode"]))
                    if body.find("${idNumber}") != -1:
                        body = body.replace("${idNumber}", str(apidata["idNumber"]))
                    if body.find('${taskname}') != -1:
                        body = body.replace('${taskname}', str(apidata["taskname"]))
                    if body.find('${starttime}') != -1:
                        body = body.replace('${starttime}', str(apidata["starttime"]))
                    if body.find('${endtime}') != -1:
                        body = body.replace('${endtime}', str(apidata["endtime"]))
                    if body.find('${startDate}') != -1:
                        body = body.replace('${startDate}', str(apidata["startDate"]))

                code = sheet.cell(i, 8).value
                msg = sheet.cell(i, 9).value
                checkdata=sheet.cell(i,10).value
                if checkdata is not None:
                    if checkdata.find("${packet_name}") != -1:
                        checkdata = checkdata.replace("${packet_name}", apidata["packetName"])
                    if checkdata.find("${billcode}") != -1:
                        checkdata = checkdata.replace("${billcode}", apidata["billcode"])
                    if checkdata.find("${customercode}") != -1:
                        checkdata = checkdata.replace("${customercode}", str(apidata["customercode"]))
                    if checkdata.find("${idNumber}") != -1:
                        checkdata = checkdata.replace("${idNumber}", str(apidata["idNumber"]))
                    if checkdata.find('${taskname}') != -1:
                        checkdata = checkdata.replace('${taskname}', str(apidata["taskname"]))
                sqldata=sheet.cell(i,11).value
                if sqldata is not None:
                    if sqldata.find("${packet_name}") != -1:
                        sqldata = sqldata.replace("${packet_name}", apidata["packetName"])
                    if sqldata.find("${billcode}") != -1:
                        sqldata = sqldata.replace("${billcode}", apidata["billcode"])
                    if sqldata.find("${customercode}") != -1:
                        sqldata = sqldata.replace("${customercode}", str(apidata["customercode"]))
                    if sqldata.find("${idNumber}") != -1:
                        sqldata = sqldata.replace("${idNumber}", str(apidata["idNumber"]))
                    if sqldata.find('${taskname}') != -1:
                        sqldata = sqldata.replace('${taskname}', str(apidata["taskname"]))
                sqlassert = sheet.cell(i, 12).value
                if sqlassert is not None:
                    if sqlassert.find("${packet_name}") != -1:
                        sqlassert = sqldata.replace("${packet_name}", apidata["packetName"])
                    if sqlassert.find("${billcode}") != -1:
                        sqlassert = sqldata.replace("${billcode}", apidata["billcode"])
                    if sqlassert.find("${customercode}") != -1:
                        sqlassert = sqldata.replace("${customercode}", str(apidata["customercode"]))
                    if sqlassert.find("${idNumber}") != -1:
                        sqlassert = sqldata.replace("${idNumber}", str(apidata["idNumber"]))
                    if sqlassert.find('${taskname}') != -1:
                        sqlassert = sqldata.replace('${taskname}', str(apidata["taskname"]))
                data = {"module": module, "id": id,"usecase":usecase, "url": url, "headers": header, "method": method, "body": body,
                        "code": code, "msg": msg,"checkdata":checkdata,"sqldata":sqldata,"sqlassert":sqlassert}
                #print(data)
                if flag == "all":
                    test_data.append(data)
                # 从config获取到的值均为str，eval转成list
                elif id in eval(flag):
                    test_data.append(data)
        except Exception as e:
            Log().error(e)
        return test_data

    def write_excel(self,i,value,file=setting.testcasedir):
        wb=openpyxl.load_workbook(file)
        sheet=wb["Sheet1"]
        sheet.cell(i,13).value=value
        wb.save(file)

    def updata_excel(self,i,value,file=setting.testcasedir):
        wb=openpyxl.load_workbook(file)
        sheet=wb["Sheet1"]
        sheet.cell(i,11).value=value
        wb.save(file)


if __name__ == '__main__':
    test=Read_Excel().read_data()
    print(test[0]["checkdata"])
    # a=eval(test[0]['checkdata'])[0]
    # print(a)








