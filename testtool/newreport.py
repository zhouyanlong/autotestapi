import os
from testtool import setting
def new_report(testreport=setting.reportdir):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_list=[]
    file_new=os.path.join(testreport,lists[-1])
    file_list.append(file_new)
    file_admin=os.path.join(testreport,lists[-2])
    file_list.append(file_admin)
    return file_list



if __name__ == '__main__':
    a=new_report()
    print(a)
    for i in a:
        print(i)