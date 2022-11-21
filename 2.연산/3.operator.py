#   대입연산, 산술연산, 비교연산, 논리연산

x = 5
y = 2

#   산술연산
#   -   연산자        설명
#   -   //           몫
#   -   **          제곱

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# 문자열 연산
tag1 = "#노이즈 캔슬링"
tag2 = "#후면 통풍구"
tag3 = "#외부 소리 감지"

tag = tag1 + tag2 + tag3
print(tag)

message = "파이썬 \n" * 5
print(message)

#복합할당연산자
level = 10
#  레벨 1 증가
level = level + 1
print(level)
level += 1
print(level)
level -= 1
print(level)

health = 2000
health -= 300 # 체력 300 감소
print(level, health)

attack = 300
attack *= 1.5   #공격력 1.5배 증가

speed = 420
speed /= 2  #스피드 50%감소

print (level, health, attack, speed)