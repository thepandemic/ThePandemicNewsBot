# 라이브러리 불러오기
from config import TELEGRAM_TOKEN, CHAT_ID
import requests
from bs4 import BeautifulSoup
import telegram

# 서치 키워드
search_word = '코로나'
# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 스크래핑 함수 
def extract_links(old_links=[]):
    url = f'http://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}&nso=p%3Aall%2Cso%3Add'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('.type01')
    news_list = search_result.select('li a')

    links = []
    for news in news_list[:10]:
        link = news['href']
        links.append(link)
    
    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)
    
    return new_links

# 이전 링크를 매개변수로 받아서, 비교 후 새로운 링크만 출력
# 차후 이 부분을 메시지 전송 코드로 변경하고 매시간 동작하도록 설정
# 새로운 링크가 없다면 빈 리스트 반환
for i in range(3):
    new_links = extract_links(old_links)
    send(new_links)
    old_links += new_links.copy()
    old_links = list(set(old_links))
    
"""
===보낼 링크===
 ['https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=101&oid=008&aid=0004349743', 'http://it.chosun.com/site/data/html_dir/2020/01/31/2020013103216.html', 'https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=101&oid=031&aid=0000523810', 'https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=102&oid=001&aid=0011371561', 'http://www.fintechpost.co.kr/news/articleView.html?idxno=100097'] 

===보낼 링크===
 [] 

===보낼 링크===
 [] 
"""

