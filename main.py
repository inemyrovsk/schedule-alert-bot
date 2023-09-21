import os

import telebot

BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)


def start_bot():
    bot.infinity_polling()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    print("starting")
    start_bot()
