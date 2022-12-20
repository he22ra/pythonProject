'''
    정규 표현식
        1) reqular expression
            - 특정한 패턴과 일치하는 문자열을 '검색', '치환', '제거'하는 기능 지원
            - 정규표현식의 도움없이 패턴을 찾는 작업은 불완전. 작업의 cost가 높음
        2) 정규표현식 메타 문자 (기호)
            -
        - 문자열 패턴                패턴비교
            문자열1    ab123       동일한 패턴
            문자열2    cd456           즉, 문자2개+숫자3개
            문자열3    ef789
            문자열4    abc12       다른 패턴
'''

import re

mylist = ['ab123', 'cd456', 'ef789', 'abc12']

#정규표현식 작성
regex = '[a-z]{2}\d{3}'     #[a-z]는 알파벳 소문자 중 1개 글자를 선택
#패턴 객체 생성
#compile()
pattern = re.compile(regex)

print('#문자 2개로 시작하고, 숫자3개로 끝나는 항목')
matchlist = []

for item in mylist:
    if pattern.match(item):
        print(item, ' : 조건에 적합')
        matchlist.append(item)
    else:
        print(item, ' : 조건에 부적합')

print('적합한 항목들')
print(matchlist)