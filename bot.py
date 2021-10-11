import os
import logging
from bs4 import BeautifulSoup
import requests
from pyrogram import Client, filters, idle
from vars import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "moviebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.command("movies"))
async def score(_, message):
    m = await message.reply_text("`Gathering Movies...`")
    try:       
        url = "https://slmovieshd2020.blogspot.com/search/label/Dubbed"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        movie_image = soup.select("entry-image")
        movie_title = soup.select("entry-title")
        status = soup.select("entry-excerpt excerpt")
        text = ""
        text = text + "**🔴 𝐋𝐈𝐕𝐄 𝐈𝐏𝐋 𝐒𝐂𝐎𝐑𝐄 🏏**\n\n" + f"**{movie_image[0].text}**" + "\n\n" + f"**⦿ {movie_title[0].text}**" + "\n\n" + f"**{status[0].text}**" + "\n\n" + "**Bot by -** <a href='https://t.me/dihanrandila'>**Dihan Randila**</a>\n**Developer -** <a href='https://github.com/dihanofficial'>**Dihan**</a>"
        text = text.replace("Check ", "")
        text = text.replace("(", " (")
        text = text.replace(")", ") ")
        await m.edit(text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(
                                     "View Now 🔁", url="https://slmovieshd2020.blogspot.com")]]))
        return
    except Exception as e:
        print(str(e))
        return await m.edit("`No any movie`")


bot.start()
idle()



