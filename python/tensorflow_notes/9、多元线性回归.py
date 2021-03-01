import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.utils import shuffle
df = pd.read_csv("data/boston.csv", header=0)
df = df.drop(columns=["Unnamed: 0", "black"])
df = np.array(df)
df.shape
# 对特征(0到11列)数据做归一化
for i in range(12):
    df[:, i] = (df[:, i]-df[:, i].min())/(df[:, i].max()-df[:, i].min())
x_data = df[:, :12]
y_data = df[:, 12]

x = tf.placeholder(tf.float32, [None, 12], name='X')
y = tf.placeholder(tf.float32, [None, 1], name='Y')

with tf.name_scope("Model"):  # 定义一个命名空间
    w = tf.Variable(tf.random_normal([12, 1], stddev=0.01), name='W')
    b = tf.Variable(1.0, name='b')
    pred = tf.matmul(x, w)+b

    train_epochs = 50
    learning_rate = 0.01
    loss_function = tf.reduce_mean(tf.pow(y-pred, 2))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(train_epochs):
            loss_sum = 0.0
            for xs, ys in zip(x_data, y_data):
                xs = xs.reshape(1, 12)
                ys = ys.reshape(1, 1)
                _, loss = sess.run([optimizer, loss_function], feed_dict={x: xs, y: ys})
                loss_sum += loss
            # 打乱数据顺序防止过拟合
            xvalues, yvalues = shuffle(x_data, y_data)
            b0temp = b.eval(sess)
            w0temp = w.eval(sess)
            loss_average = loss_sum / len(y_data)

            print('epoch: ', epoch+1, '\t', 'loss=', loss_average, '\tb=', b0temp, '\tw=', w0temp)

        # 预测
        n = 348
        x_test = x_data[n].reshape(1, 12)
        predict = sess.run(pred, feed_dict={x: x_test})
        print(predict)
        target = y_data[n]
        print(target)
