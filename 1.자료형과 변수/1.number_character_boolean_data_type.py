# 주석(comments)
'''
복수줄 주석

'''

# 숫자형 - 숫자 데이터, 정수형, 실수형
# 문자열 - 문자를 나열한 것
#       - "(큰따옴표) 또는 '(작은따옴표)로 문자열의 시작과 끝을 나타냄
#       - ' "" ', " '' " 둘다 사용 가능
# 불린형 - 참 또는 거짓 (True or False)

'''
print()
    -,로 여러 변수를 나열하면 한줄로 출력
    - 기본적으로는 한 칸 띄어쓰기 후 출력
'''
"""
여러줄에 걸쳐 문자열 표현 가능
"""
# - indexing & slicing string
# - 문자 열의 각 문자는 순서가 있음
# - 이 때

print(1)
print(1.1, -2.0, 3.14, -0.1)
print("문장 문자열")
print('문장 문자열')
print('"문장 문자열"')
print(True)

c = None
print(c)

d = ''' Hello
        Ezen !
    '''
e = """ 
        Hello
    World !
    """
print(d)
print(e)

f = 'Hello World'
print(f[10])
print(f[0])
print(f[-1])
# print(f[11])      # 범위를 넘어갈 경우 에러 발생
print(f[0:11])
print(f[0:1])
print(f[:5])
print(f[3:])
print(f[:])

print(f.upper())
print(f.replace('H','j'))

temperature = 15.5
prob = 50.0

g = '오늘 기온{}도 이고, 비올 확률은 {}%입니다.'.format(temperature, prob)
print(g)