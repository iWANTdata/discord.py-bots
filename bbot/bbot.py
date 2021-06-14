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
from discord import embeds
from discord.utils import get
import json

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
bbot_channel: int = 851459857076584498
bbot_prefix: str = '!bbot'
bbot_permission = [451776092785737728, 758301777178918922, 526692364782272532, 853233996565577739]

class Bbot(discord.Client):

    async def on_ready(self):
        self.profile_picture = client.user.avatar_url
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='bbond beim Pixeln zu'))
        print('Bbot: logged in')

    async def on_message(self, message):
        if message.content.startswith(bbot_prefix):
            member = message.author
            channel = message.channel

            if message.author != client.user:

                if message.channel.id == bbot_channel:

                    if message.content == (bbot_prefix + ' info'):
                        info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                                   colour=discord.Colour(0x65158d))

                        info_embed.set_author(name="Electionbot Info",
                                              icon_url=self.profile_picture)

                        info_embed.add_field(name="General ❕:",
                                             value="In general this bot is a private project. I made the bot in my freetime.",
                                             inline=True)
                        info_embed.add_field(name="Personalize ✏:",
                                             value="You can personalize this bot by download the code from github (https://github.com/Fynnyx/discord.py-bots) and run it by yourself.",
                                             inline=True)
                        info_embed.add_field(name="Help Command 📜:",
                                             value="The bot prefix is `" + bbot_prefix + "`. You will use this in front off all other  commands. More infos you'll get by using `" + bbot_prefix + " help`.",
                                             inline=True)
                        info_embed.add_field(name='GitHub:',
                                             value='Want to use more bots? Visit https://github.com/Fynnyx/discord.py-bots to get more open source Discord bots.',
                                             inline=False)
                        info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
                        await channel.send(embed=info_embed)

                    if message.content == bbot_prefix + ' help':
                        help_embed = discord.Embed(title='Community Texturepack ‍🎨', colour=discord.Colour(0x65158d))
                        help_embed.set_author(name="Texturepackbot",
                                                       icon_url=self.profile_picture)
                        help_embed.add_field(name='textures',
                                                value='Mit `' + bbot_prefix + ' textures` kannst du alle texturen vom texturepack bekommen',
                                                inline=True)
                        help_embed.add_field(name='add',
                                                value="Bbond kann mit `" + bbot_prefix + ''' add` `"itemname"` `'description'` `zugehöhriger Spieler` neue Items hinzufügen.''',
                                                inline=True)
                        help_embed.add_field(name='downloads',
                                             value='Mit `' + bbot_prefix + ' downloads` bekommst du den link zu der immer aktuellen version', inline=True)
                        help_embed.add_field(name='Fehler gefunden?',
                                             value='schreibe Fynnyx, Bbond, Quacky oder notmappy an, sie können es ändern',
                                             inline=False)

                        await channel.send(embed=help_embed)


                    if message.content == bbot_prefix + ' textures':

                        with open('textures.json', encoding='UTF-8') as f:
                            data = json.load(f)

                        textures = data['textures']

                        textures_embed = discord.Embed(title='Community Texturepack 🎨', colour=discord.Colour(0x65158d))
                        textures_embed.set_author(name="Texturepackbot", icon_url=self.profile_picture)

                        for texture in textures:
                            textures_embed.add_field(name=texture, value=data['textures'][texture]['description'], inline=True)

                        await channel.send(embed=textures_embed)

                    if message.content.startswith(bbot_prefix + ' add'):
                            if member.id in bbot_permission:
                                    add_message = message.content
                                    get_description = add_message.split("'")
                                    get_name = add_message.split('"')
                                    add_message = add_message.split(' ')
                                    range = len(add_message) - 1
                                    if range >= 5:

                                        itemname = get_name[1]
                                        description = get_description[1]
                                        user = add_message[range]

                                        description = description + ' \n Für `' + user + '`'

                                        with open('textures.json', encoding='UTF-8') as f:
                                            data = json.load(f)

                                        data['textures'][str(itemname)] = {'name' : str(itemname), 'description' : str(description)}

                                        with open('textures.json', 'w', encoding='UTF-8') as f:
                                            f.write(json.dumps(data))

                                        added_item_embed = discord.Embed(title='New Item added', description='Bbond hat eine neue Textur zum Texturepack hinzugefügt \n **' + str(itemname) + '**', colour=discord.Colour(0x65158d))

                                        added_item_embed.set_author(name="Texturepackbot",
                                              icon_url=self.profile_picture)

                                        await channel.send(embed=added_item_embed)
                                    else:
                                        add_error_embed = discord.Embed(title="Something went wrong",
                                                                        description="`" + bbot_prefix + "` add `itemname` `description` `für wen`",
                                                                        colour=discord.Colour(0x65158d))
                                        add_error_embed.set_author(name="Texturepackbot",
                                                                    icon_url=self.profile_picture)

                                        await channel.send(embed=add_error_embed)
                            else:
                                no_permission_embed = discord.Embed(title="Permission Error",
                                                                description="Du hast keine Rechte zum hinzufügen von Items. Frage Bbond oder Quacky",
                                                                colour=discord.Colour(0x65158d))
                                no_permission_embed.set_author(name="Texturepackbot",
                                                                icon_url=self.profile_picture)

                                await channel.send(embed=no_permission_embed)


                    if message.content == bbot_prefix + ' downloads':
                        download_embed = discord.Embed(title='Community Texturepack ‍🎨', colour=discord.Colour(0x65158d))
                        download_embed.add_field(name='Demo Version', value='https://www.mediafire.com/file/6mwrqpi4idmyf2b/%25C2%25A76%25C2%25A7lKahlifar_%25C2%25A76%25C2%25A7lDemo_%25C2%25A7a%25C2%25A7lPack.zip/file', inline=False)
                        download_embed.add_field(name='Vollversion vom --.--.----', value='PASTELINKHERE', inline=False)

                        await channel.send(embed=download_embed)

                else:
                    wrong_channel_embed = discord.Embed(title='Community Texturepack ‍🎨', colour=discord.Colour(0x65158d))
                    wrong_channel_embed.set_author(name="Texturepackbot",
                                              icon_url=self.profile_picture)
                    wrong_channel_embed.add_field(name='Wrong Channel', value='Um den DC aufgeräumt zu halten benutze bitte den dafür vorhergesehene Channel')

                    await message.delete()

                    await channel.send(embed=wrong_channel_embed)

client = Bbot()
client.run(TOKEN)
