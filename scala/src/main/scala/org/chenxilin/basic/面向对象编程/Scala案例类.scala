package org.chenxilin.basic.面向对象编程

object Scala案例类 {
  def main(args: Array[String]): Unit = {
    // # 1、定义一个case class
    // 一个最简单的case class定义由关键字 case class，类名，参数列表（可为空）组成：
    case class Book(isbn: String)
    val frankenstein = Book("978-0486282114")
    println(frankenstein.isbn)
    // 注意在实例化case class Book时，并没有使用关键字 new，
    // 这是因为case class有一个默认的 apply方法来负责对象的创建。
    // 当你创建包含参数的case class时，这些参数是公开（public）的 val :
    case class Message(sender: String, recipient: String, body: String)

    val message1 = Message("guillaume@quebec.ca", "jorge@catalonia.es", "Ça va ?")

    println(message1.sender) // prints guillaume@quebec.ca
    // 错误代码 -> message1.sender = "travis@washington.us"
    // 不能给 message1.sender 赋值，因为是 message1.sender 是 val 。
    // 在case class中使用 var 也是可以的，但不推荐这样做。

    // # 2、比较两个case class
    val message2 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
    val message3 = Message("jorge@catalonia.es", "guillaume@quebec.ca", "Com va?")
    println(message2 == message3) // true
    // 比较 case class  时是按照值比较而不是按照引用比较。
    // 尽管 `message2`和 `message3`引用不同的对象，但是他们的值是相等的，所以 `message2 == message3`为 `true`

    // # 3、拷贝一个case class
    // 通过 copy方法创建一个案例类实例的浅拷贝，同时可以指定构造参数来做一些改变:
    val message4 = Message("julien@bretagne.fr",
      "travis@washington.us",
      "Me zo o a gant ma b")
    val message5 = message4.copy(
      sender = message4.recipient,
      recipient = "claire@bourgogne.fr"
    )
    println(message5.sender) // travis@washington.us
    println(message5.recipient) // claire@bourgogne.fr
    println(message5.body) // "Me zo o a gant ma b"
    // 上述代码指定`message4`的`recipient`作为`message5`的`sender`，指定`message5`的`recipient`为”claire@bourgogne.fr”，
    // 而`message4`的`body`则是直接拷贝作为`message5`的`body`了
  }
}
