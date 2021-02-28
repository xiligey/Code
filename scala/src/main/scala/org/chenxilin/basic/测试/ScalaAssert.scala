package org.chenxilin.basic.测试

/**
 * Scala中，断言的写法是对预定义方法assert的调用，有两种调用方式：
 *   - assert(condition: Boolean)
 *   - assert(condition: Boolean, explanation: Any)
 *     如果不满足condition表达式，第一种将跑出AssertionError，第二种将抛出包含给定explanation的AssertionError
 *
 * 还有更精简的方式来断言：ensuring。 这个方法可以被用于任何结果类型。
 * 如果前提条件返回false 将抛出AssertionError
 * 如果前提条件返回true，则正常返回结果
 */
object ScalaAssert {
  val N = 1

  def main(args: Array[String]): Unit = {
    val a = 1
    val b = 2
    assert(a < b)
    // assert(a > b, "a <= b")
    println(f(0))
    //println(f(1)) // 当x=1时 ensuring判断前提条件为false 则引发AssertionError

  }

  def f(x: Int): Int = {
    if (x < N)
      x
    else
      x + 1 ensuring (x != 0)
  }
}
