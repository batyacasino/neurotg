import config
import telebot
from telebot import apihelper
import time


bot = telebot.TeleBot(config.token)
apihelper.proxy = {'https':'socks5://69.163.160.115:12803'}


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


while True:
	try:
		bot.infinity_polling()
	except:
		time.sleep(2)


'''
	


5m 58s ago		United States		SOCK4/5	555ms
6m 3s ago		United States		SOCK4	500ms
6m 10s ago		United States		SOCK4/5	489ms
6m 21s ago	66.110.216.105:39431	United States		SOCK4/5	120ms
6m 27s ago	174.76.48.246:4145	United States		SOCK4/5	380ms
6m 30s ago	192.169.139.161	8975	United States		SOCK4/5	196ms
6m 35s ago	104.238.111.150	27427	United States		SOCK4/5	834ms
6m 40s ago	174.76.35.15	36163	United States		SOCK5	348ms
6m 40s ago	173.245.239.223	16938	United States		SOCK4/5	445ms
6m 50s ago	69.163.165.232	49264	United States		SOCK4/5	582ms
6m 59s ago		United States		SOCK5	92ms
11m 4s ago	43.224.8.121	6667	India		SOCK4	616ms
13m 5s ago	109.74.144.130	1080	Slovak Republic		SOCK5	514ms
13m 25s ago	108.61.250.229	40003	Japan		SOCK5	46ms
13m 59s ago	134.209.100.103	49616	United States		SOCK4	1000ms
14m 10s ago	174.76.48.230	4145	United States		SOCK4/5	688ms
14m 16s ago	174.76.48.228	4145	United States		SOCK4/5	433ms
14m 25s ago	185.174.102.193	52149	United States		SOCK5	117ms
14m 29s ago	174.70.241.7	24385	United States		SOCK4/5	301ms
14m 33s ago	174.76.35.7	36171	United States		SOCK4/5	178ms
15m 29s ago	64.90.49.252	3875	United States		SOCK4	843ms
17m 13s ago	69.163.164.14	16431	United States		SOCK4	92ms
17m 20s ago	72.210.252.143	46173	United States		SOCK4/5	247ms
17m 26s ago	70.166.38.71	24801	United States		SOCK4/5	103ms
17m 32s ago	64.90.52.221	62919	United States		SOCK4	372ms
'''