from settings import *

import telebot
from telebot.types import Message

import random


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['group_order'])
def handle_group_order(message: Message):
    chat_id = message.chat.id
    user_nickname = message.from_user.username

    if user_nickname and user_nickname in ADMINS:
        message_text = "Вот случайно сгенерированный список группы:\n"

        group_list = GROUP.copy()
        random.shuffle(group_list)

        message_text += "\n".join([str(i + 1) + '. ' + group_list[i] for i in range(len(group_list))])

        bot.send_message(chat_id, message_text)
    else:
        bot.send_message(chat_id, f"Только админы: {', '.join(['@' + nickname for nickname in ADMINS])} – могут составлять порядок группы")


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Напишите /group_order, чтобы получить случайно сгенерированный список группы")


bot.infinity_polling(non_stop=True, skip_pending=True)
