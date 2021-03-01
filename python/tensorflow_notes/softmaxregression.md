[TOC]

# 1、载入数据
以one-hot编码读取MNIST数据集(label是 只有一个值为1其他为0 的一维数组，1对应的位置代表其类别)
```python
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/MNIST_data/", one_hot=True)



```
查看数据集情况
```python
print(mnist.train.images.shape, mnist.train.labels.shape)
print(mnist.test.images.shape, mnist.test.labels.shape)
print(mnist.validation.images.shape, mnist.validation.labels.shape)
```

# 2、注册session并创建SoftMax模型
```python
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None, 784])  # None表示行数待定，784=28*28表示将一张图片平铺为一维数组
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, w) + b)
```

# 3、定义损失函数和优化器

```python
# y_是真实的label
y_ = tf.placeholder(tf.float32, [None, 10])
# 损失函数 交叉熵
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y), reduction_indices=[1))

# 优化器 随机梯度下降
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
```

# 4、开始训练
```python
tf.global_variables_intializer().run()

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	optimizer.run({x: batch_xs, y_: batch_ys})
```

# 5、预测与评估
```python
# 判断是否预测正确
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))  
# 计算准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))
```