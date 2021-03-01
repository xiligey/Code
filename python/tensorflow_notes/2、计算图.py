import tensorflow as tf

node1 = tf.constant(3.0, tf.float32, name='node1')
node2 = tf.constant(4.0, tf.float32, name='node2')
node3 = tf.add(node1, node2)
print(node3)
with tf.session() as sess:
    print(sess.run(node3))
