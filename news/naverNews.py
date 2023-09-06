# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "2jnsvCU4ILz1d9iopeAc"
client_secret = "NlP_x5Mez_"
#encText = urllib.parse.quote("정신질환")

#quote = "정신질환"  #검색어 입력받기
#num = 1000  #최대 검색건수
 
encText = urllib.parse.quote("정신질환") # 검색단어 입력
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)