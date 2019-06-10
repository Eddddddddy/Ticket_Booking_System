# -*- coding:utf-8 -*-

import pymssql


class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode('utf-8'))
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql.encode('utf-8'))
        self.conn.commit()
        self.conn.close()

# ms = MSSQL(host="localhost", user="", pwd="", db="airplane")
# reslist = ms.ExecQuery("select * from passenger")
# for i in reslist:
#     print(i)
#
# newsql = "update passenger set name='%s' where ID=130203199903202114" % u'王定一'
# print(newsql)
# ms.ExecNonQuery(newsql)
