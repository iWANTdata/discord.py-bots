'''
# -----------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 08.06.2021
(c) Copyright. Not for commercial use. All rights reserved
GitHub
https://github.com/Fynnyx/discord.py-bots
# -----------------------------------------------------------------------------------------------------------------------------------
'''

# Imports
import discord
import asyncio
import json

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
alteria_staff_channel: int = 850646620655058944
alteria_prefix: str = '?'
alteria_staff : list= []
alteria_staff_role : str = 'Alteria Staff'

class Alteriabot(discord.Client):

    async def on_ready(self):
        self.profile_picture = client.user.avatar_url
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Alteria'))
        print('Alteria: logged in')

    async def on_message(self, message):
        channel = message.channel
        print(message)
        if message.content == alteria_prefix + ' info':
            # creates the info embed
            info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                       colour=discord.Colour(0x29485e))

            info_embed.set_author(name="Electionbot Info",
                                  icon_url=self.profile_picture)

            info_embed.add_field(name="General ❕:",
                                 value="In general this bot is a private project. I made the bot in my freetime.",
                                 inline=True)
            info_embed.add_field(name="Personalize ✏:",
                                 value="You can personalize this bot by download the code from github (https://github.com/Fynnyx/discord.py-bots) and run it by yourself.",
                                 inline=True)
            info_embed.add_field(name='GitHub:',
                                 value='Want to use more bots? Visit https://github.com/Fynnyx/discord.py-bots to get more open source Discord bots.',
                                 inline=True)
            info_embed.add_field(name="Help Command 📜:",
                                 value="The bot prefix is `" + alteria_prefix + "`. You will use this in front off all other  commands. More infos you'll get by using `" + alteria_prefix + " help`.",
                                 inline=True)
            info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
            # sends the info embed
            await channel.send(embed=info_embed)

        if message.content == alteria_prefix + '':


client = Alteriabot()
client.run(TOKEN)
