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
economybot_channel: int = 841768678940213270
economybot_guild_id: int = 840237524982956072
economybot_prefix: str = '!economybot'
economybot_decline: str = '❌'
economybot_accept: str = '✔'
economybot_role_bank_permission: str = 'Banker'


# creates the class for the Election bot
class EconomyBot(discord.Client):


    # if the bot started
    async def on_ready(self):
        self.profile_picture = client.user.avatar_url
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Fynnyx'))
        print('EconomyBot: logged in')


    async def not_registered_error_you(self, you_id):
        pls_register_embed = discord.Embed(
                                title="You have to register first",
                                description="<@" + str(you_id) + ">",
                                colour=discord.Colour(0x29485e))
        pls_register_embed.set_author(
                                name="Economybot Register Error",
                                icon_url=self.profile_picture)

        await self.channel.send(embed=pls_register_embed)

    async def not_registered_error_other(self, other_id):
        pls_register_embed = discord.Embed(
                                    title="The member has to register first",
                                    description="<@" + str(other_id) + ">",
                                    colour=discord.Colour(0x29485e))
        pls_register_embed.set_author(
                                    name="Economybot Register Error",
                                    icon_url=self.profile_picture)

        await self.channel.send(embed=pls_register_embed)

    async def something_went_wrong(self):
        add_error_embed = discord.Embed(
                                title="Something went wrong", 
                                description="`" + economybot_prefix + "` add/remove `@member` `amount`",
                                colour=discord.Colour(0x29485e))

        add_error_embed.set_author(
                                name="Economybot Add Error",
                                icon_url=self.profile_picture)

        await self.channel.send(embed=add_error_embed)

    async def item_shop(self):
        with open("shop.json") as f:
            data = json.load(f)

        items_shop = data['shop']['ITEMSHOP']['items']

        itemshop_embed = discord.Embed(title="ITEMSHOP", description="Buy items and use them later",
                                       colour=discord.Colour(0x29485e))
        itemshop_embed.set_author(name="Economybot Shop",
                                  icon_url=self.profile_picture)
        for item in items_shop:
            itemshop_embed.add_field(name=data['shop']['ITEMSHOP']['items'][item]['item_name'],
                                     value=data['shop']['ITEMSHOP']['items'][item]['description'], inline=True)

        await self.channel.send(embed=itemshop_embed)




    async def on_message(self, message):
        # get the channel where the message was sended
        self.channel = message.channel

        # get the author
        member = message.author

        # if the help command got called
        if message.content == (economybot_prefix + ' help'):
            print('Help')

        # if the info command got called
        elif message.content == (economybot_prefix + ' info'):
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
                                 value='Wanna use more bots? Visit https://github.com/Fynnyx/discord.py-bots to get more open source Discord bots.',
                                 inline=True)
            info_embed.add_field(name="Help Command 📜:",
                                 value="The bot prefix is `" + economybot_prefix + "`. You will use this in front off all other  commands. More infos you'll get by using `" + economybot_prefix + " help`.",
                                 inline=True)
            info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
            # sends the info embed
            await self.channel.send(embed=info_embed)

        # if someone want to to send money to another member
        elif message.content.startswith(economybot_prefix + ' give'):
            # if someone got mentioned in the message
            if message.mentions != []:
                    # get the content of the message
                    message_request = message.content
                    # split it at every space
                    message_request_split = message_request.split(' ')
                    # the recipient is the first user in the mention list
                    money_recipient = message.mentions[0]
                    # the sender is the author
                    money_sender = message.author
                    # how long the message is
                    range = len(message_request_split) - 1
                    # the range only can be 4 words long
                    if range == 3:
                        # set the amount of money
                        sender_money_amount = message_request_split[int(range)]
                        # open the json file
                        with open('users.json') as f:
                            # save the data in data
                            data = json.load(f)
                        # if the sender is registered
                        if str(money_sender.id) in data['users']:
                            # if the recipient is registered
                            if str(money_recipient.id) in data['users']:
                                # get the money count of the sender
                                money_sender_money = data['users'][str(money_sender.id)]['money']
                                # check if the sender has enough money
                                if int(money_sender_money) - int(sender_money_amount) < 0:
                                    # if he hasn't enough money
                                    not_enough_money_embed = discord.Embed(
                                        title="You dont have enough money", description="<@" + str(message.mentions[0].id) + "> you only have " + data['users'][str(money_sender.id)]['money'],
                                        colour=discord.Colour(0x29485e))
                                    not_enough_money_embed.set_author(name="Economybot Register Error",
                                                                      icon_url=self.profile_picture)
                                    # send the embed
                                    await self.channel.send(embed=not_enough_money_embed)
                                # if the sender has enough money
                                else:
                                    # get the amount of money from the recipient
                                    money_recipent_money = data['users'][str(money_recipient.id)]['money']
                                    # add the money to the recipient
                                    money_amount = int(money_recipent_money) + int(sender_money_amount)
                                    # add it to the dict
                                    data['users'][str(money_recipient.id)]['money'] = str(money_amount)

                                    # write it in the file
                                    with open('users.json', 'w') as f:
                                        f.write(json.dumps(data))

                                    # get the moneyamount from the sender
                                    money_sender_money = data['users'][str(money_sender.id)]['money']
                                    # remove the amount of money from the sender
                                    money_amount = int(money_sender_money) - int(sender_money_amount)
                                    # add it to the dict
                                    data['users'][str(money_sender.id)]['money'] = str(money_amount)

                                    # write it in the file
                                    with open('users.json', 'w') as f:
                                        f.write(json.dumps(data))

                                    # embed that the money has been send
                                    send_embed = discord.Embed(
                                        title= money_sender.name + " sended money.",
                                        description="<@" + str(message.mentions[0].id) + "> you got " + sender_money_amount + " coins  💸  from <@" + str(money_sender.id) + ">",
                                        colour=discord.Colour(0x29485e))
                                    send_embed.set_author(name="Economybot Register Error",
                                                                      icon_url=self.profile_picture)
                                    # send the embed
                                    await self.channel.send(embed=send_embed)
                            # if the recipient hasnt registered yet
                            else:
                                await self.not_registered_error_other(str(message.mentions[0].id))

                        # if the sender hast registered
                        else:
                            await self.not_registered_error_you(str(message.author.id))

        # if a 'Banker' want to add money to a member
        elif message.content.startswith(economybot_prefix + ' add'):
            # get all roles
            for role in member.roles:
                # if the user has the permissiont to use the economybot admin functions
                if str(role) == economybot_role_bank_permission:
                    # if someone got mentioned
                    if message.mentions != []:
                        # define the recipent
                        money_recipent = str(message.mentions[0].id)
                        # get the message
                        add_message = message.content
                        # split the message to a list
                        add_message = add_message.split(' ')
                        # define the length of the list
                        range = len(add_message) - 1
                        # if the message has 4 words
                        if range == 3:
                            # set the amount
                            sender_money_amount = add_message[int(range)]

                            # open the file
                            with open('users.json') as f:
                                data = json.load(f)

                            # if the user is registered
                            if str(money_recipent) in data['users']:
                                # get the money from the recipient
                                money_recipent_money = data['users'][money_recipent]['money']
                                # add the money
                                money_amount = int(money_recipent_money) + int(sender_money_amount)
                                # save it in the dict
                                data['users'][money_recipent]['money'] = str(money_amount)

                                # write it into the file
                                with open('users.json', 'w') as f:
                                    f.write(json.dumps(data))

                                # say that money has been send
                                added_embed = discord.Embed(title="Added "+ str(sender_money_amount) + " coins  💸  to" , description="<@" + str(message.mentions[0].id) + ">",
                                                           colour=discord.Colour(0x29485e))
                                added_embed.set_author(name="Economybot Coins",
                                                      icon_url=self.profile_picture)

                                await self.channel.send(embed=added_embed)
                                break

                            else:
                                # the recipient has to register first
                                await self.not_registered_error_other(str(message.mentions[0].id))
                                break
                        # if the command is not right
                        else:
                            await self.something_went_wrong()
                            break
                    # if th command is not right
                    else:
                        await self.something_went_wrong()
                        break

        # if someone has to much money :)
        elif message.content.startswith(economybot_prefix + ' remove'):
            # check the permission
            for role in member.roles:
                # if the user has the permissiont to use the economybot
                if str(role) == economybot_role_bank_permission:
                    # if someone got mentioned in the message
                    if message.mentions != []:
                        # get the recipient
                        money_recipent = str(message.mentions[0].id)
                        # save the message
                        add_message = message.content
                        # split the message
                        add_message = add_message.split(' ')
                        # save the length of the message
                        range = len(add_message) - 1
                        # the message has to have 4 words
                        if range == 3:
                            # defin the amount of money
                            sender_money_amount = add_message[int(range)]

                            # opne the json file
                            with open('users.json') as f:
                                data = json.load(f)
                            # if the recipient is registered
                            if str(money_recipent) in data['users']:
                                # get the money amount from the recipient
                                money_recipent_money = data['users'][money_recipent]['money']
                                # remove the money from the bank acc
                                money_amount = int(money_recipent_money) - int(sender_money_amount)
                                # write it into the dict
                                data['users'][money_recipent]['money'] = str(money_amount)

                                # write it into the file
                                with open('users.json', 'w') as f:
                                    f.write(json.dumps(data))

                                # send what has been removed
                                added_embed = discord.Embed(title="Removed "+ str(sender_money_amount) + " coins  💸  from" , description="<@" + str(message.mentions[0].id) + ">",
                                                           colour=discord.Colour(0x29485e))
                                added_embed.set_author(name="Economybot Removed Coins",
                                                      icon_url=self.profile_picture)

                                await self.channel.send(embed=added_embed)
                                break
                            # if the recipient isn't registered
                            else:
                                await self.not_registered_error_other(str(message.mentions[0].id))
                                break
                        # if the command is false
                        else:
                            await self.something_went_wrong()
                            break
                    # if the command is wrong
                    else:
                        await self.something_went_wrong()
                        break

        # to get the amount of coins from a user
        elif message.content.startswith(economybot_prefix + ' coins'):
            # if someone got mentioned
            if message.mentions != []:
                # save the member
                coin_member = message.mentions[0]

                # open the file
                with open('users.json') as f:
                    data = json.load(f)
                # if the user isn't registered
                if str(coin_member.id) in data['users']:
                    # save the amount of coins from the mentioned user
                    coins = data['users'][str(coin_member.id)]['money']

                    # write the embed
                    coin_embed = discord.Embed(title=coin_member.name + " has " + coins + " coins  💸", colour=discord.Colour(0x29485e))
                    coin_embed.set_thumbnail(url=coin_member.avatar_url)
                    coin_embed.set_author(name="Economybot Coins", icon_url=self.profile_picture)
                    # send the embed
                    await self.channel.send(embed=coin_embed)
                else:
                    await self.not_registered_error_other(str(message.mentions[0].id))

            # if noone got metioned
            else:
                # save the author
                coin_member = message.author

                # open the file and read the data
                with open('users.json') as f:
                    data = json.load(f)
                # if the user isn't registered
                if str(coin_member.id) in data['users']:

                    # save the amount of money
                    coins = data['users'][str(coin_member.id)]['money']

                    # write the embed
                    coin_embed = discord.Embed(title=coin_member.name + " has " + coins + " coins  💸",
                                               colour=discord.Colour(0x29485e))
                    coin_embed.set_thumbnail(url=coin_member.avatar_url)
                    coin_embed.set_author(name="Economybot Coins",
                                          icon_url=self.profile_picture)
                    # send the mebd
                    await self.channel.send(embed=coin_embed)
                else:
                    # if the user isn't registered send the mbed
                    await self.not_registered_error_you(str(coin_member.id))

        # if someone want to register
        elif message.content == economybot_prefix + ' register':
            # save the author
            user = message.author
            # open the file and read the data
            with open('users.json', 'r') as f:
                data = json.load(f)

                # if the user is already registered
                if str(user.id) in data['users']:
                    register_error_embed = discord.Embed(title="You can't register because youre already in 👍",
                                          colour=discord.Colour(0x29485e))
                    register_error_embed.set_author(name="Economybot Register Error",
                                     icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                    await self.channel.send(embed=register_error_embed)
                # if not registered
                else:
                    # add a dict
                    data['users'][str(user.id)] = {'dc_id' : str(user.id), 'money' : '0', "inventory" : {"coconut" : "0", "Bronze Role" : "0"}}

                    # write it into the file
                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data))

                    # welcome the new user
                    registered_embed = discord.Embed(title="Welcome ❤",
                                                    description="<@" + str(message.author.id) + '> you can now use the bot and get money 💸',
                                                    colour=discord.Colour(0x29485e))
                    registered_embed.set_author(name="Economybot Register",
                                               icon_url=self.profile_picture)
                    await self.channel.send(embed=registered_embed)

        elif message.content == economybot_prefix + ' shop':
            await self.item_shop()

        

# start the bot
client = EconomyBot()
client.run(TOKEN)