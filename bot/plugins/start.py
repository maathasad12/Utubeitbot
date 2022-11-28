from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
                  [
                      InlineKeyboardButton("شلون تستخدمني ولا اصير حيوان", callback_data="/help")
                  ],
                  [
                      InlineKeyboardButton("قناة مالني اشتراك بيه لا ب44 على راسك!", url="https://t.me/Maathasad1999"),
                      InlineKeyboardButton("كروب الدعم", url="https://t.me/Maathali92")
                  ],
                  [  
                      InlineKeyboardButton("دعم نفسي", url="https://www.youtube.com/channel/UCp3AqHeAy-n4_utbsw15yhQ")
                  ]]
        ),
    )
