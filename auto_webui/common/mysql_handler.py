#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pymysql
from pymysql.cursors import DictCursor


class MysqlHandler():
    def __init__(
            self,
            host=None,
            port=3306,
            user=None,
            password=None,
            charset='utf8',
            cursorclass=DictCursor
    ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass
        )
        self.cursor = self.conn.cursor()

    def query(self, sql, one=True):
        self.conn.commit() # 把最新的数据进行更新（提交事务。）
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def query_all(self):
        pass

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = MysqlHandler(
        host="120.78.128.25",
        port=3306,
        user="future",
        password="123456",
        charset='utf8',
        cursorclass=DictCursor
    )

    data = db.query("SELECT * FROM futureloan.member WHERE mobile_phone={} LIMIT 10;".format(13120208090))
    print(data)