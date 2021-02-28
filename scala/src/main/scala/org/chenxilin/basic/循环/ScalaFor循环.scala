package org.chenxilin.basic.循环

object ScalaFor循环 {
  def main(args: Array[String]): Unit = {
    // 一般用法
    val filesHere = new java.io.File(".").listFiles
    for (file <- filesHere)
      println(file)

    // 过滤
    for (i <- 1 to 10 if i % 2 == 0) //单个过滤条件
      println(i)

    for (
      i <- 1 to 10 // 多个过滤条件
      if i % 2 == 0
      if i >= 3
    ) println(i)

    // 嵌套迭代
    for (i <- 1 to 5; j <- 6 to 10)
      println(i * j)

    // 中途变量绑定
    for (
      i <- 1 to 5;
      j <- 6 to 10;
      k = j + 1
      if k > 7
    ) println(i, j, k)

    // 产生一个新的集合
    val array = for (i <- 1 to 5) yield i ^ 2
    println(array)
  }
}
