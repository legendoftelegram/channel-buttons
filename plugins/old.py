#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import os
import sqlite3
import time

from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
logging.getLogger("pyrogram").setLevel(logging.WARNING)

message_id = []

@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP
    )
  
  

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
    )
   


@pyrogram.Client.on_message(pyrogram.Filters.document)
async def old(client, message):
    try:
        await client.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🌀TᴀᴍɪʟRᴏᴄᴋᴇʀs★🌀', url="Config.TAMIL_LINK")],
                    [InlineKeyboardButton("🌀HEVC🌀", url="Config.HEVC_LINK"), InlineKeyboardButton("🌀OLD movies🌀", url="Config.OLD_LINK")],
                    [InlineKeyboardButton("🌀Malayalam🌀", url="Config.MALA_LINK), InlineKeyboardButton("🌀English🌀", url="Config.ENGLISH_LINK")],
                ]
            )
        )
    except FloodWait as e:
                          await asyncio.sleep(e.x)
