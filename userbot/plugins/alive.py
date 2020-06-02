"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                     "`☞Telethon version: 1.11.3\n`"
                     "`☞Python: 3.8.2\n`"
                     "`☞Bot was modified by:` @darthvade_r\n"
                     "`☞and created by :` snapdragon,anubis\n"
                     "`☞Database Status: Databases functioning normally!\n\n`"
                     "`☞Always with you, my master!\n`"
                     f"`☞Owner Name`: [{DEFAULTUSER}](t.me/darthvade_r)\n"
                     "☞[Deploy this userbot Now](https://github.com/Sur-vivor/CatUserbot)"
                    )

    
CMD_HELP.update({
    "alive":
    ".alive\
    \nUsage: Type .alive to see wether your bot is working or not.\
    "
})    
