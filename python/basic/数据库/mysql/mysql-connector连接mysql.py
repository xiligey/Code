import mysql.connector


def execute(sql, user, password, host, database):
    conn = mysql.connector.connect(user, password, host, database)
    cursor = conn.cursor()
    sql = "select * from table limit 10"
    cursor.execute(sql)
    values = cursor.fetchall()  # 所有执行结果
    conn.close()  # 关闭连接
    return values


def main():
    user, password, host, database = "mysql_user", "Mysql_123", "39.96.116.227", "chenxilin"
    sql = "select * from c_cumu limit 10"
    values = execute(sql, user, password, host, database)
    for value in values:
        print(value)


if __name__ == '__main__':
    main()
