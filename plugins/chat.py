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
from pyrogram import Filters
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
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SUC_SE,
    )
    a=await bot.forward_messages(
          chat_id=int("-1001368143298"),
          from_chat_id=update.chat.id,
          message_ids=update.message_id
    )
    await bot.edit_message_media(
        chat_id=update.chat.id,
        document=a,
        thumb="tr.jpg"
    )
