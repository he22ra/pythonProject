# 입력함수 : 사용자로부터 데이터를 입력 받는 함수 (input())
# x = input()
#   - 1) 할당연산자(=) 오른쪽부터 실행
#   - 2) input() 함수 실행시, 입력을 기다림
#   - 3) 사용자가 데이터를 입력하고 엔터를 침
#   - 4) intput() 함수 자리에 데이터가 들어감

# x = input("입력하세요>>>")
#   - 1) 할당연산자(=) 오른쪽부터 실행
#   - 2) input() 함수 실행시, 메세지를 출력하고 입력을 기다림
#   - 3) 사용자가 데이터를 입력하고 엔터를 침
#   - 4) intput() 함수 자리에 데이터가 들어감

#   자료형 확인하기 : type(x)

# 사용자로부터 두 개의 숫자를 입력받고, 더한 결과를 출력하시오
x = input("첫번째 숫자를 입력하세요>>>")
y = input("두번째 숫자를 입력하세요>>>")

#print(type(x))
result = int(x) + int(y)
print("x + y = "+result)