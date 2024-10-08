#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import asyncio
import os
import sys
import shutil
import subprocess

from git import Repo
from git.exc import InvalidGitRepositoryError

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix, requirements_list
from utils.db import db
from utils.scripts import format_exc, restart


def check_command(command):
    return shutil.which(command) is not None


@Client.on_message(filters.command("restart", prefix) & filters.me)
async def restart_cmd(_, message: Message):
    db.set(
        "core.updater",
        "restart_info",
        {
            "type": "restart",
            "chat_id": message.chat.id,
            "message_id": message.id,
        },
    )

    if "LAVHOST" in os.environ:
        await message.edit("<b>Your lavHost is restarting...</b>")
        os.system("lavhost restart")
        return

    await message.reply("<blockquote>Sedang Merestart...</blockquote>")
    restart()

@Client.on_message(filters.command("update", prefix) & filters.me)
async def update(_, message: Message):
    db.set(
        "core.updater",
        "restart_info",
        {
            "type": "update",
            "chat_id": message.chat.id,
            "message_id": message.id,
        },
    )

    if "LAVHOST" in os.environ:
        await message.edit("<b>Your lavHost is updating...</b>")
        os.system("lavhost update")
        return

    await message.reply("<blockquote>Wet...</blockquote>\n<blockquote>Sedang Update!</blockquote>")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "pip"])
        subprocess.run(["git", "pull"])
    except Exception as e:
        await message.reply(format_exc(e))
        db.remove("core.updater", "restart_info")
    else:
        await message.reply("<blockquote>Update: selesai sayang!</blockquote>\n\n<blockquote>Merestart...</blockquote>")
        restart()
        await message.reply("<b>_Sudah Selesai Restartnya sayang_...</b>")

#nganu


modules_help["updater"] = {
    "update": "Update Userbot Lu. Jika ada update an.",
    "restart": "Restart Userbotnya",
}
