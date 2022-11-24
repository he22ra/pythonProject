'''
    상속의 업그레이드
        - 클래스 변수(인스턴스들이 모두 공유하는 변수)

    드래곤 클래스에 인스턴스 속성을 추가하기
    부모 클래스에 클래스 변수를 추가하기
'''
# 부모클래스
class Monster:
    max_num = 1000      #클래스변수
    def __init__ (self, name, health, attack, location):
        self.name = name
        self.health = health
        self.attack = attack
        self.location = location
        Monster.max_num -= 1

    def move(self, num):
        self.location += num
        return print(f"[{self.name}]님이 {num}만큼 이동합니다. 현재 위치 : {self.location}")