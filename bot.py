import config
import telebot
#from telebot import apihelper
import time


bot = telebot.TeleBot(config.token)
#apihelper.proxy = {'https':'socks5://69.163.160.115:12803'}


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


while True:
	try:
		bot.infinity_polling()
	except:
		time.sleep(2)
