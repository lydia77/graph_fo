from common.DbCommon import mysql2pd
import pandas as pd
import configparser
conf_file='../common/db.conf'
conf = configparser.ConfigParser()
conf.read(conf_file)
conn=mysql2pd(conf.get('db','host'),conf.get('db','port'),conf.get('db','db'),conf.get('db','user'),conf.get('db','pwd'))
# data=conn.getdata('person_para')
data=conn.doget('select * from person_para limit 20')
data.to_csv('../data/res.csv',encoding='utf8')
# print(data.head(10))