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

from utils.misc import modules_help, prefix

#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


@Client.on_message(filters.command(["ping", "p"], prefix) & filters.me)
async def ping(_, message: Message):
    start = time.time()
    delta_ping = time.time() - start
    await message.reply(f"<blockquote>Pong! {delta_ping * 1000000:.3f}ms</blockquote>")


modules_help["ping"] = {
    "ping": "Check ping to Telegram servers",
}
