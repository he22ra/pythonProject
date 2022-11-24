# 함수의 입력 parameter의 개수를 모를 때
# *(aserisk)를 앞에 붙이는 것으로 여러개의 parameter를 받아서 tuple로 변환

def add_many(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_many(1, 2, 3))
print(add_many(1, 2, 3, 4, 5))

def add(a,b):
    return a+b

f = lambda a, b : a + b
print(f(3, 5))
print(add(3, 5))

def get_length(s):
    return len(s)

#글자 길이에 따른 정렬
strings = ['Meet', 'themost', 'rugged', 'and']
strings.sort(key=lambda s:len(s))
print(strings)

# 수학 계산
import math
number = 3.14
print(abs(number))  #절대값
print(math.ceil(number)) #올림
print(math.floor(number)) #내림

print(math.sin(number))
print(math.cos(number))