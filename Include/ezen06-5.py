#ezeon06-5
'''
  6) Dataframe
    - index 행
    - column 행
    - 데이터 선택 (slicing)
      - 데이터 위치를 활용한 데이터 가공 : loc(), iloc()
    
'''
import pandas as pd

df = pd.DataFrame()
print(type(df))

stu_list = [['Susan', 'Jessica', 'John', 'Michael'], [19, 15, 16, 17]]
print(stu_list)

df = pd.DataFrame(stu_list)
print(df)

df = df.T
print(df)

print("================")

columns_name = ['name', 'age']
df.columns = columns_name
print(df)

'''
"I am quitting this exam"
"This is the quickest approach I ever seen"
"The king should make quick decision"

주어진 문장을 모두 맞게 변경 replace()

"I am wuitting this exam"
"This is the wuickest approach I ever seen"
"The king should make wuick decision"
'''
quotes = ["I am wuitting this exam", "This is the wuickest approach I ever seen", "The king should make wuick decision"]

for quote in quotes:
  print(quote.replace('w','q'))

print("=============")
# 주어진 문장의 단어 갯수 출력
for quote in quotes:
  print(len(quote.split(" ")))

print("=============")
candidates = {"이순신" : 146, "이도" : 160, "유성룡": 167, "정철": 175.3, "이황" : 207}
soccer_team=[]

#키가 175 이상인 사람만 추가
for key, value in candidates.items():
  if (value >= 175) :
    soccer_team.append(key)

print(soccer_team)
print("======short.ver======")
soccer_team2=[ name for name, height in candidates.items() if height >= 175]
print(soccer_team2)

#구구단
for num2 in range(1,10):
  for num1 in range(2, 10):
    print("{} x {} = {}".format(num1, num2, num1*num2), end="\t")
  print()

print()
#구구단 가로 출력 (while문)

num2 = 1
while num2 < 10 :
  num1 = 2
  while num1 < 10 :
    print("{} x {} = {}".format(num1, num2, num1*num2), end="\t")
    num1 += 1
  
  print()
  num2 += 1

print()

'''
  1~1000000까지 숫자 중 3의 배수 찾고 갯수 출력
  코드를 실행하는데 걸린 시간
'''
import time
start = time.time()

num = range(1, 1000000)
ls = []
for num in range(1, 1000000+1) :
  num+=1
  if num % 3 == 0 :
    ls.append(num)

end = time.time()

print(f"소요시간 : {end - start}")
print(f"리스트 원소 갯수 : {len(ls)}개")
print()

'''
지갑 5000원이상이면, 택시를 탐
걸어서 갈수도 있음
택시 : 3000원 소비

2000원 이상이면, 버스를 탐
버스 : 1000원 소비

2000원 미만이면, 걸어감
위 조건을 반영하는 코드 작성
'''
money = 2000
taxi = True
bus = True
walk = True

if money < 2000 :
  taxi = False
  bus = False
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  print("걷기")
  print(f"잔액 : { money}원")
 
elif money < 5000 :
  taxi = False
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  print("버스 타기")
  print(f"잔액 : { money - 1000}원")

else :
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  if taxi :
    print("택시 타기")
    print(f"잔액 : { money - 3000}원")
  else :
    print("걷기")

print("================================")
'''
게임 1회: 500원

현재까지 게임한 횟수는 :
현재 잔액 : 

최종 게임 횟수 :
최종 잔액 : 

'''

money = 4980
game = 500
counts = 0
taxi = True
bus = True
walk = True

if money < 2000 :
  taxi = False
  bus = False
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  print("걷기")
  print(f"잔액 : { money}원")
 
elif money < 5000 :
  taxi = False
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  print("버스 타기")
  print(f"잔액 : { money - 1000}원")

else :
  print(f"taxi : {taxi},  bus : {bus}, walk: {walk}")
  if taxi :
    print("택시 타기")
    print(f"잔액 : { money - 3000}원")
  else :
    print("걷기")

while money > 0 :
  counts += 1
  money -= game
  print(f"현재까지 게임한 횟수는 : {counts}")
  print(f"현재 잔액 : {money}")
print()
print(f"최종 게임 횟수 : {counts}")
print(f"최종 잔액 : {money}")