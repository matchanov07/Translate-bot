import logging
from aiogram import Bot, Dispatcher, executor,types
from confing import TOKEN
from googletrans import Translator
from gtts import gTTS


logging.basicConfig(level=logging.INFO)

bot  = Bot(TOKEN)

db = Dispatcher(bot)

@db.message_handler(commands=['start','help'])
async def do_start(message: types.Message):
    frist_name = message.from_user.first_name
    # id_name = 
    await message.answer(f"Assalomu aleykum {frist_name}\nBotga xush kelibsiz🤗\nBu bot sizga rus tilidan ingiliz tiliga o'giradi yoki aksini qaytaradi🤝")
@db.message_handler(commands=['img'])
async def png(message:types.Message):
    await message.answer_photo(photo=open("photo/uD6M0s2F_male_-5_cartoon6.png", 'rb'))


@db.message_handler(commands=['hasan'])
async def xasan(message:types.Message):
    await message.answer_photo(photo=('C:/Users/TEMA/Pictures/Camera Roll/mirxasan.png'))

@db.message_handler()
async def trans(message: types.Message):
    msg = message.text
    tren = Translator()
    if msg.isascii():
        tarjima = tren.translate(msg, dest='ru') 
        tts  = gTTS(tarjima.text, lang='ru')
        tts.save('audio_ru.mp3')
        await message.answer(tarjima.text)
        await message.answer_audio(audio=open('audio_ru.mp3' , 'rb'))
    else:
        tarjima = tren.translate(msg, dest='en')
        tts  = gTTS(tarjima.text, lang='en')
        tts.save('audio_en.mp3')
        await message.answer(tarjima.text)
        await message.answer_audio(audio=open('audio_en.mp3' , 'rb'))


if __name__=='__main__':
    executor.start_polling(db,skip_updates=True)
    
    
    
    
    
    
    
    
    
    
    # tren = Translator()
    
    # if msg.isascii():
    #     tarjima = tren.translate(msg, dest="en")
    #     tts = gTTS(tarjima)


    #     await message.answer(tarjima.text)
    # else:
    #     tarjima = tren.translate(msg, dest='uz')

    #     await message.answer(tarjima.text)

    # if msg.isascii():
    #     tarjima = tren.translate(msg, dest="uz")


    #     await message.answer(tarjima.text)
    # else:
    #     tarjima = tren.translate(msg, dest='en')

    #     await message.answer(tarjima.text)    




