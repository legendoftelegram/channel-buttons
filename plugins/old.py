#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client,Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
logging.getLogger("pyrogram").setLevel(logging.WARNING)



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
async def old(bot, update):
    await bot.edit_message_reply_markup(
        chat_id=update.chat.id,
        message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('•TᴀᴍɪʟRᴏᴄᴋᴇʀs★•', url='https://t.me/joinchat/AAAAAEoI9qHQDl54X6hrnA')],
                [InlineKeyboardButton("🌀HEVC🌀", url="https://t.me/joinchat/AAAAAFSZfpvuqvHrlJ-Vig"), InlineKeyboardButton("🌀OLD movies🌀", url="https://t.me/joinchat/AAAAAFMMxf1wotQy7G3kfg")],
                [InlineKeyboardButton("🌀Malayalam🌀", url="https://t.me/joinchat/AAAAAFPCFsHvCo9WTClaVg"), InlineKeyboardButton("🌀English🌀", url="https://t.me/joinchat/AAAAAFcgVJN1SCE_QDcLRg")],
                [InlineKeyboardButton("🌀Kannada🌀", url="https://t.me/joinchat/AAAAAFco7KkVwmdDvF8LJw"), InlineKeyboardButton("🌀WEB SERIES🌀", url="https://t.me/joinchat/AAAAAEXHnHCKUuSUu0yM2A")],
                [InlineKeyboardButton("🌀STREAM🌀", url="https://t.me/joinchat/AAAAAEowm0foYx11yTQotA"), InlineKeyboardButton("🌀400MB🌀", url="https://t.me/joinchat/AAAAAEL_N1cxaMN4GGEctw")],
                [InlineKeyboardButton("🌀All movies🌀", url="https://t.me/joinchat/AAAAAESroNzOW8OJKX4hCg"), InlineKeyboardButton("🌀Love and status🌀", url="https://t.me/joinchat/AAAAAEXHnHCKUuSUu0yM2A")],
                [InlineKeyboardButton('🌀TR NETWORK🌀', url='https://t.me/TR_NETWORK')],
            ]
        )
    )

    
