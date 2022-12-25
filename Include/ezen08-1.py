'''
    * 웹 크롤링
        - 웹 페이지에 있는 데이터를 요청하여 가져오는 방법 활용 
        - request, bs4 라이브러리 활용 
            - beautifulsoup4(bs4)
                - HTML source에서 tag별 계층 구조 를 파악하기 쉽게 parse 
                  tree 형태로 변환해주는 라이브러리 
                - 손쉽게 HTML source에서 원하는 정보를 추출할 수 있음 
                    - find(), find_all() 함수를 이용하면 원하는 tag와 속성에 맞는
                      모든 정보를 가져올 수 있음

        - 해당 페이지의 page source를 직접 가져옴 
        - 웹 페이지 우클릭 "페이지(프레임) 소스보기"로 같은 HTML 소스를 볼수 있음 
        - 마우스 우클릭을 하면 "검사" 기능 활용 
'''

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

import requests
source = requests.get(page_url).text
# print(source)

#beautifulsoup4(bs4)를 불러옴 = 소스 불러오기
import bs4
source = bs4.BeautifulSoup(source, features="html.parser")
# print(source)

#prettify()함수는 소스를 트리형태로 보여준다.
# source = source.prettify()
# print(source)

#find_all() : HTML source에서 조건을 만족하는 모든 tag를 가져오는 함수
result = source.find_all('td', class_ = 'number_1')
print(result)