# importing
import openai
import telebot
import re
import bardapi
import os

global TOKEN
TOKEN = '6591453315:AAFZ2nlZgRP9mcUPRES4OEzQyJzFsCa_NA0'
bot = telebot.TeleBot(TOKEN)


# set your __Secure-1PSID value to key
token_bard = 'Zwi46l42B9zXFKWqQnCK194pBgfZLWXiqS8QyVsdinNGZC68nTxLE9lYCQ23u6eo7MN56Q.'


@bot.message_handler(commands=['Greet'])
def greet(message): {
    bot.reply_to(message, "Hello! I'm your way to Bard")
}


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'On it. Please wait...')
    # set your input text
    input_text = message.text
    print(input_text)

    # Send an API request and get a response.
    response = bardapi.core.Bard(token_bard).get_answer(input_text)['content']
    print(response)
    bot.reply_to(message, response)


bot.polling()
