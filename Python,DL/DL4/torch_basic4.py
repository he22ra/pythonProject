'''

'''
import torch
import numpy as np

#list로부터 tensor 생성
data = [
    [1, 2],
    [3, 4]
]
x_data = torch.tensor(data)
print(x_data)

# copy본 생성
np_array = np.array(data)
x_np_1 = torch.tensor(np_array)
print(x_np_1)

#view를 만듦 (실체를 가리킴)
x_np_2 = torch.as_tensor(np_array)
print(x_np_2)

x_np_3 = torch.as_tensor(np_array)
print(x_np_3)

x_np_1[0,0] = 5
print(x_np_1)
print(np_array)

print('-------------------------------------')
a = torch.ones(2, 3)
print(a)

b = torch.zeros(2, 3)
print(b)

c = torch.full((2, 3), 2)
print(c)

# empty : 메모리 초기화가 안됐으면 다른 값이 나올 수 있음.
d = torch.empty(2, 3)
print(d)

f = torch.rand(2, 3)
print(f)

# 음수(-)값도 포함
g = torch.randn(2, 3)
print(g)

print(f"Shape of tensor : {f.shape}")
print(f"Datatype of tensor : {f.dtype}")
print(f"Device of tensor : {f.device}")

print('-------------------------------------')
a = torch.arange(1, 13).reshape(3, 4)
print(a)

# indexing
print(a[1])     #2번째 줄(행)
print(a[0, -1])     #1번째 줄(행)에서 끝에서 1번째

# slicing
print(a[1:-1])
print(a[:2, 2:])        #

x = torch.tensor([
    [1, 2],
    [3, 4]
], dtype=torch.float32)

y = torch.tensor([
    [5, 6],
    [7, 8]
], dtype=torch.float32)

print(x)
print(y)

print(x @ y)
print('='*30)

print(torch.add(x, y))
print(torch.subtract(x, y))
print(torch.multiply(x, y))
print(torch.divide(x, y))
print(torch.matmul(x, y))