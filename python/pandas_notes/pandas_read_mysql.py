import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymysql

conn = pymysql.connect(host="39.107.52.113",
                       user="mysql_user",
                       db="dmp",
                       passwd="Mysql_123")

data = pd.read_sql("select * from w_cdh_app_daydata", conn)

conn.close()
