'''

'''
try:
    x = 10
    result = x / 0
    print(result)
except:
    print("예외 발생")

print()

arr = [7, 5, 9]
index = 3

try:
    data = arr[index]
    print(data)
except IndexError as e:
    print("배열의 크기를 벗어난 인덱스에 접근할 수 없습니다.")
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다.")
    print("[오류메시지 : ]")
    print(e)
