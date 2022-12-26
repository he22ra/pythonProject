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
