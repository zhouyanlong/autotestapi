import logging
from testtool import setting
class Log():
    def get_log(self,level,msg,file=setting.logdir):
        #创建收集器
        mylog=logging.getLogger("接口测试")
        #设置收集的level
        mylog.setLevel("DEBUG")

        #设置输出到控制台
        sh=logging.StreamHandler()
        sh.setLevel("INFO")
        sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        mylog.addHandler(sh)

        #设置输出到日志文件
        fh=logging.FileHandler(file,encoding="UTF-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        mylog.addHandler(fh)
        if level=="DEBUG":
            mylog.debug(msg)
        elif level=="INFO":
            mylog.info(msg)
        elif level=="WARNING":
            mylog.warning(msg)
        elif level=="ERROR":
            mylog.error(msg)
        elif level=="CRITICAL":
            mylog.critical(msg)
        mylog.removeHandler(sh)
        mylog.removeHandler(fh)
        fh.close()
    def debug(self,msg):
        Log().get_log("DEBUG",msg)
    def info(self,msg):
        Log().get_log("INFO",msg)
    def warning(self,msg):
        Log().get_log("WARNING",msg)
    def error(self,msg):
        Log().get_log("ERROR",msg)
    def critical(self,msg):
        Log().get_log("CRITICAL",msg)
if __name__ == '__main__':
    Log().debug("debug")
    Log().info("info")
    Log().warning("warning")
    Log().error("error")
    Log().critical("critical")


