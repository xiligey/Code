package org.chenxilin.basic.面向对象编程

object Scala类型上下界 {
  def main(args: Array[String]): Unit = {
    // Scala中，类型参数和抽象类型都可以有一个类型边界约束。
    // 这种类型边界在限制类型变量实际取值的同时还能展露类型成员的更多信息。
    // 比如像 T <: A 这样声明的类型上界表示类型变量 T 应该是类型 A 的子类。

    // 下面例子展示了类 PetContainer 的一个类型参数的类型上界：
    {
      abstract class Animal {
        def name: String
      }

      abstract class Pet extends Animal {}

      class Cat extends Pet {
        override def name: String = "Cat"
      }

      class Dog extends Pet {
        override def name: String = "Dog"
      }

      class Lion extends Animal {
        override def name: String = "Lion"
      }

      class PetContainer[P <: Pet](p: P) {
        def pet: P = p
      }

      val dogContainer = new PetContainer[Dog](new Dog)
      val catContainer = new PetContainer[Cat](new Cat)

      // 以下代码不能编译
      val lionContainer = new PetContainer[Lion](new Lion)

      // 类`PetContainer`接受一个必须是`Pet`子类的类型参数`P`。
      // 因为`Dog`和`Cat`都是`Pet`的子类，所以可以构造`PetContainer[Dog]`和`PetContainer[Cat]`。
      // 但在尝试构造`PetContainer[Lion]`的时候会得到下面的错误信息：
      // `type arguments [Lion] do not conform to class PetContainer's type parameter bounds [P <: Pet]`
      // 这是因为`Lion`并不是`Pet`的子类。
    }

    // 类型上界将类型限制为另一种类型的子类型，而 *类型下界* 将类型声明为另一种类型的超类型。
    // 术语 `B >: A` 表示类型参数 `B` 或抽象类型 `B` 是类型 `A` 的超类型。
    // 在大多数情况下，`A` 将是类的类型参数，而 `B` 将是方法的类型参数。
    //
    // 下面看一个适合用类型下界的例子：
    {
      trait Node[+B] {
        def prepend(elem: B): Node[B]
      }

      case class ListNode[+B](h: B, t: Node[B]) extends Node[B] {
        def prepend(elem: B): ListNode[B] = ListNode(elem, this)

        def head: B = h

        def tail: Node[B] = t
      }

      case class Nil[+B]() extends Node[B] {
        def prepend(elem: B): ListNode[B] = ListNode(elem, this)
      }
    }
    // 上述程序实现了一个单链表。 `Nil` 表示空元素（即空列表）。
    // `class ListNode` 是一个节点，它包含一个类型为 `B` (`head`) 的元素和一个对列表其余部分的引用 (`tail`)。
    // `class Node` 及其子类型是协变的，因为我们定义了 `+B`。
    //
    // 但是，这个程序 *不能* 编译，因为方法 `prepend` 中的参数 `elem` 是*协*变的 `B` 类型。
    // 这会出错，因为函数的参数类型是*逆*变的，而返回类型是*协*变的。
    //
    // 要解决这个问题，我们需要将方法 `prepend` 的参数 `elem` 的型变翻转。
    // 我们通过引入一个新的类型参数 `U` 来实现这一点，该参数具有 `B` 作为类型下界。
    {
      trait Node[+B] {
        def prepend[U >: B](elem: U): Node[U]
      }

      case class ListNode[+B](h: B, t: Node[B]) extends Node[B] {
        def prepend[U >: B](elem: U): ListNode[U] = ListNode(elem, this)

        def head: B = h

        def tail: Node[B] = t
      }

      case class Nil[+B]() extends Node[B] {
        def prepend[U >: B](elem: U): ListNode[U] = ListNode(elem, this)
      }
      // 现在我们像下面这么做, 就可以为 Node[Bird] 赋值 africanSwallowList，
      // 然后再加入一个 EuropeanSwallow。
      trait Bird
      case class AfricanSwallow() extends Bird
      case class EuropeanSwallow() extends Bird

      val africanSwallowList = ListNode[AfricanSwallow](AfricanSwallow(), Nil())
      val birdList: Node[Bird] = africanSwallowList
      birdList.prepend(EuropeanSwallow())
    }
  }
}
