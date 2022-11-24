a = [1, 2, 4, 3, 5]
for i in a :
    print(i, i*2)
print('ezen')

for x in 'hello world':
    print(x, end="")

print()

# 짝수, 홀수 구분해서 출력
a = [1, 3, 10, 4, 5]
for num in a :
    if num % 2 == 0:
        print(num/2)
    else:
        print(num+1)