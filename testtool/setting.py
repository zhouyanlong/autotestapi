import os,sys
#testdir获取项目路径
testdir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(testdir)

configdir=os.path.join(testdir,"config","config.ini")
testcasedir=os.path.join(testdir,"config","apicase.xlsx")
reportdir=os.path.join(testdir,"report")
logdir=os.path.join(testdir,"log","log.txt")
testpydir=os.path.join(testdir,"testcase")
