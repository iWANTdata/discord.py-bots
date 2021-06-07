'''
# -----------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 07.06.2021
(c) Copyright. Not for commercial use. All rights reserved
GitHub
https://github.com/Fynnyx/discord.py-bots
# -----------------------------------------------------------------------------------------------------------------------------------
'''

# Imports
import discord
from discord import embeds
from discord.utils import get
import json

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
bbot_channel: int = 841768678940213270
bbot_prefix: str = '!bbot'

class Bbot(discord.Client):

    async def on_ready(self):
        print('Bbot: logged in')

    async def on_message(self, message):
        if message.content == bbot_prefix + ' help':
            print('help')

        if message.content == bbot_prefix + ' textures':
            print('textures')

        if message.content.startswith(bbot_prefix + ' add'):

            print('add')