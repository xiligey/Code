package org.chenxilin.basic.面向对象编程

trait Logger {
  def log(msg: String) // 特质中未被实现的方法默认是抽象方法

  def sayHello(): Unit = println("Hello") // 特质中的方法不一定就是是抽象的，也可以具体实现
}

/** 子类继承特质，必须要实现其中的抽象方法，非抽象方法可以不重写也可以重写 */
class ConsoleLogger extends Logger {
  override def log(msg: String): Unit = println(msg)

  override def sayHello(): Unit = println("Hi")
}

/** 子类继承多个特质，第一个用extends，后续的用with */
class MyConsoleLogger extends Logger with Cloneable with Serializable {
  override def log(msg: String): Unit = println(msg)
}

object Scala特质 {
  def main(args: Array[String]): Unit = {
    val myConsoleLogger = new MyConsoleLogger with Logger // 创建对象时可以直接（使用with）添加特质
  }
}
