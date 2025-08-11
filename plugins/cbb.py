#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_media(
            media=InputMediaPhoto(
                media="https://envs.sh/h7m.jpg",  # Replace with your photo URL or local file path
                caption=f"""<blockquote expandable> <b>
🤖 ᴍʏ ɴᴀᴍᴇ: PLAY BOT
╭───────────⍟
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : </b> <a href='tg://user?id={}'>ᴜɴᴋɴᴏᴡɴ</a>",
├➽ Lɪʙʀᴀʀy : </b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a>",
├➽ Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ 3
├➽ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : ꜱᴏʟᴏ ᴄᴏᴅᴇ
├➽ ᴏᴡɴᴇʀ : </b> <a href='tg://user?id={1718481517}'>Bʟᴀᴄᴋ Wᴀʟᴋᴇʀ 🜲</a>",
╰───────────────⍟
</b></blockquote>"""
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
