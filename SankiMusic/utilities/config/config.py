import os
import re
import sys

from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ᴍᴜꜱɪᴄ ᴏɴ˼ ✘ ˹ʙᴏᴛ˼")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5276549368").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/botmrnbrand/SankiXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "kaal")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botnrn")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/botmrn01")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "sankilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/95f4643a0662d926b821d.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/9ff31f35fbe6d91ca3b7c.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph/file/756b08a6e12f8af668b89.jpg"
GLOBAL_IMG_URL = "https://telegra.ph/file/2c65aed0ea7e621dfd960.jpg"
STATS_IMG_URL = "https://telegra.ph/file/2c65aed0ea7e621dfd960.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b8d21d3dc4f90791f7133.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/b8d21d3dc4f90791f7133.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/dc9c7840e94bcc5c8036a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/83e7221243ade95d19504.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d75c1934c7841b9e81380.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/c01000ea7f2c33dd119da.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/c01000ea7f2c33dd119da.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/c01000ea7f2c33dd119da.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "SankiMusic/resource/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/9ff31f35fbe6d91ca3b7c.jpg"

if START_IMG_URL:
    if START_IMG_URL != "SankiMusic/resource/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/659d9400ec1e8f2a7f893.jpg"
