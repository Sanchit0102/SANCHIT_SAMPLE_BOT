from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton 


API_ID = "24830912"
API_HASH = "a1a1775593531b90850b8b82e3b14940"
BOT_TOKEN = "6433293774:AAGRhgl7a9Oi9XhbZnKE_yzTqc8n1KsymZY"

TeluguZone = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@TeluguZone.on_message(filters.command("start"))
async def start_cmd(cleint,message):
    await message.reply_photo(
        photo="https://graph.org/file/3dc0d36c2bab91936a26b.jpg",
        caption="This Is A Advanced @Daemon990 Bot") 

@TeluguZone.on_message(filters.command("help"))
async def help_cmd(cleint, message):
    await message.reply_text("hi contact my father DaEmoN")

@TeluguZone.on_message(filters.command("about"))
async def about_cmd(cleint, message):
    await message.reply_text("</a>ᴍʏ ɴᴀᴍᴇ : Cinema Explorer Bot

 ‣ ᴍʏ ʙᴇꜱᴛ ꜰʀɪᴇɴᴅ: <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 

 ‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='http://t.me/Daemon990'>DAEMON</a>")


@TeluguZone.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    [[
    InlineKeyboardButton("JOIN MY UPDATES CHANNEL", url="https://t.me/TeluguZone0")
]]
    

print("Bot was Started")

TeluguZone.run()
  
