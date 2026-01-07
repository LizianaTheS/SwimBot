import os
from dotenv import load_dotenv
import telebot
load_dotenv()


token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(token)

def run_bot(_bot:telebot.TeleBot):
    _bot.infinity_polling()

