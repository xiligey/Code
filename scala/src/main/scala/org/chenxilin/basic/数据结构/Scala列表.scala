package org.chenxilin.basic.数据结构

/**
 * Scala 列表类似于数组，它们所有元素的类型都相同，但是它们也有所不同：
 * 列表是不可变的，值一旦被定义了就不能改变，其次列表 具有递归的结构（也就是链接表结构）而数组不是
 */
object Scala列表 {
  def main(args: Array[String]): Unit = {
    val site: List[String] = List("Jack", "Tom")
    val nums: List[Int] = List(1, 2, 3)
    val empty: List[Nothing] = List()
    val dim: List[List[Int]] = List(
      List(1, 1, 1),
      List(2, 3, 4)
    )

    // 构造列表的两个基本单位是Nil和::
    // Nil也可以表示为一个空列表
    val site2 = "Jack" :: "Rose" :: Nil

  }
}
