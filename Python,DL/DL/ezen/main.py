'''
    Author : 이희라
    Date : 2022-12-29
'''
'''
    keras : tensorflow를 활용해서 인공지능을 더 쉽게 만들 수 있도록 도와주는 소프트웨어
            tensorflow의 기본 기능으로 내장됨
'''

from tensorflow import keras
import data_reader

EPOCHS = 20 #전체 데이터셋을 몇 회 학습시킬 것이냐, 몇 번 반복할것이냐 의미

# 데이터를 읽어옴
dr = data_reader.DataReader()

# 인공신경망 제작
model = keras.Sequential([

])
