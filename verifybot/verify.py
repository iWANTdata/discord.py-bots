'''
# ------------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 13.05.2021
(c) Copyright. Not for commercial use. All rights reserved
Gitlab
https://gitlab.com/hochwacht/roverchiste
# ------------------------------------------------------------------------------------------------------------------------------------
'''


# Imports
import discord
from discord.utils import get

# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# Variables to change
verify_channel_name = 'verify'
verify_emoji = '✅'
verify_role = 847062220328534036
verify_permission = 'Admin'


class VerifyBot(discord.Client):

    role = 0

    async def on_ready(self):
        print('Verify: logged in')


    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.name == verify_channel_name:
            if str(reaction) == verify_emoji:
                self.role = discord.utils.get(user.guild.roles, id=verify_role)
                await user.add_roles(self.role)

    async def on_message(self, message):
        if message.channel.name == verify_channel_name:
            channel = client.get_channel(message.channel.id)
            user = message.author
            self.role = discord.utils.get(user.guild.roles, id=verify_role)

            if message.content == '!verify':


                for role in user.roles:
                    if str(role) == verify_permission:
                        await message.delete()

                        verify_embed = discord.Embed(colour=discord.Colour(0x29485e), description="By clicking/tapping on " + verify_emoji + " below, you agree with the rules on this server. You can also verify by typing agree if clicking/tapping the reaction doesn't work.")

                        verify_embed.set_author(name="Verify ", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

                        await channel.send(embed=verify_embed)

            elif message.content == 'agree':
                await message.delete()
                await user.add_roles(self.role)

            elif message.content != '!verify' and message.author != client.user:
                await message.delete()

            if message.author == client.user:
                await message.add_reaction(verify_emoji)



client = VerifyBot()
client.run(TOKEN)