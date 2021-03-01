import tensorflow as tf
node1 = tf.Variable(3.0, tf.float32, name="node1")
node2 = tf.Variable(4.0, tf.float32, name="node2")
result = tf.add(node1, node2, name="add")
with tf.Session() as sess:
    init = tf.compat.v1.global_variables_initializer()
    sess.run(init)
    print(sess.run(result))
