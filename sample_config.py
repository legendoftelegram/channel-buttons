import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    TAMIL_LINK = os.environ.get("TAMIL_LINK", "https://placehold.it/90x90")
    HEVC_LINK = os.environ.get("HEVC_LINK", "https://placehold.it/90x90")
    MALA_LINK = os.environ.get("MALA_LINK", "https://placehold.it/90x90")
    OLD_LINK = os.environ.get("OLD_LINK", "https://placehold.it/90x90")
    ENGLISH_LINK = os.environ.get("ENGLISH_LINK", "https://placehold.it/90x90")
