import tensorflow as tf

x = tf.Variable(0,"name=x")
y = tf.constant(2)
z = tf.add(x,y)
a = tf.assign(x,z)

initialize_var = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(initialize_var)
    print(sess.run(x))
    for _ in range(20):
        sess.run(a)
        print(sess.run(x))
