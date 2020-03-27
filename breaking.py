from config import TELEGRAM_TOKEN, CHAT_ID
import requests
import bs4
import time
import telepot

bot = telegram.Bot(token=TELEGRAM_TOKEN)
lists = []
old_links = []

def returns(url):
    req = requests.get(url)
    bs = bs4.BeautifulSoup(req.content, "html.parser")
    return bs

def return_list():
    bs = returns("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001")
    td = bs.find("td", {"class":"content"})

    li = td.findAll("li")
    for i in li:
        try:
            i.find("dt", {"class":"photo"}).decompose()
        except AttributeError:
            pass

        base = i.find("a")

        title = base.text
        link = base['href']
        if(link not in old_links):
            if("코로나" in title or "봉쇄" in title or "확진" in title or "감염" in title or "속보" in title):
                print(title, link)
                lists.append([title, link])
                old_links.append(link)

    if(len(lists) != 0):
        return lists
    else:
        raise TypeError

def sendBots():
    try:
        lists = return_list()
        for i in lists:
            bot.sendMessage(CHAT_ID, "new ! \n{}\n\n{}".format(i[0], i[1]))
            print("new ! \n{}\n\n{}".format(i[0], i[1]))
            time.sleep(1.5)
    except TypeError:
        print("Error")

sendBots()