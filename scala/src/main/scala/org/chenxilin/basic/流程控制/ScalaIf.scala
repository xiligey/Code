package org.chenxilin.basic.流程控制

object ScalaIf {
  def main(args: Array[String]): Unit = {
    if (args.isEmpty) {
      println("运行参数为空")
    }

    var filename = "default.txt"
    if (!args.isEmpty) {
      filename = args(0)
    }

    // 上边这段代码可以写的更精简
    val filename2 = if (!args.isEmpty) args(0) else "default.txt"


    val a = {
      if (1 > 0) {
        val b = 10
        b + 1
      } else {
        val c = 2
        c + 2
      }
    }
    println(a)
  }
}
