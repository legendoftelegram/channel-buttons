#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

import os
import pyrogram

from sample_config import Config  

#stolen from spechides anydlbot


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "buton x",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    app.run()
