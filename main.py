from aiogram import Bot , Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
import asyncio ,sys , logging
from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, WebAppInfo
import os


keyboard = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="Demo Web Apps")
]],resize_keyboard=True)

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(text="Wedo - Ecommerce",web_app=WebAppInfo(url="https://wedo.dexignzone.com/welcome.html"))
],
    [
    InlineKeyboardButton(text="Adopet - Pet Adoption",web_app=WebAppInfo(url="https://askbootstrap.com/preview/adopet/index.html"))
],
    [
    InlineKeyboardButton(text="Suha - PWA Ecommerce",web_app=WebAppInfo(url="https://suha-nextjs.vercel.app/"))
],
    [
    InlineKeyboardButton(text="Coffee Time",web_app=WebAppInfo(url="https://themesflat.co/html/coffeetime/coffee/index.html"))
]
                                                        ])

#BotFather tomonidan botga ulash uchun berilgan TOKEN
API_TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=API_TOKEN)  # TOKEN o'rniga o'zingizning botingizning tokenini yozing
dp = Dispatcher()


@dp.message(CommandStart())
#Start komandasi bosilganda quyidagi funksya ishlaydi
async def send_hi(message:types.Message):
    #botga start komandasi berilganda foydalanuvchiga salom berish
    await message.answer(f'Salom , {message.from_user.full_name} ', reply_markup=keyboard) 
   

@dp.message(F.text=="Demo Web Apps")
async def echo(message: types.Message):
    await message.answer(text="Ushbu template'lardan birini\ntanlashingiz va ko'rishingiz mumkin!\nUshbu template <a href='https://st40.uz'><b>st40.uz</b></a> tomonidan \ntaqdim etilmoqda",parse_mode="HTML",
                         reply_markup=inline_keyboard)
    

async def main() -> None:
    # Bot obyektini yaratamiz va API_TOKEN orqali boshlaymiz
    bot = Bot(API_TOKEN)  
    # Bot ishga tushgani haqida adminga xabar beramiz!
    # await bot.send_message(chat_id='443434437',text='Bot ishga tushdi ✅')
    # Botni ishga tushiramiz va voqealarni boshlaymiz
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    # Logging sozlamalarni qo'shamiz
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Asosiy funksiyani chaqirish
    asyncio.run(main())