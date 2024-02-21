from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@TeluguZone.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
  [[
    InlineKeyboardButton("JOIN MY UPDATES CHANNEL", url="https://t.me/TeluguZone0")
]]
