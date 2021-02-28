package org.chenxilin.basic.数据库

import java.sql.{Date, DriverManager}

object ScalaMySql {
  def main(args: Array[String]): Unit = {
    val mysqlConf = Map(
      "driver" -> "com.mysql.jdbc.Driver",
      "url" -> "jdbc:mysql://127.0.0.1:3306/dmp?useSSL=false",
      "username" -> "root",
      "password" -> "666666"
    )
    Class.forName(mysqlConf("driver"))
    val conn = DriverManager.getConnection(mysqlConf("url"), mysqlConf("username"), mysqlConf("password"))

    val sql1 = conn.prepareStatement("UPDATE w_cdh_app_netbrd SET rnum = ?,rnet0=?,rnet1=?,rnet2=?," +
      "rnet3=?,rnet4=?,rnet5=?,rsim0=?,rsim1=?,ropt0=?,ropt1=?,ropt2=?,ropt3=?,osv00=?,osv01=?,osv02=?,osv03" +
      "=?,osv04=?,osv05=?,osv06=?,brd00=?,brd01=?,brd02=?,brd03=?,brd04=?,brd05=?,brd06=?,brd07=?,brd08=?" +
      ",brd09=?,brd10=?,brd11=?,brd12=?,brd13=? WHERE sdate = ? and appid=?;")

    val sql = conn.prepareStatement("REPLACE INTO w_cdh_app_netbrd (rnum,rnet0,rnet1,rnet2,rnet3,rnet4,rnet5," +
      "rsim0,rsim1,ropt0,ropt1,ropt2,ropt3,osv00,osv01,osv02,osv03,osv04,osv05,osv06,brd00,brd01,brd02,brd03,brd04," +
      "brd05,brd06,brd07,brd08,brd09,brd10,brd11,brd12,brd13,sdate,appid) VALUES " +
      "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")

    for (i <- 1 to 34)
      sql.setInt(i, 100)
    sql.setDate(35, new Date(119, 5, 15))
    sql.setInt(36, 2)
    sql.executeUpdate()
    print(sql)
    conn.close()

  }
}
