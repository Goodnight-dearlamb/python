#!/usr/bin/env pytho
# -*- coding:utf-8 -*-
# import pymysql

class PDO(object):
    """docstring for PDO."""
    # 初始化连接
    def __init__(self, host="127.0.0.1", user="root", password="", database="demo", charset="utf8", port=3310):
        try:
            self.connect = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset)
            self.cursor = self.connect.cursor()
            print("> 数据库连接成功")
        except Exception as e:
            print("> 数据库连接失败！")
            exit(e)

    # 插入数据
    def insert_db(this, table, data):
        print("> 正在将数据记录到" + table + "表中")
        # print(data)
        field = ""
        values = ""
        for value in data:
            field = field + str(value) + ","
            values = values + str(data[value]) + ","
        # sql = "insert into" + table + "values" + data;
        field = field[:-1]
        values = values[:-1]
        print(field)
        print(values)
