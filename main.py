import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Institutimizning rasmiy botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Kerakli bo'limni tanlang:")

if __name__ == '__main__':
    print("Bot ishga tushdi...")
    bot.infinity_polling()

