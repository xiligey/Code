package org.chenxilin.basic

import scala.annotation.tailrec

/**
 * Scala函数
 * - Scala普通函数
 * - Scala占位符语法
 * - Scala匿名函数
 * - Scala递归函数
 * - Scala高阶函数
 *    - map
 *    - 将一个对象方法作为高阶函数的参数
 *    - 将函数作为一个高阶函数的参数
 *    - 返回函数的函数
 */
object ScalaFunction {

  def main(args: Array[String]): Unit = {
    // # Scala普通函数
    {
      // ## 不带参数的普通函数
      def sayHello(): Unit = println("Hello")

      // ## 带参数的普通函数
      def saySomething(something: String): Unit = println(something)

      // ## 带默认参数的普通函数
      def saySomethingWithDefault(something: String = "Hi"): Unit = println(something)

      // ## 重复参数
      def sayThings(things: String*): Unit = things.foreach(println)
      // 重复参数的两种调用方式
      sayThings("1", "2", "3")
      sayThings(Array("a", "b", "c"): _*)
    }

    // # Scala占位符语法
    {
      val array1 = Array(1, 2, 3, 4, 5)
      // 以下两种方式等价
      array1.filter(_ % 2 == 0).foreach(println)
      array1.filter(x => x % 2 == 0).foreach(println)
    }

    // # Scala递归函数
    {
      def factorial(x: Int): Int = {
        @tailrec
        def fact(x: Int, accumulator: Int): Int = {
          if (x <= 1) accumulator else fact(x - 1, x * accumulator)
        }

        fact(x, 1)
      }

      println(factorial(2))
      println(factorial(10))
    }

    // # Scala高阶函数
    // 高阶函数是指使用其他函数作为参数、或者返回一个函数作为结果的函数。
    // 在Scala中函数是“一等公民”，所以允许定义高阶函数。
    // 这里的术语可能有点让人困惑，我们约定，使用函数值作为参数，或者返回值为函数值的“函数”和“方法”，均称之为“高阶函数”。
    {
      // ## scala map函数
      // 最常见的一个例子是Scala集合类（collections）的高阶函数map
      val array1 = Seq(1, 2, 3, 4, 5)
      val array2 = array1.map(_ + 1)
      array2.foreach(println)

      // ## 将一个对象方法作为高阶函数的参数
      case class Human(cities: Seq[String]) {
        private def addProvince(city: String) = "北京" + city

        // 可以传入一个对象方法作为高阶函数的参数，Scala编译器会将方法强制转换为一个函数
        def addProvinces(): Seq[String] = cities.map(addProvince)
      }
      val someone = Human(Seq("成都", "南京", "厦门"))
      println(someone.addProvinces())

      // ## 将函数作为一个高阶函数的参数
      // 使用高阶函数的一个原因是减少冗余的代码。
      // 比方说需要写几个方法以通过不同方式来提升员工工资，若不使用高阶函数，代码可能像这样

      object SalaryRaiser {
        def smallPromotion(salaries: List[Double]): List[Double] =
          salaries.map(salary => salary * 1.1)

        def greatPromotion(salaries: List[Double]): List[Double] =
          salaries.map(salary => salary * math.log(salary))

        def hugePromotion(salaries: List[Double]): List[Double] =
          salaries.map(salary => salary * salary)
      }

      // 注意到上边三个方法的差异仅仅是提升的比例不同
      // 为了简化代码，其实可以把重复的代码提到一个高阶函数中：
      object SalaryRaiser2 {

        private def promotion(salaries: List[Double], promotionFunction: Double => Double): List[Double] =
          salaries.map(promotionFunction)

        def smallPromotion(salaries: List[Double]): List[Double] =
          promotion(salaries, salary => salary * 1.1)

        def bigPromotion(salaries: List[Double]): List[Double] =
          promotion(salaries, salary => salary * math.log(salary))

        def hugePromotion(salaries: List[Double]): List[Double] =
          promotion(salaries, salary => salary * salary)
      }

      // 新的方法promotion有两个参数，薪资列表和一个类型为Double => Double的函数
      //（参数和返回值类型均为Double），返回薪资提升的结果。

      // ## 返回函数的函数
      // 有的时候需要生成一个返回函数的函数
      def urlBuilder(ssl: Boolean, domainName: String): (String, String) => String = {
        val schema = if (ssl) "https://" else "http://"
        (endpoint: String, query: String) => s"$schema$domainName/$endpoint?$query"
      }

      val domainName = "www.example.com"

      def getURL = urlBuilder(ssl = true, domainName)

      val endpoint = "users"
      val query = "id=1"
      val url = getURL(endpoint, query) // "<https://www.example.com/users?id=1>": String
      println(url)

      // 注意urlBuilder的返回类型是`(String, String) => String`，
      // 这意味着返回的匿名函数有两个String参数，返回一个String。
      // 在这个例子中，返回的匿名函数是
      // (endpoint: String, query: String) => s"<https://www.example.com/$endpoint?$query>"
    }
  }
}
