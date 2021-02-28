package org.chenxilin.basic

/**
 * Scala模式匹配
 * - 模式匹配的基本用法
 * - case class上的模式匹配
 * - 模式守卫(pattern guards)
 * - 仅匹配类型
 * - 密封类
 * - 提取器对象(extractor objects)
 */
object ScalaMatch {
  def main(args: Array[String]): Unit = {
    // # 1、模式匹配的基本用法

    val city = "北京"

    city match {
      case "北京" if city(0) == '北' => println(1)
      case "上海" => println(2)
      case _ => println(3)
    }

    import scala.util.Random

    val x: Int = Random.nextInt(10)

    val y = x match {
      case 0 => "zero"
      case 1 => "one"
      case 2 => "two"
      case _ => "other"
    }

    // # 2、case class上的模式匹配

    abstract class Notification

    case class Email(sender: String, title: String, body: String) extends Notification

    case class SMS(caller: String, message: String) extends Notification

    case class VoiceRecording(contactName: String, link: String) extends Notification

    def showNotification(notification: Notification): String = {
      notification match {
        case Email(sender, title, _) =>
          s"You got an email from $sender with title: $title"
        case SMS(number, message) =>
          s"You got an SMS from $number! Message: $message"
        case VoiceRecording(name, link) =>
          s"you received a Voice Recording from $name! Click the link to hear it: $link"
      }
    }

    val someSms = SMS("12345", "Are you there?")
    val someVoiceRecording = VoiceRecording("Tom", "Rerecording.org/id/123")

    println(showNotification(someSms)) // prints You got an SMS from 12345! Message: Are you there?

    println(showNotification(someVoiceRecording))


    // # 3、模式守卫(pattern guards)
    // 为了让匹配更加具体，可以使用模式守卫，也就是在模式后面加上if <boolean expression>。
    def showImportantNotification(notification: Notification, importantPeopleInfo: Seq[String]): String = {
      notification match {
        case Email(sender, _, _) if importantPeopleInfo.contains(sender) =>
          "You got an email from special someone!"
        case SMS(number, _) if importantPeopleInfo.contains(number) =>
          "You got an SMS from special someone!"
        case other =>
          showNotification(other) // nothing special, delegate to our original showNotification function
      }
    }

    val importantPeopleInfo = Seq("867-5309", "jenny@gmail.com")

    val someSms2 = SMS("867-5309", "Are you there?")
    val someVoiceRecording2 = VoiceRecording("Tom", "Rerecording.org/id/123")
    val importantEmail = Email("jenny@gmail.com", "Drinks tonight?", "I'm free after 5!")
    val importantSms = SMS("867-5309", "I'm here! Where are you?")

    println(showImportantNotification(someSms2, importantPeopleInfo))
    println(showImportantNotification(someVoiceRecording2, importantPeopleInfo))
    println(showImportantNotification(importantEmail, importantPeopleInfo))
    println(showImportantNotification(importantSms, importantPeopleInfo))
    // 在case Email(sender, _, _) if importantPeopleInfo.contains(sender)中，
    // 除了要求notification是Email类型外，还需要sender在重要人物列表importantPeopleInfo中，才会匹配到该模式。

    // # 4、仅匹配类型
    abstract class Device
    case class Phone(model: String) extends Device {
      def screenOff = "Turning screen off"
    }
    case class Computer(model: String) extends Device {
      def screenSaverOn = "Turning screen saver on..."
    }

    def goIdle(device: Device) = device match {
      case p: Phone => p.screenOff
      case c: Computer => c.screenSaverOn
    }
    // 当不同类型对象需要调用不同方法时，仅匹配类型的模式非常有用，如上代码中goIdle函数对不同类型的Device有着不同的表现。
    // 一般使用类型的首字母作为case的标识符，例如上述代码中的p和c，这是一种惯例。

    // # 5、密封类
    // 特质（trait）和类（class）可以用sealed标记为密封的，
    // 这意味着其所有子类都必须与之定义在相同文件中，从而保证所有子类型都是已知的。
    sealed abstract class Furniture
    case class Couch() extends Furniture
    case class Chair() extends Furniture

    def findPlaceToSit(piece: Furniture): String = piece match {
      case a: Couch => "Lie on the couch"
      case b: Chair => "Sit on the chair"
    }
    // 这对于模式匹配很有用，因为我们不再需要一个匹配其他任意情况的case

    // # 5、提取器对象(extractor objects)
    // Scala的模式匹配语句对于使用案例类（case classes）表示的类型非常有用，
    // 同时也可以利用Scala提取器对象中的unapply方法来定义非案例类对象的匹配

    // 提取器对象是一个包含有 `unapply` 方法的单例对象。
    //`apply` 方法就像一个构造器，接受参数然后创建一个实例对象，反之 `unapply` 方法接受一个实例对象然后返回最初创建它所用的参数。
    //提取器常用在模式匹配和偏函数中。
    import scala.util.Random

    object CustomerID {

      def apply(name: String) = s"$name--${Random.nextLong}"

      def unapply(customerID: String): Option[String] = {
        val stringArray: Array[String] = customerID.split("--")
        if (stringArray.tail.nonEmpty) Some(stringArray.head) else None
      }
    }

    val customer1ID = CustomerID("Young")
    customer1ID match {
      case CustomerID(name) => println(name)
      case _ => println("Could not extract a CustomerID")
    }
  }
}