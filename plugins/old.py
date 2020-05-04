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
   


@pyrogram.Client.on_message(pyrogram.Filters.video | Filters.document)
async def old(bot, update):
    await bot.edit_message_reply_markup(
        chat_id=int("-1001393346045"),
        message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Tamilrockers", url="https://t.me/joinchat/AAAAAFGqNJrNmUesTrn35Q"), InlineKeyboardButton("Classic cinemas", url="https://t.me/joinchat/AAAAAFbp_MV44jysESlYUA")],
                [InlineKeyboardButton("Film City", url="https://t.me/joinchat/AAAAAFcWmGkDtzO6fKov9A"), InlineKeyboardButton("Malayalam Movies", url="https://t.me/joinchat/AAAAAFQq5ByVjeEzTQxtdw")],
                [InlineKeyboardButton("Leaked Movies", url="https://t.me/joinchat/AAAAAFj23kEV6_DfuUg0wQ"), InlineKeyboardButton("Netflix Movies series", url="https://t.me/joinchat/AAAAAFJF5c1kZSlroRT1sQ")],
                [InlineKeyboardButton("All In One Movie Channel", url="https://t.me/joinchat/AAAAAEXBrsq98fFfilU2Mw"), InlineKeyboardButton("Hevc Movies", url="https://t.me/joinchat/AAAAAEdvAySlFirppj4ACg")],
                [InlineKeyboardButton("Old Movies", url="https://t.me/joinchat/AAAAAEjQX-exc-sdyC1Tiw"), InlineKeyboardButton("Tamil Moviez", url="https://t.me/joinchat/AAAAAFb1t0WASPF-ClYOAg")],
                [InlineKeyboardButton("Amazon Prime Movies", url="https://t.me/joinchat/AAAAAFZtHEDtkdq1zLXsmQ"), InlineKeyboardButton("Kickass Torrents", url="https://t.me/joinchat/AAAAAFi-jZsSc3OlHRSltQ")],
                [InlineKeyboardButton("TamilBlasters", url="https://t.me/joinchat/AAAAAEbDumtV24nDeKVtRw"), InlineKeyboardButton("Movie Archives And Filmography", url="https://t.me/FC_Archives")],
                [InlineKeyboardButton('TgNetworks', url='http://T.me/TgNetworks')],
            ]
        )
    )

    
