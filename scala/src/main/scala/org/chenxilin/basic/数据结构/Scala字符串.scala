package org.chenxilin.basic.数据结构

object Scala字符串 {
  def main(args: Array[String]): Unit = {
    println("abc123".startsWith("abcabcd"))

    "12.3.4..5.6".split("\\.").foreach(println)
  }

}
