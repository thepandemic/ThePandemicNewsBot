from config import TELEGRAM_TOKEN, CHAT_ID
import os

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception('TELEGRAM_TOKEN, CHAT_ID 확인필요')