package org.chenxilin.basic.流程控制

import java.io.{BufferedReader, InputStreamReader}
import scala.util.control.Breaks.{break, breakable}

object ScalaBreakContinue {
  def continueTest(): Unit = {
    val array = Array(1, 2, 3, 4, 5, 6)
    for (i <- array) {
      breakable(if (i != 3) println(i) else break)
    }
  }

  def main(args: Array[String]): Unit = {
    continueTest()
    // scala是没有break和continue的
    // 如果你想写一段类似如下java代码的功能
    //    while (i< args.length){
    //      if (args[i].startswith("-")){
    //        i = i + 1
    //        continue;
    //      }
    //      if (args[i].endsWith(".scala")) {
    //        foundIt = true;
    //        break;
    //      }
    //      i = i + 1
    //    }
    // 可以用以下scala代码代替：
    var i = 0
    var foundIt = false

    while (i < args.length && !foundIt) {
      if (!args(i).startsWith("-")) {
        if (args(i).endsWith(".scala"))
          foundIt = true
      }
      i = i + 1
    }

    // 如果想去掉var, 一种做法是将循环重写成递归的函数
    def searchForm(i: Int): Int = {
      if (i >= args.length) -1
      else if (args(i).startsWith("-")) searchForm(i + 1)
      else if (args(i).endsWith(".scala")) i
      else searchForm(i + 1)
    }

    //如果上述的方法依旧不能满足你对break的需求，scala标准库类中提供了以下方法：
    val in = new BufferedReader(new InputStreamReader(System.in))
    breakable {
      while (true) {
        println("?")
        if (in.readLine() == "") break
      }
    }

  }
}
