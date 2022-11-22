'''
    턱걸이 평균 측정 프로그램
    턱걸이 횟수 저장 리스트 생성
    일주일간의 턱걸이 횟수를 입력받아 리스트에 저장
    리스트에 저장된 데이터의 평균 출력

    예) 1일차 턱걸이 횟수 >>>
        2일차 턱걸이 횟수 >>>
        ..
        7일차 턱걸이 횟수 >>>
        평균 턱걸이 횟수 : []
'''

day1 = int(input("1일차 턱걸이 횟수 >>>"))
day2 = int(input("2일차 턱걸이 횟수 >>>"))
day3 = int(input("3일차 턱걸이 횟수 >>>"))
day4 = int(input("4일차 턱걸이 횟수 >>>"))
day5 = int(input("5일차 턱걸이 횟수 >>>"))
day6 = int(input("6일차 턱걸이 횟수 >>>"))
day7 = int(input("7일차 턱걸이 횟수 >>>"))

week_pull_up = [day1, day2, day3, day4, day5, day6, day7]
pull_up_total = day1 + day2 + day3 + day4 + day5 + day6 + day7
pull_up_avg = pull_up_total / len(week_pull_up)

print(week_pull_up)
print("평균 턱걸이 횟수>>>", int(pull_up_avg))