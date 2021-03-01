import os
import tensorflow as tf


def full_connected_layer_network(inputs, input_dim, output_dim, activation=None):
    """建立全连接层网络
    Parameters
    ----------
    inputs: 输入数据
    input_dim: 输入神经元数量
    output_dim: 输出神经元数量
    activation: 激活函数
    """
    # 产生正太分布的值如果与均值的差值大于两倍的标准差，那就重新生成
    w = tf.Variable(tf.truncated_normal([input_dim, output_dim], stddev=0.1))
    b = tf.Variable(tf.zeros([output_dim]))
    y = tf.matmul(inputs, w)+b

    outputs = y if activation is None else activation(y)
    return outputs


x = tf.placeholder(tf.float32, [None, 784], name='X')
H1_NN = 256  # 第1层隐藏层的神经元个数
H2_NN = 64  # 2
H3_NN = 32  # 3

h1 = full_connected_layer_network(x, 784, H1_NN, tf.nn.relu)
h2 = full_connected_layer_network(h1, H1_NN, H2_NN, tf.nn.relu)
h3 = full_connected_layer_network(h2, H2_NN, H3_NN, tf.nn.relu)

forward = full_connected_layer_network(h3, H3_NN, 10, None)
pred = tf.nn.softmax(forward)


"""
这里有个问题：我们花了大量的时间去训练这个模型，当我们重新开机时，由刚刚训练得到的比较好的模型参数就全部丢失了，没有办法直接拿来用，只能利用以前记录下来的比较好的那组超参数接着进行模型训练，训练完成后再应用。这样是比较麻烦的，不符合日常的应用场景。
我们需要把训练好的模型做持久化保存，哪怕关机重启也不会丢失，可以把模型重新读取出来以供使用。这么做还有一个好处：当我们在处理一个比较复杂的模型时，需要花费大量时间，有的大型模型可能需要几天甚至几十天，如果训练中发生断电或是需要关机，模型不能保存下来，是比较麻烦的。
这里会提到一个“断点续训”的概念，即不管训练到什么阶段，可以暂停训练，下一次需要的时候，可以从暂停点继续训练。这可以通过模型的保存和还原来实现。
"""
"""
```python
# 保存模型

save_step = 5  # 存储模型的粒度
model_dir = "data/model/"
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

saver = tf.train.Saver()
saver.save(sess, modelpath)

# 读取模型
saver = tf.train.Saver()
ckpt=tf.train.get_checkpoint_state(model_dir)
if ckpt and ckpt.model_checkpoint_path:
    saver.restore(sess,ckpt.model_checkpoint_path)
```
