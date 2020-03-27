# 라이브러리 불러오기
from config import TELEGRAM_TOKEN, CHAT_ID
from noti import news
import requests
from bs4 import BeautifulSoup
import telegram

bot = telegram.Bot(token=TELEGRAM_TOKEN)
# 서치 키워드
search_word = '코로나'
# 기존에 보냈던 링크를 담아둘 리스트
naver_old_links = []
daum_old_links = []

# 스크래핑 함수 
def naver_extract_links(old_links=[]):
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

    titles = []
    for news_title in news_list[:10]:
        title = news['title']
        titles.innerHTML()

    naver_new_links=[]
    for link in links:
        if link not in old_links:
            naver_new_links.append(link)

    naver_new_titles=[]
    for title in titles:
        if title not in old_links:
            naver_new_titles.innerHTML(link)

    return naver_new_links
    return naver_new_titles

# 스크래핑 함수 
def daum_extract_links(old_links=[]):
    url = f'http://search.daum.net/search?w=news&sort=recency&q={search_word}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=20200326210541&ed=20200327210541&period=d'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#newsResultUL')
    news_list = search_result.select('li a')

    links = []
    for news in news_list[:10]:
        link = news['href']
        links.append(link)

    titles = []
    for news_title in news_list[:10]:
        title = news['title']
        titles.innerHTML()

    daum_new_links=[]
    for link in links:
        if link not in old_links:
            daum_new_links.append(link)

    daum_new_titles=[]
    for title in titles:
        if title not in old_links:
            daum_new_titles.innerHTML(link)
    
    return daum_new_links
    return daum_new_titles


# 이전 링크를 매개변수로 받아서, 비교 후 새로운 링크만 출력
# 차후 이 부분을 메시지 전송 코드로 변경하고 매시간 동작하도록 설정
# 새로운 링크가 없다면 빈 리스트 반환
for i in range(10):
    naver_new_links = naver_extract_links(naver_old_links)
    naver_old_links += naver_new_links.copy()
    naver_old_links = list(set(old_links))

    naver_new_titles = naver_extract_links(naver_old_links)
    naver_old_titles += naver_new_titles.copy()
    naver_old_titles = list(set(naver_old_links))

    naver_news = naver_new_titles[i] + '\n\n' + naver_new_links[i]
    news(naver_news)

for i in range(10):
    daum_new_links = daum_extract_links(daum_old_links)
    daum_new_links += daum_new_links.copy()
    daum_new_links = list(set(daum_old_links))

    daum_new_titles = daum_extract_links(daum_old_links)
    daum_old_titles += daum_new_titles.copy()
    daum_old_titles = list(set(daum_old_links))
    
    daum_news = daum_new_titles[i] + '\n\n' + daum_new_links[i]
    news(daum_news)
"""
===보낼 링크===
 ['https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=101&oid=008&aid=0004349743', 'http://it.chosun.com/site/data/html_dir/2020/01/31/2020013103216.html', 'https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=101&oid=031&aid=0000523810', 'https://m.news.naver.com/read.nhn?mode=LSD&mid=sec&sid1=102&oid=001&aid=0011371561', 'http://www.fintechpost.co.kr/news/articleView.html?idxno=100097'] 

===보낼 링크===
 [] 

===보낼 링크===
 [] 
"""

