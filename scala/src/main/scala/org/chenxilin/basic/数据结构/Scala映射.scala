package org.chenxilin.basic.数据结构


import java.awt.Font
import java.util

/**
 * 1、构造映射
 * 2、获取映射中的值
 * 3、更改映射中的值
 * 4、迭代映射
 * 5、已排序映射
 * 6、与Java的互操作
 */

object Scala映射 {
  def main(args: Array[String]): Unit = {
    //1、构造映射
    val major = new scala.collection.immutable.HashMap[String, String]
    println(major)
    val scores = Map("Jack" -> 88, "Rose" -> 89) // 不可变映射（该映射的值不可变）
    println(123123123)
    println(scores - "Jack")
    val scores2 = Map(("Jack", 88), ("Rose", 89)) // 另一种方式构建不可变映射
    val cities = new scala.collection.mutable.HashMap[String, String]
    // mutable.HashMap[String, String] // 空的可变映射
    cities.put("Sandy", "NewYork")

    //2、获取映射中的值
    println(scores("Jack")) // 返回88 Jack对应Value，若Jack不存在，则引发异常
    println(scores.get("Jack")) // 返回Option对象 Some(88), 若Jack不存在，则引发异常
    println(scores.getOrElse("Tom", 100)) // 若Tom不存在，则返回100; 若存在则返回Tom对应value
    println(scores.contains("Tom")) // 检查映射中是否有某个指定的键，true/false
    println(scores.get("Jack") match { case Some(x) => x })

    //3、更改映射
    println(cities)
    cities("Sindy") = "BeiJing" // 修改某个键的value
    println(cities)
    cities += ("Andy" -> "ShangHai", "Rose" -> "NanChang") // 增加键值对
    println(cities)
    cities -= "Andy" // 减少键值对
    println(cities)

    //4、迭代映射
    for ((key, value) <- cities) println(key, value) // 迭代key，value
    for (key <- cities.keysIterator) println(key) // 只迭代key
    for (value <- cities.valuesIterator) println(value) // 只迭代value

    //5、已排序映射
    val name = scala.collection.immutable.SortedMap("A" -> "1", "D" -> "2", "C" -> "3")

    //6、与Java的互操作
    // Java映射转为Scala映射
    import scala.collection.JavaConversions.mapAsScalaMap
    val m: scala.collection.mutable.Map[String, String] = new util.TreeMap[String, String] //Java TreeMap转为Scala Map
    println(m)

    import scala.collection.JavaConversions.propertiesAsScalaMap
    val n: scala.collection.Map[String, String] = System.getProperties() //java.util.Properties转为scala map

    // Scala映射转为Java映射
    import java.awt.font.TextAttribute._

    import scala.collection.JavaConversions.mapAsJavaMap
    val attrs = Map(FAMILY -> "Serif", SIZE -> 12)
    val font = new Font(attrs) //这个是java映射

    // 映射的map操作
    val name2 = scala.collection.immutable.SortedMap("A" -> "1", "D" -> "2", "C" -> "3")
    name2.map { case (key, value) => (key, value + "suffix") }

    // 合并两个map
    var a = Map(1 -> 2, 2 -> 3, 3 -> 4)
    val b = Map(4 -> 5, 5 -> 6, 6 -> 7)
    a ++= b
    println(a)
    val c = a ++ b
    println(c)
  }
}
