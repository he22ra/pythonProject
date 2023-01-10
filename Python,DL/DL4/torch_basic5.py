import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
import torchvision.transforms as tr
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt
import numpy as np

'''
    * 파이토치에서 제공하는 데이터 셋 (Dataset)
        - 토치비전(torchvision) : 파이토치에서 제공하는 데이터셋들이 모여있는 패키지
        - data, label
        - ex) Fashion-MINIST data
        
    * Dataloader
        - Dataset을 model에 공급할 수 있도록 iterable 객체로 감싸줌
'''

training_data = datasets.FashionMNIST(
    root='data',
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ToTensor()
)

print(training_data)
print(type(training_data))

print('-'*30)
print(training_data[0])

# 데이터 시각화
labels_map = {
    0: 'T-Shirt',
    1: 'Trouser',
    2: 'PullOver',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle Boot'
}
figure = plt.figure(figsize=(8,8))
cols, rows = 3, 3

for i in range(1, cols*rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis('off')
    plt.imshow(img.squeeze(), cmap='gray')

plt.show()

print('-'*30)

training_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=False)

# Dataloader를 통해 반복하기 iterate
train_features, train_labels = next(iter(training_dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap='gray')
plt.title(labels_map[label])
plt.axis('off')
plt.show()
print(f"Label: {label}")

print('-'*30)
'''
    * CustomDataset
'''
class CustomDataset(datasets):
    # 필요한 변수 선언, 데이터셋의 전처리
    def __init__(self, np_data, transform=None):
        self.data = np_data
        self.transform = transform
        self.len = np_data.shape[0]
    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
            return sample

'''
    tr.Compose() : 여러개의 이미지 전처리 기능
'''
def squre(sample):
    return sample ** 2

trans = tr.Compose([squre])

# 커스텀 데이터 셋 생성
np_data = np.arrange(10)

# CustomDataset 클래스의 인스턴스 생성
# 이미지 전처리 기능인 squre함수를 적용할 수 있는 데이터셋
custom_dataset = CustomDataset(np_data, transform=trans)

# custom_dataset으로부터 새로운 데이터로더 생성
# batch_size는 각각의 샘플 개수, shuffle은 샘플을 섞어서 읽어옴
custom_dataloader = DataLoader(custom_dataset, batch_size=2, shuffle=True)

for _ in range(3):
    for data in custom_dataloader:
        print(data)
    print('='*20)

# device 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

'''
    * Model Class 만들기
'''

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()       # nn.Module의 생성자 호출
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 10)
        )
    def forward(self, x):
        x = self.flatten(x)     # 입력 x를 전달받아 전체 신경망을 순전파하는 함수
        ezen = self.linear_relu_stack(x)    # 입력 x를 펼치는 flatten 계층을 적용한 후, linear_relu_stack 객체 적용
        return ezen

model = NeuralNetwork().to(device)
print(model)
