from os import listdir, mkdir
from pyrogram import Client
from Mariamusic import config
from Mariamusic.tgcalls.queues import clear, get, is_empty, put, task_done
from Mariamusic.tgcalls import queues
from Mariamusic.tgcalls.youtube import download
from Mariamusic.tgcalls.calls import run, pytgcalls
from Mariamusic.tgcalls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from Mariamusic.tgcalls.convert import convert
