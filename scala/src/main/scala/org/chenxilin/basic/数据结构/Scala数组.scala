package org.chenxilin.basic.数据结构

import scala.collection.mutable.ArrayBuffer

object Scala数组 {
  def main(args: Array[String]): Unit = {
    val a = ArrayBuffer(1, 3, 2, 4, 20, 10, 15, 3, 8, 2, 7)

    // ++=
    a ++= Array(-1, -2, -3)
    println(a)
  }
}