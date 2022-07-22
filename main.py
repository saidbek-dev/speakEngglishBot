import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordLookup import getDefinitions
from googletrans import Translator

translator = Translator()

API_TOKEN = '5330111166:AAF3J0F14hFnEkKtNn_P9jBzF8MsySkq8u4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nMen \"Speak English Bot\" man.\nMenga so'z yuboring.")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Ikkitadan ko'p so'zni tarjimasini, aks holda, ma'nosi va aytilishini qaytaraman.")

@dp.message_handler()
async def tarjimon(message: types.Message):
    try:
        lang = translator.detect(message.text).lang
        if len(message.text.split()) > 2:
            if lang=='en':
                await message.reply(translator.translate(message.text, dest='uz').text)
            else:
                await message.reply(translator.translate(message.text, dest='en').text)
        else:
            if lang=='en':
                word_id = message.text
            else:
                word_id = translator.translate(message.text, src='uz', dest='en').text
            lookup = getDefinitions(word_id)
            if lookup:
                await message.reply(f"Word: {word_id}\nDefinitions:\n{lookup['definitions']}")
                if lookup.get('audio'):
                    await message.reply_voice(lookup['audio'])
            else:
                await message.reply("Bunday so'z topilmadi!")
    except:
        await message.reply("So'zni noto'g'ri kiritdingiz!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)