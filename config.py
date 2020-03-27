import os

TELEGRAM_TOKEN = os.environ.get('1014840884:AAHRl3QtKjOjTAz9BIgPV-4XWXA95Y5s3bE', '')
CHAT_ID = os.environ.get('CHAT_ID', '')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception('1014840884:AAHRl3QtKjOjTAz9BIgPV-4XWXA95Y5s3bE, CHAT_ID 확인필요')