'''
    7) 텐서의 연산
        - 텐서에 대하여 사칙 연산
    8) 텐서의 평균 함수
        - 텐서플로우에서는 차원이 감소한다는 의미로

'''
import os
import numpy as np
import tensorflow as tf

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

a = tf.constant([
    [1, 2],
    [3, 4]
])
b = tf.constant([
    [5, 6],
    [7, 8]
])

print(a + b)
print(a - b)
print(a * b)

# 행렬 곱 (matrix multiplication)
print(tf.matmul(a, b))

print('-------------------------------------------')

a = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(a)
print(tf.reduce_mean(a))            # 전체 원소에 대한 평균
print(tf.reduce_mean(a, axis=0))    # 각 열에 대하여 평균 계산
print(tf.reduce_mean(a, axis=1))    # 각 행에 대하여 평균 계산
print('-------------------------------------------')
print(tf.reduce_sum(a))             # 전체 원소 합
print(tf.reduce_sum(a, axis=0))
print(tf.reduce_sum(a, axis=1))
print('-------------------------------------------')
print(tf.reduce_max(a))             # 전체 원소 중 최대값
print(tf.reduce_max(a, axis=0))     # 각 열에서 최대값
print(tf.reduce_max(a, axis=1))     # 각 행에서 최대값
print('-------------------------------------------')
print(tf.argmax(a, axis=0))         # 각 열에서 최대값의 인덱스
print(tf.argmax(a, axis=1))         # 각 행에서 최대값의 인덱스
print('-------------------------------------------')
# 첫번째 축에 차원추가(2차원 -> 3차원)
a = tf.expand_dims(a, 0)
print(a)
# 네번째 축에 차원추가
a = tf.expand_dims(a, 3)
print(a)

# 크기가 1인 차원 제거
a = tf.squeeze(a)
print(a)