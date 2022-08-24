import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس حسام","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/46fa55b49b85c084159ce.png",
        caption=f"""[ٓ❍ | 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒔𝒔𝒂𝒎 .](https://t.me/SOU_LOFFY_RCE)\n\n[❍ | 𝒉𝒐𝒔𝒔𝒂𝒎 𝒕𝒉𝒆 𝒃𝒆𝒔𝒕 𝒔𝒐𝒖𝒓𝒄𝒆 𝒐𝒏 𝒕𝒆𝒍𝒆 .](https://t.me/XxvprxX)\n\n[❍ | 𝐅𝐨𝐥𝐥𝐨𝐰 𝐓𝐡𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 .](https://t.me/SOU_LOFFY_RCE)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ˹ حــــســــام الــــهــــولـــنــــدي ✶ ✶ 🇳🇱）⛧", url=f"https://t.me/H_OS_S_AM"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆«𝒉𝒐𝒔𝒔𝒂𝒎🖥", url=f"https://t.me/SOU_LOFFY_RCE"),
                ],[
                    InlineKeyboardButton(
                        "اضغط لاضافه البوت لمجموعتك✅.", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],

            ]

        ),

    )