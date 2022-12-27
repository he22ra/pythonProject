import matplotlib as mpl
import matplotlib.pyplot as plt             # 그림 그리기 위한 pyplot 서브모듈을 가져오는 작업
# plt.plot([1,2,3,4])
plt.plot([0,1,2,3], [1,2,3,4])
plt.ylabel('y label')
plt.xlabel('x label')
# plt.show()

import numpy as np
x = np.arange(10)   # 0에서 9까지 정수
plt.plot(x**2)      # x^2 함수
# plt.show()

x = np.arange(10)
plt.plot(x**2)
plt.axis([0,100,0,100]) # 범위 지정
# plt.show()          # x값이 증가할 경우 y값이 가파르게 증가하는 형태

x = np.arange(-20, 20)
y1 = 2* x
y2 = (1/3) * x **2 + 5
y3 = -x **2 - 5

# 각각 다른 스타일로 그림
# 녹색 실선, 빨강색 점선과 세모기호, 파랑색 별표와 점선
plt.plot(x, y1, 'g--', x, y2, 'r^-', x, y3, '')

