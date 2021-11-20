from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Eldor Jo\'raboyev', url='https://t.me/captainphotoshop')
    ],
                     [
        InlineKeyboardButton(text="Obunani tekshirish",callback_data="check_subs")
    ]]
)