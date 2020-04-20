#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math
import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

userids = []

async def progress_for_pyrogram(client, current, total, ud_type, message_id, chat_id, start, update, bot):
    now = time.time()
    diff = now - start
    if round(diff % 3.00) > 2.999 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        #elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        time_to_completion = await time_formatter(milliseconds=time_to_completion)
        #estimated_total_time = elapsed_time + time_to_completion
        #elapsed_time = await time_formatter(milliseconds=elapsed_time)
        #estimated_total_time = await time_formatter(milliseconds=estimated_total_time)

        progress = "<code>[{0}{1}]| {2}%</code>\n\n".format(
            ''.join(["◼️" for i in range(math.floor(percentage / 5))]),
            ''.join(["◻️" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "<b>{}</b> <b>of</b> <b>{}</b>\n<b>Speed:</b> <b>{}/s</b>\n<b>Remaining:</b> <b>{}</b> /Cancel".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            time_to_completion if time_to_completion != '' else "0 s"
        )
        if update.chat.id in userids:
            userids.remove(update.chat.id) 
            await client.send_message(
                chat_id=chat_id,
                text="cancelled"
            )
            await client.stop_transmission()
        if speed < 1000000:
            await client.send_message(
                chat_id=chat_id,
                text="slow file detected😡canceling."
        )
        if speed < 1000050:
            await client.stop_transmission()

    try:
        await client.edit_message_text(
            chat_id,
            message_id,
            text="{}\n {}".format(
                ud_type,
                tmp
            )
        )
    except:
        pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


async def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
          ((str(hours) + "h, ") if hours else "") + \
          ((str(minutes) + "m, ") if minutes else "") + \
          ((str(seconds) + "s, ") if seconds else "") + \
          ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
