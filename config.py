## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB1zJ0Aei6Z98KQkDI9M4S5Urumc2j6GyThl8kRq2TGzcF77eUCSJupjj8jf_fcI5ACfrDHBDZuMJR8Q3_id6tqs-Dt7MgU7YKH4y_NRGjv21I0MYllZ02XXSHyq75Dnl7Zdmd3UyoHpE5hMuL0f3vUCCqgKDBhtZmlcr_R-RQOSFpWxPteqMZ6jBUPg-K6A0zB-__TnJpkFZ_JaOchNkU2A-20JI8a8Hv5rImI-rQYT8yuvNleTweM4nA41JQzpTlJhvb_v4eGlxhs_Shc8jCu1K7lh1fBMSo_5Rd2Pc8KWWyhYLWev2hhswQIQKOkXj-vHnKVQdKqcJB8GX1g8AuoGM273gAAAAB5OWZSAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5040909726:AAFuQPfz5eloUbjczJQwgjAkBWsA0PHX1fU")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "LEGEND")
OWNER_USERNAME = getenv("OWNER_USERNAME", "L120N")
ALIVE_NAME = getenv("ALIVE_NAME", "SOSKA")
BOT_USERNAME = getenv("BOT_USERNAME", "S120KBOT")
OWNER_ID = getenv("OWNER_ID", "1236115329")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SOSKA")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "baj_bo")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "baj_bo")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1236115319").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/dfb36a99be9f9a2e48b15.jpg")
