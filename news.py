# 라이브러리 불러오기
from config import TELEGRAM_TOKEN, CHAT_ID
import requests
from bs4 import BeautifulSoup
import telegram
#from apscheduler.schedulers.blocking import BlockingScheduler

# 검색 키워드
search_word = '코로나'

# 텔레그램 봇 생성
token = 'TELEGRAM_TOKEN'
bot = telegram.Bot(token=token)
# 스케쥴러 생성
sched = BlockingScheduler()
# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 링크 추출 함수
def extract_links(old_links=[]):
    url = f'http://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}&nso=p%3Aall%2Cso%3Add'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)
    
    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)
    
    return new_links
    
# 텔레그램 메시지 전송 함수
def send_links():
    global old_links
    new_links = extract_links(old_links)
    if new_links:
        for link in new_links:
            bot.sendMessage(chat_id='TELEGRAM_TOKEN', text=link)
    else:
        bot.sendMessage(chat_id='TELEGRAM_TOKEN', text='아직 새로운 뉴스가 없습니다.')
    old_links += new_links.copy()
    old_links = list(set(old_links))

# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', hours=1)
sched.start()