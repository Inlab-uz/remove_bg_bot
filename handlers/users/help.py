from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Botimizdan foydalanish shartlari oddiy:\n"
            "1️⃣ Istagan rasmingizni tanlaysiz\n"
            "2️⃣ Uni bizga yuborasiz\n"
            "3️⃣ 2 yoki 3 soniya kutasiz\n"
            "4️⃣ Va biz uni orqa fonsiz holda sizga jo'natamiz")
    
    await message.answer(text)