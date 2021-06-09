'''
# ------------------------------------------------------------------------------------------------------------------------------------
Author: Fynn Westerath
Last Change: 01.06.2021
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

# variables to change
commandbot_prefix: str = '!commandbot'
commandbot_dj_role: int = 849245260382339123
commandbot_invitelink: str = 'https://discord.gg/THISISONLYATEST'

# creates the class for the Election bot
class CommandBot(discord.Client):

    # All commandbot commands
    commands = {
        'info' : 'Get info embed with all commands',
        'help' : 'Sends the help embed with all commands',
        'get bots' : 'Gives back all bots',
        'get dj' : 'Gives you the DJ role for the music bots',
        'invitelink' : 'Sends the invitelink',

        'ip-adress': 'Shows you the ip-adress from the server',

    #     Insert your own commands with description
    }

    # All bots i made witt description
    bots = {
        'commandbot' : 'This bot has little commands like `botprefix help` and gives you infoamtion about all bots.',
        'electionbot' : 'The electionbot can start, end and evaluate an election.',
        'verifybot' : 'With this bot you can send a verify button. With this other member have to verify first.'
    }

    # if teh bot is ready
    async def on_ready(self):
        print('CommandBot: logged in')

    # If someone send a message
    async def on_message(self, message):
        channel = message.channel
        user = message.author

        # Preset commands. I think they are usefull
        if user != client.user:
            # Sends the info embed
            if message.content == commandbot_prefix + ' info':
                # creates the info embed
                info_embed = discord.Embed(title="Here you can get the most information about this bot!",
                                           colour=discord.Colour(0x29485e))

                info_embed.set_author(name="Commandbot Info",
                                      icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

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
                                     value="Type the bot prefix + help, then you get every command you can use. Use `" + commandbot_prefix + " help` for commands",
                                     inline=True)
                info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
                # sends the info embed
                await channel.send(embed=info_embed)

            # Shows all commands of this bot
            if message.content == commandbot_prefix + ' help':
                help_embed = discord.Embed(colour=discord.Colour(0x29485e))
                for command in self.commands:

                    help_embed.add_field(name=command, value=self.commands[command], inline=True)

                await channel.send(embed=help_embed)

            # shows all bot i made and what they do
            if message.content == commandbot_prefix + ' get bots':
                get_bot_embed= discord.Embed(colour=discord.Colour(0x29485e))

                get_bot_embed.set_author(name='Commandbot all bots',
                                         icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                for bot in self.bots:
                    get_bot_embed.add_field(name=bot, value=self.bots[bot], inline=False)

                await channel.send(embed=get_bot_embed)

            # Gives the user the DJ role for music bots
            if message.content == commandbot_prefix + ' get dj':
                dj_role = discord.utils.get(user.guild.roles, id=commandbot_dj_role)
                await user.add_roles(dj_role)

            # Sends the invitelink of this dc
            if message.content == commandbot_prefix + ' invitelink':
                await channel.send(commandbot_invitelink)

            # Here you can insert youre own commands ...

            # ... like this
            if message.content == commandbot_prefix + ' ip-adress':
                await channel.send('IP adress: REPLACEWITHIP')






client = CommandBot()
client.run(TOKEN)