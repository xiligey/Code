package org.chenxilin.basic.读写

/**
 * Scala文件读写
 * - 从屏幕上读取用户输入
 * - 从文件上读取内容
 * - 读取csv文件
 * - 写入文本
 */
object ScalaFileIO {
  def main(args: Array[String]): Unit = {
    // readFromScreen()
    // readFromFile("/Users/chenxilin/Code/scala/src/main/scala/org/chenxilin/basic/io/ScalaFileIO.scala")
    // saveToFile("/Users/chenxilin/Code/scala/src/main/resources/1.txt")
    readFromCsv("/Users/chenxilin/Code/scala/src/main/resources/1.csv").foreach(_.foreach(println))
  }

  /** 从屏幕上读取用户输入 */
  def readFromScreen(): Unit = {
    import scala.io.StdIn
    val input = StdIn.readLine("Input something: ")
    println(s"You are typing: $input")
  }

  /** 从文件上读取内容 */
  def readFromFile(file: String): Unit = {
    import scala.io.Source
    val source = Source.fromFile(file)
    source.foreach(println)
    // 不要忘记关闭资源
    source.close()
  }

  def readFromCsv(file: String): Seq[Array[String]] = {
    import scala.io.Source
    val source = Source.fromFile(file)
    val csv = source.getLines().map(_.split(",")).toIndexedSeq
    source.close()
    csv
  }

  /** 写入文本 */
  def saveToFile(file: String): Unit = {
    import java.io.FileWriter
    val out = new FileWriter(file, true)
    out.write("123")
    out.write("\n")
    out.write("456")
    out.close()

  }
}
