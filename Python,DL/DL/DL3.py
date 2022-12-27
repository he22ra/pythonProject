'''
    1. 사이킷런을 이용한 선형 회귀
        1) scikit-learn
            - 2007년 구글 코드 프로젝트 모임에 개발자 중심이 되어 시작된 라이브러리
        2) 머신러닝
            - 특성과 레이블로 이루어진 데이터
            - 데이터를 바탕으로 동작이 결정되는 모델
            - 모델을 위한 적절한 하이퍼파라미터(hyperparameter)
            - 학습을 위한 훈련
            - 검증

    2. 선형 회귀 모델의 계수와 절편
        - 가장 간단한 모델로 이차원 평면상에 있는 직선 방정식


'''

import numpy as np
# 사이킷런을 코드에 가져오기 위해서 sklearn이라는 이름으로 가져와야 함
#  선형 회귀를 구현하기 위해서 linear_model을 import 함
from sklearn import linear_model

# LinearRegeression() 생성자를 통해 선형 회귀 모델(객체)을 생성
regr = linear_model.LinearRegression()

# 입력 데이터 집합 X
X = [[163], [179], [166], [169], [171]]     # 입력 데이터
y = [54, 63, 57, 56, 58]                    # 정답
regr.fit(X, y)                              # 데이터 사용하여 훈련(학습)하기

# 직선의 기울기
coef = regr.coef_                           # regr 모델의 coef_속성값으로 얻음

# 직선의 절편
intercept = regr.intercept_                 # regr 모델의 intercept_ 속성값으로 얻음

score = regr.score(X, y)

print("y = {} * x + {:.2f}".format(coef.round(2), intercept))
print("데이터와 선형 회귀 직선의 관계 함수 : {:.1%}".format(score))

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))

# 학습 데이터와 y값을 산포도로 그리기
plt.scatter(X,y, color='blue', marker='D')
y_pred = regr.predict(X)            # 학습 데이터를 입력하여 예측값 계산
plt.plot(X, y_pred, 'r:')           # 계산된 기울기와 y절편을 가지는 점선 그리기

fig.savefig("LinearRegression_result.png")

# 167 키를 넣어서 추정값 계산
person = [[167]]
result = regr.predict(person)
print('키가 {}이므로 몸무게는 {}kg으로 추정됨'.format(\
            person, result.round(1)))

