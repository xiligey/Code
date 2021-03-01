# 基于变量的数据类型
## 1、逻辑型 "logical"
v1 = TRUE
v2 = FALSE
print(class(v1))
## 2、数字型 "numeric"
v3 = 12
v4 = 1.5
v5 = -1
print(class(v5))
## 3、整型 "integer"
v6 = 1L
v7 = -2L
print(class(v7))
## 4、复合型 "complex"
v8 = 1+2i
print(class(v8))
## 5、字符 "character"
v9 = "123"
print(class(v9))
## 6、原型 raw
v10 = charToRaw(v9)
print(class(v10))

# 基于向量的数据类型
## 1、Vector向量
a1 = c(1, 2, 3)
print(a1)
print(class(a1))
## 2、List列表  类似python列表 元素可以是任何对象
a2 = list(1, "a", c(2, 3, 4))
print(a2[3][1])
print(class(a2))
## 3、Matrix二维矩阵
a3 = matrix(c("a", "b", "c", "d", "e", "f"), nrow = 2)
print(a3)
## 4、array数组
a4 = array(a3, dim = c(2,3,1))
print(a4)
## 5、Factor因子 因子是使用向量创建的r对象
a5 = factor(c(1,1,2,3,2,3))
print(nlevels(a5))  # 应用nlevels函数可以知道不重复值的个数
## 6、DataFrame
a6 = data.frame(gender=c("Male", "Male", "Female"), weight=c(80, 100, 90), Age=c(28, 19, 25))
print(a6)
