# Copyright (©️) @Mariamusic_OFFICIAL
# By : Pavan Magar

from pyrogram import Client
from Mariamusic.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from Mariamusic.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"എടാ പൊട്ടാ ഞാൻ ഒരു music  ബോട്ട് ആണ് . സംശയം ഉണ്ടെങ്കിൽ @kk_kovilakam ത്തോട്ട് കയറി vc open ചെയ്തിട്ട് ഒന്ന് '/play' അടിച്ചു അതിന്റെ കൂടെ പാട്ടിന്റെ പേരും കൂടെ കൊടുക്ക്")
  return
