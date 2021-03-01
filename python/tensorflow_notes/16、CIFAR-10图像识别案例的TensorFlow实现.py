import urllib.request
import os
import pickle as p
import tarfile
import matplotlib.pyplot as plt
import numpy as np
from time import time
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
# 下载
url = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
filepath = 'data/cifar-10-python.tar.gz'
if not os.path.isfile(filepath):
    result = urllib.request.urlretrieve(url, filepath)
    print('downloaded', result)
else:
    print('Data file already exists')
# 解压
if not os.path.exists('data/cifar-10-batches-py'):
    tfile = tarfile.open('data/cifar-10-python.tar.gz', 'r:gz')
    result = tfile.extractall('data/')
    print('Extracted to data/cifar-10-batches-py')
else:
    print('Directory already exists.')


def load_CIFAR_batch(filename):
    """读取一个批次的样本"""
    with open(filename, 'rb') as f:

        data_dict = p.load(f, encoding='bytes')
        images = data_dict[b'data']
        labels = data_dict[b'labels']
        images = images.reshape(10000, 3, 32, 32)  # BCWH
        # 把通道数据C移动到最后一个维度
        images = images.transpose(0, 2, 3, 1)  # BWHC
        labels = np.array(labels)
        return images, labels


def load_CIFAR_data(filename):
    """读取数据集的完整样本"""
    images_train = []
    labels_train = []
    for i in range(5):
        f = os.path.join(data_dir, 'data_batch_%d' % (i+1))
        print('loading ', f)
        # 调用 load_CIFAR_batch( )获得批量的图像及其对应的标签
        image_batch, label_batch = load_CIFAR_batch(f)
        images_train.append(image_batch)
        labels_train.append(label_batch)
        Xtrain = np.concatenate(images_train)
        Ytrain = np.concatenate(labels_train)
        del image_batch, label_batch

    Xtest, Ytest = load_CIFAR_batch(os.path.join(data_dir, 'test_batch'))
    print('finished loadding CIFAR-10 data')

    # 返回训练集的图像和标签，测试集的图像和标签
    return Xtrain, Ytrain, Xtest, Ytest


data_dir = 'data/cifar-10-batches-py/'
Xtrain, Ytrain, Xtest, Ytest = load_CIFAR_data(data_dir)

# 显示数据集信息
print('Training data shape:', Xtrain.shape)
print('Training labels shape:', Ytrain.shape)
print('Test data shape:', Xtest.shape)
print('Test labels shape:', Ytest.shape)
# 训练集有50000条数据，测试集有10000条数据，图像的尺寸为32×32，通道为RGB三通道。

plt.imshow(Xtrain[6])
print(Ytrain[6])

# 查看多项images和label
label_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat',
              4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 6)
    num = min(num, 10)
    for i in range(num):
        ax = plt.subplot(2, 5, i+1)
        ax.imshow(images[idx], cmap='binary')  # 从第idx个图片开始画 画num个
        title = str(i)+','+label_dict[labels[idx]]
        if len(prediction) > 0:
            title += '=>'+label_dict[prediction[idx]]
        ax.set_title(title, fontsize=10)
        idx += 1
    plt.show(block=[bool])


plot_images_labels_prediction(Xtest, Ytest, [], 10, 10)

# 数据预处理
# #图像数据预处理
"""
我们可以查看第一个训练样本的第一个像素点：
由于图像是三通道的，所以59、62、63这三个数分别代表了图像的第一个像素点在RGB三个通道上的像素值。
"""
print(Xtrain[0][0][0])
"""然后我们对数字标准化"""
Xtrain_normalize = Xtrain.astype('float32')/255.0
Xtest_normalize = Xtest.astype('float32')/255.0
"""
因为图像的数字标准化可以提高模型的准确率。在没有进行标准化或归一化之前，图像的像素值是0-255，如果我们想对它进行归一的话，最简单的做法就是除以255。
"""
# #标签数据预处理
print(Ytrain[:10])
"""
对于CIFAR-10数据集，它的label是0-9。
比如船这个分类，它对应的label是8，我们希望通过独热编码来表示它的分类
"""
encoder = OneHotEncoder(sparse=False)
yy = [[i] for i in range(10)]
encoder.fit(yy)
Ytrain_reshape = Ytrain.reshape(-1, 1)
Ytrain_onehot = encoder.transform(Ytrain_reshape)
Ytest_reshape = Ytest.reshape(-1, 1)
Ytest_onehot = encoder.transform(Ytest_reshape)

# 建立CIFAR-10图像分类模型
"""将要建立的卷积神经网络结构如下：(见data/CIFAR10卷积网络结构图.png)
输入层：32*32图像，通道为3（RGB）
卷积层1：第一次卷积，输入通道3，输出通道32，卷积后图像尺寸不变(32*32)
降采样层1：第一次降采样，将32*32图像缩小为16*16，池化不改变通道数量(32)
卷积层2：输入通道32，输出通道64 卷积不改变图像尺寸(16*16)
降采样2：将16*16缩小为8*8，池化不改变通道数量(64)
全连接层：将64个8*8的图像转换为长度为4096的一维向量，该层有128个神经元
输出层：10个神经元，对应0-9这10个类别
"""

# 定义共享函数
tf.reset_default_graph()


def weight(shape):
    """定义权值"""
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1), name='w')


def bias(shape):
    """定义偏置，初始化为0.1"""
    return tf.Variable(tf.constant(0.1, shape=shape), name='b')


def conv2d(x, w):
    """定义卷积操作"""
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    """定义池化操作 步长为2 原尺寸的长和宽各除以2"""
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# 定义网络结构


# # 输入层 32*32图像，通道为3
with tf.name_scope('input_layer'):
    x = tf.placeholder('float', shape=[None, 32, 32, 3], name='x')
# # di==第一个卷积层
# # 输入通道3，输出通道32，卷积后图像尺寸不变32*32
with tf.name_scope('conv_1'):
    w1 = weight([3, 3, 3, 32])  # [k_width, k_height, input_chn,. output_chn]
    b1 = bias([32])  # 与output_chn一致
    conv_1 = conv2d(x, w1)+b1
    conv_1 = tf.nn.relu(conv_1)
# # 第一个池化层
# # 将32*32图像缩小为16*16 不改变通道数量32
with tf.name_scope('pool_1'):
    pool_1 = max_pool_2x2(conv_1)
# # 第二个卷积层
# # 输入通道32 输出通道64 卷积后图像尺寸不变16*16
with tf.name_scope('conv_2'):
    w2 = weight([3, 3, 32, 64])
    b2 = bias([64])
    conv_2 = conv2d(pool_1, w2)+b2
    conv_2 = tf.nn.relu(conv_2)
# # 第二个池化层
# # 将16*16图像缩小为8*8 不改变通道数64
with tf.name_scope('pool_2'):
    pool_2 = max_pool_2x2(conv_2)
# # 全连接层
# # 将第二个池化层的64个8*8的图像转化为一维向量 长度为64*8*8=4096
# # 128个神经元(可自己调整)
with tf.name_scope('fc'):
    w3 = weight([4096, 128])
    b3 = bias([128])
    flat = tf.reshape(pool_2, [-1, 4096])
    h = tf.nn.relu(tf.matmul(flat, w3)+b3)
    h_dropout = tf.nn.dropout(h, keep_prob=0.8)
# # 输出层 10个神经元
with tf.name_scope('output_layer'):
    w4 = weight([128, 10])
    b4 = bias([10])
    pred = tf.nn.softmax(tf.matmul(h_dropout, w4)+b4)

# 构建模型
# # 定义损失函数和优化器
with tf.name_scope('optimizer'):
    y = tf.placeholder('float', shape=[None, 10], name='label')
    loss_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels == y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.0001).minimize(loss_function)
# # 定义准确率
with tf.name_scope('evaluation'):
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

# 训练模型
train_epochs = 25
batch_size = 50
total_size = 50
total_batch = int(len(Xtrain)/batch_size)
epoch_list, accuracy_list, loss_list = [], [], []

epoch = tf.Variable(0, name='epoch', trainable=False)
startTime = time()

sess = tf.Session()
init = tf.global_variables_initilizer()
sess.run(init)
# # 断点续训
"""
我们知道，程序的训练，尤其对于大规模数据集或者复杂的网络，它的训练时间非常长，往往需要数个小时甚至数天，有时还可能会因为某些原因导致了计算机宕机。这样的话，前面的训练就会前功尽弃。解决的方案呢，就是增加一个断点续训的机制，每次程序执行完训练之后，将模型的权重保存一下，下次程序在执行训练之前，我们先加载这个模型的权重，再继续训练就可以了。
介绍到这里，大家可能回想起这个断点续训跟我们在MNIST案例中介绍的模型的存储和加载很类似。
首先我们定义一个存储路径，这里就用当前目录下的"CIFAR10_log/"目录。当这个目录不存在的时候，我们就会创建一个。
由于我们已经定义完所有的变量了，所以我们可以调用tf.train.Saver（）来保存和提取变量。这个变量包含了权重以及其他在程序中定义的变量。
再接下来就是加载模型。如果存储路径中已经有训练好的模型文件，那我们可以用saver.restore（）来加载所有的参数，然后就可以直接使用模型进行预测，或者接着继续训练了。
在这里，我们取了“断点续训”这个名字，是因为我们除了希望保存和加载模型之外，还希望知道断点在哪里、我们是从哪里开始继续训练的。我们在启动会话中定义了一个不可训练的变量epoch，然后在断点续训的时候，通过sess.run(epoch)获得它的值，从而我们就可以知道，我们是从第几轮开始继续迭代训练的。
"""
ckpt_dir = 'data/CIFAR10_log'  # 设置检查点存储目录
if not os.path.exists(ckpt_dir):
    os.mkdir(ckpt_dir)

saver = tf.train.Saver(max_to_kee=1)
ckpt = tf.train.latest_checkpoint(ckpt_dir)
if ckpt is not None:
    saver.restore(sess, ckpt)  # 加载所有的参数
    # 从这里开始就可以直接使用模型进行预测，或者接着训练了
else:
    print('Training from scratch.')

start = sess.run(epoch)  # 获取训练参数
print('Training starts from {} epoch'.format(start+1))


def get_train_batch(number, batch_size):
    return Xtrain_normalize[number*batch_size:(number+1)*batch_size], Ytrain_onehot[number*batch_size:(number+1)*batch_size]


for ep in range(start, train_epochs):
    for i in range(total_batch):
        batch_x, batch_y = get_train_batch(i, batch_size)
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})
        if i % 100 == 0:
            print('step {}'.format(i), 'finished')
    loss, . acc = sess.run([loss_function, accuracy], feed_dict={x: batch_x, y: batch_y})
    epoch_list.append(ep+1)
    loss_list.append(loss)
    accuracy_list.append(acc)

    print('Train Epoch:', '%02d' % (sess.run(epoch)+1), 'Loss=', '{:.6f}'.format(loss), 'Accuracy='，acc)
    # 保存检查点
    saver.save(sess, ckpt_dir+"CIFAR10_cnn_model.cpkt", global_step=ep+1)
    sess.run(epoch.assign(ep+1))
duration = time() - startTime
print('Train finished takes:', duration)

# 可视化损失值
fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.plot(epoch_list, loss_list, label='loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss']，loc='upper right')

# 可视化准确率
plt.plot(epoch_list, accuracy_list, label='accuracy')
fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.ylim(0.1, 1)
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend()
plt.show()
# 准确率的变化趋势是越来越高的。从上面损失值的图片可以看到，它并没有处于一个收敛的状态，因此准确率也还有上升的空间。

# 计算测试集上的准确率
"""
现在，我们已经建立好了模型并且完成了模型的训练，当你觉得训练的准确率已经能够达到你所期待的准确率的时候，你就可以用这个模型来进行预测了。
在CIFAR数据集上，对卷积神经网络进行模型评估及预测跟我们在MNIST数据集上进行的模型评估是一样的。
"""
test_total_batch = int(len(Xtest_normalizer)/batch_size)
test_acc_sum = 0.0
for i in range(test_total_batch):
    test_image_batch = Xtest_normalize[i*batch_size:(i+1)*batch_size]
    test_label_batch = Ytest_onehot[i*batch_size:(i+1)*batch_size]
    test_batch_acc = sess.run(accuracy, feed_dict={x: test_image_batch, y: test_label_batch})
    test_acc_sum += test_batch_acc
test_acc = float(test_acc_sum/test_total_batch)
print('Test accuracy: {.6f}'.format(test_acc))

# 预测
test_pred = sess.run(pred, feed_dict={x: Xtest_normalize[:10]})
prediction_result = sess.run(tf.argmax(test_pred, 1))

plot_images_labels_prediction(Xtest, Ytest, prediction_result, 0, 10)
