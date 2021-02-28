package org.chenxilin.basic.循环

/**
 * Scala While循环
 */
object ScalaWhile循环 {
  def main(args: Array[String]): Unit = {
    println(gcdLoop(128, 6540))
    doWhileLoop()
  }

  /** 使用while循环计算最大公约数 */
  def gcdLoop(x: Long, y: Long): Long = {
    var a = x
    var b = y
    while (a != 0) {
      val temp = a
      a = b % a
      b = temp
    }
    b
  }

  /** do while循环 */
  def doWhileLoop(): Unit = {
    var line = ""
    do {
      line = scala.io.StdIn.readLine("input:\n")
      println("Read: " + line)
    } while (line != "")
  }
}
