"""
准备数据
构建模型
训练模型
进行预测
"""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


logdir = "./log"
writer = tf.summary.FileWriter(logdir, tf.get_default_graph())


x_data = np.linspace(-1, 1, 100)
y_data = 2*x_data+1.0+np.random.randn(*x_data.shape)*0.4

x = tf.placeholder(tf.float32, name='x')
y = tf.placeholder(tf.float32, name='y')

w = tf.Variable(1.0, name='w0')
b = tf.Variable(0.0, name='b0')
pred = tf.multiply(x, w) + b

epochs = 10  # 训练轮数
learning_rate = 0.05  # 学习率
display_step = 10  # 控制显示loss值的粒度

loss_function = tf.reduce_mean(tf.square(y-pred))  # mse损失函数
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)  # 梯度下降优化器

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    step = 0  # 记录训练步数
    losses = []  # 用于保存loss值的列表
    for epoch in range(epochs):
        for xs, ys in zip(x_data, y_data):
            _, loss = sess.run([optimizer, loss_function], feed_dict={x: xs, y: ys})
            losses.append(loss)
        if step % display_step == 0:
            print(epoch+1, ":", loss)
        b0temp = b.eval(session=sess)
        w0temp = w.eval(session=sess)
        plt.plot(x_data, w0temp*x_data+b0temp)

    # 预测
    x_test = 3.21
    predict = sess.run(pred, feed_dict={x: x_test})
    print(predict)
    target = 2*x_test+1
    print(target)

plt.show()  # 从绘制的图可以看出，本案例所拟合的模型较简单，训练3次之后已经接近收敛 对于复杂模型，需要更多次训练才能收敛。
plt.close()
print(b0temp, w0temp)
writer.close()
