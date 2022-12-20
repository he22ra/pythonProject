#파이썬 데이터 타입(자료형)
#리스트, 튜플

#리스트 자료형 (순서o, 중복o, 수정o, 삭제o)

#선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Powerful', 'Health', 'Features']
e = [10, 100, ['Powerful', 'Health', 'Features']]

#인덱싱
print()
print('d : ', type(d), d)
print('d : ', d[1])
print('d : ', d[0] + d[1]+ d[1])
print('d : ', d[-1])
print('e : ', e[-1][1])
print('e : ', e[-1][1][-2])

#수정 삭제

c[1:2] = ['a','b','c']
print('c : ', c)
c[1:2] = [['a','b','c']]
print('c : ', c)
c[1:3] = []
print('c : ', c)
del c[3]
print('c : ', c)