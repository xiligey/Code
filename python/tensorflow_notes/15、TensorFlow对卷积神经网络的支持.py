import tensorflow as tf
# 卷积操作

"""
卷积函数定义在tensorflow/python/ops下的nn_impl.py和nn_ops.py文件中。
它包括了很多类型的卷积函数：
tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None, name=None)
tf.nn.depthwise_conv2d(input, filter, strides, padding, name=None)
tf.nn.separable_conv2d(input, depthwise_filter, pointwise_filter, strides, padding, name=None)
……

在这里，我们只对平时用的比较多的二维卷积进行介绍。其他函数的使用方法跟二维卷积是一样的。
tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None, name=None)
首先，我们来看一下上面这个函数中各个输入参数的定义：
input：需要做卷积的输入数据。注意：这是一个4维的张量（[batch, in_height, in_width, in_channels]）。对于图像数据来说，batch是这一批样本的个数，in_height和in_width是图像的尺寸，in_channels是图像的通道数，而且要求图像的类型为float32或float64。因此，我们在对图像进行处理的时候，首先要把图像转换成这种特定的类型。
filter：卷积核。这也是一个4维的张量（[filter_height, filter_width, in_channels, out_channels]）。filter_height,和filter_width是图像的尺寸，in_channels,是输入的通道数，out_channels是输出的通道数。
strides：图像每一维的步长。是一个一维向量，长度为4。
padding：定义元素边框与元素内容之间的空间。这里只能选择"SAME"或"VALID"，这个值决定了不同的卷积方式。当它为"SAME"时，表示边缘填充，适用于全尺寸操作；当它为"VALID"时，表示边缘不填充。
use_cudnn_on_gpu：bool类型，是否使用cudnn加速。
name：该操作的名称。
返回值：返回一个张量（tensor），即特征图（feature map）。

"""
input_data = tf.Variable(np.random.rand(10, 9, 9, 4), dtype=np.float32)
filter_data = tf.Variable(np.random.rand(3, 3, 4, 2), dtype=np.float32)
y = tf.nn.conv2d(input_data, filter_data, [1, 1, 1, 1], "SAME")
print(input_data)
print(y)
"""
我们可以看到，原本输入的shape是（10，9，9，4），由于padding为"VALID",不对图像的边缘进行填充，所以在进行卷积之后，图像的尺寸发生了改变。
如果将padding改为"SAME"，图像的尺寸不变。
"""

# 池化操作
"""
我们用的比较多的是下面这两个池化函数：
最大池化：tf.nn.max_pool(value, ksize, strides, padding, name=None)
平均池化：tf.nn.avg_pool(value, ksize, strides, padding, name=None)

这里所需要指定的输入参数，跟我们之前介绍的二维卷积函数是一样的：
value：需要池化的输入。一般池化层接在卷积层后面，所以输入通常是conv2d所输出的feature map，依然是4维的张量（[batch, height, width, channels]）。
ksize：池化窗口的大小。由于一般不在batch和channel上做池化，所以ksize一般是[1,height, width,1]。
strides：图像每一维的步长。是一个一维向量，长度为4。
padding：和卷积函数中padding含义一样。
name：该操作的名称。
返回值：返回一个张量（tensor）。
"""
input_data = tf.Variable(np.random.rand(10, 6, 6, 4), dtype=np.float32)
filter_data = tf.Variable(np.random.rand(2, 2, 4, 2), dtype=np.float32)
y = tf.nn.conv2d(input_data, filter_data, [1, 1, 1, 1], "SAME")
output = tf.nn.max_pool(value=y, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
print(y)
print(output)
