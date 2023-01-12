'''
    * 사이킷런 가상 데이터 생성
        1) 분류(classification) 모델 학습을 위한 가상 데이터 생성

'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=1234)
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
print(df.head(10))

print("데이터 개수: ", len(df))

plt.scatter(df["x"], df["y"], s=100, c=y)
plt.show()