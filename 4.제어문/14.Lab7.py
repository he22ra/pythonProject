'''
    사용자로부터 국어, 수학 영어 성적이 입력됩니다.
    세 과목의 평균점수가 80점 이상이면 합격.
    프로그램의 오류로 80점 이상일경우 불합격이 표시되도록 프로그램 작성
    (단, 0~100사이의 숫자를 입력하지 않으면 잘못입력했습니다를 출력하시오)

    예시)
        국어 >>>
        수학 >>>
        영어 >>>

        결과 : 불합격
'''

korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))

subject_num = 3
point_sum = korean + math + english
point_avg = point_sum/subject_num

if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100 :

    if  point_avg >= 80 :
        print("평균점수 : "+str(point_avg))
        print("불합격")
    else :
        print("평균점수 : " + str(point_avg))
        print("합격")

else:
    print("잘못입력했습니다")


if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100 :
    print("잘못입력했습니다")
elif point_avg >= 80 :
    print("평균점수 : " + str(point_avg))
    print("불합격")
else :
    print("평균점수 : " + str(point_avg))
    print("합격")
