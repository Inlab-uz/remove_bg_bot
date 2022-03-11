import logging
import sqlite3
from aiogram import types
from data.config import CHANNELS, ADMINS
from keyboards.inline.subscribtion import check_button
from loader import bot, dp, db
from utils.misc import subscription


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    # Foydalanuvchini bazaga qoshamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        msg = f'<a href="tg://user?id={user_id}">{name}</a> bazaga qoshildi. \nBazada {count} ta foydalanuvchi bor.' \
              f'\nID {user_id}.'
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        # await bot.send_message(chat_id=ADMINS[0], text=err)
        pass
    await message.answer(f"Assalomu aleykum <b>{message.from_user.full_name}</b>\n"
                         f"Remove background botiga xush kelibsiz!")
    # channels_format = str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     invite_link = await chat.export_invite_link()
    #     # logging.info(invite_link)
    #     channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    #
    # await message.answer(f"Foydalanish uchun quyidagi kanalga obuna bo'ling: \n"
    #                      f"{channels_format}",
    #                      reply_markup=check_button,
    #                      disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz ✅\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz ❌ \n"
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
