import configparser
from testtool import setting
class Tool():
    def get_config(self,option,key,file=setting.configdir):
        cf=configparser.ConfigParser()
        #cf.read("../config/config.ini",encoding="UTF-8")
        #cf.read(r"D:\pycharm\testautoapi\venv\config\config.ini", encoding="UTF-8")
        cf.read(file, encoding="UTF-8")
        con=cf.get(option,key)
        return con









if __name__ == '__main__':
    #T=Tool().get_config("tester","name")
    T = Tool().get_config("casemanage", "num")
    print(T,type(T))
