package org.chenxilin.basic.正则表达式

object ScalaRE {
  def main(args: Array[String]): Unit = {
    val city = "SHANGHai"
    val pattern = "(?i)shanghai".r
    pattern.findAllIn(city).foreach(println)

    val name = "123CPU456"
    val highPriorList = Set(".*cpu.*", ".*db.*")
    for (highPrior <- highPriorList) {
      val pattern = highPrior.r
      if (pattern.findFirstIn(name).isDefined) println(s"$highPrior, 1")
    }
  }
}
