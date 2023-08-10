# importing
import openai
import telebot
import re

global TOKEN
TOKEN = '6591453315:AAFZ2nlZgRP9mcUPRES4OEzQyJzFsCa_NA0'
bot = telebot.TeleBot(TOKEN)

openai.api_key = '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'

messages = [{'role': 'system', 'content': 'You are a kind helpful assistant.'}]

# @bot.message_handler(commands=['Greet'])
# def greet(message): {
#     bot.reply_to(message, "Hello! I'm your way to ChatGPT")
# }


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# bot.polling()
