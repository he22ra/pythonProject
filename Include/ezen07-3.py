'''
  리스트 내 원소 중에서 가장 큰 값의 인덱스(위치)를 찾아서 반환하는 함수를 작성하시오
  data = [7,1,5,9,3,2,4]
  for i in data:
  if data.index(i) > data.index(i+1):
    print(data.index(i))
  else:
    print(data.index(i+1))
'''
data = [7,1,5,9,3,2,4]

def find_index_largest(data):
  largest_index = 0
  for i in range(len(data)):
    if data[largest_index] < data[i]:
      largest_index = i
  return largest_index

data = [71,1,115,9,13,2,4]
largest_index = find_index_largest(data)
print(largest_index)

'''
  특정한 값을 가지는 원조의 인덱스를 찾는 함수를 작성해보시오
  [3,5,7,9],2 ==> -1 없을 때
  [3,5,7,9],7 ==> 2

  enumerate()
  '''


def find_index_num(list, num):
  same_index = 0
  for i, val in enumerate(list):
    print(type(i), type(val))
    if val == num :
       return i
  return -1

def find_index_num2(list, num):
  same_index = 0
  for i, val in enumerate(list):
    print(type(i), type(val))
    while i < len(list):
      same_index = -1
      if val == num :
        same_index = i
  return same_index


list = [3,5,7,9]
same_index = find_index_num(list,5)
print(same_index)

'''
 자연수 중 소수 판별 함수 작성
 소수면 True,
 소수가 아니면 False
'''
def find_prime_number(num):
  if num <= 1:    # 1이하인 경우 소수가 아님
    return False  
  for i in range(2, num) :
    if num % i == 0:
      return False
  return True

print(find_prime_number(89))