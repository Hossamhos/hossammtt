import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","حسام","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5db1e9940a55de6c46625.jpg",
        caption=f"""◍ الزرار الاول: قناه السورس \n◍ الزرار الثاني: هو مبرمج السورس\n√""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒔𝒔𝒂𝒎", url=f"https://t.me/SOU_LOFFY_RCE"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "ᯓ˹ حــــســــام الــــهــــولـــنــــدي）", url=f"https://t.me/H_OS_S_AM"),
                ],
            ]
        ),
    )