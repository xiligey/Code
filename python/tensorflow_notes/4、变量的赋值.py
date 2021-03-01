import tensorflow as tf

value = tf.Variable(0, name="value")
one = tf.constant(1)
new_value = tf.add(value, one)
update_value = tf.assign(value, new_value)  # 把value的值变为new_value的值

init = tf.global_variables_initializer()

with tf.compat.v1.Session() as sess:
    sess.run(init)
    print(sess.run(update_value))
    for _ in range(10):
        sess.run(update_value)
        print(sess.run(value))
