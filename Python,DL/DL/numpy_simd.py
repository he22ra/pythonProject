'''
    1. 파이썬 리스트 & 넘파이
        1) 넘파이 배열
            - 형상 (shape) : 차원의 크기를 지정하는 정수의 튜플
                - (3, 3)
            - 축 (axis) : 차원
                - axis=1(컬럼)
                - axis=0(행)
'''

import numpy as np
a = np.array([2,3,4])
print(a.shape)  # a 객체의 형상
print(a.ndim)   #         차원
print(a.dtype)  # 요소의 자료형
print(a.itemsize)   # 요소크기 (byte)
print(a.size)       # 요소의 수

print()

store_a = [20, 10, 30]  # 파이썬 리스트 (매장 A의 매출)
store_b = [70, 90, 70]  # 파이썬 리스트 (매장 B의 매출)

