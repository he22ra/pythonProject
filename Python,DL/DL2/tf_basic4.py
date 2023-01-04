import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


a = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
print(a)

print('-------------------------------------------')

a = tf.random.uniform((64, 32, 3))
print(a)
print(a.shape)
b = tf.transpose(a, perm=[2, 1, 0])     # 차원 자체를 교환
# (2번째 축, 1번째 축, 0번째 축)의 형태가 됨
print(b.shape)
