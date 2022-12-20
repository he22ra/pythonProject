import requests
import bs4

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"

source = requests.get(page_url).text
source = bs4.BeautifulSoup(source, features="html.parser")

#find_all() : HTML source에서 조건을 만족하는 모든 tag를 가져오는 함수
pages = source.find_all('td', class_ = 'pgRR')[0]
print(pages)
last_url = source.find_all('td', class_ = 'pgRR')[0].find_all('a')[0]['href']
print(last_url)
result = last_url.split('&page=')
last_page = int(last_url.split('&page=')[-1])
print(last_page)

date_list=[]
closing_price_list=[]

for page_no in range(1, last_page+1):
  page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"

  #날짜 추출
  dates = source.find_all('td', class_ = 'date')
  for date in dates:
    date_list.append(date.text)
  
  #체결가 추출
  closing_prices = source.find_all('td', class_ = 'number_1')
  for closing_price in closing_prices[::4]:
    closing_price_list.append(closing_price.text)

print(len(date_list))
print(len(closing_price_list))





