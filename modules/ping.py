#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

import time

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import Message
from time import get_readable_time

from utils.scripts import time_formatter
from utils.misc import modules_help, prefix

#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += f"{time_list.pop()}, "

    time_list.reverse()
    readable_time += ":".join(time_list)

    return readable_time

@Client.on_message(filters.command(["ping", "p"], prefix) & filters.me)
async def ping(_, message: Message):
    start = time.time()
    nganu = time.time() - start
    uptime = time_formatter(time.time() - time.time())
    await message.reply(f"<blockquote>❏ POMG!!🏓 {nganu * 1000000:.3f}ms</blockquote>\nUptime {uptime}")


modules_help["ping"] = {
    "ping": "Check ping to Telegram servers",
}
