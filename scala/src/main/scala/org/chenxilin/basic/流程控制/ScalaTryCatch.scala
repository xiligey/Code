package org.chenxilin.basic.流程控制

import java.io.{FileNotFoundException, FileReader, IOException}
import java.net.{MalformedURLException, URL}

object ScalaTryCatch {
  def main(args: Array[String]): Unit = {
    // 抛出异常
    val n = 4 // 改成3则会抛出异常
    val half = if (n % 2 == 0) n / 2 else throw new RuntimeException("n must be even")
    println(half)

    // 捕获异常
    try {
      val f = new FileReader("input.txt")
    } catch {
      case ex: FileNotFoundException => println("File not found.") //处理找不到文件的情况
      case ex: IOException => println("IO error.") // 处理其他情况
    }

    // finally子句
    val file = new FileReader("D:\\Code\\Scala\\Scala_Notes\\src\\main\\scala\\流程控制\\Try表达式.scala")
    try {
      // 使用文件
    } finally file.close() // 确保文件关闭

    // 交出值
    def url(path: String): URL =
      try {
        new URL(path)
      } catch {
        case e: MalformedURLException => new URL("http://www.scala-lang.org")
      }

    println(url("http://www.baidu.com"))

    // 注意：最好避免在finally子句中返回值
    def f(): Int = try 1 finally return 2 // 2
    def g(): Int = try 1 finally 2 // 1
    println(f(), g())

  }
}
