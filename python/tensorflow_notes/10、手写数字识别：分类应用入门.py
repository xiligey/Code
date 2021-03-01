import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("data/MNIST_data/", one_hot=True)


def plot_image(image):
    plt.imshow(image.reshape(28, 28), cmap='binary')
    plt.show()


plot_image(mnist.train.images[1])

x = tf.placeholder(tf.float32, [None, 784], name='X')
y = tf.placeholder(tf.float32, [None, 10], name='Y')
W = tf.Variable(tf.random_normal([784, 10]), name='W')
b = tf.Variable(tf.zeros([10]), name='b')


def plot_images_labels_prediction(images, labels, prediction, index, num=10):
    """
    images: 图像列表
    labels: 标签列表
    prediction: 预测值列表
    index: 从第index个开始显示
    num=10: 缺省 一次显示10幅
    """
    fig = plt.gcf()
    fig.set_size_inches(10, 12)
    num = min(25, num)  # 最多显示25个子图
    for i in range(num):
        ax = plt.subplot(5, 5, i+1)  # 获取当前要处理的子图
        ax.imshow(np.reshape(images[index], (28, 28)), cmap='binary')
        title = "label="+str(object=np.argmax(labels[index]))
        if len(prediction) > 0:
            title += ", predict=" + str(object=prediction[index])
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        index += 1
    plt.show()


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    forward = tf.matmul(x, W)+b  # 前向传播
    pred = tf.nn.softmax(forward)  # softmax分类

    train_epochs = 50
    batch_size = 100
    total_batch = int(mnist.train.num_examples/batch_size)
    display_step = 1
    learning_rate = 0.01

    # 损失函数
    loss_function = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
    # 优化器
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function)

    # 准确率
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 训练
    for epoch in range(train_epochs):
        for batch in range(total_batch):
            xs, ys = mnist.train.next_batch(batch_size)
            sess.run(optimizer, feed_dict={x: xs, y: ys})
        loss, acc = sess.run([loss_function, accuracy], feed_dict={
                             x: mnist.validation.images, y: mnist.validation.labels})
        if (epoch+1) % display_step == 0:
            print("epoch=", epoch+1, "\tloss=", loss, "\taccuracy=", acc)
    print("Train Finished")

    # 评估模型
    accu_test = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
    print("Test Accuracy", accu_test)

    # 通过对数据集的合理划分，它在训练集和验证集的效果基本上是差不多的，如果对这个准确率还比较满意，就可以进行模型的应用了。

    # 模型应用
    # 只需要用到前面已经定义好的pred操作以及把需要进行预测的图像或图像样本集（mnist.test.images）作为输入填充到占位符x中，之后通过argmax函数把pred得到的one hot形式的结果转换成所需要的0-9的数字，就能得到预测结果。这里输入的参数是测试集的样本：
    prediction_result = sess.run(tf.argmax(pred, 1), feed_dict={x: mnist.test.images})
    print(prediction_result[:10])

    # 可视化结果
    # 输出预测结果时同时显示图像
    plot_images_labels_prediction(mnist.test.images, mnist.test.labels, prediction_result, 10, 25)
