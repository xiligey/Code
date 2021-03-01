# TODO https://minghuiwu.gitbook.io/tfbook/di-qi-zhang-mnist-shou-xie-shu-zi-shi-bie-jin-jie-duo-ceng-shen-jing-wang-luo-yu-ying-yong/di-qi-zhang-mnist-shou-xie-shu-zi-shi-bie-jin-jie-duo-ceng-shen-jing-wang-luo-yu-ying-yong/7.3-tensorboard-jin-jie-yu-tensorflow-you-le-chang
import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784], name='X')
image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
tf.summary.image('input', image_shaped_input, 10)
