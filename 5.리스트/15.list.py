'''
    리스트 자료형
     - 리스트명 = [데이터, 데이터, 데이터, ...]
'''

# 데이터가 없는 리스트
empty = []

# 데이터가 있는 리스트
earpods = ["액티브 노이즈 캔슬링", "적용형 주변음 허용 모드", "터치 제어", "개인 맞춤형 공간 음향"]
print(earpods)

# 데이터 조작하기
# 인덱스는 0부터 시작
print(earpods[2])
print(earpods[-1])

# 데이터 추가하기
earpods.append("강한 생활 방수 디자인")
print(earpods)

# 데이터 할당하기
earpods[1] = "기기 간 자동 전환"
print(earpods)

# 데이터 삭제하기
del earpods[0]
print(earpods)

# 리스트 슬라이싱
print(earpods[2:3])

# 리스트 길이
print(len(earpods))

# 리스트 정렬
earpods.sort()
print(earpods)