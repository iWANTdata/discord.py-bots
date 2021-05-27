'''
# ------------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 26.05.2021
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

# Variables to change
verify_channel_name = 'verify'
verify_prefix = '!verify'
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

            # if the message is with info
            elif message.content == verify_prefix + ' info':
                # creates the info embed
                info_embed = discord.Embed(title="Here you can get the most information about this bot!", colour=discord.Colour(0x29485e))
                
                info_embed.set_author(name="Electionbot Info", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                info_embed.add_field(name="General ❕:", value="In general this bot is a private project. I made the bot in my freetime.", inline=True)
                info_embed.add_field(name="Personalize ✏:", value="You can personalize this bot by download the code from github and run it by yourself.", inline=True)
                info_embed.add_field(name="Help Command 📜:", value="The bot prefix is `" + electionbot_prefix +"`. You will use this in front off all other  commands. More infos you'll get by using `" + electionbot_prefix +" help`.", inline=True)
                info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
                # sends the info embed
                await channel.send(embed=info_embed)

            elif message.content == 'agree':
                await message.delete()
                await user.add_roles(self.role)

            elif message.content != '!verify' and message.author != client.user:
                await message.delete()

            if message.author == client.user:
                await message.add_reaction(verify_emoji)



client = VerifyBot()
client.run(TOKEN)