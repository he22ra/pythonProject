'''
    파일 입출력
        1) 파일을 읽어 다른 파일에 기록하기
            - 파일_객체 = open(file, mode)
        2) read()
            readline() : 파일 내에서 1줄을 읽어옴
            readlines() : 모든 내용 읽어오기
'''

print('파일을 읽기모드로 오픈한다')
myfile01 = open('ezen.txt', 'rt', encoding='UTF-8')
linelists = myfile01.readlines()
# print(linelists)
myfile01.close()

total = 0
for one in linelists:
    score = int(one)
    total += score

average = total / len(linelists)

print('파일을 쓰기모드로 오픈한다')
with open('result2.txt', 'wt', encoding='UTF-8') as f:
    f.write('총점 : '+str(total)+'점 \n')
    f.write('평균 : '+str(average)+'점 \n')

print('작업완료')


