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