'''
    세 개의 정수를 인자로 받아,
    합계와 평균을 출력해주는 함수를 만드시오

    예) 합계:      평균:

'''
def num(a, b, c):
    sum = a+b+c
    avg = (a+b+c)/3
    print("합계:",sum," ","평균:",avg)

num(5,7,3)

#설명문(docstring) """ """
#문자열 포매팅(f"")
def print_sum_avg(a,b,c):
    """
    세개의 숫자를 입력받아 합계와 평균을 출력하는 함수
    :param x:
    :param y:
    :param z:
    :return:
    """
    sum = a + b + c
    avg = (a + b + c) / 3
    print(f"합계: {sum} 평균: {avg}")

print_sum_avg(8,9,10)