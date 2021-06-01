'''
# ------------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 01.06.2021
(c) Copyright. Not for commercial use. All rights reserved
GitHub
https://github.com/Fynnyx/discord.py-bots
# ------------------------------------------------------------------------------------------------------------------------------------
'''


# Imports
import discord
from discord.utils import get

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
electionbot_prefix: str = '!commandbot'

# creates the class for the Election bot
class CommandBot(discord.Client):

    async def on_ready(self):
        print('CommandBot: logged in')


client = CommandBot()
client.run(TOKEN)