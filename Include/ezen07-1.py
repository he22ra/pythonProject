# ezen07-1
# 파이썬 함수 및 람다(lambda)

'''
  1. 함수 정의
  def function_name(parameter):
    code

  2. 함수 호출
  funtion_name()
'''
def hello(world) :
  print("Hello,", world)

hello("Nice Year")

print()

#funtion2
def hello_return(world):
  value = "Hello, " +str(world)
  return value

str = hello_return("Ezen!")
print(str)

#function3 다중리턴

def func_mul(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return (y1, y2, y3)

print()
#튜플리턴

#리스트리턴
def func_mul3(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return [y1, y2, y3]

lis = func_mul3(6)
print(type(lis), lis, set(lis))

print()
#dictionary return

def func_mul4(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return {'ret1' : y1, 'ret2' : y2, 'ret3' : y3}

dic = func_mul4(8)
print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())

#함수4 (*args, **kwargs)

# *args
def args_func(*args) : #매개변수명 자유롭게 변경 가능
  for i,v in enumerate(args) :
    print('{}'.format(i), v, end=' ')

args_func('ezen')
print()
args_func('ezen', 'ezenit')
print()
args_func('ezen', 'ezenit', 'seoul')

print()
print("==========================")

# **kwargs

def args_func2(**kwargs) : #매개변수명 자유롭게 변경 가능
  for v in kwargs.keys() : # key, value 형태
    print('{}'.format(v), kwargs[v], end=' ')

args_func2(name1='lee')

print()
print("==========================")

#함수5 - 전체 혼합

print()
print("==========================")

#함수6 - 중첩 함수
def nested_func(num):
  def func_in_func(num):
    print(num)
  
  print("In func")
  func_in_func(num + 100)

#func_in_func(1)
nested_func(1)

print()
print("==========================")

#함수6 - 중첩 함수