from bs4 import BeautifulSoup

# beautiful soup 라이브러리를 이용한 태그 속성 다루기
html = open('cartoon.html', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

# string 속성 : 특정 요소의 문자 추출
h1 = soup.select_one('div#cartoon > h1').string
print("h1 = ", h1)

# 객체.select(<선택자>) : css 선택자로 여러 요소를 리스트로 추출
elements = soup.select("ul.elements > li")
for element in elements:
    print("elements = ", element.string)

print('='*20)

choice = lambda x : print(soup.select_one(x).string)

print('\nchoice("#item5") : ', end=' ')
choice("#item5")

print('\nchoice("#item4") : ', end=' ')
choice("#item4")

print('\nchoice("ul > #item3") : ', end=' ')
choice("ul > #item3")

print()
print('\nsoup.select("li")[1].string : ', end=' ')
print(soup.select("li")[1].string)

#find_all : 조건에 맞는 HTML 태그를 전부 찾아줌
print('\nsoup.find_all("li")[3].string : ', end=' ')
print(soup.find_all("li")[3].string)

print()

#^= : ~으로 시작하는, $= : ~으로 끝나는
result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])

print()

# *= : ~을 포함하고 있는
result = soup.select('a[href*="ezen"]')
for item in result:
    print(item['href'])

