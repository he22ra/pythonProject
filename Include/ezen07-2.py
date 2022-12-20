'''
    ezen07-2

    * Default parameter (기본 인자)
        - 함수의 파라미터에 기본값 지정 가능
        - 파라미터를 명시하지 않을 경우, 지정된 기본값으로 대체 
        - 디폴트 파라미터 뒤에 일반 파라미터가 위치할수 없음
            - e.g) def test(a,b,c = 1)
                   def test(a,b = 1, c = 2)
                   def test(a = 1,b = 1, c = 3)

                  올바르지 않은 예)
                   def test(a,b =1, c)
                   def test(a=1,b,c) 
                   def test(a=1,b=1,c) 
'''
print('test')
#help(print)

def plus_ver2(number_01, number_02 = 100):
  print(number_01 + number_02)

plus_ver2(11)
plus_ver2(number_01 = 0, number_02 = 77)

print()

'''
  *agrs : 함수를 호출할 때 아규먼트의 갯수를 특정지을 수 없을 때 사용
          불특정한 수의 숫자들은 'args'라는 튜플에 추가됨
'''

def plus_unlimited(*args):
  print(type(args), args)
  sum(args)
  print(sum(args))

plus_unlimited(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

print()
'''
  **kwargs : 함수를 호출할 때 키워드 아규먼트의 개수를 특정지을 수 없을 때
              불특정한 수의 키워드들은 'kwargs'라는 딕셔너리에 추가됨

'''
def plus_unlimited(*args, **kwargs):
  print(type(kwargs), kwargs)
  sum(kwargs.values())   # 키워드 아규먼트의 합
  sum(args)             # 아규먼트의 합
  print(sum(args) + sum(kwargs.values()))

plus_unlimited(1,2,3,1, num1 = 100, num2 = 3000, num3 = 20, num4 = 7)

'''
    list를 함수의 파라미터로 넣어 실행하는 경우
'''
list_numbers = [1,2,3,4,5,6,7,8,9,10]
plus_unlimited(*list_numbers)


'''
    딕셔너리를 함수의 파라미터로 넣어 실행하는 경우
'''
dict_heights = {'ezen_height' : 178, 'ezenyoung_height' : 180, 'sugiezen_height' : 176, 'ezensun_height' : 180}
plus_unlimited(**dict_heights)

'''
  Docstring : 함수의 설명을 작성해놓은 기술문서
              수 많은 파이썬 함수의 사용법과 정보를 나타냄
'''

#help(plus_unlimited)
#help(print)
#help(input)

'''
    * Lambda 함수
        - 단일문으로 표현되는 익명함수 
            - 익명함수란 이름이 없는 구현체만 존재하는 간단한 함수를 의미 
        - 코드 상에서 한번만 사용되는 기능이 있을 때, 
          굳이 함수로 만들지 않고 1회성으로 만들어서 쓸때 사용         

        - lambda가 유용하게 사용되는 대표적 함수(3가지)
            - 함수형 프로그래밍의 기본 요소이기도 함
            - filter() : 특정 조건을 만족하는 요소만 남기고 필터링
            - map() : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트를 반환
            - reduce() : 앞 2개의 원소를 가지고 연산.
                         연산의 결과가 또 다음 연산의 입력으로 진행됨.
                         따라서 마지막까지 진행되면 최종 출력은 한개의 값만 남게됨.              
'''

square = lambda x:x**2
print(square(5))

def add(x, y):
  return x + y

add = lambda x,y:x+y 
print(add(10,20))

def pythagoras(num1, num2):
  return(num1**2 + num2**2)**0.5

pythagoras_lambda = lambda num1, num2:(num1**2 + num2**2)**0.5
print(pythagoras_lambda(1,1))

'''
  키가 180이상이면 "키가 큽니다"
  그렇지않은 경우, "계속 키가 클 겁니다." 메세지 출력
  height_high(181)
  height_high(178)
'''
def height_high(height):
  if height >= 180 :
    print("키가 큽니다")
  else :
    print("계속 키가 클 겁니다.")
  
height_high(181)
height_high(178)

def height_high(height):
    return '키가 정말 큽니다.' if height >= 180 else '계속 키가 클 겁니다.'

result = height_high(181)
print(result)
result = height_high(178)        
print(result)



'''
    다섯 사람의 키입니다.
    height_high() 함수를 이용하여 실행해보기
    
    map(함수, 입력들)
    map(function, *iterables) 형태로 사용가능함 
        - *iterables : 원소를 하나씩 차례로 반환 가능한 object를 의미함 (list, str, tuple..)

'''

def calc(x):
    return x*x

for i in range(1,6): 
    print(calc(i))   

print()
list(map(calc, range(1,6)))


dict_heights = {'ezen_height' : 178, 'ezenyoung_height' : 180, 'sugiezen_height' : 176, 'ezensun_height' : 180, 'sunge_height' : 175}
result = list(map(height_high, dict_heights.values()))
print(result)


