from testtool.setconfig import Tool
from pymysql import connect,cursors
from pymysql.err import OperationalError
from testtool.mylog import Log
host = Tool().get_config("mysqlconf","host")
port = Tool().get_config("mysqlconf","port")
user = Tool().get_config("mysqlconf","user")
password = Tool().get_config("mysqlconf","password")
class DB():
    def select(self,db,sql):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor
                                )
        except OperationalError as e:
            Log().error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        try:
            real_sql=sql
            cursor=self.conn.cursor()
            cursor.execute(real_sql)
            data = cursor.fetchall()[0]
            return data
        except Exception as e:
            Log().error("查询数据库结果错误{}".format(e))

            #cursor.commit()


    # 关闭数据库
    def close(self):
        self.conn.close()

if __name__ == '__main__':
    #sql='SELECT * FROM `biz_divisional_packet` WHERE created >"2021-03-06 16:03:41"; '
    sql="select remark from bill_contact_info_202103 where tel='13192293682' order by created desc limit 1"
    res=DB().select("bc",sql)
    print(res)
