import os
import time
import asyncio
from time import sleep
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, HNDLR, OWNER_ID

@Client.on_message(filters.user(OWNER_ID) & filters.command(['dtg'], prefixes=f"{HNDLR}"))
async def asa(client, m: Message):
   await m.edit("`hallo ges zeinzo hadir buat mencerahkan meki meki kalian yang gelap`")

@Client.on_message(filters.user(OWNER_ID) & filters.command(['plg'], prefixes=f"{HNDLR}"))
async def wasa(client, m: Message):
   await m.edit("`yaudah ya ges zeinzo mau pamit,meki kalian udh cerah kan?yaudah byee`")

@Client.on_message(filters.user(OWNER_ID) & filters.command(['durhaka'], prefixes=f"{HNDLR}"))
async def tol(client, m: Message):
   await m.edit("**iya gua tau hidup lu lebih ampas**")
   sleep(1)
   await m.edit("**tapi jangan lu lampiasin ke telgram**")
   sleep(1)
   await m.edit("**emang bokap lu ga bisa jadi pelampiasan?**")
   sleep(1)
   await m.edit("**coba dah biar lu ngerasa lebih lega,lu pukul bokap lu**")
   sleep(1)
   await m.edit("**terus lu tendang kepalanya**")
   sleep(1)
   await m.edit("**terus lu smackdown ke aspal**")
   sleep(1)
   await m.edit("**terus lu kunci biar lu menang**")
   sleep(1)
   await m.edit("**menjalani hidup yang ampas jangan nanggung nanggung**")


