"""
TensorBoard可视化初步

https://minghuiwu.gitbook.io/tfbook/di-san-zhang-mo-dao-bu-wu-kan-chai-gong-tensorflow-ji-chu/di-san-zhang-tensorflow-ji-chu/3.11-tensorboard-ke-shi-hua-chu-bu

报错 tensorflow.python.framework.errors_impl.UnimplementedError: /home/chenxilin; Operation not supported TODO
"""
import tensorflow as tf

# 清除default graph 和不断增加的节点
tf.reset_default_graph()

# 自定义日志文件目录
logdir = "/home/chenxilin/.tensorflow/log"

# 定义一个简单的计算图，计算向量的加法
input1 = tf.constant([1.0, 2.0, 3.0], name='input1')
input2 = tf.Variable(tf.random_uniform([3]), name='input2')
output = tf.add_n([input1, input2], name='add')  # add_n将数组所有元素都相加
writer = tf.summary.FileWriter(logdir, tf.get_default_graph())
writer.close()
