from config
import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import telegram 

bot = telegram.Bot(token=1014840884:AAHRl3QtKjOjTAz9BIgPV-4XWXA95Y5s3bE)

def send(t):
  bot.sendMessage(1146016071, t, parse_mode=telegram.ParseMode.HTML)