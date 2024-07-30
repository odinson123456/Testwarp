import asyncio
import uvloop
import json
from os import getenv
from datetime import datetime, timedelta
from pyrogram import Client

def timeformat(isotime):
    utc_time = datetime.fromisoformat(isotime.replace('Z', '+00:00'))
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    ist_formatted = ist_time.strftime("%d-%m-%Y %I:%M:%S %p IST")
    return ist_formatted

async def main():
    app = Client(
        name="bot",
        api_id=int(getenv("API_ID")),
        api_hash=getenv("API_HASH"),
        bot_token=getenv("TOKEN"),
    )
    chat = int(getenv("CHAT"))
    async with app:
        filejs = json.loads(open("info.json").read())
        #await app.send_message(chat_id=chat, text=filejs["body"])
        try:
            await app.send_document(
                    chat_id=chat,
                    document="Infinity.apk",
                    caption="Version : {}\nReleased on : {}\n\n{}".format(filejs['tag_name'],timeformat(filejs['created_at']),filejs['body']),
                )
        except Exception as e:
                print(e)

uvloop.install()
asyncio.run(main())