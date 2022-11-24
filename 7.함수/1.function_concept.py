'''
    함수의 기본 형태
        def 함수이름():
            명령블록

    함수 호출하기
        함수이름()

    4. 함수의 매개변수와 반환값이 있는 형태
        def 함수이름(매개변수1, 매개변수2):
            명령블록
            return 반환값

        함수 호출하기
            함수이름(인자1, 인자2)
'''

def printMessage(name, date):
    print("안녕하세요 ", name, "님", sep="")
    print("현재 2022년도 쿠폰 사용 남은 기간이 ", date, "일 남았습니다")

printMessage("순신", 30)
printMessage("임당", 15)
printMessage("방원", 7)
printMessage("도", 5)