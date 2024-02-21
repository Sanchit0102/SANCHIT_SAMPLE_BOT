#(©) 𝚂𝙰𝙽𝙲𝙷𝙸𝚃 ♛⛧
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton 


API_ID = "25833520"
API_HASH = "7d012a6cbfabc2d0436d7a09d8362af7"
BOT_TOKEN = "6362281925:AAGSTs25eytppfuN-AF-IMKCtxrvtxhXWJ8"

Sanchit = Client(
    name="Samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@Sanchit.on_message(filters.command("start"))
async def start_cmd(cleint,message):
    await message.reply_photo(
        photo="https://telegra.ph/file/2ab88e1d0a62e75e4b2ff.jpg",
        caption="This Is A Advanced Bot") 

@Sanchit.on_message(filters.command("help"))
async def help_cmd(cleint, message):
    await message.reply_text("hi contact my father DaEmoN")

@Sanchit.on_message(filters.command("about"))
async def about_cmd(cleint, message):
    await message.reply_text('''</a>ᴍʏ ɴᴀᴍᴇ : Cinema Explorer Bot

 ‣ ᴍʏ ʙᴇꜱᴛ ꜰʀɪᴇɴᴅ: <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 

 ‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='http://t.me/THE_DS_OFFICIAL'>🤧</a>''')


@Sanchit.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    [[
    InlineKeyboardButton("JOIN MY UPDATES CHANNEL", url="https://t.me/THE_SILENT_TEAMS")
]]
    

print("Bot was Started")

Sanchit.run()
  
