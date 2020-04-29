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
  


@pyrogram.Client.on_message(pyrogram.Filters.command(["channels"]))
async def channels(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CH_LIST,
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
    )
   


@pyrogram.Client.on_message(pyrogram.Filters.video | Filters.document | Filters.text)
async def chats(bot, update):
    await bot.edit_message_text(
        chat_id=update.chat.id,
        message_id=update.message_id,
        text=update.text,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🥴SUPPORT🥴",
            url="https://t.me/joinhereforcross")]]
        )
    )
