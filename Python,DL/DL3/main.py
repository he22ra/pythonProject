'''
    피마 인디언을 대상으로 당뇨병 여부를 측정한 데이터
        1) 피마 인디언 데이터
            - 속성
                - pregnant  과거 임신 횟수
                - plasma    공복 혈당 농도
                - pressure  혈압
                - thickness 심두근 피부 주름 두께
                - insulin   혈청 인슐린
                - bmi       체질량 지수
                - predigree 당뇨병 가족력
                - age       나이
                - diabetes  당뇨 1, 당뇨아님 0
'''
import os
import pandas as pd
import numpy as np
import seaborn as sns
import tensorflow as tf
from matplotlib import pyplot as plt

# 로그레벨이 3이 되면 warning이 뜨지 않음
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 피마 인디언 당뇨병 데이터셋 불러오기
df = pd.read_csv('./ezen/pima-indians-diabetes3.csv')

# 처음 10줄 보기
print(df.head(10))

print('-----------------------------------------------')
# 정상과 당뇨 환자가 각각 몇 명인지 확인(정상0: 500명, 당뇨1: 268명)
print(df["diabetes"].value_counts())

print('-----------------------------------------------')
# 각 정보별 특징 자세히 출력
print(df.describe())

print('-----------------------------------------------')
# 상관 관계 출력 (1에 가까울수록 관련도 높음)
print(df.corr())
# 시각화
colormap = plt.cm.gist_heat     # 그래프 색상 구성
plt.figure(figsize=(12,12))     # 그래프 크기

# 그래프 속성
'''
    사본 라이브러리 중 각 항목 간 상관관계를 나타내는 heatmap() 함수 통해 그래프 표시
'''
# sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=colormap, linecolor='white', annot=True)
# plt.show()

# plasma를 기준으로 각각 정상과 당뇨가 어느 정도 비율로 분포 확인
'''
    hist()함수
'''
plt.hist(x=[df.plasma[df.diabetes == 0], df.plasma[df.diabetes ==1]], bins=30, histtype='barstacked', label=['normal', 'diabetes'])
plt.legend()
plt.show()


# bmi를 기준으로 각각 정상과 당뇨가 어느 정도의 비율로 분포 확인
# plt.hist(x=[df.bmi[df.diabetes == 0], df.bmi[df.diabetes == 1]], bins=30, histtype='barstacked', label=['nomal', 'diabetes'])
# plt.legend()
# plt.show()

print('-----------------------------------------------')
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 세부 정보(독립변수)를 X로 지정
X = df.iloc[:, 0:8]
# 당뇨병 여부(종속변수)를 y로 지정
y = df.iloc[:, 8]

# 모델 설정
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu', name='Dense_1'))
model.add(Dense(8, activation='relu', name='Dense_2'))
model.add(Dense(1, activation='sigmoid', name='Dense_3'))
model.summary()

# 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 실행
# 100번 반복한 결과 75%의 정확도
model.fit(X, y, epochs=100, batch_size=5)

