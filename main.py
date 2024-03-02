import telebot

bot = telebot.TeleBot("5400907139:AAEhRjzwYcmZz4NgOC7v18M09CpF8vXopko")

@bot.message_handler(["start"])
def start(message):
	bot.send_message(message.chat.id,"This Bot Working With Free Vps")
bot.infinity_polling()
