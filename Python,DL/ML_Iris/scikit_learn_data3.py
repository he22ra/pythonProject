import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=500, noise=0.05, random_state=1234)
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
print(df.head(10))

print("데이터 개수: ", len(df))

plt.scatter(df["x"], df["y"], s=100, c=y)
plt.show()