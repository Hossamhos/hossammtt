import asyncio
from YukkiMusic import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["ايدي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text(       f"""◂ اسمك ↫ {message.from_user.mention}\n\n◂ معرفك ↫ @{message.from_user.username}\n\n◂ ايديك ↫ `{message.from_user.id}`\n\n◂ ايدي الجروب ↫ `{message.chat.id}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "『 𝗦𝗢𝗨𝗥𝗖𝗘 𝗞𝗔𝗥𝗠𝗔𝗡 』", url=f"https://t.me/YDDCJ"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
