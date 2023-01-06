import torch

# 텐서의 평균 함수
a = torch.tensor([
    [1.0, 2, 3, 4],
    [5, 6, 7, 8]
])
print(a)
print(a.mean())     #전체 원소에 대한 평균
print(a.mean(dim=0)) #각 열에 대하여 평균 계산
print(a.mean(dim=1)) #각 행에 대하여 평균 계산

# 텐서의 합계
print('---------------------------------------')
print(a)
print(a.sum())     #전체 원소에 대한 합
print(a.sum(dim=0)) #각 열에 대하여 합
print(a.sum(dim=1)) #각 행에 대하여 합

# max() 함수 : 전체 원소에 대한 최대값
# argmax() : 가장 큰 원소의 인덱스 반환

# 텐서의 차원 줄이기 : squeeze() - 크기가 1인 차원을 제거
# 텐서의 차원 늘리기 : unsqueeze()
print('---------------------------------------')
print(a.shape)

# 첫번째 축에 차원 추가
a = a.unsqueeze(0)
print(a)
print(a.shape)

# 네번째 축에 차원 추가
a = a.unsqueeze(3)
print(a)
print(a.shape)

# 크기가 1인 차원 제거
a = a.squeeze()
print(a)
print(a.shape)