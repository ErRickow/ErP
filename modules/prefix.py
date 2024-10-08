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

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.db import db
from utils.misc import modules_help, prefix
from utils.scripts import restart


@Client.on_message(
    filters.command(["sp", "setprefix", "setprefix_Moon"], prefix) & filters.me
)
async def setprefix(_, message: Message):
    if len(message.command) > 1:
        pref = message.command[1]
        db.set("core.main", "prefix", pref)
        await message.reply(f"<blockquote>Prefix [ <code>{pref}</code> ] telah di set!</blockquote>")
        restart()
    else:
        await message.reply("<blockquote>Prefix gaboleh kosong kontol!</blockquote>")


modules_help["prefix"] = {
    "setprefix [prefix]": "Set custom prefix",
    "setprefix_Moon [prefix]": "Set custom prefix",
}
