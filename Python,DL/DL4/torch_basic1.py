'''
    1. 파이토치(PyTorch)
        1) 파이썬의 넘파이 라이브러리처럼 과학 연산을 위한 라이브러리 공개 -> 딥러닝 프레임워크로 발전
            - 넘파이를 대체하면서 GPU를 이용한 연산이 필요한 경우
            - 최대한 유연성, 속도 제공하는 딥러닝 플랫폼이 필요한 경우
        2) GPU에서 텐서 조작 및 동적 신경망 구축이 가능한 프레임워크
            - 딥러닝에서는 기울기 계산할 때 미분을 쓰는데, GPU를 사용하면 빠른 계산이 가능

'''
import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = a + b

print(c)
print(torch.tensor([[1, 2], [3, 4]]))

# GPU가 없어서 구글Colab으로 실행
from torch._C import device
# print(torch.tensor([[1, 2], [3, 4]], device='cuda:0'))

print('-----------------------------------------')

data = [
    [1, 2],
    [3, 4]
]

x = torch.tensor(data)
