from testtool.setconfig import Tool
from testtool import setting
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from testtool.mylog import Log
def send_mail(file):
    f = open(file,'rb')
    mail_body = f.read()
    f.close()
    # --------- 读取config.ini配置文件 ---------------
    HOST = Tool().get_config("user","HOST_SERVER")
    SENDER = Tool().get_config("user","FROM")
    RECEIVER = Tool().get_config("user","TO")
    USER = Tool().get_config("user","user")
    PWD = Tool().get_config("user","password")
    SUBJECT = Tool().get_config("user","SUBJECT")

    msg = MIMEText(mail_body, "html", "utf-8")
    msg['Subject'] = Header(SUBJECT, "utf-8")
    msg['from'] = SENDER
    msg['to'] = RECEIVER

    try:
        server=smtplib.SMTP()
        server.connect(HOST)
        server.login(USER,PWD)
        server.sendmail(SENDER,RECEIVER,msg.as_string())
        server.quit()
        Log().info("邮件发送成功！")
    except Exception as  e:
        Log.error("失败: " + str(e))
if __name__ == '__main__':
    send_mail()
