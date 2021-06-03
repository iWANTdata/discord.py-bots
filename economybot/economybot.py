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
            # creates the info embed
            info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                       colour=discord.Colour(0x29485e))

            info_embed.set_author(name="Electionbot Info",
                                  icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

            info_embed.add_field(name="General ❕:",
                                 value="In general this bot is a private project. I made the bot in my freetime.",
                                 inline=True)
            info_embed.add_field(name="Personalize ✏:",
                                 value="You can personalize this bot by download the code from github (https://github.com/Fynnyx/discord.py-bots) and run it by yourself.",
                                 inline=True)
            info_embed.add_field(name="Help Command 📜:",
                                 value="The bot prefix is `" + economybot_prefix + "`. You will use this in front off all other  commands. More infos you'll get by using `" + economybot_prefix + " help`.",
                                 inline=True)
            info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
            # sends the info embed
            await channel.send(embed=info_embed)


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
                    if message.mentions != []:
                        money_recipent = str(message.mentions[0].id)
                        add_message = message.content
                        add_message = add_message.split(' ')
                        range = len(add_message) - 1
                        if range == 3:

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
                        else:
                            add_error_embed = discord.Embed(title="Something went wrong", description="`" + economybot_prefix + "` add `@member` `amount",
                                                                 colour=discord.Colour(0x29485e))

                            add_error_embed.set_author(name="Economybot Add Error",
                                                            icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

                            await channel.send(embed=add_error_embed)
                    else:
                        add_error_embed = discord.Embed(title="Something went wrong",
                                                        description="`" + economybot_prefix + "` add `@member` `amount",
                                                        colour=discord.Colour(0x29485e))

                        add_error_embed.set_author(name="Economybot Add Error",
                                                   icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

                        await channel.send(embed=add_error_embed)

        elif message.content.startswith(economybot_prefix + ' remove'):
            for role in member.roles:
                # if the user has the permissiont to use the economybot
                if str(role) == economybot_role_bank_permission:
                    money_recipent = str(message.mentions[0].id)

                    remove_message = message.content
                    remove_message = remove_message.split(' ')
                    range = len(remove_message) - 1
                    if range == 3:

                        sender_money_amount = remove_message[int(range)]

                        with open('economy.json') as f:
                            data = json.load(f)

                        money_recipent_money = data['users'][money_recipent]['money']
                        money_amount = int(money_recipent_money) - int(sender_money_amount)
                        data['users'][money_recipent]['money'] = str(money_amount)

                        with open('economy.json', 'w') as f:
                            f.write(json.dumps(data))

                        added_embed = discord.Embed(title="Added " + str(sender_money_amount) + " coins  💸  to",
                                                    description="<@" + str(message.mentions[0].id) + ">",
                                                    colour=discord.Colour(0x29485e))
                        added_embed.set_author(name="Economybot Coins",
                                               icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                        await channel.send(embed=added_embed)
                    else:
                        add_error_embed = discord.Embed(title="Something went wrong",
                                                        description="`" + economybot_prefix + "` add `@member` `amount",
                                                        colour=discord.Colour(0x29485e))

                        add_error_embed.set_author(name="Economybot Add Error",
                                                   icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

                        await channel.send(embed=add_error_embed)


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