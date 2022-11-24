'''
    1. 클래스
        - 속성
            - 체력
            - 공격력
            - 방어력
            - 이동속도
        - 메서드
            - 위치로 이동하기
            - 공격하기
            - 아이템 사용하기
            - 귀환하기

    2. 클래스 만들기
        class 클래스이름 :
            def 메서드이름 :
                명령블록

    3. 클래스 사용하기
        인스턴스 = 클래스이름()
        인스턴스.함수()
'''

class Champion :
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{self.name}님 환영합니다.")

    def basic_attack(self):
        print(f"{self.name}님의 기본 공격력 : {self.attack}")

ezrael = Champion("이즈라엘", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 750, 92)

ezrael.basic_attack()