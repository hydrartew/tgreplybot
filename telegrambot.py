import telebot

token = ''

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def ReplyMessage(message):
    if message.chat.type == 'private':
        bot.send_message(chat_id=message.chat.id, text=message.text)

# RUN
bot.polling(none_stop=True)
