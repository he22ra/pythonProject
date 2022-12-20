'''
    * 크롤링
        1) urllib 라이브러리 이용한 웹 페이지 크롤링
            - urlib.request 모듈
                - url을 열어서 내용을 읽어들이는 기능
                - 웹을 통하여 데이터를 요청하는 기능
                - http 클라이언트의 인터페이스를 위한 함수 및 클래스 제공
                    - urlretrieve : url파일을 savename 파일명으로 저장
                    - urlopen() : 네트워크를 통해 원격 객체를 읽고 메모리에 올리는 역할 수행
                                    read() 함수로 읽어들인 데이터는 바이너리 데이터임
'''

import urllib.request           #라이브러리 읽어들임

url = "https://shared-comic.pstatic.net/thumb/webtoon/785703/thumbnail/thumbnail_IMAG04_bece7723-5efa-48cf-ab7e-61a4c7b83f77.jpg"
savename = "urldownload_webtoon02.png"

#urlopen() 함수이용하여 다운로드
result = urllib.request.urlopen(url)

#read() 함수를 이용해 바이너리 형식으로 변경
data = result.read()
print('type() : ', type(data))

# 파일로 저장하기 (close()는 자동)
with open(savename, mode='wb') as f:
    f.write(data)
    print(savename + ' 파일로 저장되었습니다.')