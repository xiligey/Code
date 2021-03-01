package org.chenxilin.basic.面向对象编程

object Scala泛型类 {
  def main(args: Array[String]): Unit = {
    // 泛型类指可以接受类型参数的类。泛型类在集合类中被广泛使用。

    // # 1、定义一个泛型类
    // 泛型类使用 `[]` 来接受类型参数。
    class Stack[A] {
      private var elements: List[A] = Nil

      def push(x: A) {
        elements = x :: elements
      }

      def peek: A = elements.head

      def pop(): A = {
        val currentTop = peek
        elements = elements.tail
        currentTop
      }
    }
    // 上面的 Stack 类的实现中接受类型参数 A。 这表示其内部的列表，
    // var elements: List[A] = Nil，只能够存储类型 A 的元素。
    // 方法 def push 只接受类型 A 的实例对象作为参数(注意：elements = x :: elements 将
    // elements 放到了一个将元素 x 添加到 elements 的头部而生成的新列表中)。

    // # 2、使用一个泛型类
    // 要使用一个泛型类，需要将一个具体的类型放到方括号中。
    val stack = new Stack[Int]
    stack.push(1)
    stack.push(2)
    println(stack)
    // 上述实例对象 stack 只能接受整型值。然而，如果类型参数有子类型，子类型可以被传入：
    class Fruit
    class Apple extends Fruit
    class Banana extends Fruit

    val stack2 = new Stack[Fruit]
    val apple = new Apple
    val banana = new Banana

    stack2.push(apple)
    stack2.push(banana)

    // 注意：泛型类型的子类型是不可传导的。这表示如果我们有一个字母类型的栈 Stack[Char]，
    // 那它不能被用作一个整型的栈 Stack[Int]。否则就是不安全的，
    // 因为它将使我们能够在字母型的栈中插入真正的整型值。结论就是，
    // 只有当类型 B = A时， Stack[A] 是 Stack[B]
    // 的子类型才成立。因为此处可能会有很大的限制，
    // Scala 提供了一种 类型参数注释机制 用以控制泛型类型的子类型的行为。

  }
}
