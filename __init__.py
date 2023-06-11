from telethon import TelegramClient
import logging
import time

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6173228203:AAFwB9MS_H-3zq9HeE7HK9cUEzy_UYbtkxo"

bot = TelegramClient(("lakhanbishnoi_bot"), api_id, api_hash).start(bot_token = bot_token)