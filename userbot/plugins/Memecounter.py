"""Syntax:
.cmeme"""

import asyncio
import os
import sys
import random

from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"cmeme", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    x=(random.randrange(1,27)) 
    if (x==1):
      await event.edit("**Sei un meme, valore : 1%**")
    if (x==2):
      await event.edit("**Sei un meme, valore : 5%**")
    if (x==3):
      await event.edit("**Sei un meme, valore : 10%**")
    if (x==4):
      await event.edit("**Sei un meme, valore : 15%**")
    if (x==5):
      await event.edit("**Sei un meme, valore : 20%**")
    if (x==6):
      await event.edit("**Sei un meme, valore : 25%**")
    if (x==7):
      await event.edit("**Sei un meme, valore : 30%**")
    if (x==8):
      await event.edit("**Sei un meme, valore : 35%**")
    if (x==9):
      await event.edit("**Sei un meme, valore : 40%**")
    if (x==10):
      await event.edit("**Sei un meme, valore : 45%**")
    if (x==11):
      await event.edit("**Sei un meme, valore : 50%**")
    if (x==12):
      await event.edit("**Sei un meme, valore : 55%**")
    if (x==13):
      await event.edit("**Sei un meme, valore : 60%**")
    if (x==14):
      await event.edit("**Sei un meme, valore : 65%**")
    if (x==15):
      await event.edit("**Sei un meme, valore : 70%**")
    if (x==16):
      await event.edit("**Sei un meme, valore : 75%**")
    if (x==17):
      await event.edit("**Sei un meme, valore : 80%**")
    if (x==18):
      await event.edit("**Sei un meme, valore : 85%**")
    if (x==19):
      await event.edit("**Sei un meme, valore : 89%**")
    if (x==20):
      await event.edit("**Sei un meme, valore : 90%**")
    if (x==21):
      await event.edit("**Sei un meme, valore : 92%**")
    if (x==22):
      await event.edit("**Sei un meme, valore : 95%**")
    if (x==23):
      await event.edit("**Sei un meme, valore : 97%**")
    if (x==24):
      await event.edit("**Sei un meme, valore : 98%**")
    if (x==25):
      await event.edit("**Sei un meme, valore : 99%**")
    if (x==26):
      await event.edit("**Sei un meme, valore : 100%**")
    if (x==27):
      await event.edit("**Sei il capo dei Meme**")
