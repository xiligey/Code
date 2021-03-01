package org.chenxilin.basic.数据结构


import java.text.SimpleDateFormat
import java.util.{Calendar, Date}

object Scala日期 {
  def main(args: Array[String]): Unit = {
    // 时间戳转时间
    val timestamp = 1571501220000L
    val fm = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    val t = new Date(timestamp)
    val time = fm.format(t)
    println(time)
    println(getDayOfWeek())
    println(getYearOfTimeStamp(1591231231233L))
  }

  /** 根据时间戳计算今天是周几 1->周一 7->周日 */
  def getDayOfWeek(timestamp: Long = System.currentTimeMillis): Int = {
    val ts = timestamp.toString.length match {
      case 10 => timestamp * 1000
      case 13 => timestamp
      case _ => throw new Exception("时间戳长度为10或13")
    }
    val m = Map(1 -> 7, 2 -> 1, 3 -> 2, 4 -> 3, 5 -> 4, 6 -> 5, 7 -> 6)
    val calendar = Calendar.getInstance()
    val date = new Date(ts)
    calendar.setTime(date)
    val n = calendar.get(Calendar.DAY_OF_WEEK)
    m(n)
  }

  def getYearOfTimeStamp(timestamp: Long): Int = {
    val calendar = Calendar.getInstance()
    val date = new Date(timestamp)
    calendar.setTime(date)
    val year = calendar.get(Calendar.DAY_OF_MONTH)
    year
  }


}