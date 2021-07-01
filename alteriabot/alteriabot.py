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
import discord.utils
import asyncio
import json

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
# alteria_staff_channel: int = 850646620655058944
alteria_bewerber_channel = 860126598254952458
alteria_prefix: str = '?'
alteria_staff : list= []
alteria_staff_role : str = 'Alteria Staff'

class Alteriabot(discord.Client):

    async def on_ready(self):
        self.profile_picture = client.user.avatar_url
        self.embed_color = 0xb30117
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Alteria'))
        print('Alteria: logged in')

    async def on_message(self, message):
        channel = message.channel
        if message.author != client.user:
            if message.content == alteria_prefix + ' info':
                # creates the info embed
                info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                           colour=discord.Colour(self.embed_color))

                info_embed.set_author(name="Alteriabot Info",
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

            if message.content == alteria_prefix + 'help':
                await channel.send('Hie stehen die Commands')

            if message.content == alteria_prefix + 'warps':
                await channel.send('Hier stehen die **Warps**')

            if message.content == alteria_prefix + 'regeln':
                await channel.send('regel embed')

            if message.content.startswith(alteria_prefix + 'bewerbung '):
                bew_message = str(message.content)
                bew_message_list = bew_message.split(' ', 1)

                if len(bew_message_list) > 0:

                    bew_text = str(bew_message_list[1])
                    bewerber = str(message.author.name)
                    bewerber_profile_picture = str(message.author.avatar_url)

                    bewerbung_embed = discord.Embed(title='Neue Bewerbung', colour=discord.Colour(self.embed_color))
                    bewerbung_embed.add_field(name='Discordname', value=bewerber)
                    bewerbung_embed.add_field(name='Bewerbertext' ,value=bew_text)
                    bewerbung_embed.set_thumbnail(url=bewerber_profile_picture)

                    bewerbungs_channel = discord.utils.get(client.get_all_channels(), id=alteria_bewerber_channel)

                    await bewerbungs_channel.send(embed=bewerbung_embed)

                    await channel.send('✅ Deine Bewerbung ist eingetroffen wenn du nichts von uns höhrst sollte alles gut sein.\n'
                                        'Sonst melden wir uns bei dir und du bewirbst dich nochmal')
                else:
                    await channel.send(
                        '❌ Beim versuch deine Bewerbung zu senden ist was schiefgelaufen probiere ...\n'
                        ' `?bewerbung <bewerbertext [Alter] [Warum möchtest du mitmachen] [Gutes Mikrfon?] [Deine Erfahrung mit solchen Projekten] und [Etwas über dich]>`')



client = Alteriabot()
client.run(TOKEN)
