#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27438051"))
API_HASH = environ.get("API_HASH", "7770205091")
BOT_TOKEN = environ.get("BOT_TOKEN", "7584045215:AAEFr_D9Z2yOsMaP7ykPHHT6r7XvQ7BDVJw")
OWNER = int(environ.get("OWNER", "762718870"))
CREDIT = "♥M♥A♥H♥A♥D♥E♥V♥"
AUTH_USER = os.environ.get('AUTH_USERS', '762718870').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
