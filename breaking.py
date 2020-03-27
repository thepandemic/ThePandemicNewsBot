from config import TELEGRAM_TOKEN, CHAT_ID
import requests
import bs4
import BeautifulSoup
import time
import telegram

bot = telegram.Bot(token=TELEGRAM_TOKEN)

daum_breaking_news_amount = 10
daum_news_amount = 10

naver_breaking_news_amount = 10
naver_news_amount = 10

lists = []
old_links = []
keyword = ["코로나", "코비드", "봉쇄", "확진", "감염", "속보"]

#max_length 최대길이 제한
def returns(url):
    req = requests.get(url)
    bs = bs4.BeautifulSoup(req.content, "html.parser")
    return bs

def daum_breaking_return_list(max_length):

    x = len(keyword)

    for j in range(x):
        bs = returns("https://news.daum.net/")
        td = bs.find("div", {"id":"kakaoContent"})
        strong = td.findAll("strong")
        length = 0

        for i in strong:
            try:
                i.find("strong", {"class":"tit_thumb"}).decompose()
            except AttributeError:
                pass

            base = i.find("a")
            link = base['href']

            try:
                title = base.text
            except AttributeError:
                img = base.find("img", {"class":"link_thumb"}).decompose()
                title = img.text

            if(link not in old_links):
                if("코로나" in title or "코비드" in title or "봉쇄" in title or "확진" in title or "감염" in title or "속보" in title):
                    if(length == max_length):
                        return lists
                    else:
                        lists.append([title, link])
                        old_links.append(link)
                        length+=1
                        #print(length)

        if(len(lists) != 0):
            return lists
        else:
            raise TypeError

def daum_return_list(max_length):

    x = len(keyword)

    for j in range(x):
        bs = returns("https://search.daum.net/search?w=news&sort=recency&q={keyword[j]}&cluster=n&DA=STC&dc=STC&pg=1&r=1&p=1&rc=1&at=more&sd=&ed=&period=")
        ul = bs.find("ul", {"id":"newsResultUL"})
        li = ul.findAll("li")
        div = li.findAll("div", {"class":"wrap_cont"})
        div2 = div.findAll("div", {"class":"cont_inner"})
        p = div2.findAll("p", {"class":"desc"})
        length = 0

        for i in li:
            try:
                i.find("div", {"class":"wrap_thumb"}).decompose()
            except AttributeError:
                pass

            base = i.find("a")
            title = base.text
            desc = p.text
            link = base['href']

            if(link not in old_links):
                if("코로나" in title or "코비드" in title or "봉쇄" in title or "확진" in title or "감염" in title or "속보" in title or "코로나" in desc or "코비드" in desc or "봉쇄" in desc or "확진" in desc or "감염" in desc or "속보" in desc):
                    if(length == max_length):
                        return lists
                    else:
                        lists.append([title, link])
                        old_links.append(link)
                        length+=1
                        #print(length)

        if(len(lists) != 0):
            return lists
        else:
            raise TypeError

def naver_breaking_return_list(max_length):

    bs = returns("https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001")
    td = bs.find("td", {"class":"content"})

    li = td.findAll("li")
    length = 0
    for i in li:
        try:
            i.find("dt", {"class":"photo"}).decompose()
        except AttributeError:
            pass

        base = i.find("a")

        title = base.text
        link = base['href']
        if(link not in old_links):
            if("코로나" in title or "봉쇄" in title or "확진" in title or "감염" in title):
                if(length == max_length):
                    return lists
                else:
                    lists.append([title, link])
                    old_links.append(link)
                    length+=1

    if(len(lists) != 0):
        return lists
    else:
        raise TypeError

def naver_return_list(max_length):

    bs = returns("https://news.naver.com/main/home.nhn")
    td = bs.find("id", {"class":"container"})

    li = td.findAll("li")
    length = 0
    for i in li:
        
        base = i.find("a")

        title = base.text
        link = base['href']
        if(link not in old_links):
            if("코로나" in title or "봉쇄" in title or "확진" in title or "감염" in title):
                if(length == max_length):
                    return lists
                else:
                    lists.append([title, link])
                    old_links.append(link)
                    length+=1

    if(len(lists) != 0):
        return lists
    else:
        raise TypeError


def sendBots():
    try:
        lists = daum_breaking_return_list(daum_breaking_news_amount)
        print(lists)
        for i in lists:
            #bot.sendMessage로 대체
            bot.sendMessage(CHAT_ID, "{}\n{}".format(i[0], i[1]))
            print("{}\n{}".format(i[0], i[1]))
            time.sleep(1)

    except TypeError:
        print("Error")

    try:
        lists = daum_return_list(daum_news_amount)
        print(lists)
        for i in lists:
            #bot.sendMessage로 대체
            bot.sendMessage(CHAT_ID, "{}\n{}".format(i[0], i[1]))
            print("{}\n{}".format(i[0], i[1]))
            time.sleep(1)

    except TypeError:
        print("Error")

    try:
        lists = naver_breaking_return_list(naver_breaking_news_amount)
        for i in lists:
            #bot.sendMessage로 대체
            bot.sendMessage(CHAT_ID, "{}\n\n{}".format(i[0], i[1]))
            print("{}\n{}".format(i[0], i[1]))
            time.sleep(1)

    except TypeError:
        print("Error")

    try:
        lists = naver_return_list(naver_news_amount)
        for i in lists:
            #bot.sendMessage로 대체
            bot.sendMessage(CHAT_ID, "{}\n\n{}".format(i[0], i[1]))
            print("{}\n{}".format(i[0], i[1]))
            time.sleep(1)

    except TypeError:
        print("Error")

sendBots()