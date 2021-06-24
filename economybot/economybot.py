"""
# ----------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 14.06.2021
(c) Copyright. Not for commercial use. All rights reserved
GitHub
https://github.com/Fynnyx/discord.py-bots
# ----------------------------------------------------------------------------------------------------------------------
"""


# Imports
import discord
import asyncio
import json
import random


# gets the Token from .env (more infos in README and .env.example)
f = open(".env")
TOKEN = f.read()

# variables to change
economybot_channel: int = 841768678940213270
economybot_guild_id: int = 840237524982956072
economybot_prefix: str = '!economybot'
economybot_role_bank_permission: str = 'Banker'

economybot_role_lvl1 = 855021146889650177
economybot_role_lvl2 = 855081293742080013

inv_items = {"coconut": "0", "banana": "0"}


# creates the class for the Election bot
class EconomyBot(discord.Client):


    # if the bot started
    async def on_ready(self):
        self.profile_picture = client.user.avatar_url
        self.shop_status = 'item'
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

    async def something_went_wrong_add_remove(self):
        add_error_embed = discord.Embed(
                                title="Something went wrong", 
                                description="`" + economybot_prefix + "` add/remove `@member` `amount`",
                                colour=discord.Colour(0x29485e))

        add_error_embed.set_author(
                                name="Economybot Add Error",
                                icon_url=self.profile_picture)

        await self.channel.send(embed=add_error_embed)

    async def something_went_wrong_use(self):
        add_error_embed = discord.Embed(
                                title="Something went wrong", 
                                description="`" + economybot_prefix + "` `use` `item`",
                                colour=discord.Colour(0x29485e))

        add_error_embed.set_author(
                                name="Economybot Add Error",
                                icon_url=self.profile_picture)

        await self.channel.send(embed=add_error_embed)

    async def cant_find_item(self):
        add_error_embed = discord.Embed(
                                title="Cant find this item", 
                                description="Check your spelling and try again",
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
                                     value='Price: ' + data['shop']['ITEMSHOP']['items'][item]['price'] + '  💸\n' + data['shop']['ITEMSHOP']['items'][item]['description'], inline=True)

        try:
            await self.shop_message.delete()
        except:
            print('An Error occurred by deleting the message')

        self.shop_message = await self.channel.send(embed=itemshop_embed)

        await self.shop_message.add_reaction('▶')

    async def upgrade_shop(self):
        with open("shop.json") as f:
            data = json.load(f)

        items_shop = data['shop']['UPGRADESHOP']['items']

        upgradeshop_embed = discord.Embed(title="UPGRADESHOP", description="Buy items and use them later",
                                       colour=discord.Colour(0x29485e))
        upgradeshop_embed.set_author(name="Economybot Shop",
                                  icon_url=self.profile_picture)
        for item in items_shop:
            upgradeshop_embed.add_field(name=data['shop']['UPGRADESHOP']['items'][item]['item_name'],
                                     value='Price: ' + data['shop']['UPGRADESHOP']['items'][item]['price'] + '  💸\n' + data['shop']['UPGRADESHOP']['items'][item]['description'], inline=True)

        try:
            await self.shop_message.delete()
        except:
            print('An Error occurred by deleting the message')

        self.shop_message = await self.channel.send(embed=upgradeshop_embed)

        await self.shop_message.add_reaction('◀')
        await self.shop_message.add_reaction('▶')

    async def random_shop(self):
        with open("shop.json") as f:
            data = json.load(f)

        items_shop = data['shop']['RANDOMSHOP']['items']

        randomshop_embed = discord.Embed(title="RANDOMSHOP", description="Buy items and use them later",
                                       colour=discord.Colour(0x29485e))
        randomshop_embed.set_author(name="Economybot Shop",
                                  icon_url=self.profile_picture)
        for item in items_shop:
            randomshop_embed.add_field(name=data['shop']['RANDOMSHOP']['items'][item]['item_name'],
                                     value='Price: ' + data['shop']['RANDOMSHOP']['items'][item]['price'] + '  💸\n' + data['shop']['RANDOMSHOP']['items'][item]['description'], inline=True)

        try:
            await self.shop_message.delete()
        except:
            print('An Error occurred by deleting the message')

        self.shop_message = await self.channel.send(embed=randomshop_embed)

        await self.shop_message.add_reaction('◀')

    async def add_to_inventory(self, item, user_id):
        with open("users.json") as f:
            data = json.load(f)

        if item in data['users'][str(user_id)]['inventory']:
            item_amount = data['users'][str(user_id)]['inventory'][str(item)]
            item_amount = int(item_amount) + 1

            data['users'][str(user_id)]['inventory'][str(item)] = item_amount

        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

    async def remove_money(self, user, amount):
        # opne the json file
        with open('users.json') as f:
            data = json.load(f)
        # if the recipient is registered
        if str(user) in data['users']:
            # get the money amount from the recipient
            money_recipent_money = data['users'][str(user)]['money']
            # remove the money from the bank acc
            money_amount = int(money_recipent_money) - int(amount)
            # write it into the dict
            data['users'][str(user)]['money'] = str(money_amount)

            # write it into the file
            with open('users.json', 'w') as f:
                f.write(json.dumps(data, indent=2))

            # send what has been removed
            added_embed = discord.Embed(title="Removed " + str(amount) + " coins  💸  from",
                                        description="<@" + str(user) + ">",
                                        colour=discord.Colour(0x29485e))
            added_embed.set_author(name="Economybot Removed Coins",
                                   icon_url=self.profile_picture)

            await self.channel.send(embed=added_embed)

        else:
            await self.not_registered_error_other(str(user))

    async def remove_money_shop(self, user, amount, item):
        user = str(user.id)
        # opne the json file
        with open('users.json') as f:
            data = json.load(f)
        # if the recipient is registered
        if str(user) in data['users']:
            # get the money amount from the recipient
            money_recipent_money = data['users'][str(user)]['money']
            # remove the money from the bank acc
            money_amount = int(money_recipent_money) - int(amount)
            # write it into the dict
            data['users'][str(user)]['money'] = str(money_amount)

            # write it into the file
            with open('users.json', 'w') as f:
                f.write(json.dumps(data, indent=2))

            bought_embed = discord.Embed(title="You bought ",
                                        description="`" + item + "` for " + amount + "   💸",
                                        colour=discord.Colour(0x29485e))
            bought_embed.set_author(name="Economybot Removed Coins",
                                   icon_url=self.profile_picture)

            await self.channel.send(embed=bought_embed)
        else:
            await self.not_registered_error_you(user)

    async def start_work(self, user_id, where):
        with open('users.json', 'r') as f:
                data = json.load(f)

        data['users'][str(user_id)]['is_working'] = "is_working"
        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        amount = random.randint(150, 250)

        data['users'][str(user_id)]['amount'] = str(amount)
        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        if where == "work":
            started_working_embed = discord.Embed(title="You started working",
                                            description="Come back in one hour to earn your reward of " + str(amount) + "   💸",
                                            colour=discord.Colour(0x29485e))
            started_working_embed.set_author(name="Economybot Work",
                                       icon_url=self.profile_picture)
            await self.channel.send(embed=started_working_embed)

        await asyncio.sleep(3600)

        data['users'][str(user_id)]['is_working'] = "is_done"
        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

    async def done_work(self, user_id, where):
        with open('users.json', 'r') as f:
                data = json.load(f)

        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        amount = int(data['users'][str(user_id)]['amount'])
        user_money = int(data['users'][str(user_id)]['money'])

        full_amount = user_money + amount

        data['users'][str(user_id)]['money'] = str(full_amount)

        # write it into the file
        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))

        data['users'][str(user_id)]['is_working'] = "is_ready"
        with open('users.json', 'w') as f:
            f.write(json.dumps(data, indent=2))
        
        if where == 'again':

            done_work_again_embed = discord.Embed(title="You are done with working",
                                            description="You earned " + str(amount) + "   💸 and started again",
                                            colour=discord.Colour(0x29485e))
            done_work_again_embed.set_author(name="Economybot Done Work",
                                       icon_url=self.profile_picture)
            await self.channel.send(embed=done_work_again_embed)

            await self.start_work(str(user_id), "again")    

        elif where == 'claim':
            done_work_claim_embed = discord.Embed(title="You claimed your coins",
                                            description="You earned " + str(amount) + "   💸 \n start again by user `" + economybot_prefix + " work`",
                                            colour=discord.Colour(0x29485e))
            done_work_claim_embed.set_author(name="Economybot Claimed Coins",
                                       icon_url=self.profile_picture)
            await self.channel.send(embed=done_work_claim_embed)
        

    async def on_message(self, message):
        # get the channel where the message was sended
        self.channel = message.channel

        # get the author
        member = message.author

        # if the help command got called
        if message.content == (economybot_prefix + ' help'):
            # create the embed for help
            help_embed = discord.Embed(colour=discord.Colour(0x29485e))

            help_embed.set_author(name="Electionbot Help",
                                  icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

            help_embed.add_field(name="Start working",
                                 value="With `" + economybot_prefix + " work` you can start to work. If you are done with working you claim your coins and start again working.")
            help_embed.add_field(name="Claim coins after work",
                                 value="By tiping `" + economybot_prefix + " work claim` you can end the current election")

            help_embed.add_field(name="❗Banker Role❗", value="Banker has access to extra commands")
            help_embed.add_field(name="Add money",
                                 value="If you use `" + economybot_prefix + " add @mention`. You can add money \n")
            help_embed.add_field(name=":exclamation: Attention :exclamation:",
                                 value="If you voted once you cant delete your vote")
            # sends the embed
            await self.channel.send(embed=help_embed)

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
                                 value='Want to use more bots? Visit https://github.com/Fynnyx/discord.py-bots to get more open source Discord bots.',
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
                                        title="You dont have enough money", description="<@" + str(message.mentions[0].id) + "> you only have " + data['users'][str(money_sender.id)]['money'] + ' 💸',
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
                                        f.write(json.dumps(data, indent=2))

                                    # get the moneyamount from the sender
                                    money_sender_money = data['users'][str(money_sender.id)]['money']
                                    # remove the amount of money from the sender
                                    money_amount = int(money_sender_money) - int(sender_money_amount)
                                    # add it to the dict
                                    data['users'][str(money_sender.id)]['money'] = str(money_amount)

                                    # write it in the file
                                    with open('users.json', 'w') as f:
                                        f.write(json.dumps(data, indent=2))

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
                                    f.write(json.dumps(data, indent=2))

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
                            await self.something_went_wrong_add_remove()
                            break
                    # if th command is not right
                    else:
                        await self.something_went_wrong_add_remove()
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

                            await self.remove_money(message.mentions[0].id ,sender_money_amount)


                        # if the command is false
                        else:
                            await self.something_went_wrong_add_remove()
                            break
                    # if the command is wrong
                    else:
                        await self.something_went_wrong_add_remove()
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
                    data['users'][str(user.id)] = {'dc_id' : str(user.id), 'money' : '0', "is_working" : "is_ready", "amount" : "0", "inventory" : inv_items}

                    # write it into the file
                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data, indent=2))

                    # welcome the new user
                    registered_embed = discord.Embed(title="Welcome ❤",
                                                    description="<@" + str(message.author.id) + '> you can now use the bot and get money 💸',
                                                    colour=discord.Colour(0x29485e))
                    registered_embed.set_author(name="Economybot Register",
                                               icon_url=self.profile_picture)
                    await self.channel.send(embed=registered_embed)

        elif message.content == economybot_prefix + ' shop':
                await self.item_shop()

        elif message.content.startswith(economybot_prefix + ' buy'):
            user = message.author

            buy_message = str(message.content)
            item_message = buy_message.split(' ')
            item = item_message[2]

            with open('shop.json', 'r') as f:
                data = json.load(f)

            if item in data['shop']['ITEMSHOP']['items']:
                if data['shop']['ITEMSHOP']['items'][item]['type'] == 'role':
                    self.lvl1_role = discord.utils.get(member.guild.roles, id=economybot_role_lvl1)
                    # for role in user.roles:
                    if self.lvl1_role in user.roles:
                        has_the_role_embed = discord.Embed(
                            title="You still have this Role",
                            colour=discord.Colour(0x29485e))
                        has_the_role_embed.set_author(
                            name="Economybot Role Error",
                            icon_url=self.profile_picture)
                        await self.channel.send(embed=has_the_role_embed)
                    else:
                        with open('shop.json', 'r') as f:
                            data = json.load(f)

                        amount = data['shop']['ITEMSHOP']['items'][str(item)]['price']

                        await user.add_roles(self.lvl1_role)

                        await self.remove_money_shop(user, amount, item)


                else:
                    await self.add_to_inventory(item, str(message.author.id))

            else:
                print('Cant find this item')

        elif message.content == economybot_prefix + ' inventory':
            user = message.author

            with open('users.json', 'r') as f:
                data = json.load(f)

            inventory = data['users'][str(user.id)]['inventory']

            inventory_embed = discord.Embed(title="Inventory of " + str(user.name),
                                           colour=discord.Colour(0x29485e))
            inventory_embed.set_author(name="Economybot inventory",
                                      icon_url=self.profile_picture)
            for item in inventory:
                inventory_embed.add_field(name=item,
                                         value=data['users'][str(user.id)]['inventory'][item], inline=True)

            await self.channel.send(embed=inventory_embed)

        elif message.content.startswith(economybot_prefix + ' use'):
            channel = message.channel

            user = message.author
            use_message = str(message.content)
            item_message = use_message.split(' ')
            item = item_message[2]

            with open('users.json', 'r') as f:
                data = json.load(f)

            if item in data['users'][str(user.id)]['inventory']:
                if int(data['users'][str(user.id)]['inventory'][item]) > 0:

                    item_amount = int(data['users'][str(user.id)]['inventory'][item])
                    
                    if item == 'coconut':
                        await channel.send('And now you have to open it')
                        await asyncio.sleep(2)
                        await channel.send('Just a Joke. You can it is still open :coconut:')

                    if item == 'banana':
                        await channel.send('enojy your meal <@' + str(user.id) + ">")


                    item_amount = item_amount - 1

                    data['users'][str(user.id)]['inventory'][item] = item_amount

                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data, indent=2))

                else:
                    await self.cant_find_item()
            else:
                await self.something_went_wrong_use()

        elif message.content == economybot_prefix + ' work':
            user = message.author

            with open('users.json', 'r') as f:
                data = json.load(f)

            if str(user.id) in data['users']:

                if data['users'][str(user.id)]['is_working'] == "is_ready":
                    await self.start_work(str(user.id), "work")


                elif data['users'][str(user.id)]['is_working'] == "is_working":

                    still_working_embed = discord.Embed(title="You are still working",
                                                    description="Come back in when you are done with working to earn the reward",
                                                    colour=discord.Colour(0x29485e))
                    still_working_embed.set_author(name="Economybot Work Error",
                                               icon_url=self.profile_picture)
                    await self.channel.send(embed=still_working_embed)

                elif data['users'][str(user.id)]['is_working'] == "is_done":
                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data, indent=2))

                    amount = int(data['users'][str(user.id)]['amount'])
                    user_money = int(data['users'][str(user.id)]['money'])

                    full_amount = user_money + amount

                    data['users'][str(user.id)]['money'] = str(full_amount)

                    # write it into the file
                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data, indent=2))

                    data['users'][str(user.id)]['is_working'] = ""
                    with open('users.json', 'w') as f:
                        f.write(json.dumps(data, indent=2))

                    still_working_embed = discord.Embed(title="You are done with working",
                                                    description="You earned " + str(amount) + "   💸 and started again",
                                                    colour=discord.Colour(0x29485e))
                    still_working_embed.set_author(name="Economybot Work Error",
                                               icon_url=self.profile_picture)
                    await self.channel.send(embed=still_working_embed)

                    await self.start_work(str(user.id), "again")



            else:
                await self.not_registered_error_you(user.id)

        elif message.content == economybot_prefix + ' work claim':
            user = message.author

            with open('users.json', 'r') as f:
                data = json.load(f)

            if data['users'][str(user.id)]['is_working'] == "is_done":
          
                await self.done_work(str(user.id), 'claim')

            else:
                still_working_embed = discord.Embed(title="You are still working",
                                                    description="Come back in when you are done with working to earn the reward",
                                                    colour=discord.Colour(0x29485e))
                still_working_embed.set_author(name="Economybot Work Error",
                                           icon_url=self.profile_picture)
                await self.channel.send(embed=still_working_embed)




    async def on_reaction_add(self, reaction, user):
        if user != client.user:
            if self.shop_status == 'item' and str(reaction) == '▶':
                self.shop_status = 'upgrade'
                await self.upgrade_shop()

            elif self.shop_status == 'upgrade' and str(reaction) == '◀':
                self.shop_status = 'item'
                await self.item_shop()

            elif self.shop_status == 'upgrade' and str(reaction) == '▶':
                self.shop_status = 'random'
                await self.random_shop()

            elif self.shop_status == 'random' and str(reaction) == '◀':
                self.shop_status = 'upgrade'
                await self.upgrade_shop()


        

# start the bot
client = EconomyBot()
client.run(TOKEN)