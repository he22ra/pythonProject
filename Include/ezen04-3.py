# 딕셔너리 자료형 (순서x, 중복x, 수정O, 삭제O)
'''
  1. 사전(dictionary) 자료형
    1) 데이터를 키(key)와 값(value) 쌍의 형태로 저장할 때 사용할 수 있음

    사전 데이터[키] = 값

'''
# 선언
a = {'name' : 'ezen', 'address':'seoul', 'birth': '2022-01-13'}
b = {0 : 'Hello Ezen!'}
c = {'arr':[1, 2, 3, 4]}


arr1 = ['컴퓨터', '키보드', '모니터']
arr2 = ['computer', 'keyboard', 'moniter']

data = {}
for i in range(3):
  data[arr1[i]] = arr2[i]

print(data)

# 모든 키(key)를 하나씩 확인할 때는 keys()메서드 사용
data = {}
data['apple'] = '사과'
data['banana'] = '바나나'
data['carrot'] = '당근'

for key in data.keys():
  print("key : ", key)

#keys()
print('a : ', a.keys())
print('b : ', b.keys())
print('c : ', c.keys())

print('a : ', list(a.keys()))
print('b : ', list(b.keys()))
print('c : ', list(c.keys()))

print('a : ', a.values())
print('b : ', b.values())
print('c : ', c.values())

print('a : ', list(a.values()))
print('b : ', list(b.values()))
print('c : ', list(c.values()))