from flask import Flask
from threading import Thread  # ✅ Add this line

# == Flask App ==
app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Flask is running! Bot should be running too.'

def run_flask():
    app.run(host='0.0.0.0', port=8000)
flask_thread.start()
# Start Flask in a separate thread
flask_thread = Thread(target=run_flask)
import os
import logging
from . import client
from aiohttp import ClientSession
from pyrogram import idle


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)


async def main():
    await client.startup()
    await client.bot.set_bot_commands(client.config.BOT_COMMANDS)
    session = ClientSession()
    client.session = session
    if client.config.AUTH_USERS:
        client.config.AUTH_USERS.append(client.config.OWNER_ID)
    client.logger.info(f'{client.bot.me.first_name} Started!')
    await idle()


if __name__ == '__main__':
    if not os.path.isdir(client.config.DOWNLOAD_LOCATION):
        os.makedirs(client.config.DOWNLOAD_LOCATION)
    client.run(main())
    #flask_thread.start()
