import telebot
import re
import os
from downloader import *
from convert import *

global TOKEN
TOKEN = '6591453315:AAFZ2nlZgRP9mcUPRES4OEzQyJzFsCa_NA0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def greet(message): {
    bot.reply_to(message, "Hello! I'm your personal chatbot\nSend message in following way:\n.gen prompt => To generate prompt to image\n.ask prompt => To generate response based on prompt\n.vid prompt => To generate prompt to video\n.anim prompt => To generate prompt to animated\n.musi prompt => To generate prompt to music")
}
@bot.message_handler(func=lambda message: True)
def getID(message):
    # print(message.from_user.id)
    bot.reply_to(message, 'On it. Please wait, {}...'.format(
        message.from_user.first_name))
    if ((message.text).startswith('.musi')):
        link = (message.text.split('.musi '))[1]
        bot.reply_to(message, 'Downloading Required Files')
        download_yt(link)
        fileName = ''
        for file in os.listdir('./'):
            if file.endswith('.webm'):    fileName = file
        audioFileName = fileName.split('.webm')[0] + '.mp3'
        # print(fileName, audioFileName)
        
        bot.reply_to(message, 'Downloaded Required Files for {}. Converting to MP3...'.format((fileName.split('.webm')[0])))
        convert_webm_to_mp3(fileName, audioFileName)
        bot.reply_to(message, 'Conversion Done. Sending...')
        bot.send_audio(chat_id=message.chat.id, audio=open(audioFileName,'rb'))
        os.remove(audioFileName)
        os.remove(fileName)
    elif ((message.text).startswith('.vid')):
        link = (message.text.split('.vid '))[1]
        bot.reply_to(message, 'Downloading Required Files')
        download_yt(link)
        fileName = ''
        for file in os.listdir('./'):
            if file.endswith('.webm'):    fileName = file
        # audioFileName = fileName.split('.webm')[0] + '.mp3'
        # print(fileName, audioFileName)
        
        # bot.reply_to(message, 'Downloaded Required Files for {}. Converting to MP3...'.format((fileName.split('.webm')[0])))
        # convert_webm_to_mp3(fileName, audioFileName)
        # bot.reply_to(message, 'Conversion Done. Sending...')
        # bot.send_audio(chat_id=message.chat.id, audio=open(audioFileName,'rb'))
        # os.remove(audioFileName)
        # os.remove(fileName)
        bot.send_document(chat_id=message.chat.id, document=open(fileName, 'rb'))
        


bot.polling()
