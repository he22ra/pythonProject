# 비만도 계산기를 만들어보시오
'''
예시)
    BMI계산기입니다.
    신장 : [입력]
    체중 : [입력]
    BMI : ?
'''
print("BMI계산기입니다")
height = float(input(" 신장(cm) : [입력해주세요] >>>"))
weight = float(input(" 체중(kg) : [입력해주세요] >>>"))
print("BMI : "+str(weight/(height*0.01)**2))
