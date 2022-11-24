'''
    몬스터
    땅몬스터 물몬스터 공중몬스터

    2. 부모클래스
    - 속성
        - 이름, 체력, 공격력
    - 함수
        - 이동하기(move)
'''
# 부모클래스
class Monster:
    def __init__ (self, name, health, attack, location):
        self.name = name
        self.health = health
        self.attack = attack
        self.location = location

    def move(self, num):
        self.location += num
        return print(f"[{self.name}]님이 {num}만큼 이동합니다. 현재 위치 : {self.location}")

#자식클래스  (부모클래스) >> 상속
class Wolf(Monster):
    pass    # 정의는 나중에..

class Shark(Monster):
    def move(self):   #메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날아가기")

wolf = Wolf("늑대", 500, 200, 0)
wolf.move(20)
wolf.move(-10)
wolf.move(100)

shark = Shark("샤크", 1200, 400, 10)
shark.move()

dragon = Dragon("드래곤", 1000, 500, 30)
dragon.move()