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

# variables to change
electionbot_channel: int = 840238020509696031
electionbot_prefix: str = '!electionbot'
electionbot_reaction1: str = '👍'
electionbot_reaction2: str = '👎'
electionbot_reaction_end: str = '❌'
electionbot_role: int = 840350620259188736
electionbot_role_end_permission: str = 'Presidents'

# creates the class for the Election bot
class VoteBot(discord.Client):

    # self. variables
    voteInProgress: bool = False

    electionbot_reaction1_user: list = []
    electionbot_reaction2_user: list = []

    # if the bot started
    async def on_ready(self):
        # get the 
        channel = client.get_channel(electionbot_channel)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Fynnyx'))
        print('Electionbot: logged in')

        ## Activate for start signal in dc channel
        # await channel.send("Vote for response receiving less support, get promoted to Coomer!")


    # Function to reset all variables
    def reset(self):
        self.electionbot_reaction1_user = []
        self.electionbot_reaction2_user = []

        self.electionbot_reaction2_user_count = []
        self.electionbot_reaction1_user_count = []

        self.voteInProgress = False

    # Gives back who the winner is
    async def winner(self, reaction1_user, reaction2_user):
        # deletes all duplikates in the list
        reaction1_user = list(dict.fromkeys(reaction1_user))
        reaction2_user = list(dict.fromkeys(reaction2_user))

        # set the _count list for de punlic use in the class
        self.electionbot_reaction1_user_count = reaction1_user
        self.electionbot_reaction2_user_count = reaction2_user

        # Checks who won thw election
        if len(reaction1_user) > len(reaction2_user):
            # gives the role to all loser
            for user in reaction2_user:
                await user.add_roles(self.role)

        # same again ...
        elif len(reaction1_user) < len(reaction2_user):

            for user in reaction1_user:
                await user.add_roles(self.role)


    # if a reaction been added to the election/question 
    async def on_reaction_add(self, reaction, user):
        channel = client.get_channel(electionbot_channel)
        # checks that the user isn't the bot
        if user != client.user:

            # checks wich reaction it is and add the user to the list
            if str(reaction) == electionbot_reaction1:
                self.electionbot_reaction1_user.append(user)

            # checks wich reaction it is and add the user to the list
            elif str(reaction) == electionbot_reaction2:
                self.electionbot_reaction2_user.append(user)

            # cheacks if it was teh end emoji
            elif str(reaction) == electionbot_reaction_end:
                # searcehs for every role
                for role in user.roles:

                    # if the user has the permission_role the election ends
                    if str(role) == electionbot_role_end_permission:
                        self.voteInProgress = False
                        
                        # calls the winner fuction to get the winner of the election
                        await self.winner(self.electionbot_reaction1_user, self.electionbot_reaction2_user)

                        # creates the win_lose embed to print out the winner
                        win_lose_embed = discord.Embed(title="Result of the election", colour=discord.Colour(0x29485e))

                        win_lose_embed.set_author(name="Electionbot Result", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")


                        win_lose_embed.add_field(name=str(len(self.electionbot_reaction1_user_count))+' Vote/s for', value=electionbot_reaction1, inline=True)
                        win_lose_embed.add_field(name=str(len(self.electionbot_reaction2_user_count))+' Vote/s for', value=electionbot_reaction2, inline=True)

                        win_lose_embed.add_field(name='-----------------', value="Election ended :no_entry:", inline=False)

                        # prints out the embed
                        await channel.send(embed=win_lose_embed)
                        # resets the hole variables
                        self.reset()

    # startes when a message is posted
    async def on_message(self, message):
        channel = client.get_channel(electionbot_channel)

        member = message.author
        # saves all roles of the server in self.role
        self.role = discord.utils.get(member.guild.roles, id=electionbot_role)
        # checks if the message starts with the botprefix 
        if message.content.startswith(electionbot_prefix):
            
            # if the message is botprefix + help
            if message.content == electionbot_prefix + ' help':
                
                # create the embed for help
                help_embed = discord.Embed(colour=discord.Colour(0x29485e))

                help_embed.set_author(name="Electionbot Help", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                help_embed.add_field(name="Start an election", value="With `" + electionbot_prefix + " [question]?` you can start a election.")
                help_embed.add_field(name="End an election", value="By tiping `" + electionbot_prefix + " end` you can end the current election")
                help_embed.add_field(name="Role", value="All member who lost the election will get the `elction_role`\n")
                help_embed.add_field(name=":exclamation: Attention :exclamation:", value="If you voted once you cant delete your vote")
                # sends the embed
                await channel.send(embed=help_embed)

            elif message.content == electionbot_prefix + ' info':
                # creates the info embed
                info_embed = discord.Embed(title="Here you can get the most information about this bot!", colour=discord.Colour(0x29485e))
                
                info_embed.set_author(name="Electionbot Info", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")

                info_embed.add_field(name="General ❕:", value="In general this bot is a private project. I made the bot in my freetime.", inline=True)
                info_embed.add_field(name="Personalize ✏:", value="You can personalize this bot by download the code from gitlab and run it by yourself.", inline=True)
                info_embed.add_field(name="Help Command 📜:", value="The bot prefix is `" + electionbot_prefix +"`. You will use this in front off all other  commands. More infos you'll get by using `" + electionbot_prefix +" help`.", inline=True)
                info_embed.add_field(name="Everything done? ", value="Have fun ❤", inline=False)
                # sends the info embed
                await channel.send(embed=info_embed)

            elif self.voteInProgress == False:
                # checks if the message is a question
                if message.content[-1] == '?':
                    # create a new embed if a election has started
                    start_embed = discord.Embed(title="A new election has started", colour=discord.Colour(0x29485e), description="You can vote by using the reactions above\n\nHave fun :exclamation:")

                    start_embed.set_author(name="Electionbot Start", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")
                    #  sends the embed
                    await channel.send(embed=start_embed)
                    # reset all variables
                    self.reset()

                    # adds the reactions to the election/question (doesnt count for the election)
                    await message.add_reaction(emoji = electionbot_reaction1)
                    await message.add_reaction(emoji = electionbot_reaction2)
                    await message.add_reaction(emoji = electionbot_reaction_end)

                    # changes the status
                    self.voteInProgress = True
                
                # if the message isnt a question
                if message.content[-1] != '?':
                    await channel.send('This is no question :question:')

                # if the message calls the end of a never started election
                if message.content == electionbot_prefix + ' end':
                    await channel.send('You have to start an election first')
            
            # if a election is running
            elif self.voteInProgress == True:
                
                # if the end of an election got called
                if message.content == electionbot_prefix + ' end':
                    user = message.author
                    # checks if the user has the permission to and a election
                    for role in user.roles:
                        if str(role) == electionbot_role_end_permission:

                            # if the user has the permission the code below will get called
                            self.voteInProgress = False

                            await self.winner(self.electionbot_reaction1_user, self.electionbot_reaction2_user)

                            win_lose_embed = discord.Embed(title="Result of the election", colour=discord.Colour(0x29485e))

                            win_lose_embed.set_author(name="Electionbot result", icon_url="https://cdn.discordapp.com/app-icons/840235732533510154/8424444588ad2b5a1a79252a4556c532.png?size=64")


                            win_lose_embed.add_field(name=str(len(self.electionbot_reaction1_user_count))+' Vote/s for', value=electionbot_reaction1, inline=True)
                            win_lose_embed.add_field(name=str(len(self.electionbot_reaction2_user_count))+' Vote/s for', value=electionbot_reaction2, inline=True)

                            win_lose_embed.add_field(name='-----------------', value="Election ended :no_entry:", inline=False)


                            await channel.send(embed=win_lose_embed)

                            self.reset()
                        # if the user doesnt have the permission
                        else:
                             await channel.send('You have no permission to end an election :no_entry:')
                # if a new election want to get started but an election is still in Progress
                if message.content[-1] == '?':
                    await channel.send('If you want to start a new election, stop the current election first')

# start the bot
client = VoteBot()
client.run(TOKEN)
