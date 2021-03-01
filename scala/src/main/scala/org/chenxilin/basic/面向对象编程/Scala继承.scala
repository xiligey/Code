package org.chenxilin.basic.面向对象编程

/**
 * extend、final关键字和java一样
 * 重写方法必须用override
 * 只有主构造器可以调用超类的主构造器
 * 你可以重写字段
 */
class People {
  def toStr(a: Int): String = a.toString

}

class Student extends People {
  // 声明为final的类不能被扩展，同理方法和字段也是
  override def toStr(a: Int): String = super.toStr(a) + " "

  // 重写 def只能重写def、val只能重写val和不带参数的def、var只能重写var
}

object 继承 {
  def main(args: Array[String]): Unit = {
    val alien: People = new People {
      def sayHello(): Unit = println("Hello")
    }
  }
}
