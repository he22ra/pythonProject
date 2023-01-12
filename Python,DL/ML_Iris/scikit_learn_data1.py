'''
    * 머신러닝 분야의 고전적인 데이터셋인 붓꽃(Iris)
        0) 대표적인 지도 학습 데이터
        1) 출력 데이터는 3개의 클래스
            - Setosa, 부채 붓꽃
            - Versicolor, 버시컬러
            - Virginica, 버지니카
            - 세 종류(품종) => (레이블) 벡터 y에 할당 (답)
        2) 입력 데이터는 4개의 특징
            - sepal length 꽃받침 길이
            - sepal width 꽃받침 너비
            - petal length 꽃잎 길이
            - petal width 꽃잎 너비
        3) 150개의 꽃 샘플에서 꽃잎 길이와 꽃잎 넓이 => 행렬 X에 할당
'''
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
# 데이터셋 불러오기
dataset = datasets.load_iris()
data = dataset["data"]
target = dataset["target"]
feature_names = dataset["feature_names"]

print(f"총 데이터 개수 : {len(data)}")
print(f"총 타겟 개수 : {len(target)}")
print("[입력특징]")
for i in range(len(feature_names)):
    feature_name = feature_names[i]
    print(f"{i + 1}: {feature_name}")

print("입력 데이터")
print(data[:5])

target_names = dataset["target_names"]
print("[출력 특징]")
for i in range(len(target_names)):
    target_name = target_names[i]
    print(f"{i + 1}: {target_name}")

print("출력 데이터")
print(target[:5])

# print(iris)
# X = iris.data[:, [2,3]]
# y = iris.target

# irist.target에 저장된 세 개의 고유한 클래스 레이블을 반환
# 붓꽃 클래스 이름 : Iris-Setosa, Iris-Versicolor, Iris-Virginica 각각 (0, 1, 2) 정수로 저장되어있음.
# print('클래스 레이블: ', np.unique(y))

