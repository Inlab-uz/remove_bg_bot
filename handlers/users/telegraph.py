import logging
import time
import os
from pathlib import Path

from aiogram import types
from aiogram.types import InputFile

from loader import dp
from utils import photo_link
from utils import remove_background

download_path = Path().joinpath("downloads")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    name_photo = f'{msg.from_user.id}.jpg'
    await msg.photo[-1].download(name_photo)
    answer = await msg.answer("Iltimos biroz kuting ...")


    # photo = msg.photo[-1]
    # link = await photo_link(photo)
    # await msg.answer(link)
    try:
        await remove_background(name_photo)
        photo_file = InputFile(path_or_bytesio=name_photo)
        await msg.reply_document(photo_file)
        # await msg.reply_photo(new_photo, caption="Bu rasm")

    except:
        await msg.answer("Botda xatolik yuz berdi iltimos qaytadan harakat qilib koring")
    await answer.delete()
    os.remove(name_photo)