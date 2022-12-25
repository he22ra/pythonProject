'''
    * 웹 크롤링
      - 날짜 추출
        - td 태그중에 원하는 정보만을 따로 가져와야 함
        - 날짜 태그 규칙 찾아서 td 태그들 중에 날짜를 가져옴


'''
page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)

import requests
source = requests.get(page_url).text

#beautifulsoup4(bs4)를 불러옴 = 소스 불러오기
import bs4
source = bs4.BeautifulSoup(source, features="html.parser")

#find_all() : HTML source에서 조건을 만족하는 모든 tag를 가져오는 함수
dates = source.find_all('td', class_ = 'date')
print(dates) # 리스트타입
print(dates[0]) # 1번째 출력 >> <td class="date">2022.12.19</td>
print(dates[0].text) # 텍스트만 출력 >> 2022.12.19

date_list = []

for date in dates:
  date_list.append(date.text)

print(date_list)

#체결가 추출
closing_prices = source.find_all('td', class_ = 'number_1')
print(closing_prices[0].text)
print(closing_prices[::4])
print(closing_prices[::4][0].text)

closing_price_list = []
for closing_price in closing_prices[::4]:
  closing_price_list.append(closing_price.text)

print(closing_price_list)







