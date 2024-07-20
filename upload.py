import asyncio
import uvloop
import json
from os import getenv
from pyrogram import Client


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
                    caption=str(filejs["body"]),
                )
        except Exception as e:
                print(e)

uvloop.install()
asyncio.run(main())