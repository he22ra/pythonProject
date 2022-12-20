'''
    * 크롤링
        1) urllib 라이브러리 이용한 웹 페이지 크롤링
            - urlib.request 모듈
                - url을 열어서 내용을 읽어들이는 기능
                - 웹을 통하여 데이터를 요청하는 기능
                - http 클라이언트의 인터페이스를 위한 함수 및 클래스 제공
                    - urlretrieve : url파일을 savename 파일명으로 저장
'''

import urllib.request           #라이브러리 읽어들임

url = "https://shared-comic.pstatic.net/thumb/webtoon/785703/thumbnail/thumbnail_IMAG04_bece7723-5efa-48cf-ab7e-61a4c7b83f77.jpg"
savename = "urldownload_webtoon01.png"

#다운로드
urllib.request.urlretrieve(url, savename)
print('웹이 있는 이미지' + url + '를', end=' ')
print(savename+'파일로 저장하였습니다.')
