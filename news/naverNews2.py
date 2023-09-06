from bs4 import BeautifulSoup
import requests
import re
import time
import os
import sys
import urllib.request
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# WebDriver Setting
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)


# selenium으로 검색 페이지 불러오기 #
naver_urls = []
pub_dates = []

# Naver API key 입력
client_id = '2jnsvCU4ILz1d9iopeAc' 
client_secret = 'NlP_x5Mez_'

# 검색어 입력
keword = input("검색할 키워드를 입력해주세요:")
encText = urllib.parse.quote(keword)

# 검색을 끝낼 페이지 입력
end = input("\n크롤링을 끝낼 페이지 위치를 입력해주세요. (기본값:1, 최대값:100):")  
if end == "":
    end = 1
else:
    end = int(end)

print("\n 1 ~ ", end, "페이지 까지 크롤링을 진행 합니다")

# 한번에 가져올 페이지 입력
display = input("\n한번에 가져올 페이지 개수를 입력해주세요.(기본값:10, 최대값: 100):")
if display == "":
    display = 10
else:
    display = int(display)
print("\n한번에 가져올 페이지 : ", display, "페이지")


for start in range(end):
    url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&start=" + str(start+1) + "&display=" + str(display+1) # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body.decode('utf-8'))['items']
        for row in data:
            if('news.naver' in row['link']):
                naver_urls.append(row['link'])
                pub_dates.append(row['pubDate'])
        time.sleep(3)
    else:
        print("Error Code:" + rescode)


###naver 기사 본문 및 제목 가져오기###

# ConnectionError방지
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

titles = []
contents = []
comments_texts = []
for i in naver_urls:
    original_html = requests.get(i, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")
    # 뉴스 제목 가져오기
    title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
    # list합치기
    title = ''.join(str(title))
    # html태그제거
    pattern1 = '<[^>]*>'
    title = re.sub(pattern=pattern1, repl='', string=title)
    titles.append(title)

    # 뉴스 본문 가져오기

    content = html.select("div#dic_area")

    # 기사 텍스트만 가져오기
    # list합치기
    content = ''.join(str(content))

    # html태그제거 및 텍스트 다듬기
    content = re.sub(pattern=pattern1, repl='', string=content)
    pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
    content = content.replace(pattern2, '')
    contents.append(content)

    # 댓글 가져오기
    driver.get(i)
    time.sleep(1)  # 대기시간 변경 가능
    # 네이버 댓글 눌러서 댓글 가져오기#
    a = driver.find_element(By.CSS_SELECTOR, 'a._COMMENT_COUNT_VIEW')
    
    # 댓글 더보기 클릭
    a.click()

    # 대기시간 변경 가능
    time.sleep(3)  

    # 네이버 뉴스 댓글 가져오기
    html = driver.page_source
    c_soup = BeautifulSoup(html)

    comments = c_soup.select('span.u_cbox_contents')
    comments_text = ', '.join([comment.text.strip() for comment in comments])
    comments_texts.append(comments_text)


# 데이터프레임으로 정리
import pandas as pd

news_df = pd.DataFrame({'title': titles, 'link': naver_urls, 'content': contents, 'comments': comments_texts,'date': pub_dates})

news_df.to_csv('news.csv', index=False, encoding='utf-8-sig')