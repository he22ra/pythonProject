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
korean = ["사랑해", "귀엽다", "고마워", "행복해"]
print("Let's Learning Korean")
while True:
    for i in range(0,len(korean)) :
        key = input(korean[i])
        if key == korean[i] :
            i += i
        else:
            print("프로그램 종료")
            break
    break