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

# create Bot Class
class VerifyBot(discord.Client):
    
    # set class variable 'role'
    role = 0

    # if the bot is ready
    async def on_ready(self):
        print('Verify: logged in')

    # if someone reacted
    async def on_reaction_add(self, reaction, user):
        # if the message is in the verify channel
        if reaction.message.channel.name == verify_channel_name:
            # if the reaction is the verify reaction
            if str(reaction) == verify_emoji:
                # get the role
                self.role = discord.utils.get(user.guild.roles, id=verify_role)
                # give the user the role
                await user.add_roles(self.role)

    # if someone send a message
    async def on_message(self, message):
        # get the channel
        channel = client.get_channel(message.channel.id)
        # if the channel si the right one
        if message.channel.name == verify_channel_name:
            # get the user
            user = message.author
            # get the role
            self.role = discord.utils.get(user.guild.roles, id=verify_role)

            # if someone whant to send the button
            if message.content == '!verify':

                # if the author has the permisson to do that
                for role in user.roles:
                    if str(role) == verify_permission:
                        # delete the message
                        await message.delete()

                        # create the verify embed
                        verify_embed = discord.Embed(colour=discord.Colour(0x29485e), description="By clicking/tapping on " + verify_emoji + " below, you agree with the rules on this server. You can also verify by typing agree if clicking/tapping the reaction doesn't work.")

                        verify_embed.set_author(name="Verify ", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                        # send the embed
                        await channel.send(embed=verify_embed)
            
            # if someone type agree in the chat
            elif message.content == 'agree':
                # delete the message
                await message.delete()
                # give the verified role
                await user.add_roles(self.role)

            # if the message is another message
            elif message.content != '!verify' and message.author != client.user:
                await message.delete()


            elif message.author == client.user:
                channel = message.channel
                # add the button
                await message.add_reaction(verify_emoji)

        # if the message is with info
        if message.content == verify_prefix + ' info':
        # creates the info embed
            info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                       colour=discord.Colour(0x29485e))
            info_embed.set_author(name="Verifybot Info",
                                  icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")
            info_embed.add_field(name="General ❕:",
                                 value="In general this bot is a private project. I made the bot in my freetime.",
                                 inline=True)
            info_embed.add_field(name="Personalize ✏:",
                                 value="You can personalize this bot by download the code from github (https://github.com/Fynnyx/discord.py-bots) and run it by yourself.",
                                 inline=True)
            info_embed.add_field(name="Help Command 📜:",
                                 value="The bot prefix is `" + verify_prefix + "`. You will use this in front off all other  commands. More infos you'll get by using `" + verify_prefix + " help`.",
                                 inline=True)
            info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
            # sends the info embed
            await channel.send(embed=info_embed)

        if message.content == verify_prefix + ' help':
            # create the embed for help
            help_embed = discord.Embed(colour=discord.Colour(0x29485e))

            help_embed.set_author(name="Verifybot Help",
                                  icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

            help_embed.add_field(name="Send the verify button",
                                 value="With `" + verify_prefix + "` You can send the verify button.")
            help_embed.add_field(name="Agree hte rules",
                                 value="By typing `agree` in the right channel, you agree the rules")
            # sends the embed
            await channel.send(embed=help_embed)




# start the bot
client = VerifyBot()
client.run(TOKEN)