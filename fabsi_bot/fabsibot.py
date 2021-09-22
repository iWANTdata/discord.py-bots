import discord
from discord import Member
from discord import message
from discord.ext import commands
import discord.utils
import asyncio
import json

with open("properties.json") as f:
    data = json.load(f)

TOKEN = data["properties"]["token"]
PREFIX = data["properties"]["prefix"]

discord_link = data["properties"]["discord_link"]

intents = discord.Intents()
intents.guilds = True
intents.members = True
intents.emojis = True
intents.messages = True
intents.reactions = True
intents.dm_messages = True



client = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)

# Functions ---------------------------------------------------------------------------

async def status_task():
    messages = data["properties"]["status"]["messages"]
    time = data["properties"]["status"]["time"]    
    while True:
        for x in range(len(messages)):
            await client.change_presence(activity=discord.Game(name=messages[x]))
            await asyncio.sleep(time)


async def check_permissions(command, user:Member, channel):
    command_perm_list = data["properties"]["commands"][str(command)]["permissions"]
    user_allowed = False
    for perm in command_perm_list:
        for role in user.roles:
            if str(perm) == str(role.name):
                user_allowed: bool = True
    if user_allowed == True:
        return True
    else:
        msg = await channel.send("⛔Permission Denied")
        await asyncio.sleep(3)
        await msg.delete()
        return False

async def send_error(error, channel):
    msg = await channel.send("⛔Error: %s" % error)
    await asyncio.sleep(5)
    await msg.delete()


# Events ---------------------------------------------------------------------------

@client.event
async def on_ready():
    print("FabsiBot: logged in")
    client.loop.create_task(status_task())

@client.event
async def on_member_join(member):
    channel_id = int(data["properties"]["events"]["on_member_join"]["welcome_channel"])
    channel = await client.fetch_channel(channel_id)
    rule_channel = await client.fetch_channel(data["properties"]["events"]["on_member_join"]["rules_channel"])
    info_channel = await client.fetch_channel(data["properties"]["events"]["on_member_join"]["info_channel"])
    await channel.send("Hey <@" + str(member.id) + "> schön dass du auf Fabsi's Server gejoint bis, lies dir bitte die Regeln in <#" + str(rule_channel.id) + "> durch und schau in <#" + str(info_channel.id) + "> für mehr Informationen")



# Moderator ---------------------------------------------------------------------------

@client.command(aliases=data["properties"]["commands"]["clear"]["aliases"])
async def clear(ctx, amount:str):
    channel = ctx.message.channel
    if await check_permissions("clear", ctx.message.author, channel):
        if amount == 'all':
            await channel.purge()
            await send_deleted_msgs("all", channel)
        elif amount:
            try:
                amount = int(amount)
                await channel.purge(limit=amount)
                await send_deleted_msgs(amount, channel)
            except TypeError:
                await send_error("Amount must be a number!", channel)
            except:
                await send_error("Please try this format -> `-clear [amount(number)]`", channel)
    else:
        await ctx.message.delete()


async def send_deleted_msgs(amount, channel):
    msg = await channel.send("🗑Deleted `%s` messages" % amount)
    await asyncio.sleep(2)
    await msg.delete()

# Help Command ---------------------------------------------------------------------------

@client.command(pass_context=True, aliases=list(data["properties"]["commands"]["help"]["aliases"]))
async def help(ctx):
    await send_help_embed(ctx)

async def send_help_embed(ctx):
    help_embed = discord.Embed(title="Hilfe für den %s." % str(client.user.name),
                                    description="Hier werden dir alle Informationen über die verschiedenen Commands die der <@%s> kann, welche Aliasse er hat und wer die Rechte hat den Command zu benutzen." % str(client.user.id),
                                    colour=discord.Colour(0x9013fe))

    for command in data["properties"]["commands"]:
        
        help_embed.add_field(name="-- %s --" %(command),
                                value="*Beschreibung:* %s \n *Aliasse:* %s \n *Rechte:* %s hat/haben Zugriff auf diesen Command." % (data["properties"]["commands"][command]["description"], data["properties"]["commands"][command]["aliases"], data["properties"]["commands"][command]["permissions"]),
                                inline=False)

    await ctx.channel.send(embed=help_embed)

# Commands ---------------------------------------------------------------------------

@client.command()
async def stage(ctx, *, name):
    if await check_permissions("stage", ctx.message.author, ctx.channel):
        category_id = int(data["properties"]["commands"]["stage"]["category_id"])
        category = discord.utils.get(ctx.guild.categories, id=category_id)
        name = "🔴 " + name
        await ctx.guild.create_stage_channel(name, category=category, position=1)
        await ctx.channel.send("Created Stage channel: " + name)
    else:
        await ctx.message.delete()

@client.command()
async def social_media(ctx):
    await ctx.channel.send("comming soon")

client.run(TOKEN)