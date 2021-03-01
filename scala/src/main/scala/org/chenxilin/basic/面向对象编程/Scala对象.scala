package org.chenxilin.basic.面向对象编程

/**
 * 用对象作为单例存放工具方法
 * 类可以拥有一个同名的伴生对象
 * 对象可以扩展类或特质
 * 对象的apply方法通常用来构造伴生类的新实例
 * 如果不想显示定义main，可以用扩展App特质的对象
 * 你可以通过扩展Enumeration来实现枚举
 */
object 对象 extends Undo("Do Nothing") { //为class对象的半生对象
  // 对象的构造器在对象第一次被使用时调用，如果一个对象从未使用，其构造器也从未被执行

  //scala中没有静态字段、静态方法，你可以通过object这个语法结构来达到同样目的
  private var lastNumber = 0

  def main(args: Array[String]): Unit = {
    println(Color.Green)
    println(Color.withName("Red"))
    println(Color(0))
  }

  def newUniqueNumber(): Int = {
    lastNumber += 1;
    lastNumber
  }

  def apply(): 对象 = {
    new 对象()
  }

  override def undo(): Unit = {}

  override def redo(): Unit = {}
}

//在Java中经常会有既有实例方法又有静态方法的类，scala中可以通过类与类同名的伴生对象来达到同样的目的
// 类和对象需在一个文件中，可以互相访问私有特性
class 对象 {

}

abstract class Undo(val description: String) {
  def undo(): Unit

  def redo(): Unit
}

object Color extends Enumeration { //枚举类
  val Red, Yellow, Green = Value
}
