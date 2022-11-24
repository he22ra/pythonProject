'''
    1.로또 번호 6개 생성
    2.로또 번호는 1~ 45까지 랜덤
    3.6개의 숫자 모두 달라야함
    4.get_random_number() 함수 사용

    출력 예) 1 8 11 13 26 42
    -리스트, 반복문, 조건문
'''
import random
def get_random_number():
    number = random.randint(1,45)
    return number
number_list = []
count = 0
while True :
    if count > 5 :
        break
    x = get_random_number()
    if x not in number_list :
        number_list.append(x)
        count += 1

number_list.sort()

for num in number_list:
    print(num, end="번 ")