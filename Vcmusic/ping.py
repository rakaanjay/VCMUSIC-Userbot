import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, OWNER_ID
from time import time
from time import sleep
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.user(OWNER_ID) & filters.command(['rmusic'], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
   KONTOL = f"⚙️ **Source code**\n• **😼 Github :** [Vcmusic-Userbot](https://github.com/KennedyProject/Vcmusic-Userbot)\n• 🗂️ **GPL - 3.0 License**"
   await m.edit(KONTOL, disable_web_page_preview=True)
