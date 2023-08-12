# importing
# import openai
import telebot
import re
# import bardapi
import os
import replicate

global TOKEN
TOKEN = '6591453315:AAFZ2nlZgRP9mcUPRES4OEzQyJzFsCa_NA0'
bot = telebot.TeleBot(TOKEN)


# set your __Secure-1PSID value to key
token_bard = 'Zwi46tbFnl9E1THSAXlx58kwzLbNyKtM1OHs6d7vXOxhhv735SVPj2fMCKz9cfXx_h8Fmg.'


@bot.message_handler(commands=['help'])
def greet(message): {
    bot.reply_to(message, "Hello! I'm your personal chatbot\nSend message in following way:\n.gen prompt => To generate prompt to image\n.ask prompt => To generate response based on prompt\n.vid prompt => To generate prompt to video\n.anim prompt => To generate prompt to animated\n.musi prompt => To generate prompt to music")
}


# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, 'On it. Please wait...')
#     # set your input text
#     input_text = message.text
#     print(input_text)

#     # Send an API request and get a response.
#     response = bardapi.core.Bard(token_bard).get_answer(input_text)['content']
#     print(response)
#     bot.reply_to(message, response)

# @bot.message_handler(func=lambda message: True)
# def getID(message):
#     # print(message.from_user.id)
#     bot.reply_to(message, "Hello {}".format(message.from_user.first_name))

@bot.message_handler(func=lambda message: True)
def getID(message):
    # print(message.from_user.id)
    bot.reply_to(message, 'On it. Please wait, {}...'.format(
        message.from_user.first_name))
    if ((message.text).startswith('.gen')):
        input = ((message.text).split('.gen '))[1]
        output = replicate.run(
            "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
            input={"prompt": input}
        )
        bot.send_photo(chat_id=message.chat.id, photo=output[0])
    elif ((message.text).startswith('.ask')):
        input = ((message.text).split('.ask '))[1]
        text = ''
        output = replicate.run(
            "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
            input={"prompt": input}
        )
        for item in output:
            text += item
            print(item)
        bot.reply_to(message, text)
    elif ((message.text).startswith('.vid')):
        input = ((message.text).split('.vid '))[1]
        output = replicate.run(
            "anotherjesse/zeroscope-v2-xl:9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351",
            input={"prompt": input}
        )
        print(output)
        bot.send_video(chat_id=message.chat.id, video=output[0])
    elif ((message.text).startswith('.anim')):
        inp = ((message.text).split('.anim '))[1]
        output = replicate.run(
            "lucataco/animate-diff:1531004ee4c98894ab11f8a4ce6206099e732c1da15121987a8eef54828f0663",
            input={
                "motion_module": "mm_sd_v14", 'prompt': inp},
        )
        print(output)
        bot.send_video(chat_id=message.chat.id, video=output)
    elif ((message.text).startswith('.musi')):
        inp = ((message.text).split('.musi'))[1]
        output = replicate.run(
            "facebookresearch/musicgen:7a76a8258b23fae65c5a22debb8841d1d7e816b75c2f24218cd2bd8573787906",
            input={
                "model_version": "melody", 'prompt': inp,
                "output_format": 'mp3',
                'duration': 15},
        )
        print(output)
        bot.send_audio(chat_id=message.chat.id, audio=output)


bot.polling()
