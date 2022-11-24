'''
    한국어 연습 프로그램
        - 연습할 한국어 리스트
        - 리스트에서 순서대로 단어를 가져와 화면에 출력
        - 프로그램 사용자는 단어를 그대로 입력하고
        - 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료

        Let's Learning Korean
        사랑해
        사랑해
        귀엽다
        귀엽다
        고마워
        고마워
        행복해
        햄복해
        프로그램 종료
'''
korean_list = ["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
score = 0
while True:
    for korean in korean_list :
        print(korean)
        key = input()
        if key == korean :
            score += 1
        else:
            break
    print("프로그램 종료")
    print("전체 문제 개수 :", len(korean)+1, "개")
    print("맞힌 문제 개수 :", score, "개")
    print("틀린 문제 개수 :", len(korean)+1 - score, "개")
    break

# 전체 문제 개수 : 4개 len(korean)
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개

