'''
    if
    if - else
    if - elif
    if - eli - else

    현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력해주는 프로그램 작성
    조건 ) 20000원 이상 : 치킨, 10000원 이상 : 떡볶이, 3000원 이상 : 편의점김밥, 그 외 : 굶기
'''
account = int(input("현재 가진 금액 : >>>"))
if account>=20000 :
    print("치킨")
elif account>10000 :
    print("떡볶이")
elif account > 3000:
    print("편의점김밥")
else:
    print("굶기")