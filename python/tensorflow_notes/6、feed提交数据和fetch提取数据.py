"""
如果构建了一个包含placeholder操作的计算图，在程序在session中调用run方法时，需要通过feed_dict参数将placeholder占用的变量传递进去
"""
import tensorflow as tf

a = tf.placeholder(tf.float32, name='a')
b = tf.placeholder(tf.float32, name='b')
c = tf.multiply(a, b, name='c')
d = tf.subtract(a, b, name='d')  # a-b
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # 可以一次feed多个数据
    result = sess.run(c, feed_dict={a: 8.0, b: 3.5})
    print(result)

with tf.Session() as sess:
    sess.run(init)
    rc, rd = sess.run([c, d], feed_dict={a: [8.0, 2.0, 3.1], b: [1.5, 2.0, 4.1]})
    print(rc, rd)
