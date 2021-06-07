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
bbot_channel: int = 851459857076584498
bbot_prefix: str = '!bbot'

class Bbot(discord.Client):

    async def on_ready(self):
        print('Bbot: logged in')

    async def on_message(self, message):
        if message.content.startswith(bbot_prefix):
            member = message.author
            channel = message.channel

            if message.author != client.user:

                if message.channel.id == bbot_channel:

                    if message.content == bbot_prefix + ' help':
                        print('help')

                    if message.content == bbot_prefix + ' textures':

                        with open('textures.json', encoding='UTF-8' ) as f:
                            data = json.load(f)

                        textures = data['textures']

                        textures_embed = discord.Embed(title='Community Texturepack')
                        textures_embed.set_author(name="Texturepackbot", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                        for texture in textures:
                            textures_embed.add_field(name=texture, value=data['textures'][texture]['description'], inline=True)

                        await channel.send(embed=textures_embed)

                    if message.content.startswith(bbot_prefix + ' add'):
                            if member.id == 451776092785737728:
                                    add_message = message.content
                                    add_message = add_message.split(' ')
                                    range = len(add_message) - 1
                                    if range == 4:

                                        itemname = add_message[2]
                                        description = add_message[3]
                                        user = add_message[4]

                                        description = description + ' \n für ' + user

                                        with open('textures.json') as f:
                                            data = json.load(f)

                                            data['textures'][str(itemname)] = {'name' : str(itemname), 'description' : str(description)}

                                            with open('textures.json', 'w') as f:
                                                f.write(json.dumps(data))

                                    else:
                                        add_error_embed = discord.Embed(title="Something went wrong",
                                                                        description="`" + bbot_prefix + "` add `itemname` `description` `für wen`",
                                                                        colour=discord.Colour(0x29485e))

                                        add_error_embed.set_author(name="Economybot Add Error",
                                                                    icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                                        await channel.send(embed=add_error_embed)
                else:
                    wrong_channel_embed = discord.Embed(title='Community Texturepack')
                    wrong_channel_embed.set_author(name="Texturepackbot",
                                              icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")
                    wrong_channel_embed.add_field(name='Wrong Channel', value='Um den DC aufgeräumt zu halten benutze bitte den dafür vorhergesehene Channel')

                    await channel.send(embed=wrong_channel_embed)

client = Bbot()
client.run(TOKEN)
