# coding:utf-8
from flask import Flask  # 默认
import MySQLdb
# app入口定义
app = Flask(__name__)
#链接数据库
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='ca2')
#建立操作游标
cursor=conn.cursor()
#设置数据输入输出编码格式
cursor.execute('set names utf8')
