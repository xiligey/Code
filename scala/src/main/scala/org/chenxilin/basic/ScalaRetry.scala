package org.chenxilin.basic

import scala.annotation.tailrec

object ScalaRetry {
  @tailrec
  def retry[T](n: Int)(fn: => T): T = {
    try {
      fn
    } catch {
      case e: Throwable =>
        if (n > 1) retry(n - 1)(fn)
        else throw e
    }
  }

  def main(args: Array[String]): Unit = {
    retry(3) {
      println(1 / 0)
    }
  }
}
