''' 
# -----------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 02.06.2021
(c) Copyright. Not for commercial use. All rights reserved
GitHub
https://github.com/Fynnyx/discord.py-bots
# -----------------------------------------------------------------------------------------------------------------------------------
'''


# Imports
import discord
from discord.utils import get

import json


# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
economybot_channel: int = 841768678940213270
economybot_guild_id: int = 840237524982956072
economybot_prefix: str = '!economybot'
economybot_decline: str = '❌'
economybot_accept: str = '✔'
economybot_role_bank_permission: str = 'Banker'
economybot_general_permission = 'Moneyboy'


# creates the class for the Election bot
class EconomyBot(discord.Client):


    # if the bot started
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Fynnyx'))
        print('EconomyBot: logged in')


    async def on_message(self, message):
        channel = message.channel
        member = message.author
        if message.content == (economybot_prefix + ' help'):
            print('Help')


        elif message.content == (economybot_prefix + ' info'):
            print('Info')


        elif message.content.startswith(economybot_prefix + ' give'):
            guild = message.guild
            message_request = str(message.content)
            money_recipient = str(message.mentions[0].id)
            money_sender = message.author
            with open('economy.json') as f:
                data = json.load(f)


        elif message.content.startswith(economybot_prefix + ' add'):
            for role in member.roles:
                # if the user has the permissiont to use the economybot
                if str(role) == economybot_role_bank_permission:
                    money_recipent = str(message.mentions[0].id)

                    add_message = message.content
                    add_message = add_message.split(' ')
                    range = len(add_message) - 1
                    sender_money_amount = add_message[int(range)]


                    with open('economy.json') as f:
                        data = json.load(f)

                    money_recipent_money = data['users'][money_recipent]['money']
                    money_amount = int(money_recipent_money) + int(sender_money_amount)
                    data['users'][money_recipent]['money'] = str(money_amount)

                    with open('economy.json', 'w') as f:
                        f.write(json.dumps(data))

                    added_embed = discord.Embed(title="Added "+ str(sender_money_amount) + " coins  💸  to" , description="<@" + str(message.mentions[0].id) + ">",
                                               colour=discord.Colour(0x29485e))
                    added_embed.set_author(name="Economybot Coins",
                                          icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                    await channel.send(embed=added_embed)


                    break


        elif message.content.startswith(economybot_prefix + ' coins'):
            coin_member_str = str(message.mentions[0].id)
            coin_member = message.mentions[0]

            with open('economy.json') as f:
                data = json.load(f)

            coins = data['users'][coin_member_str]['money']

            coin_embed = discord.Embed(title=coin_member.name + " has " + coins + " coins  💸", colour=discord.Colour(0x29485e))
            coin_embed.set_thumbnail(url=coin_member.avatar_url)
            coin_embed.set_author(name="Economybot Coins", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

            await channel.send(embed=coin_embed)


        elif message.content == economybot_prefix + ' register':

            user = message.author

            with open('economy.json', 'r') as f:
                data = json.load(f)

                if str(user.id) in data['users']:
                    register_error_embed = discord.Embed(title="You can't register because youre already in 👍",
                                          colour=discord.Colour(0x29485e))

                    register_error_embed.set_author(name="Economybot Register Error",
                                     icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

                    await channel.send(embed=register_error_embed)
                else:
                    data['users'][str(user.id)] = {'dc_id' : str(user.id), 'money' : '0'}

                    with open('economy.json', 'w') as f:
                        f.write(json.dumps(data))






# start the bot
client = EconomyBot()
client.run(TOKEN)