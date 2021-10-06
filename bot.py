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

@bot.on_message(filters.private & filters.command("dubbedmovies"))
async def score(_, message):
    m = await message.reply_text("`Gathering Movies..`")
    try:       
        url = "https://slmovieshd2020.blogspot.com/search/label/Action"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        
        match_descrition = soup.select(".description")
        obj1 = soup.select(".teams")
        status = soup.select(".status-text")
        text = ""
        text = text + match_descrition[1].text + "\n\n" + obj1[0].text + "\n\n" + status[0].text + "\n\n" + "**@SophiaSLBot**"    
        await m.edit(text)
        return
    except Exception as e:
        print(str(e))
        return await m.edit("`No Movies`")


bot.start()
idle()



