package org.chenxilin.basic.re;

/**
 * @author chenxilin
 */
public class RegularExpression {
    public static void main(String[] args) {
        // # replaceAll(String pattern, String replaceStr)
        // 用replaceStr替换pattern匹配到的所有内容
        {
            String field = "abc123abc456abc";
            System.out.println(field.replaceAll("a.c", ""));
        }

        // # replaceFirst(String pattern, String replaceStr)
        // 用replaceStr替换pattern第一个匹配到的内容
        // ## Example1 去掉后缀 _string or _number
        {
            String field = "abc_string_number";
            System.out.println(field.replaceFirst("(_string)$|(_number)$", ""));
        }
    }
}
