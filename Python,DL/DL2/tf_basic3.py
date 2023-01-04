'''
    1. 텐서의 형변환 및 차원 변경
        1) 텐서는 넘파이 배열처럼 조작할 수 있음
        2)

'''

import os
import numpy as np      # 벡터 및 행렬 연산에서 매우 편리한 기능 제공하는 파이썬 라이브러리 패키지
import tensorflow as tf
import pandas as pd     # 데이터 분석을 위해 사용되는 파이썬 라이브러리 패키지
import matplotlib.pyplot as plt
import seaborn as sns

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

tensor = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(tensor[0])        # first row
print(tensor[:, 0])     # first column
print(tensor[..., -1])  # last column
print(tensor[..., -2])  # 끝에서 2번째

print('-------------------------------------------')

# axis : 축 (0, 1)
result = tf.concat([tensor, tensor, tensor], axis=0)
print(result)

print('-------------------------------------------')

# 1번 축(열)을 기준으로 이어 붙이기
result = tf.concat([tensor[:, 0], tensor[:, 0], tensor[:, 0]], axis=0)
print(result)
result2 = tf.concat([tensor, tensor, tensor], axis=1)
print(result2)

print('-------------------------------------------')

a = tf.constant([2])
b = tf.constant([5.0])

print(a.dtype)
print(b.dtype)

# 텐서 a를 float32 형식으로 변경한 뒤에 더하기 수행
print(tf.cast(a, tf.float32) + b)



