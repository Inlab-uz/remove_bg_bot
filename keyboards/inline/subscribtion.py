from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Remove background', url='https://t.me/removebgtest')
    ],
                     [
        InlineKeyboardButton(text="Obunani tekshirish",callback_data="check_subs")
    ]]
)