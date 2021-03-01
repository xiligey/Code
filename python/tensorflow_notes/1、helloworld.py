import tensorflow as tf
hello = tf.constant("Hello World")
print(hello)
with tf.compat.v1.Session() as sess:
    print(sess.run(hello))
