## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgD3t-EARC4vAcKAdWwchlRDtPwAENmPblrFw6QTCatv2x3C_SScxjT4vzgsWFGIrmKbLjrgRAjMokvOJWXoUKEkHA8Aov85-bujW9OgJgllrG4gNQNV1jKqDPrlMxtK1OqRnKYmTVSA3fpuP1rLL6wezuy11QLprgkIQDw3pcNDQKDYAuq3LdRpc8FUFASc66BY5suDGWswpaPTLDIdnq7mYwMk1YWp251JQBXI_8WaUjzNmqd9vQdtZa4Coy4KYwFDLhN5u9FZyRoCVgkMLf2PJ8GGSvEIv35VclJtVw0idRaixESiedY8WGIEPWa7g3qSZW7yaTlQ5T71pQwtYwwolwvHTgAAAAE6hfYhAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5570263294:AAHpLEoT6XnPSTAPtal2a0ckQKq3DvnWwFU")
BOT_NAME = getenv("BOT_NAME", "ʙᴀɴᴅᴀ♕")
API_ID = int(getenv("API_ID", "16234465"))
API_HASH = getenv("API_HASH", "8e67f77b5527aa5dbedd7d283e6199b5")
OWNER_NAME = getenv("OWNER_NAME", ".")
OWNER_USERNAME = getenv("OWNER_USERNAME", "U_F_Z_R")
ALIVE_NAME = getenv("ALIVE_NAME", "U_F_Z_R")
BOT_USERNAME = getenv("BOT_USERNAME", "Ull0ibot")
OWNER_ID = getenv("OWNER_ID", "5276825121")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paaane")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "U_X_B_F")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Uniiiiit5")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
