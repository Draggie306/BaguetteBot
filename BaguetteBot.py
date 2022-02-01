DraggieBot_version = "v1.19a"

print("Importing all modules...\n")
import      discord
from        discord import emoji
from        discord.flags import Intents
from        discord_slash import SlashCommand, SlashContext
from        discord_slash.dpy_overrides import send_message
from        discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from        discord_slash.utils.manage_commands import create_option, create_choice
from        discord import Embed
from        discord.ext import commands   
from        discord import ext
from        discord.errors import ClientException, Forbidden, NotFound #       CMD Prequisite: py -3 -m pip install -U discord.py
from        dotenv import load_dotenv #                             CMD Prequisite: py -3 -m pip install -U python-dotenv
import      os#                                                     PIP:            python -m ensurepip  
import      os.path
from        requests import api
from        requests import auth#                                                UPDATE PIP:     python -m pip install --upgrade pip
import      youtube_dl
from        youtube_search import YoutubeSearch
import      time
import      random 
import      sys
from        datetime import datetime
import      requests
from        requests import get
from        json import loads
from        discord.ext.commands import bot
import      asyncio
from        pathlib import Path
import      uuid
from        requests.auth import HTTPBasicAuth
from        gc import enable
import      json
import      subprocess
from        mcstatus import MinecraftServer
import		kahoot
import      asyncio
import      functools
import      itertools
import      math
import      random
from        async_timeout import timeout
from        discord.ext import commands
import      discord
from        discord_slash import SlashCommand, SlashContext
import      uuid
from        discord_slash.utils import *
from        discord_slash import *
import      difflib
import      termcolor
from        termcolor import cprint
from        ctypes import WinError
from        attr import attr
from        discord_slash.context import MenuContext
from        discord_slash.model import ContextMenuType
from        instadm import InstaDM
import      threading

"""   
    To do:
        Replace ALL dirs/msgs/vars with f strings so it looks cleaner
"""

youtube_dl.utils.bug_reports_message = lambda: ''

print("Done!\nInitialising Bot...")

sys.setrecursionlimit(99999999)

global voiceVolume, upvote, downvote
global draggie
global start_time
voiceVolume = 0.3
start_time = time.time()

PYTHONIOENCODING="utf-8"

client = discord.Client()
intents = discord.Intents().all()

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents)

slash = SlashCommand(client, sync_commands=True)

###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

print("Done!\nSlash commands initialising...")

tester_guilds = [384403250172133387, 759861456300015657, 833773314756968489, 921088076011425892] # Server IDs where I'm an admin so can change stuff before it reaches other servers
brigaders = [759861456300015657]

@slash.slash(name="debug", guild_ids=tester_guilds, description="Spits out debug info for debugging bugs")
async def test(ctx):
    nolwenniumUserDir = f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\{ctx.author.id}.txt"
    my_file = Path(nolwenniumUserDir)
    if not my_file.is_file():
        nolwenniumBal = "null"
        nolly = nolwenniumBal
    else:
        f = open(nolwenniumUserDir, 'r')
        nolwenniumBal = f.read()
        f.close()
        nolly = str(nolwenniumBal) + str(" <:NolwenniumCoin:846464419503931443>")
    x = False
    Admin = discord.utils.get(ctx.guild.roles, name="Admin")
    if Admin in ctx.author.roles:
        x = True
    shard_id = ctx.guild.shard_id
    await ctx.send(f"Debug info: S: {ctx.guild.id} in C: {ctx.channel.id} - A: {ctx.author.id}, hA: {x}, Nolwennium: {nolly} + l:{client.latency}s, iID: {uuid.uuid4()}, sO: {ctx.guild.owner.id}, bbPremium = False, usesEmilite: False, sID: {shard_id}")#\n<a:HmmThinkSpin:857307788572098610> *Unsure what this is?* These are just guild/channel ids, send this to Draggie#3060 if you have issues")

@slash.slash(name="Ping", description="Shows bot latency to Discord's servers, using Discord WebSocket protocol.")
async def _ping(ctx):
    print("ping'd")
    if round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="PING", description=f"Message delay is is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 150:
        embed=discord.Embed(title="PING", description=f"Message delay is is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 150:
        embed=discord.Embed(title="PING", description=f"Message delay is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f"OOF! Message delay is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a", encoding="utf8")
    f.write((str ("\nCOMMAND RAN -> '.ping' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

@slash.slash(name="whitelist",
            description="MC Server Whitelist Command.",
            guild_ids = brigaders,
            options=[create_option(
                    name="add",
                    description="Add a username to the whitelist.",
                    option_type=3,
                    required=True)])
async def _whitelist(ctx, add:str):
    message=(f"whitelist add {add}")
    console = client.get_channel(912429726562418698)
    await console.send(message)
    await ctx.send(f"**{add}** has been added to the whitelist. Please rejoin the Minecraft server!")

@slash.slash(name="cuisine",
            description="Cuisine.",
            guild_ids = brigaders,
            options=[create_option(
                    name="country",
                    description="Choose country.",
                    option_type=3,
                    required=True,
                    choices=[
                        create_choice(name="France",value="france"),
                        create_choice(name="Italy", value="italy")])])
async def _cuisine(ctx, country:str):
    await ctx.send(f"You chose {country}.")


@slash.slash(name="rgb", description="Updates rgb advisor colour.", guild_ids = brigaders)
async def _rgb(ctx):
    rgb = discord.utils.get(ctx.guild.roles, name="RGB Advisor")
    admin = discord.utils.get(ctx.guild.roles, name="Admin")
    mod = discord.utils.get(ctx.guild.roles, name="Mod")
    print(f"RGB ran by {ctx.author.name}")
    if rgb or mod or admin in ctx.author.roles:
        guild=ctx.guild
        colour = random.randint(1000,16777215)
        colour = discord.Color(colour)
        role = discord.utils.get(guild.roles, name="RGB Advisor")
        await role.edit(server=guild, role=role, colour=colour)
        await ctx.send(f"RGB Advisor updated to {colour}")
    else:
        await ctx.send("no")
    
@slash.slash(name="components",
    description="Enables/disables specified BaguetteBot components.",
    guild_ids=tester_guilds,
    options=[create_option(
            name="enable",
            description="Select components to enable",
            option_type=3,
            required=True,
            choices=[create_choice(name="Logging",value="log"),
                    create_choice(name="Role Grant DMs", value="rolegrants"),
                    create_choice(name="DMs", value="dms"),
                    create_choice(name="Redacted Messages", value="redactions"),
                    create_choice(name="-", value="nothing")]),
            create_option(
            name="disable",
            description="Select components to disable",
            option_type=3,
            required=True,
            choices=[create_choice(name="Logging",value="log"),
                    create_choice(name="Role Grant DMs", value="rolegrants"),
                    create_choice(name="DMs", value="dms"),
                    create_choice(name="Redacted Messages", value="redactions"),
                    create_choice(name="-", value="nothing")
                    ])])
async def _components(ctx, enable:str, disable:str):
    print(enable, disable)
    print("Someone ran log command")
    Admin = discord.utils.get(ctx.guild.roles, name="Admin")
    if Admin in ctx.author.roles:
        if "log" in enable:
            try:
                LoggingChannel = discord.utils.get(ctx.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                print(f"Logging Channel {LoggingChannel}")
                if LoggingChannel is None:
                    print("Creating channel")
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False)
                    }
                    await ctx.guild.create_text_channel('event-log-baguette', overwrites=overwrites)
                LoggingChannel = discord.utils.get(ctx.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await LoggingChannel.send("**Logging enabled**")

                sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{ctx.guild.id}\\sendMessages.txt")
                x = open(sendLogsDir, "a", encoding='utf-8')
                x.close()
                await ctx.send(f"Enabled logging for server {ctx.guild.id}")
                
            except Exception as e:
                e = (str(e))
                if "forbidden" in e.lower():
                    await ctx.send(f"An error occured: `{e}` - ensure the bot has sufficient permissions!")
                
                if "winerror" in e.lower():
                    print(e)
                    await ctx.send(f"Option name: `'switch'` already set to value `'Enabled'`!")
            
        if "log" in disable:
            try:
                sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{ctx.guild.id}\\sendMessages.txt")
                os.remove(sendLogsDir)
                await ctx.send(f"Disabled sending logs for server {ctx.guild.id}. The following messages in the log channel will not be sent:\nMessages in the log channel when a user joins, types, changes status, activity, username\nMessages deleted\nDMs to users welcoming them when they join.\n")
            except Exception as e:
                await ctx.send(f"Option name: `'switch'` already set to value `'Disabled'`!")

        if "rolegrants" in enable:
            await ctx.send("Role Grant Enabled Notification Dialogue")
        if "rolegrants" in disable:
            await ctx.send("Role Grant Disabled Notification Dialogue")
            #delete file here

        if "redactions" in enable:
            sendRedactions = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{ctx.guild.id}\\sendRedactions.txt")
            x = open(sendRedactions, "a", encoding='utf-8')
            x.close()
            await ctx.send("Redacted messages have been enabled. Announcements showing a message's deletion will be sent in DMs and broadcasted in the channel.")
        if "redactions" in disable:
            try:
                sendRedactions = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{ctx.guild.id}\\sendRedactions.txt")
                os.remove(sendRedactions)
                x = "enabled" if os.path.isfile(f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{ctx.guild.id}\\sendMessages.txt") else "disabled"
                await ctx.send(f"Redacted messages have been disabled. Messages will not be sent in the channel or to DMs. Logging is {x}.")
            except Exception:
                await ctx.send("Cannot perform that function. `sendRedactions` is `disabled`")
        if "nothing" in enable and disable:
            await ctx.send("Nothing was changed.")
    else:
        await ctx.send("You are not admin, or do not have Admin as an assigned role")

@slash.slash(name="SelectClass",
    description="Select your classes in school.",
    guild_ids = tester_guilds,
    options=[create_option(
            name="name",
            description="Select a class.",
            option_type=3,
            required=True,
            choices=[create_choice(name="11Mat-A1",value="11A1 - Maths"),
                    create_choice(name="11Mat-A2", value="11A2 - Maths"),
                    create_choice(name="11Mat-A3", value="11A3 - Maths"),
                    create_choice(name="11Mat-B1", value="11B1 - Maths"),
                    create_choice(name="11Mat-B2", value="11B2 - Maths"),
                    create_choice(name="11Mat-B3", value="11B3 - Maths"),
                    create_choice(name="11Fre-R", value="11R - French"),
                    create_choice(name="11Fre-S", value="11S - French"),
                    create_choice(name="11Sci-A1", value="11A1 - Science"),
                    create_choice(name="11Sci-A2", value="11A2 - Science"),
                    create_choice(name="11Cmp-S", value="11S - Computing"),
                    create_choice(name="11Geo-P", value="11P - Geography"),
                    create_choice(name="11Geo-P", value="11R - Geography")
                    ])])

async def _SelectClass(ctx, name: str):
    await ctx.defer()
    if name == name:
        #await ctx.send(f"Read as {name}, you are {ctx}")
        try:
            classRole = discord.utils.get(ctx.guild.roles, name=f"{name}")
            if classRole in ctx.author.roles:
                await ctx.author.remove_roles(classRole)
                await ctx.send(f"You've been removed from **{name}**")
                return

            await ctx.author.add_roles(classRole)
            await ctx.send(f"You have been added to class **{name}**.")
        except:
            print("\nClass selected doesn't exist!\n")
            await ctx.guild.create_role(name=f"{name}")
            classRole = discord.utils.get(ctx.guild.roles, name=f"{name}")
            await ctx.author.add_roles(classRole)
            await ctx.send(f"You have been added to class **{name}**.")
            print(f"{ctx.author} You have been added to class **{name}**.")
    else:
        await ctx.send("Invalid Class Name")

@slash.slash(name="nsfw",
            description="haha yes.",
            guild_ids = tester_guilds,
            options=[create_option(
                    name="character",
                    description="Select character.",
                    option_type=3,
                    required=True,
                    choices=[create_choice(name="Wattson",value="Wattson"),
                            create_choice(name="Chun-Li", value="Chun-Li")])]
                            )
async def nsfw(ctx, character: str):
    global debugMode
    global amount
    global currentAmount
    amount = 0
    currentAmount = amount + 0
    #await ctx.message.delete()

    async def beanery():
        if character == "Wattson":
            randomiser = random.randint(1,290)
            await ctx.send(file=discord.File(f"D:\\BaguetteBot\\MaximumWattage\\wattson ({randomiser}).png", filename="SPOILER_wattson{randomiser}.png"))
        if character == "Chun-Li":
            await ctx.send("Omg you are so down bad 😂😂😂😂")
    
    await beanery()

@slash.slash(name="revision",
            description="Get a random exam question from the chosen subject and topic.",
            guild_ids = tester_guilds,
            options=[create_option(
                    name="subject",
                    description="Select a subject.",
                    option_type=3,
                    required=True,
                    choices=[create_choice(name="English",value="English"),
                            create_choice(name="Maths", value="Maths"),
                            create_choice(name="Science: Biology", value="Biology"),
                            create_choice(name="Science: Chemistry", value="Chemistry"),
                            create_choice(name="Science: Physics", value="Physics"),
                            create_choice(name="Computer Science", value="CmpSci")
                            ])])
async def _revision(ctx, subject: str):
    if subject == "English":
        await ctx.send("English selected")
    if subject == "Maths":
        await ctx.send("Maths selected")
    else:
        await ctx.send("This feature is not out yet")

@slash.slash(name="CodeSearch",
            description="Search the bot's code for a term.",
            guild_ids = tester_guilds,
            options=[create_option(
                    name="term",
                    description="Type in a term to search for. Returns an integer value.",
                    option_type=3,
                    required=True)])
async def _CodeSearch(ctx, term: str):
    await ctx.defer()
    message = term
    searchTerm = message.lower()
    file=open(((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\GitHub\\BaguetteBot\\BaguetteBot.py"))),encoding="UTF-8").read().lower()
    num_chars = sum(1 for line in file)
    num_lines = sum(1 for line in open ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\GitHub\\BaguetteBot\\BaguetteBot.py", encoding='utf-8'))

    count=file.count(searchTerm)
    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{searchTerm}**' in code:", value=f"{count}", inline=False)
    embed.set_footer(text=((str (f"Searching {num_chars} characters in {num_lines} lines of code. Requested by {ctx.author}"))))
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write((str (f"\nSLASH COMMAND RAN -> '/CodeSearch' ran by {ctx.author} at {str (datetime.now())}")))
    f.close()


###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

DisabledComponents = "Unknown"
EnabledComponents = "Unknown"

GlobalLogDir=("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\GlobalLog.txt")

""" BULK READ JSONS so it doesn't have to read the file every time a message is sent
    people = nolTighe (p1, g, b, T), oliver, sam (g), jack (r, g), joe (g), charlie (g), haydn, maisy, flo (a), ish, maya, boris (gl), josephTighe (p13, g, c, T)
    "g = grouped", "r = remade", "a = affiliated", "gl = global" 
"""

with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\NollyMention.json", "r", encoding="utf8") as file:
    nollyWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\OliverMention.json", "r", encoding="utf8") as file:
    oliverWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\SamMention.json", "r", encoding="utf8") as file:
    samWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\JackMention.json", "r", encoding="utf8") as file:
    jackWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\JoeMention.json", "r", encoding="utf8") as file:
    joeWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\HaydnMention.json", "r", encoding="utf8") as file:
    haydnWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\MaisyMention.json", "r", encoding="utf8") as file:
    maisyWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\BenMention.json", "r", encoding="utf8") as file:
    benWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\FloMention.json", "r", encoding="utf8") as file:
    floWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\IshMention.json", "r", encoding="utf8") as file:
    ishWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\BorisMention.json", "r", encoding="utf8") as file:
    borisWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\MayaMention.json", "r", encoding="utf8") as file:
    mayaWords = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\JosephTigheMention.json", "r", encoding="utf8") as file:
    josephTighe = loads(file.read())
with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\JSONs\\CharlieMention.json", "r", encoding="utf8") as file:
    charlieSewards = loads(file.read())
with open("D:\\BaguetteBot\\JSONs\\names.json", "r", encoding="utf8") as file:
    protectedNames = loads(file.read())

@client.event
async def on_ready():
    print(f'\n\n\n\nLogged in as {client.user} - {(datetime.now())}')
    global ready_start_time
    ready_start_time = time.time()

    channel = client.get_channel(838107252115374151)
    await channel.send((str ("Online at **")) + (str (datetime.now()) + (str ("**"))))

    #channel = client.get_channel(759861456761258045)
    #await channel.send("Baguette")
    #print("Message sent in #general, please check.")

    f = open(GlobalLogDir, "a")
    f.write((str ("\n\nREADY at ")) + (str (datetime.now())))
    f.write(' - Logged in as {0.user}'.format(client))
    f.close()
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members")))
    global draggie, general, console, upvote, downvote
    draggie = client.get_user(382784106984898560)
    general = client.get_channel(759861456761258045)
    console = client.get_channel(912429726562418698)
    guild = client.get_guild(759861456300015657)
    upvote = client.get_emoji(803578918488768552)
    downvote = client.get_emoji(803578918464258068)
    colour = random.randint(1000,16777215)
    colour = discord.Color(colour)
    role = discord.utils.get(guild.roles, name="RGB Advisor")
    await role.edit(server=guild, role=role, colour=colour)
    
@client.event
async def on_member_join(member):
    sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{member.guild.id}\\sendMessages.txt")
    if member.guild.id == 759861456300015657:
        await member.send(f"Hello! Welcome to Baguette Brigaders. If you joined from the vanity link, welcome! Please verify yourself. Also, add me to your server! >> https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=8&scope=bot%20applications.commands. (for what I do, click: https://www.ibaguette.com/p/bots.html)")
        print("Welcomed user")
        await draggie.send(f"Welcomed user {member}")
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members")))
    #if os.path.isfile(sendLogsDir):
    #    await member.send(f"Welcome to {member.guild.name}")
    #    channel = discord.utils.get(member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
    #    await channel.send(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{member.guild.id}\\sendMessages.txt")
    if os.path.isfile(sendLogsDir):
        try:
            channel = discord.utils.get(member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
            await channel.send(f"{member} has left the server.")
        except Forbidden:
            await draggie.send(f"Removed from server {member.guild.name} / {member.guild.id}")
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members")))
    
@client.event
async def on_raw_reaction_add(payload=None):
    if payload.guild_id == 759861456300015657:#     Must, while reaction roles are not available for all servers.
        msgID = 835227251695288391
        msgRandomId = 931577920512725083
        vaccinatedID = 895386703144034364
        smp2ID = 912012054414630973
        birthdayID = 892114380005715978
        guild = discord.utils.get(client.guilds, name='Baguette Brigaders')
        roleAllRandoms = discord.utils.get(guild.roles, id=930186230442905620)
        roleMember = discord.utils.get(guild.roles, name='Member')
        roleVaccinated = discord.utils.get(guild.roles, name='Vaccinated ✅')
        roleUnverified = discord.utils.get(guild.roles, name='Unverified')
        roleSMP2 = discord.utils.get(guild.roles, name='SMP Season 2')
        roleNew = discord.utils.get(guild.roles, name='New Baguette')
        robloxDev = discord.utils.get(guild.roles, name="Roblox Developer")
        LoggingChannel = discord.utils.get(payload.member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

        if payload is not None:
            if payload.channel_id == 809112184902778890:
                if payload.emoji.name == "downvote":
                    channel = client.get_channel(809112184902778890)
                    message = await channel.fetch_message(payload.message_id)
                    reaction = discord.utils.get(message.reactions, emoji=payload.emoji)
                    count = reaction.count
                    if count > 3:
                        await channel.send(f"{message.author.mention}'s 'epic' meme has been removed.")
                        await message.delete()

        if payload is not None:
            if payload.message_id == birthdayID:
                await payload.member.send("You are too late to claim the birthday role, sorry. More exclusive roles will be given in the future!")

        if payload is not None:
            if payload.message_id == smp2ID:
                await payload.member.add_roles(roleSMP2)
                print(f"Added role to {roleMember.name}")
                await payload.member.send(f"{payload.member.mention}, you've been granted SMP Season 2 role in Baguette Brigaders! Enjoy your time on the server.")
                print(f"Sent DM to {payload.member.name}")

        if payload is not None:
            if payload.message_id == 936320104193474630:
                print(f"Sent Roblox Message message to {payload.member}")
                await payload.member.add_roles(robloxDev)
                await payload.member.send(f"Welcome to the roblox team, {payload.member.name}.")
                channel = client.get_channel(936317698772697118)
                await channel.send(f"Welcome to the team, {payload.member.mention}!")
            
        if payload is not None:
            if payload.message_id == msgRandomId:#     
                channel = client.get_channel(930489645014331442)
                authorName = (str (payload.member.name))
                authorName = (authorName.lower())
                #for word in protectedNames:#            Check protected name list.
                #    if word in authorName:
                #        await payload.member.send(f"Sorry {payload.member.mention} your account has been flagged as [Protected username], please send proof of identity in <#842046293504819200>.")
                #        return
                if roleAllRandoms not in payload.member.roles:
                    await payload.member.add_roles(roleAllRandoms)
                    await payload.member.send(f"Welcome, {payload.member.mention}! You have been verified! Maybe check out <#930488896838586448> now?")
                    print(f"Sent message to {payload.member}")     
                    await LoggingChannel.send((str (payload.member)) + (str (" has been verified.")))
                    await payload.member.remove_roles(roleUnverified)
                else:
                    print(f"{payload.member.name} already has Members role")

        if payload is not None:
            if payload.message_id == 931586778245247018:
                authorName = (str (payload.member.name))
                authorName = (authorName.lower())
                choices = ["OK, you'll no longer see the other side.", "No longer seeing the other side. Enjoy your time on this side!", "Who likes the other side anyway, this side is better!"]
                if roleAllRandoms not in payload.member.roles:
                    await payload.member.add_roles(roleAllRandoms)
                    await LoggingChannel.send((str (payload.member)) + (str (" has been allowed access to the other side.")))
                else:
                    print(f"{payload.member.name} already has Members role, removing it.")
                    await payload.member.remove_roles(roleAllRandoms)
                    await payload.member.send(f"{random.choice(choices)}")

        if payload is not None:
            if payload.message_id == msgID:#                VERIFICATION MESSAGE ONLY
                if str(payload.emoji) == "✅":
                    channel = client.get_channel(835200388965728276)
                    authorName = (str (payload.member.name))
                    authorName = (authorName.lower())
                    for word in protectedNames:#            Check protected name list.
                        if word in authorName:
                            await channel.send(f"Sorry {payload.member.mention} your account has been flagged as [Protected username], please send proof of identity in <#842046293504819200>.")
                            await asyncio.sleep(8)
                            await channel.purge(limit=1)
                            return

                    #await draggie.send(f"Attempting to ban user {payload.member.name}...")
                    #await payload.member.ban(reason="Banned while i fix this code.")
                    #await draggie.send(f"Banned user {payload.member.name} ({payload.member.mention})")
                    #await general.send(f"Banned user {payload.member.name} ({payload.member.mention})")
                    #return
                    #await payload.member.add_roles(roleMember)
                    #await payload.member.add_roles(roleNew)
                    #await channel.send((str ("Welcome, ")) + (str (payload.member.mention)) + (str ("! You have been verified! Maybe check out <#759861456761258045> now?")))
                    #print("Sent message")
                
                    #await LoggingChannel.send((str (payload.member)) + (str (" has been verified.")))
                    #await payload.member.remove_roles(roleUnverified)
                    #await asyncio.sleep(5)
                    #await channel.purge(limit=1)
                    #print("And it's gone in", channel)

        if payload is not None:
            if payload.message_id == vaccinatedID:
                if str(payload.emoji) == "✅":
                    await payload.member.add_roles(roleVaccinated)
                    await LoggingChannel.send((str (payload.member)) + (str (" has been granted vaccination status.")))

        
        #if os.path.isfile(f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{message.guild.id}\\sendMessages.txt"):
        #    x = 1
    if payload.guild_id == 384403250172133387:#     Must, while reaction roles are not available for all servers.
        if payload.message_id == 907318418712170538:
            channel = client.get_channel(907318241498656850)


async def on_guild_remove(guild):
    print(f"Removed from guild {guild}")
    channel = client.get_channel(838107252115374151)  # notification channel
    await channel.send(f"DEV MODE: removed from guild {guild}")

#   Client evenys

@client.event
async def on_message_delete(message):
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    sendRedactionsInChannel = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{message.guild.id}\\sendRedactions.txt")
    print(f"Message deleted: '{message.content}' channel: '{message.channel.name}' server: '{message.guild.name}'")
    if message.channel.id == 825470734453047297:
        await message.channel.send(f"Stop deleting your messages in here, we're literally adding numbers, {message.author.mention}. *Their message was {message.content}*")
        return 
    if os.path.isfile(sendRedactionsInChannel):
        if message.author.id != 792850689533542420:
            await message.channel.send(f"{message.author.mention}'s message has been *redacted*.")
            user = client.get_user(int(message.author.id))
            await user.send(f"Your message, '`{message.content}`', has been ***redacted***.")
    if os.path.isfile(f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{message.guild.id}\\sendMessages.txt"):
        LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        embed = discord.Embed(title=f"User's message deleted", colour=0xFF0000)
        embed.add_field(name="User", value=message.author.mention)
        embed.add_field(name='Channel', value=f"<#{message.channel.id}>")
        embed.add_field(name='Time', value=tighem)
        embed.add_field(name='Message', value=message.content, inline=False)
        await LoggingChannel.send(embed=embed)

@client.command(pass_context=True)
async def discorddm(ctx):
    message = ctx.message.content
    x = message.split()
    sp1 = message.split(' ', 2)[-1]
    userID = (x[1])
    user = client.get_user(int (userID))
    await user.send(f"{sp1}")
    await draggie.send(f"{sp1}")

def InstaDMSend(ctx):
    message = ctx.message.content
    x = message.split()
    user = (x[1])
    msg = message.split(' ', 2)[-1]

    with open("D:\\BaguetteBot\\TextValues\\password.txt", encoding="utf-8") as f:
        password = f.read()

    try:
        if __name__ == '__main__':
            insta = InstaDM(username='draggie306', password=password, headless=False)
            insta.sendMessage(user=f'{user}', message=f'{msg}')
    except Exception as e:
        print(f"An unexpected error occured: {e}")

@client.command(pass_context=True)
async def dm(ctx):
    message = ctx.message.content
    x = message.split()
    user = (x[1])
    msg = message.split(' ', 2)[-1]
    if ctx.message.author.id == 382784106984898560:
        accounts = ("`draggiefn`, `nolwenntighe`, `charli3_s3w`, `xxnova_smokexx`, `ismail_ahmed_06_2`, `sam_partridge._`, `b3nny_b0oze`, `_reuben_72`, `therealwillbyrne`, `unicornkid_72`, `riaz_bari_`, `drevilo.19`, `some_one_acctually`, `harrigeorg`")
        if user not in accounts:
            await ctx.send(f"Sorry! I can only send DMs to the following accounts: {accounts}")
            return

        await ctx.send(f"OK! Trying to send **{msg}** to Instagram user @**{user}**. This may take over 30 seconds.")
        t1 = threading.Thread(target=InstaDMSend, args=[ctx])
        t1.start()
    else:
        await ctx.send(f"you don't have permission to message {user} ")

@client.event
async def on_message_edit(before, after):
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{after.guild.id}\\sendMessages.txt")
    print(f"Message updated >>> '{before.content}' changed to '{after.content}' in {after.guild.name}/{after.guild.name}")

    LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
    if os.path.isfile(sendLogsDir):
        embed = discord.Embed(title=f"Message edited")
        embed.add_field(name='User', value=after.author.mention)
        embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
        embed.add_field(name='Time', value=tighem)
        if before.content == '' and after.content == '':
            embed.add_field(name= "Data", value='<attachment sent>', inline=False)
            await LoggingChannel.send(embed=embed)
            return
        embed.add_field(name= "Message before", value=before.content, inline=False)
        embed.add_field(name= "Message after", value=after.content, inline=False)
        await LoggingChannel.send(embed=embed)
        return
    if before == after:
        embed = discord.Embed(title=f"Message state changed")
        embed.add_field(name='User', value=after.author.mention)
        embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
        embed.add_field(name='Time', value=tighem)
        case_a = str(before)
        case_b = str(after)
        output_list = [li for li in difflib.ndiff(case_a, case_b) if li[0] != ' ']
        embed.add_field(name='Modified strings (beta)', value=output_list, inline=False)
        await LoggingChannel.send(embed=embed)
        return
    
@client.event
async def on_typing(channel, user, when):
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{channel.guild.id}\\sendMessages.txt")
    except Exception as e:
        print(e)
        await draggie.send(f"{user.mention} ({user}) is DMing me")
        print(f"{user.name} is DMing")
        return
    if os.path.isfile(sendLogsDir):
        if channel.guild.id == 759861456300015657:
            croissant = discord.utils.get(channel.guild.roles, name='Croissant')
            baguette = discord.utils.get(channel.guild.roles, name='Baguette')
            trigger = "high profile role [Croissant]"
            if croissant in user.roles:
                #print("Croissant detected")
                embed = discord.Embed(title=f"HIGH PROFILE typing", colour=0xc27c0e)
                embed.add_field(name='User', value=user.mention)
                embed.add_field(name='Before', value=user.status)
                embed.add_field(name='After', value=user.status)
                embed.add_field(name='Trigger', value=trigger)
                embed.add_field(name='Date/Time', value=tighem)
                LoggingChannel = discord.utils.get(channel.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await LoggingChannel.send(embed=embed)
                await draggie.send(f"{user.mention} has been seen **TYPING** in {channel.guild.name}! Triggered by {trigger}: `{tighem}`")
                return
            if baguette in user.roles:
                print("Baguette detected")
                embed = discord.Embed(title=f"HIGH PROFILE typing", colour=0x00acff)
                embed.add_field(name='User', value=user.mention)
                embed.add_field(name='Before', value=user.status)
                embed.add_field(name='After', value=user.status)
                embed.add_field(name='Trigger', value="high profile role [Baguette]")
                embed.add_field(name='Date/Time', value=tighem)
                LoggingChannel = discord.utils.get(channel.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await LoggingChannel.send(embed=embed)
                await draggie.send(f"{user.mention} has been seen **TYPING** in {channel.guild.name}! Triggered by [BAGUETTE]: `{tighem}`")
                return
        LoggingChannel = discord.utils.get(channel.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        embed = discord.Embed(title=f"User typing", colour=0x00ff00)
        embed.add_field(name='User', value=user.mention)
        embed.add_field(name='Channel', value=f"<#{channel.id}>")
        embed.add_field(name='Time', value=tighem)
        await LoggingChannel.send(embed=embed)
    print(f"TYPING >>> {user.name} started typing in {channel.name} at {tighem}/{when} in {channel.guild.name}")

@client.event
async def on_member_update(before, after):
    #print(f"Member updated - BEFORE = {before} AFTER = {after} - {datetime.now()}")
    send = False
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    guild = after.guild

    if before.status != after.status:  # to only run on status
        if guild.id == 759861456300015657:
            croissant = discord.utils.get(after.guild.roles, name='Croissant')
            baguette = discord.utils.get(after.guild.roles, name='Baguette')
            if croissant in after.roles:
                embed = discord.Embed(title=f"HIGH PROFILE status update", colour=0xc27c0e)
                embed.add_field(name='User', value=before.mention)
                embed.add_field(name='Before', value=before.status)
                embed.add_field(name='After', value=after.status)
                embed.add_field(name='Trigger', value="high profile role [Croissant]")
                embed.add_field(name='Date/Time', value=tighem)
                LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await draggie.send(f"{before.mention} has been seen **STATUS CHANGING {before.status} -> {after.status}** in {before.guild.name}! Triggered by [CROISSANT]: `{tighem}`")
                await LoggingChannel.send(embed=embed)
                return
            if baguette in after.roles:
                embed = discord.Embed(title=f"HIGH PROFILE status update", colour=0x00acff)
                embed.add_field(name='User', value=before.mention)
                embed.add_field(name='Before', value=before.status)
                embed.add_field(name='After', value=after.status)
                embed.add_field(name='Trigger', value="high profile role [Baguette]")
                embed.add_field(name='Date/Time', value=tighem)
                LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await draggie.send(f"{before.mention} has been seen **STATUS CHANGING {before.status} -> {after.status}** in {before.guild.name}! Triggered by [BAGUETTE]: `{tighem}`")
                await LoggingChannel.send(embed=embed)
                return

        embed = discord.Embed(title=f"Status updated", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.status)
        embed.add_field(name='After', value=after.status)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: STATUS of {after} has been updated FROM {before.status} TO {after.status} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.nick != after.nick:  # to only run on status
        embed = discord.Embed(title=f"Changed nick", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.nick)
        embed.add_field(name='After', value=after.nick)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: NICK of {after} has been updated FROM {before.nick} TO {after.nick} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        embed = discord.Embed(title=f"Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role added', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: ROLES of {after} has been updated: ADDED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
        if after.guild.id == 759861456300015657:
            await draggie.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!')
            await after.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!')
            print(f"Sent >>> {after.mention}, you\'ve been given the role **\"{new_role}\"** in {after.guild.name}! <<< to {after.name}")

    elif len(after.roles) < len(before.roles):
        new_role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title=f"Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role removed', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: ROLES of {after} has been updated: REMOVED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.name != after.name:  # to only run on status
        embed = discord.Embed(title=f"Changed name", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.name)
        embed.add_field(name='After', value=after.name)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: NAME of {after} has been updated FROM {before.name} TO {after.name} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.discriminator != after.discriminator:  # to only run on status
        embed = discord.Embed(title=f"Changed discriminator", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.discriminator)
        embed.add_field(name='After', value=after.discriminator)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"OP WATCHDOG: DISCRIMINATOR of {after} has been updated FROM {before.discriminator} TO {after.discriminator} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
    
    sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{after.guild.id}\\sendMessages.txt")
    if os.path.isfile(sendLogsDir):
        if send == True:
            LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
            send = False

            if LoggingChannel is None:
                print("Creating channel")
                guild = after.guild

                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(view_channel=False)
                }

                try:
                    await guild.create_text_channel('event-log-baguette', overwrites=overwrites)
                except Exception as e:
                    print(f"Couldn't create channel in {guild.id}/{guild.name}: {e}")
                    return

                bbLogChnlId = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                try:
                    await bbLogChnlId.send("Logging channel created. You can do whatever you want with this channel but deleting it **will** cause issues, as this channel is used to point to various IDs in this server.\nPermissions have been set automatically to admin only (everyone permission denied).\n\nUse /log disable if you don't want to have logs (more functionality will be coming in a leter version)")
                except:
                    print(f"unable to send message in server {guild.name} / {guild.id}")
                    await draggie.send(f"unable to send message in server {guild.name} / {guild.id}")
                LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        
            await LoggingChannel.send(embed=embed)
    else:
        send = False
        return

    #print(watchdogMsg)

#   on message

@client.event
async def on_message(message):
    if "UUID of player EmileTigger is d0b393de-e783-45b6-9d13-19ba56c5451e" in message.content:
        termcolor.cprint("Emile joined", 'red', attrs=['blink'])
        await asyncio.sleep(3)
        await console.send("say FRENCH Detected!!!!")
    if "EmileTigger lost connection" in message.content:
        await console.send("say Au revoir!")
    if message.author.bot:
       return

    person = message.author
    personID = message.author.id

    if not message.guild:
        message = message.content
        if message.startswith(".a"):
            x = message.split()
            msgchannel = (x[1])
            sp1 = message.split(' ', 2)[-1]
            channel = client.get_channel((int (msgchannel)))
            await channel.send((str ("`")) + (str (sp1)) + (str ("`")))
            return
        if message.startswith(".sa"):
            x = message.split()                
            msgchannel = (x[1])
            sp1 = message.split(' ', 2)[-1]
            channel = client.get_channel((int (msgchannel)))
            await channel.send(str (sp1))
            return
        await draggie.send(((str ("\n'")) + (str (message)) + (str ("' DMed by ")) + (str (person)) + (str (" at ") + (str (datetime.now())))))
        print(((str ("\n'")) + (str (message)) + (str ("' DMed by ")) + (str (person)) + (str (" at ") + (str (datetime.now())))))
        dmLocation = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\DMs\\")) + (str (personID)) + (str (".txt")))
        logAllMessages = open(dmLocation, "a", encoding='utf-8')
        logAllMessages.write((str ("\n'")) + (str (message)) + (str ("' DMed by ")) + (str (person)) + (str (" at ") + (str (datetime.now()))))
        logAllMessages.close()
        return
            
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    serverName = message.guild.name
    serverID = message.guild.id
    channelName = message.channel.name
    channelID = message.channel.id
    messageRepeat = message.content

    filedir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\")))
    if not os.path.exists(filedir):
        os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\")))

    try:
        with open((str (filedir)) + (str ("MessageLog.txt")), "a", encoding='utf-8') as logAllMessages:
            logAllMessages.write((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (message.author)) + (str (" in [{}".format(serverName) + f" - #{channelName}]")) + (str (" at ") + (str (datetime.now())) + (str (f" - IDs: {serverID} - {channelID}"))))
            logAllMessages.close()
    except Exception as e:
        errorMsg = str(f"\nError!!!! Logging file corruption has occured!!! cc: <@382784106984898560> \n\n{e}")
        print(errorMsg)
        #await message.channel.send(errorMsg)
        try:
            with open((str (filedir)) + (str ("MessageLog1.txt")), "a", encoding='utf-8') as logAllMessages:
                logAllMessages.write((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (message.author)) + (str (" in [{}".format(serverName) + f" - #{channelName}]")) + (str (" at ") + (str (datetime.now())) + (str (f" - IDs: {serverID} - {channelID}"))))
                logAllMessages.close()
        except Exception as e:
                errorMsg = str(f"\nCRITICAL ERROR!!!! Server file corruption has occured!!! cc: <@382784106984898560>, server ID is {serverID} / {channelID}\nDM Draggie#3060 if this does not get resolved in 10 minutes\nError: {e}")
                print(errorMsg)
                await message.channel.send(errorMsg)

    print((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (message.author)) + (str (" in [{}".format(serverName) + f" - #{channelName}]")) + (str (" at ") + (str (datetime.now())) + (str (f" - IDs: {serverID} - {channelID}"))))

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    async def DLstuff():
        if len(message.attachments) < 1: # Checks if there is an attachment on the message
            return
        else: # If there is it gets the filename from message.attachments
            if message.channel.id == 930494689105309777 or message.channel.id == 930496092754284576:
                upvote = client.get_emoji(803578918488768552)
                downvote = client.get_emoji(803578918464258068)
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
            attachmentsDir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Attachments\\")))
            if not os.path.exists(attachmentsDir):
                os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Attachments\\")))
                print("Made directory" + (attachmentsDir))
            nameOfFile = str(message.attachments).split("filename='")[1]
            filename = str(nameOfFile).split("' ")[0]
            beans = ((str (attachmentsDir)) + (str ("{}".format(filename))))
            if os.path.isfile(beans):
                filename = str(nameOfFile).split("' ")[0]
                beans = ((str (attachmentsDir)) + (str (uuid.uuid4())) + (str ("-name={}".format(filename))))
            await message.attachments[0].save(fp=beans)

            LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
            sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{message.guild.id}\\sendMessages.txt")
            if os.path.isfile(sendLogsDir):
                await LoggingChannel.send((str (f"Attachment sent in <#{channelID}>: **{filename}**")))

    await DLstuff()

    if message.author.id == 629321969615110154:
        blacklistCheck = message.content.lower()
        with open("D:\\BaguetteBot\\JSONs\\antiFrench.json", "r", encoding="utf8") as file:
            data = loads(file.read())
            for word in data:
                if word in blacklistCheck:
                    person = message.author   
                    await message.channel.send(f"Sorry but you can't say that, {person.mention}")
                    await message.delete()
                    print("Deleted!")

    if message.channel.name == 'nolwennium-138':
        emoji = client.get_emoji(786177817993805844)
        await message.add_reaction(emoji)
        
    if message.channel.id == 809112184902778890 or message.channel.id == 911968267881574441:
        upvote = client.get_emoji(803578918488768552)
        await message.add_reaction(upvote)
        downvote = client.get_emoji(803578918464258068)
        await message.add_reaction(downvote)
    if message.channel.id == 80911218490277889 or message.channel.id == 786178591268274176:
        httpCheck = message.content
        if ("http") in httpCheck.lower():
            upvote = client.get_emoji(803578918488768552)
            await message.add_reaction(upvote)
            downvote = client.get_emoji(803578918464258068)
            await message.add_reaction(downvote)
        if ("idea") in httpCheck.lower():
            upvote = client.get_emoji(803578918488768552)
            await message.add_reaction(upvote)
            downvote = client.get_emoji(803578918464258068)
            await message.add_reaction(downvote)
        else:
            print("not there")

    authorID = message.author.id
    person = message.author
    boosterRole = discord.utils.find(lambda r: r.name == 'Server Booster', person.roles)
    global currentMinute
    global coinDir
    
    coinDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
    serverdir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins")))
    
    if not os.path.exists(serverdir):
        os.makedirs(serverdir)

    try:
        f = open(coinDir, 'r')
        coins = f.read()
        #print ((str ("coins = ")) + (str (coins)))
        f.close()

        f = open(coinDir, 'w+')
        coins = (int (str (coins))) + 1
        f.close()
        #print ((str ("new coins = ")) + (str (coins)))

        with open(coinDir, 'a') as f:
            #print ((str ("appended coins = ")) + (str (coins)))
            f.write(str (coins))
            f.close()

    except FileNotFoundError:   #   User not found
        with open(coinDir, 'a') as f:
            print ((str ("\n\nset coin value to 1, new user.")))
            try:
                f.write('1')
                f.close()
            except Exception:
                f.write('1')
                f.close()

        sendLogsDir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\{message.guild.id}\\sendMessages.txt")
        my_file = Path(sendLogsDir)
        if my_file.is_file():
            try:
                bbLogChnlId = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

                embed = discord.Embed(title="User First Message", 
                description=((str (person.mention)) + (str (" has sent their first message. Their coins balance has been set to 1."))), colour=0x00ff00)
                await bbLogChnlId.send(embed=embed)
            except Exception:
                print((str ("Unable to send that a new user has joined. This server, ")) + (str (serverName)) + (str (", doesn't have a text channel called 'event-log-baguette'.")))
                guild = message.author.guild
                await guild.create_text_channel('event-log-baguette')
                bbLogChnlId = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await bbLogChnlId.set_permissions(message.guild.default_role, VIEW_CHANNEL=False)
                await bbLogChnlId.send("Logging channel created. You can do whatever you want with this channel but deleting it may cause some issues in the future :)")
                embed = discord.Embed(title="User First Message", 
                description=((str (person.mention)) + (str (" has sent their first message. Their coins balance has been set to 1."))), colour=0x00ff00)
                await bbLogChnlId.send(embed=embed)
            
    except ValueError:
        f.write('1')
        f.close()
    
    #print (len(s))

#   Generic commands.

    if message.content == ("hi"):
        await message.channel.send('hi')
        f = open(GlobalLogDir, "a")
        f.write((str ("\nWORD MENTIONED -> 'hi' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()

    if message.content == ("Hi"):
        await message.channel.send('Hi')
        f = open(GlobalLogDir, "a")
        f.write((str ("\nWORD MENTIONED -> 'Hi' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()

# Animated emoji sender.

    if message.content.startswith('ninjarage'): #                                     ninjarage emoji animated
        await message.channel.send("<a:ninjarage:767453473133953044>")
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> '.ninjarage' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nCOMMAND RAN -> '.ninjarage' ran by ")) + (str (message.author)))
    if message.content.startswith('boris'): #                                     boris emoji animated
        await message.channel.send("<a:boris:795038238799822848>")
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> '.boris' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nCOMMAND RAN -> '.boris' ran by ")) + (str (message.author)))
    if message.content.startswith('Colette'): #                                     boris emoji animated
        await message.channel.send("<a:colette:790577621690875956>")
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> 'colette' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nCOMMAND RAN -> 'colette' ran by ")) + (str (message.author)))

#   Fanficcs

    if message.content.startswith('fanfics'):
        await message.channel.purge(limit=1)
        await message.channel.send('I sure do love FANFICS!!!')
        f = open(GlobalLogDir, "a")
        f.write((str ("\nWORD DETECTED, message sent -> 'fanfics' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()

#   Reply to custom message, write here:

#    if message.content.startswith('..'): #
#        await message.channel.send('actually yeah it is kinda cool, everyone run it plz thanks :))))')

    if message.content.startswith("bbot://"):
        if personID == 382784106984898560:
            await message.channel.send("```Executed instruction.```")
        else:
            await message.channel.send(f"```{uuid.uuid4()}_callstack/MainThread: operation rejected, traceback includes data: message.author.id is {personID}```")

#   In the loop

    if message.content.startswith('.loop 5'): #  loop                           LOOP5
        await message.channel.send('loop!')
        await asyncio.sleep(0.1)
        await message.channel.send('loop!')
        await asyncio.sleep(0.1)
        await message.channel.send('loop!')
        await asyncio.sleep(0.1)
        await message.channel.send('loop!')
        await asyncio.sleep(0.1)
        await message.channel.send('loop!')
        await asyncio.sleep(0.1)
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> '.loop 5' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nCOMMAND RAN -> '.loop' ran by ")) + (str (message.author)))

#   Mobile notifications 

    if message.content.startswith(".noti"):#NOTI                                NOTI
        await message.channel.send("On mobile: swipe from the right to the left > look at top for the notifications icon > tap it and hit notification settings > use **only @mentions** for notifications only if you are tagged, or temporarily mute the server.")
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> '.noti' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nCOMMAND RAN -> '.noti' ran by ")) + (str (message.author)))

#   test

    if message.content == ('test'):
        await message.channel.send("testerino")
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> '.test ' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()

    if message.content == ('France'):
        await message.channel.purge(limit=1)
        franceRand = 0
        franceRand = random.randint (0,720)
        if franceRand == 50:
            await message.channel.send("You must speak French in this server only for the next hour.")
            print (franceRand)
        else:
            await message.channel.send((str ("Nope. (number = ")) + (str(franceRand)) + (str (")")))
            print (franceRand)
        f = open(GlobalLogDir, "a")
        f.write((str ("\nCOMMAND RAN -> 'France' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.write((str (". Number randomly generated between 0 and 100: ")) + (str (franceRand)))
        f.close()

#    if message.content == ('...'):
#        await message.channel.send("Lmao no it's not")

#   Get user @

    if message.content == ("@"):
        person = message.author
        await message.channel.send((str ("You're ")) + (str (message.author)) + (str(" (")) + (str (person.mention)) + (str(")")))
        f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\\\Logs\\GlobalLog.txt", "a")
        f.write((str ("\nCOMMAND RAN -> '@' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()

#   Split message

    if message.content.startswith (".split"):
        txt = message.content
        x = txt.split()
        print(x[1])
        await message.channel.send(x[1])
    
#   Split message, delete original

#    if message.content.startswith (".delsplit"):
#        txt = message.content
#        print (txt)
#        x = txt.split()
#        print (x)
#        await message.channel.purge(limit=1)
#        await message.channel.send(x[1])
#
#    if message.content.startswith (".testfor"):
#        txt = message.content
#        x = txt.split()
#        print (x)
#        #await message.channel.send(x[1])
#        await message.channel.purge(limit=1)
#        await message.channel.send(str ("Testing for ") + (str (x[1])) )


#   Send Emoji for Face!

    if message.guild.id == 759861456300015657 or message.guild.id == 384403250172133387:#     Checks whether the server ID matches Baguette Brigaders's server for privacy
        messageContent = message.content.lower()
        for word in messageContent.split():
            if word in nollyWords:
                await message.add_reaction("<:nolly:786177817993805844>")
            if word in oliverWords:
                await message.add_reaction("<:oliver:790576109795409920>")
            if word in jackWords:
                await message.add_reaction("<:LilJack:901155402190823434>")
            if word in joeWords:
                await message.add_reaction("<:CuteJoe:897467228545503242>")
            if word in haydnWords:
                await message.add_reaction("<:haydn:786276584671412244>")
            if word in maisyWords:
                await message.add_reaction("<:maisy:786276271809101840>")
            if word in benWords:
                await message.add_reaction("<:bennybooze:788311580768075786>")
            if word in ishWords:
                await message.add_reaction("<:ish:791381704278540369>")
            if word in mayaWords:
                await message.add_reaction("<:maya:785942478448230470>") 
            if word in samWords:
                await message.add_reaction("<:samf:785942793280815114>")
        for word in josephTighe:
            if word in messageContent:
                integer = random.randint(1,2)#      Sets random emoji reaction as he has 2 emojis.
                if integer == 1:
                    await message.add_reaction("<:hmmnotsureaboutthis:870745923171549234>")#    if random int is 1 search for and add tighe 1
                if integer == 2:
                        await message.add_reaction("<:Joseph:865213431900143656>")#    else, search for and add tighe 2#
        for word in charlieSewards:
            if word in messageContent:
                integer = random.randint(1,2)#      Again, sets random emoji reaction as he has 2 emojis.
                if integer == 1:
                    await message.add_reaction("<:charlie:903324276147499041>")
                if integer == 2:
                    await message.add_reaction("<:CharlieUwU:857907947371495424>")

    #  here we can do global server ones because its funny

    messageContent = message.content.lower()
    for word in messageContent.split():
        if word in borisWords:
            await message.add_reaction("<:boris:785942478381121556>")
            f = open(GlobalLogDir, "a", encoding="utf8")
            f.write((str (f"\nINFO: 'boris' emoji sent, initiated by '{message.author}' at {datetime.now()}")))#    compress str writing by using f strings
            f.close()  

#   Nolly = :nolly:786177817993805844
#   Oliver = :oliver:786275811405070337
#   Jack = :jacc:786275811405070337
#   Joe = :joecat:786277202400116770

#   Charlie = 


#   Haydn = :haydn:786276584671412244
#   Maisy = :maisy:786276271809101840
#   Ben = :bennybooze:788311580768075786
#   Flo = :JacksGF:788162163289358367
#   Ish = :ish:791381704278540369
#   Boris = :boris:785942478381121556
#   Maya = :maya:785942478448230470
#   Sam = :samf:785942793280815114

#   Charlie's emoji below, enable later

#   Other Emoji Mention
       
#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

    #if message.channel.id == 759861456761258045:
    #    if message.content.startswith("."):
    #        hasAdmin = discord.utils.find(lambda r: r.name == 'Admin', message.guild.roles)
    #        async with message.channel.typing():
    #            if hasAdmin in message.author.roles:
    #                await client.process_commands(message)
    #                return
    #            else:
    #                await asyncio.sleep(0.5)
    #                await message.channel.send("Commands can't be used here, try <#785620979300302869>.")
    #                return
    else:
        await client.process_commands(message)

#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

#   baguettes
    
@client.command(help="Sends up to 9 random baguette pics", brief="Sends random baguette pics", pass_context=True)
async def baguette(ctx, member: discord.Member = None):
    baguetteRand = (str (random.randint(1,9)))
    await ctx.send(file=discord.File(f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Assets\\Baguettes\\baguette{baguetteRand}.jpg"))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.baguette ' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   ping

#@client.command(help="Says the ping immediately after user has sent the command. Used for determining latency/ping or downtime.", brief="Shows ping.", pass_context=True)
#async def ping(ctx):
#
#    if round(client.latency * 1000) <= 100:
#        embed=discord.Embed(title="PING", description=f"Message delay is is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
#    elif round(client.latency * 1000) <= 150:
#        embed=discord.Embed(title="PING", description=f"Message delay is is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
#    elif round(client.latency * 1000) <= 150:
#        embed=discord.Embed(title="PING", description=f"Message delay is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
#    else:
#        embed=discord.Embed(title="PING", description=f"OOF! Message delay is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
#    await ctx.send(embed=embed)
#    f = open(GlobalLogDir, "a", encoding="utf8")
#    f.write((str ("\nCOMMAND RAN -> '.ping' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
#    f.close()

#   Statuses

@client.command(help="Displays/changes status. Syntax: \n.status <playing | streaming | listening | watching> [custom cool text you enter here]", brief="Type .help status", pass_context=True)
async def status(ctx):

    text = ctx.message.content

    fullString = text.split(' ', 2)[-1]

    x = text.split()
    determiner = (str (x[1]))
    
    if determiner == "playing":
        await client.change_presence(activity=discord.Game(name=(fullString)))
        await ctx.send((str ("I'm playing ")) + (str (fullString)) + (str("!")))    

    if determiner == "streaming":
        await client.change_presence(activity=discord.Streaming(name=(fullString), url=(fullString)))
        await ctx.send((str ("I'm streaming ")) + (str (fullString)) + (str("!")))

    if determiner == "listening":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(fullString)))
        await ctx.send((str ("I'm listening to ")) + (str (fullString)) + (str("!")))

    if determiner == "watching":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(fullString)))
        await ctx.send((str ("I'm watching ")) + (str (fullString)) + (str("!")))

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.status' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   channel test

@client.command(help="channel", brief="channel", pass_context=True)
async def channel(ctx):
    await ctx.send(ctx.message.channel.mention)
    print(ctx.message.channel.mention)

#   Cross Server Messaging

@client.command(pass_context=True)
async def sa(ctx):
    text = ctx.message.content
    x = text.split()
    
    msgchannel = (x[1])
    #print((str ("\nmsgchannel = '")) + (str (msgchannel)) + (str ("'")))

    sp1 = text.split(' ', 2)[-1]
    #print((str ("\nsp1 = '")) + (str (sp1)) + (str ("'")))

    channel = client.get_channel((int (msgchannel)))
    #print((str ("\nchannel = '")) + (str (channel)) + (str ("'")))

    await channel.send(str (sp1))
    return

#   Last message in channel.

@client.command(pass_context=True)
async def lastMessage(ctx, users_id: int):
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]

    oldestMessage = None
    for channel in ctx.guild.text_channels:
        fetchMessage = await channel.history().find(lambda m: m.author.id == users_id)
        if fetchMessage is None:
            continue

        if oldestMessage is None:
            oldestMessage = fetchMessage
        else:
            if fetchMessage.created_at > oldestMessage.created_at:
                oldestMessage = fetchMessage

    if (oldestMessage is not None):
        await ctx.send((str ("<@!")) + (str (sp1)) + (str (">")) + (str (f"'s last message is: \n\n'{oldestMessage.content}'.")))
    else:
        await ctx.send((str ("<@!")) + (str (sp1)) + (str (">")) + (str (" has been inactive for a long time, their last message has not been sent within the past page of messages in any channel.")))

#   Kahoot botter

@client.command()
async def bot(ctx):
    global name
    #                           await ctx.send("Syntax: .bot <CODE> <AMOUNT> <NAME/random>")
    #await ctx.send("IDE detected! Unable to run command. Aborting.")
    #return
    text = ctx.message.content

    namerator = requests.get('https://apis.kahoot.it/namerator.json')
    nameratorContent = namerator.content

    f = json.loads(nameratorContent)
    nameratorName = f["name"]
    #await ctx.send(nameratorName)

    x = text.split()

    try:
        code = (x[1])
        botNum = int(x[2])
        ogName = text.split(' ', 3)[-1]
    except:
        await ctx.send("I'm not sure you have the correct syntax. Use `.bot <CODE> <AMOUNT> <NAME/random>`. The `<NAME>` section can be set to `random`, this will auto generate a Kahoot 'safe' name.\nExample: `.bot 8261910 138 Test player`\n\nNote: Bots do not answer questions, *yet*.")
        return

    clients = []

    if botNum >= 2:
        print((str ("Attempting to add `")) + (str (botNum)) + (str ("` bots to game ID `")) + (str (code)) + (str ("`!")))
    else:
        print((str ("Attempting to add `")) + (str (botNum)) + (str ("` bot to game ID `")) + (str (code)) + (str ("`!")))

    joins = 0
    targetJoins = (int(botNum))

    def getName():
        global name
        namerator = requests.get('https://apis.kahoot.it/namerator.json')
        nameratorContent = namerator.content
        f = json.loads(nameratorContent)
        name = f["name"]
        
    for client in range(botNum):
        if ogName == 'random':
            getName()
        else:
            global name
            name = ogName

        clients.append(kahoot.client())

        if ogName == 'random':
            clients[client].join(code,name)
            #await ctx.send((str ("Joined as `")) + (str (name)) + (str ("`.")))
            print(name)
            joins = joins + 1
            if joins == targetJoins:
                print("Done!")
                if botNum >= 2:
                    await ctx.send((str ("Done! `")) + (str (joins)) + (str ("` bots have been added to `")) + (str (code)) + (str ("`.")))
                else:
                    await ctx.send((str ("Done! `")) + (str (joins)) + (str ("` bot has been added to `")) + (str (code)) + (str ("`.")))

        else:
            clients[client].join(code,name+str(client+1))
            #await ctx.send((str ("Joined as `")) + (str (name)) + (str (client+1)) + (str ("`.")))#clients[client].join(code,name+str(client+1))
            print(name+str(client+1))
            joins = joins + 1
            if joins == targetJoins:
                print("Done!")
                if botNum >= 2:
                    await ctx.send((str ("Done! `")) + (str (joins)) + (str ("` bots have been added to `")) + (str (code)) + (str ("`.")))
                else:
                    await ctx.send#((str ("Done! `")) + (str (joins)) + (str ("` bot has been added to `")) + (str (code)) + (str ("`.")))

#   Elon musk

@client.command(pass_context=True, help="X Æ A-12", brief="bebe spam X Æ A-12")
async def ElonMusk(ctx):
    await ctx.send("X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12")
    f = open(GlobalLogDir, 'a')
    f.write((str ("\nCOMMAND RAN -> '.ElonMusk' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.ElonMusk' ran by ")) + (str (ctx.message.author)))

#   convert

@client.command(help="Shows coin balance. If above a threshold, shows items to buy", brief="Shows your balance, and available to buy items.", pass_context=True)
async def convert(ctx):
    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol=ETH'
    #await ctx.send("IDE detected! Unable to run command. Aborting.")
    #return
    with open("D:\\OneDrive - Sapientia Education Trust\\api_file.bin", encoding="utf-8") as f:
        api_key = f.read()

    parameters = {}
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        data = str (json.loads(response.text))

        print(data)
        f = json.loads(data)
        print(list(filter(lambda x:x["quote"]=="USD",data)))

        print(f)
        await ctx.send(data)
    except Exception as e:
        await ctx.send(e)

#   coins

@client.command(
    help="Shows coin balance. If above a threshold, shows items to buy", 
    brief="Shows your balance, and available to buy items.", 
    pass_context=True,
    aliases=['shop', 'rank', 'points', 'balance', 'bal', 'coin', 'nolly', 'nolwennium', 'nolwenn', 'score'])
async def coins(ctx):
    testForToggles = ctx.message.content
    silent = False
    if ("/s") in testForToggles.lower():
        if ctx.message.author.guild_permissions.administrator == True:
            silent = True
        else:
            await ctx.send("Your server administrator has disabled the option to use the silent toggle.")
    authorID = ctx.message.author.id
    #await ctx.send("Coins earned before 30/07/2021 are not available to use. This is a known bug and will be fixed later. You have not lost any Coins, but you cannot buy anything with your old balance. New Coins will be added to your old Coins.")
    userID = authorID
    user = ctx.message.author
    serverName = ctx.message.guild.name
    serverID = ctx.message.guild.id
    #print (serverID)

    coinDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
    f = open(coinDir, 'r')
    coinBal = f.read()
    f.close()

    nolwenniumUserDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\")) + (str (authorID)) + (str (".txt"))
    my_file = Path(nolwenniumUserDir)

    if not my_file.is_file():
        with open(nolwenniumUserDir, 'a') as f:
            print ((str ("\n\nset Nolwennium value to 0, new user.")))
            try:
                f.write('0')
                f.close()
            except Exception:
                f.write('0')
                f.close()

    f = open(nolwenniumUserDir, 'r')
    nolwenniumBal = f.read()
    f.close()
    
    canRunCommand = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
    if canRunCommand in user.roles:
        try:
            #	List of stuff BEFORE showing the user their balance
            txt = ctx.message.content
            x = txt.split()
            word1 = (str (x[1]))

            if word1.lower() == 'set':
                if ctx.message.author.guild_permissions.administrator == True:
                    userID = (str (x[2]))
                    amount = (str (x[3]))
                    usersCoins = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (userID)) + (str (".txt"))
                    oc = open(usersCoins, 'r')
                    oldCoins = oc.read()
                    oc.close()

                    e = open(usersCoins, 'w+')
                    e.close()

                    with open(usersCoins, 'a') as f:
                        f.write(str (amount))
                        f.close()

                    nc = open(usersCoins, 'r')
                    newCoins = nc.read()
                    nc.close()
                    
                    if silent == False:
                        await ctx.send((str ('<@')) + (str (userID)) + (str (">'s coins have been updated from ")) + (str (oldCoins)) + (str ("<:Coins:852664685270663194> to **")) + (str (newCoins)) + (str ("** <:Coins:852664685270663194>.")))
                    if silent == True:
                        print(f"Old coins: {oldCoins} -----> New coins: {newCoins}")
                        await ctx.message.add_reaction('✅')
                    return
            
            if word1.lower() == 'add':
                if ctx.message.author.guild_permissions.administrator == True:
                    userID = (str (x[2]))
                    amountToAdd = (str (x[3]))

                    usersCoins = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (userID)) + (str (".txt"))

                    oc = open(usersCoins, 'r')
                    oldCoins = oc.read()
                    oc.close()

                    e = open(usersCoins, 'w+')
                    e.close()

                    newCoins = int(oldCoins) + int(amountToAdd)

                    with open(usersCoins, 'a') as f:
                        f.write(str (newCoins))
                        f.close()

                    nc = open(usersCoins, 'r')
                    newCoins = nc.read()
                    nc.close()

                    if silent == False:
                        await ctx.send((str ('<@')) + (str (userID)) + (str (">'s coins have been updated from ")) + (str (oldCoins)) + (str ("<:Coins:852664685270663194> to **")) + (str (newCoins)) + (str ("** <:Coins:852664685270663194>.")))
                    if silent == True:
                        print(f"{userID}:       Old coins: {oldCoins} -----> New coins: {newCoins}")
                        await ctx.message.add_reaction('✅')
                    return
            if word1.lower() == 'lookup':
                if ctx.message.author.guild_permissions.administrator == True:
                    userID = (str (x[2]))

                    usersCoins = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (userID)) + (str (".txt"))
                    oc = open(usersCoins, 'r')
                    coinAmount = oc.read()
                    oc.close()

                    nolwenniumUserDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\")) + (str (userID)) + (str (".txt"))
                    my_file = Path(nolwenniumUserDir)

                    if not my_file.is_file():
                        with open(nolwenniumUserDir, 'a') as f:
                            print ((str ("\n\nset Nolwennium value to 0, new user.")))
                            try:
                                f.write('0')
                                f.close()
                            except Exception:
                                f.write('0')
                                f.close()

                    f = open(nolwenniumUserDir, 'r')
                    nolwenniumBal = f.read()
                    f.close()

                    if silent == False:
                        await ctx.send(f"<@{userID}> has **{coinAmount}** coins, and **{nolwenniumBal}** Nolwennium.")
                    if silent == True:
                        print(f"{userID}:       Coins: {coinAmount} -----> Nolwennium: {nolwenniumBal}")
                        await ctx.message.add_reaction('✅')
                    return
            else:
                await ctx.send("I don't know what you mean. The correct syntaxes are:\n\n`.coins set <targetUserID> <newCoins>`\n`.coins add <targetUserID> <addedAmount>`\n`.coins lookup <targetUserID>`")

        except Exception:#		AFTER the list of alternate options has been checked; the user just wants their balance.
            global citizenPurchasable
            global knightPurchasable
            global princePurchasable
            global kingPurchasable
            global adminPurchasable

            citizenPurchasable = '-'
            knightPurchasable = ' '
            princePurchasable = ' '
            kingPurchasable = ' '
            adminPurchasable = ' '

            hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
            hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
            hasPrince = discord.utils.find(lambda r: r.name == 'Prince', ctx.message.guild.roles)
            hasKing = discord.utils.find(lambda r: r.name == 'King', ctx.message.guild.roles)
            hasAdmin = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)

            randomCry = random.randint(1,7)
            global cry
            if randomCry == 1:
                cry = '<:AmberCry:828577834146594856>'
            if randomCry == 2:
                cry = '<:BibiByeBye:828683852939395072>'
            if randomCry == 3:
                cry = '<:ColetteCry:828683829631516732>'
            if randomCry == 4:
                cry = '<:JessieCry:828683805861740654>'
            if randomCry == 5:
                cry = '<:SpikeCry:828683779206807622>'
            if randomCry == 6:
                cry = '<:SurgeCry:828683755694063667>'
            if randomCry == 7:
                cry = '<:TaraCry:828683724286853151>'

            if serverID != 759861456300015657:
                await ctx.send("**WARNING! This server has not been optimised for this command, errors may be encountered.**")
            
            if hasCitizen in user.roles:
                citizenPurchasable = '\nCitizen: *🔓 Unlocked!*'
            if int (str (coinBal)) > 1:
                citizenPurchasable = 'Citizen: 0 <:Coins:852664685270663194>'

            if hasKnight in user.roles:
                knightPurchasable = '\nKnight:*🔓 Unlocked!*'

            if int (str (coinBal)) > 250:
                knightPurchasable = '\nKnight: 250 <:Coins:852664685270663194>'

            if hasPrince in user.roles:
                princePurchasable = '\nPrince:*🔓 Unlocked!*'

            if int (str (coinBal)) > 1000:
                princePurchasable = '\nPrince: 1000 <:Coins:852664685270663194>'

            if hasKing in user.roles:
                kingPurchasable = '\nKing:*🔓 Unlocked!*'

            if int (str (coinBal)) > 2500:
                kingPurchasable = '\nKing: 2,500 <:Coins:852664685270663194>'

            if int (str (coinBal)) > 1000000:
                if hasAdmin in user.roles:
                    adminPurchasable = '\nAdmin:*🔓 Unlocked!*'

                else:
                    adminPurchasable = '\nAdmin: 1,000,000 <:Coins:852664685270663194>'

            f = open (nolwenniumUserDir, 'r')
            nolwenniumBal = f.read()
            f.close()

            embed = discord.Embed(title="User Balance", description=((str ("You have ")) + (str (coinBal)) + (str (" <:Coins:852664685270663194> coins and ")) + (str (nolwenniumBal)) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium available to spend."))), colour=0xFFD700)
            embed.add_field(
            name="Items available to .buy",
            value=(citizenPurchasable) + (knightPurchasable) + (princePurchasable) + (kingPurchasable) + (adminPurchasable),
            inline=False)
            if serverID == 759861456300015657:
                embed.set_footer(text=("What can I do with these?\nYou can buy roles for Coins (this server only) by typing .buy [item], and use Nolwennium to run commands for the bot (saved across all servers)."))
            await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have permission to access the shop interface.")

#   buy

@client.command(help="Shows coin balance. If above a threshold, displays the list of roles the user can buy by typing .buy <role>", brief="Shows your balance, and available to buy items.", pass_context=True)
async def buy(ctx):
    canRunCommand = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
    if canRunCommand in ctx.message.author.roles:
        async with ctx.typing():
            member = ctx.message.author
            authorID = ctx.message.author.id
            text = ctx.message.content
            serverID = ctx.message.guild.id

            try:
                x = text.split()
                determiner = (str (x[1]))
            except Exception as e:
                await ctx.send("Please enter an item to buy.")
                return
            filedir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
            f = open(filedir, 'r')
            coinBal = f.read()
            f.close()

            if determiner.lower() == 'citizen':

                hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
                if hasCitizen in member.roles:
                    await ctx.send("You can't buy Citizen, you already have it!")
                    return

                coinBal = (int (str (coinBal))) - 1

                f = open(filedir, 'w+')
                f.close()

                with open(filedir, 'a') as f:
                    f.write(str (coinBal))
                    f.close()
                
                role = discord.utils.get(ctx.message.guild.roles, name="Citizen")
                await member.add_roles(role)

                embed = discord.Embed(title="The Shop", description=("You've just bought Citizen for free! Remaining balance: {} <:Coins:852664685270663194>".format(coinBal)), colour=0xFFD700)
                embed.add_field(name="Perks", value="• Above Member in the Member List\n• Custom nickname\n• Add reactions\n• Bonus Nolwennium", inline=False)   
                await ctx.send(embed=embed)
                return

    #   KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT

        if determiner.lower() == 'knight':

            hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
            if hasKnight in member.roles:
                await ctx.send("You can't buy Knight, you already have it!")
                return
                    
            hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
            if hasCitizen in member.roles:

                coinBalTest = (int (str (coinBal))) - 250

                if coinBalTest < 0:
                    await ctx.send("You do not have enough Coins to buy Knight.")
                    return

                coinBal = (int (str (coinBal))) - 250

                f = open(filedir, 'w+')
                f.close()

                with open(filedir, 'a') as f:
                    f.write(str (coinBal))
                    f.close()
                
                role = discord.utils.get(ctx.message.guild.roles, name="Knight")
                await member.add_roles(role)

                embed = discord.Embed(title="The Shop", description=("You've just bought Knight for 250 <:Coins:852664685270663194>! Remaining balance: {} <:Coins:852664685270663194>".format(coinBal)), colour=0xFFD700)
                embed.add_field(name="Perks", value="• Above Citizen in the Member List\n• Show embeds on your messages\n• Send TTS messages\n", inline=False)   
                await ctx.send(embed=embed)
            else:
                await ctx.send("You must buy Citizen before Knight.")
                return
            return

    #   PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE 

        if determiner.lower() == 'prince':
            hasPrince = discord.utils.find(lambda r: r.name == 'Prince', ctx.message.guild.roles)
            if hasPrince in member.roles:
                await ctx.send("You can't buy Prince, you already have it!")
                return
            
            hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
            if hasKnight in member.roles:
                coinBalTest = (int (str (coinBal))) - 1000
                if coinBalTest < 0:
                    await ctx.send("You do not have enough Coins to buy Prince.")
                    return
                coinBal = (int (str (coinBal))) - 1000

                f = open(filedir, 'w+')
                f.close()

                with open(filedir, 'a') as f:
                    f.write(str (coinBal))
                    f.close()

                role = discord.utils.get(ctx.message.guild.roles, name="Prince")
                await member.add_roles(role)

                embed = discord.Embed(title="The Shop", description=("You've just bought Prince for 1000 <:Coins:852664685270663194>! Remaining balance: {} <:Coins:852664685270663194>".format(coinBal)), colour=0xFFD700)
                embed.add_field(name="Perks", value="• Above Knight in the Member List\n• Mass ping many people\n• Priority Voice Chat speaker\n• Move other members in Voice Chats\n• Manage server emojis\n• Manage webhooks\n", inline=False)   
                await ctx.send(embed=embed)
            else:
                await ctx.send("You must buy Knight before Prince.")
            return

    #   KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING 

        if determiner.lower() == 'king':

            hasKing = discord.utils.find(lambda r: r.name == 'King', ctx.message.guild.roles)
            if hasKing in member.roles:
                await ctx.send("You can't buy King, you already have it!")
                return
            
            hasPrince = discord.utils.find(lambda r: r.name == 'Prince', ctx.message.guild.roles)
            if hasPrince in member.roles:
                coinBalTest = (int (str (coinBal))) - 2500
                if coinBalTest < 0:
                    await ctx.send("You do not have enough Coins to buy King.")
                    return

                coinBal = (int (str (coinBal))) - 2500

                f = open(filedir, 'w+')
                f.close()

                with open(filedir, 'a') as f:
                    f.write(str (coinBal))
                    f.close()
                
                role = discord.utils.get(ctx.message.guild.roles, name="King")
                await member.add_roles(role)

                embed = discord.Embed(title="The Shop", description=("You've just bought King for 2500 <:Coins:852664685270663194>! Remaining balance: {} <:Coins:852664685270663194>".format(coinBal)), colour=0xFFD700)
                embed.add_field(name="Perks", value="• Mute other members in Voice Chat\n• Deafen other members in Voice Chat\n• Delete or pin other users' messages\n• Change other peoples' nicknames\n• Kick members", inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("You must buy Prince before King.")
            return
        
        if determiner == 'admin':

            hasKing = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
            if hasKing in member.roles:
                await ctx.send("You can't buy Admin, you already have it!")
                return
            coinBalTest = (int (str (coinBal))) - 1000000

            if coinBalTest < 0:
                await ctx.send("You do not have enough Coins to buy Admin.")
                return

            coinBal = (int (str (coinBal))) - 1000000

            f = open(filedir, 'w+')
            f.close()

            with open(filedir, 'a') as f:
                f.write(str (coinBal))
                f.close()
            
            embed = discord.Embed(title="The Shop", description=("You've just bought Admin for 1,000,000 <:Coins:852664685270663194>! Remaining balance: {} <:Coins:852664685270663194>".format(coinBal)), colour=0xFFD700)
            role = discord.utils.get(ctx.message.guild.roles, name="Admin")
            await member.add_roles(role)
            await ctx.send(embed=embed)
            return
        
        else:
            await ctx.send("That's not a valid item to buy!")
    else:
        await ctx.send("You do not have permission to access the buy interface.")

#   Voice Channel Bitrate

@client.command(help="Changes voice channel bitrate. Syntax '.bitrate [channelID] [bitrateInBits]'.", brief="Changes voice channel bitrate.", pass_context=True)
async def bitrate(ctx):
    text = ctx.message.content
    x = text.split()
    channelID = (int (x[1]))
    bitrate = (int (x[2]))
    vchannel = client.get_channel(channelID)
    await vchannel.edit(bitrate=(bitrate))

#   offline status for replit

@client.command(help="Turns status to offline/invisible", brief="[Status] Turns invisible")
async def offline(ctx):
    await client.change_presence(status=discord.Status.invisible)
    await ctx.send("Status set to invisible/offline.")

#   yn

@client.command(help="Randomly answers yes or no.", brief="Ask me a yes/no question.", pass_context=True)
async def yn(ctx):
    randWord = random.randint(1,14)
    if randWord == 1:
        await ctx.send("No!")#  n
    if randWord == 2:
        await ctx.send("Yes!")# y
    if randWord == 3:
        await ctx.send("Obviously!")#   y
    if randWord == 4:
        await ctx.send("Of course not!")#   n
    if randWord == 5:
        await ctx.send("Of course!")#   y
    if randWord == 6:
        await ctx.send("Certainly!")#   y
    if randWord == 7:
        await ctx.send("Certainly not.")#   n
    if randWord == 8:
        await ctx.send("Definitely!")#  y
    if randWord == 9:
        await ctx.send("Definitely not!")#  n
    if randWord == 10:
        await ctx.send("Without a shadow of a doubt!")# y
    if randWord == 11:
        await ctx.send("Obviously not.")#   n
    if randWord == 12:
        await ctx.send("Nah!")# n
    if randWord == 13:
        await ctx.send("Nope.")#    n
    if randWord == 14:
        await ctx.send("Yessir!")#  y

    print ((str ("\nCOMMAND RAN -> '.yn' ran by ")) + (str (ctx.message.author)))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.yn' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   setdelay

@client.command(help="Sets slow mode.", brief="Sets slow mode. Syntax = .setdelay [delayInSec]", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def setdelay(ctx):
    txt = ctx.message.content
    x = txt.split()
    sp1 = (str (x[1]))
    
    await ctx.channel.edit(slowmode_delay=sp1)

    embed = discord.Embed
    embed=discord.Embed(title="Edited channel info!", description=(f"Set the slowmode delay in this channel to {sp1} seconds!"), colour=0x228B22)
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write((str ("\nCOMMAND RAN -> '.setdelay {seconds}' ran by ")) + (str (ctx.message.author)) + (str (" in channel ")) + (str (ctx.channel.mention)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print((str ("\nCOMMAND RAN -> '.setdelay {seconds}' ran by ")) + (str (ctx.message.author)) + (str (" in channel ")) + (str (ctx.channel.mention)) + (str (" at ") + (str (datetime.now()))))

#	Brawl Stars Music

@client.command(help="Plays random Brawl Stars music. This command requires the user to be in a voice channel. Also triggered by typing .r", brief="[Audio] Repeatedly plays Brawl Stars music.", aliases=['r'], pass_context=True)
async def radio(ctx):
    async with ctx.typing():
        channel = ctx.author.voice.channel
        serverName = ctx.message.guild.name
        testForToggles = ctx.message.content
        debugMode = False
        if ("/d") in testForToggles.lower():
            if ctx.message.author.guild_permissions.administrator == True:
                debugMode = True
            else:
                await ctx.send("Your server administrator has disabled the option to use the debug mode toggle.")

        #await ctx.send("IDE detected! Unable to run command. Aborting.")
        #return

        def after_audio():
            voice_client = ctx.guild.voice_client
            randomnumber = random.randint(1,69)
            musicDir = ((str("D:\\App Files\\Brawl Music\\py\\music_")) + (str(randomnumber)) + (str ('.ogg')))
            voice_client.play(discord.FFmpegPCMAudio(source=musicDir), after=lambda e: after_audio())
            print((str ("RADIO: Playing 'music_")) + (str (randomnumber)) + (str ("' in [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in after_audio")))
            if debugMode == True:
                #await ctx.channel.send((str ("RADIO: Playing 'music_")) + (str (randomnumber)) + (str ("' in [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in after_audio")))
                print("Debug mode ON but cannot send message.")
            #asyncio.run_coroutine_threadsafe(looper, client.loop)
        
        async def playtheaudio():
            try:
                await channel.connect()
                voice_client = ctx.guild.voice_client
                voice_client.stop()
                await asyncio.sleep(0.2)
                randomnumber = random.randint(1,69)
                musicDir = ((str("D:\\App Files\\Brawl Music\\py\\music_")) + (str(randomnumber)) + (str ('.ogg')))
                voice_client.play(discord.FFmpegPCMAudio(source=musicDir), after=lambda e: after_audio())
                print((str ("RADIO: Playing 'music_")) + (str (randomnumber)) + (str ("' in [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in BaguetteBot.py/funcion/playtheaudio/try")))
                if debugMode == True:
                    await ctx.channel.send((str ("```RADIO: Playing 'music_")) + (str (randomnumber)) + (str ("' in [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in BaguetteBot.py/funcion/playtheaudio/try```")))
                    
            except:
                voice_client = ctx.guild.voice_client
                voice_client.stop()
                await asyncio.sleep(0.2)
                #asyncio.run_coroutine_threadsafe(playit(), bot.loop)

        await playtheaudio()

#   vbuck calc

@client.command(help="Calculates GBP -> V-Bucks", brief="Calculates GBP -> V-Bucks. Syntax = .vbucks [tier] [GBP]", pass_context=True)
async def vbucks(ctx):
    txt = ctx.message.content
    x = txt.split()
    
    vTier = (float (x[1]))
    vAmount = (float (x[2]))
    GBP = (float (x[2]))

    vTier1 = (float (154.083205))
    vTier2 = (float (175.109443))
    vTier3 = (float (192.381685))
    vTier4 = (float (210.970464))


    if vTier == (float ("1")):
        vAmount = (float (vTier1)) * (int (vAmount))
        await ctx.send((str ("£") + (str (GBP)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 1 of vbuck purchase)."))))
    if vTier == (float ("2")):
        vAmount = (int (vTier2)) * (int (vAmount))
        await ctx.send((str ("£") + (str (GBP)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 2 of vbuck purchase)."))))
        print (vAmount)
    if vTier == (float ("3")):
        vAmount = (int (vTier3)) * (int (vAmount))
        await ctx.send((str ("£") + (str (GBP)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 3 of vbuck purchase)."))))
        print (vAmount)
    if vTier == (float ("4")):
        vAmount = (int (vTier4)) * (int (vAmount))
        await ctx.send((str ("£") + (str (GBP)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 4 of vbuck purchase)."))))
        print (vAmount)

#   Vbucks USD

@client.command()
async def vbucksUSD(ctx):
    txt = ctx.message.content
    x = txt.split()
    vTier = (str (x[1]))
    vAmount = (str (x[2]))
    USD = (str (x[2]))

    vTier1USD = (int (125.156446))
    vTier2USD = (int (140.070035))
    vTier3USD = (int (156.298843))
    vTier4USD = (int (168.771096))

    if vTier == (str ("1")):
        vAmount = (int (vTier1USD)) * (int (vAmount))
        await ctx.send((str ("$") + (str (USD)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 1 of vbuck purchase)."))))
        print (vAmount)
    if vTier == (str ("2")):
        vAmount = (int (vTier2USD)) * (int (vAmount))
        await ctx.send((str ("$") + (str (USD)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 2 of vbuck purchase)."))))
        print (vAmount)
    if vTier == (str ("3")):
        vAmount = (int (vTier3USD)) * (int (vAmount))
        await ctx.send((str ("$") + (str (USD)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 3 of vbuck purchase)."))))
        print (vAmount)
    if vTier == (str ("4")):
        vAmount = (int (vTier4USD)) * (int (vAmount))
        await ctx.send((str ("$") + (str (USD)) + (str (" is equal to ")) + (str (vAmount)) + (str(" vbucks ")) + (str ("(using tier 4 of vbuck purchase)."))))
        print (vAmount)

#   Face

@client.command(help="Allows face.", brief="Allows face.", pass_context=True)
async def face(ctx):
    await ctx.send("Face allowed. Please wait for the next DraggieBot version for your setting to be applied. This may take an hour. If your face is not already added, please go to #emoji-nominations channel to add or modify it! :)")
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.face' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.face' ran by ")) + (str (ctx.message.author)))

#   brawlstars

@client.command(help="?", brief="?", pass_context=True)
async def BrawlStars(ctx):
    num_lines = sum(1 for line in open ("C:\\Users\\Draggie\\iCloudDrive\\iCloud~is~workflow~my~workflows\\Brawl Stars Counter.txt"))
    await ctx.send((str ("I have opened Brawl Stars ***")) + (str (num_lines)) + (str ("***  times since the 19th October 2020.")))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.lines' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   log search

@client.command(help="Searches log for term. Syntax .log [term]", brief="Searches server's message log for term.", pass_context=True)
async def log(ctx):
    message = ctx.message.content
    searchTerm = message.split(' ', 1)[-1]
    searchTerm = searchTerm.lower()
    serverID = ctx.message.guild.id
    serverName = ctx.message.guild.name
    file=open(((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\MessageLog.txt"))),encoding="UTF-8").read().lower()
    count=file.count(searchTerm)

    count = count - 1
    
    #await ctx.send((str ("Searched message log file for '**")) + (str (searchTerm)) + (str ("**'. Found `")) + (str (count)) + (str ("` occurences!")))

    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{searchTerm}**':", value=f"{count}", inline=False)
    embed.set_footer(text=((str (f"Not case sensitive. Does not account bot messages. Searching in server {serverID}/{serverName}."))))
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.log' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

@slash.slash(name="stats", description="Useful bot statistics.")
async def stats(ctx):
    YTAPI_Status = "Enabled"
    SCAPI_Status = "Mixed results"  

    if round(client.latency * 1000) <= 100:
        pingColour = (0x44ff44)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xffd000)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xff6600)
    else:
        pingColour = (0x990000)

    fileSizeBytes = os.path.getsize('D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\GitHub\\BaguetteBot\\BaguetteBot.py')

    num_lines = sum(1 for line in open ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\GitHub\\BaguetteBot\\BaguetteBot.py", encoding='utf-8'))

    global secsOrMins1
    global secsOrMins2
    secsOrMins2 = "seconds"
    secsOrMins1 = "seconds"
    current_time = time.time()
    uptimeInSeconds = int(round(current_time - start_time))

    uptime_stillInSeconds = uptimeInSeconds
    print((str ("Uptime In Seconds: ")) + (str (uptime_stillInSeconds)))

    if uptimeInSeconds > 60:
        uptimeInSeconds = int(round(uptimeInSeconds / 60))
        secsOrMins2 = "minutes"

    real_uptimeInSeconds = int(round(current_time - ready_start_time))
    if real_uptimeInSeconds > 60:
        real_uptimeInSeconds = int(round(real_uptimeInSeconds / 60))
        secsOrMins1 = "minutes"

    ping = round(client.latency * 1000)

    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    DIR = 'D:\\BaguetteBot\\AudioCache\\'
    cachedVideos = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

    embed = discord.Embed(title="_**Bot Stats**_\n", colour=(pingColour))
    embed.add_field(name="Lines of Code", value="{} lines".format(num_lines), inline=False)    
    embed.add_field(name="File Size", value=((str (fileSizeBytes)) + (str (" bytes"))), inline=False)    
    embed.add_field(name="**Uptime:**", value=((str (real_uptimeInSeconds)) + (str (" ")) + (str (secsOrMins1)) + (str (" (")) + (str (uptimeInSeconds)))  + (str (" ")) + (str (secsOrMins2)) + (str (" since run)")), inline=False)
    embed.add_field(name="**Ping:**", value=((str (ping)) + (str (" ms"))), inline=False)
    embed.add_field(name="**YouTube Videos Loaded:**", value=((str (cachedVideos))), inline=False)
    embed.add_field(name="**Servers :**", value=(servers), inline=False)
    embed.add_field(name="**Members in All Servers:**", value=(members), inline=False)
    #embed.add_field(name="**Random Integer:**", value=(random.randint(0,10000000)), inline=False)

    embed.add_field(name="\n**Debug Mode:**", value="Disabled")
    embed.add_field(name="**Command Logging:**", value="Enabled")
    embed.add_field(name="**Message Logging:**", value="Enabled")
    embed.add_field(name="**Voice Channels:**", value="Enabled")
    embed.add_field(name="**YouTube Player:**", value=(YTAPI_Status))
    embed.add_field(name="**Supercell API:**", value=(SCAPI_Status))

    embed.set_footer(text=((str ("\nDraggieBot.py | ")) + (str (DraggieBot_version))))
    await ctx.send(embed=embed)

    #await ctx.send((str ("DraggieBot currently has ***")) + (str (num_lines)) + (str ("***  lines of code. ")) + (str ("(***")) + (str (DraggieBot_version)) + (str ("***)")))

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.stats' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   divide by zero

@client.command(help="Starts or querys a server instance.\n\nSyntax:\n.server - Shows details about the server mc.ibaguette.com.\n.server [smp | test] - Starts the specified server", brief="Starts or querys a server instance.", pass_context=True)
async def server(ctx):
    txt = ctx.message.content
    x = txt.split()
    try:
        version = (str (x[1]))

        if version == '1.17':
        
            os.chdir("D:\\Minecraft Server\\1.17 Fabric\\")
            os.startfile("D:\\Minecraft Server\\1.17 Fabric\\start.bat")
            embed_1 = Embed(title='Server status', description="Checking dependances...")
            await ctx.send(embed=embed_1)

            message = ctx.channel.last_message
            
            try:
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await asyncio.sleep(1)

                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
            except Exception:
                await message.delete()
                await asyncio.sleep(6)
                f = open("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                e = f.read()
                f.close()

                good = ("done")
                bad = ("fatal")

                print (e.lower())
                if good in e.lower():
                    print("Done!")
                    await ctx.send("Done!")

                if bad in e.lower():
                    await ctx.send("Fatal error occured. Output:")
                    file=discord.File("D:\\Minecraft Server\\1.17 Fabric\\logs\\latest.log")
                    await ctx.send(file=file)
            os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot")

        if version == 'smp':
        
            os.chdir("D:\\Minecraft Server\\SMP standalone\\")
            os.startfile("D:\\Minecraft Server\\SMP standalone\\start.bat")
            embed_1 = Embed(title='Server status', description="Checking dependances...")
            await ctx.send(embed=embed_1)

            message = ctx.channel.last_message
            
            try:
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)

                await asyncio.sleep(1)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await asyncio.sleep(1)

                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                log = f.read()
                newEmbed = Embed(title='Server Status', description=(log))
                f.close()
                await message.edit(embed=newEmbed)
            except Exception:
                await message.delete()
                await asyncio.sleep(6)
                f = open("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                e = f.read()
                f.close()

                good = ("done")
                bad = ("fatal")

                print (e.lower())
                if good in e.lower():
                    print("Done!")
                    await ctx.send("Done!")

                if bad in e.lower():
                    await ctx.send("Fatal error occured. Output:")
                    file=discord.File("D:\\Minecraft Server\\SMP standalone\\logs\\latest.log")
                    await ctx.send(file=file)
            os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot")
    except:
        server = MinecraftServer.lookup("mc.ibaguette.com")
        status = server.status()
        await ctx.send("mc.ibaguette.com: Players online: `{0}`".format(status.players.online))
        latency = server.ping()
        await ctx.send("mc.ibaguette.com: Server ping: `{0} ms`".format(latency))
        query = server.query()
        messagetosend = ("mc.ibaguette.com: Players connected: `{0}`".format(", ".join(query.players.names)))
        if messagetosend == ('mc.ibaguette.com: Players connected: ``'):
            await ctx.send("No players online")
        else:
            await ctx.send(messagetosend)


#   Leave voice channel id thre is no one in it

#@client.event
#async def on_voice_state_update(member, before, after):
#    voice_state = member.guild.voice_client
#    if voice_state is None:
#        # Exiting if the bot it's not connected to a voice channel
#        return 
#
#    if len(voice_state.channel.members) == 1:
#        await voice_state.disconnect()


#   divide by zero

@client.command(help="Breaks code by dividing by zero.", brief="Raises an error.", pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def kill(ctx):
    zero = 2/0
    print (zero)
    print ((str ("\nCOMMAND RAN -> '.break' ran by ")) + (str (ctx.message.author)))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.break' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   play

@client.command(help="Plays audio at specified directory.", brief="[Audio] Plays audio at directory", pass_context=True)
async def sfx(ctx):
    tighe1 = round(time.time() * 1000)
    channel = ctx.author.voice.channel
    txt = ctx.message.content
    x = txt.split()
    sp1 = txt.split(' ', 2)[-1]

    term = x[1]
    if "french" in term.lower():
        toPlay = "D:\\BaguetteBot\\QuickAudio\\FrenchAccordion"
    elif "end2" in term.lower():
        toPlay = "D:\\BaguetteBot\\QuickAudio\\NightNight2"
    else:
        await ctx.send(f"No valid sound file found for *{term}*")
        return

    try:
        voice_client = ctx.guild.voice_client
        voice_client.stop()
        voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe", source=(toPlay)))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 0.5
        tighe2 = round(time.time() * 1000)

        nTighe = tighe2 - tighe1
        ping = round(client.latency * 1000)
        tot = nTighe + ping

        await ctx.send(f"Executed, delay = **{tot}ms** (**{nTighe}ms** processing + Discord API **{ping}ms**)")

        f = open(GlobalLogDir, "a")
        f.write((str ("\nAUDIO COMMAND RAN -> '.sfx' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nAUDIO COMMAND RAN -> '.sfx' ran by ")) + (str (ctx.message.author)))
    except:
        channel = ctx.author.voice.channel
        await channel.connect()
        await sfx(ctx)

@client.command(help="Plays audio at specified directory.", brief="[Audio] Plays audio at directory", pass_context=True)
async def playdir(ctx):
    async with ctx.typing():
        channel = ctx.author.voice.channel
        text = ctx.message.content
        #await ctx.send("IDE detected! Unable to run command. Aborting.\nFeature enabled in v1.1")
        #return
        sp1 = text.split(' ', 1)[-1]

        try:
            my_file = Path((str (sp1)))
            if my_file.is_file():
                voice_client = ctx.guild.voice_client
                voice_client.stop()
                voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe", source=(str (sp1)))) 
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
                voice_client.source.volume = 0.5

                await ctx.message.add_reaction('✅')
            else:
                await ctx.message.add_reaction('❌')
                embed=discord.Embed(title="An error occured", description="*File doesn't exist lmao*", color=0x990000)
                await ctx.send(embed=embed)
                return
            f = open(GlobalLogDir, "a")
            f.write((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
            f.close()
            print ((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)))

        except:
            channel = ctx.author.voice.channel
            await channel.connect()
            await playdir(ctx)

#   oldPlay

@client.command(help="Plays audio at predefined directory.", brief="[Audio] Plays audio using old version", pass_context=True)
async def oldplay(ctx):
    channel = ctx.author.voice.channel
    #await ctx.send("IDE detected! Unable to run command. Aborting.\nFeature enabled in v1.1")
    #return
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\bin\\ffmpeg.exe", source=(str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Files\\")) + (str (sp1))))
    await ctx.send((str ("Playing audio '*") + (str (sp1)) + (str ("*' in voice channel *#")) + (str (channel))) + (str ("* using ffmpeg version from *31/08/2020*")))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nAUDIO COMMAND RAN -> '.oldplay' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nAUDIO COMMAND RAN -> '.oldplay' ran by ")) + (str (ctx.message.author)))  

#   play

@client.command(help="Sends what is written to the message log.", brief="Sends what is written to the message log.", pass_context=True)
async def message(ctx):
    messageRepeat = ctx.message.content
    serverName = ctx.message.guild.name
    await ctx.send((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (ctx.message.author)) + (str (" in [{}".format(serverName) + " - #{}]".format(ctx.channel.name))) + (str (" at ") + (str (datetime.now()))))

#   Stream YT

#@client.command(help=".", brief="[Audio] Sets audio volume (WARNING BROKEN)", pass_context=True)
#async def volume(ctx):
#    await ctx.send("Command is being worked on :)")

#   Stream YT

@client.command(help="Streams youtube audio into voice channel.", brief="Plays YouTube video", pass_context=True)
async def url(ctx, url: str):
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(URL))
    await ctx.send((str ("Streaming audio")))

#   spam

@client.command(help="Spam", brief="Spams. Syntax [number] [text]", pass_context=True)
async def spam(ctx):
    text = ctx.message.content
    txt = ctx.message.content
    x = txt.split()
    sp1 = text.split(' ', 2)[-1]
    spamNumber = (int (x[1]))
    print(x[1])
    while (int (spamNumber)) > (str ("1")):
        await ctx.send(sp1)
        spamNumber = (int (spamNumber)) - (int ("1"))

#   download

@client.command(help="Downloads a youtube video.", brief="Downloads an entire YouTube video", pass_context=True)
async def download(ctx, url: str):
    async with ctx.typing():
        os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\youtube-dl")
        text = ctx.message.content
        sp1 = text.split(' ', 1)[-1]
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
            'merge-output-format': 'mp4',
            'default_search': 'ytsearch',
            'quiet': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            await ctx.send("Attempting to download...")
            ydl.download([sp1])
            await ctx.channel.purge(limit=1)
            print("Done!")
            await ctx.send("Done!")

#   Invite link

@client.command()
async def create_invite(ctx):
    if ctx.message.author.id == 382784106984898560:
        txt = ctx.message.content
        x = txt.split()
        channel = int(x[1])
        channel = client.get_channel(channel)
        #print(channel)
        link = await channel.create_invite(max_age = 69)
        await ctx.send(str ("Channel invite link: ") + (str (link)))
    else:
        await ctx.send("Error 5: `command reserved for bot developer(s)`")

@client.command()
async def addroles(ctx):
    if ctx.message.author.id == 382784106984898560 or ctx.message.author.id == 606583679396872239 or ctx.message.author.id == 854323313631559680:
        member = ctx.message.author
        for r in ctx.guild.roles:
            try: # it will error if the bot has insufficient perms to give a role
                await ctx.author.add_roles(r)
                #await ctx.send(f"Good: **`{r.name}` given** to {member}")
            except Exception as e:
                print(f"Error: **`{r.name}` couldn't be given** to {member}: {e}")
        #await ctx.send(f"Successfully gave {member} all the roles I could!")
    else:
        await ctx.send("Error 5: `command reserved for bot developer(s)`")

@client.command()
async def adaptor(ctx):
    if ctx.message.author.id == 382784106984898560:
        txt = ctx.message.content
        x = txt.split()
        server = int(x[1])
        sp1 = txt.split(' ', 2)[-1]
        guild = await client.fetch_guild(server)
        await guild.edit(name=sp1)
    else:
        await ctx.send("Error 5: `command reserved for bot developer(s)`")
    
#@client.command()
#async def seek():
#    x = 1

#   YouTube search, download, convert, play.

@client.command(help="Downloads a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Searches for and plays YouTube video", pass_context=True)
async def yt(ctx, url: str):
    async with ctx.typing():
        await ctx.send("Warning: This is the legacy youtube player. It takes a long time if a video has not been played prevoiusly. Use `.yts` to stream audio directly.")
        global hasVideo
        testForToggles = ctx.message.content
        debugMode = False
        quickMode = False
        if ("/d") in testForToggles.lower():
            if ctx.message.author.guild_permissions.administrator == True:
                debugMode = True
                await ctx.send("Executing with debug mode enabled...")
            else:
                await ctx.send("You cannot use the debug mode toggle.")

        if ("/q") in testForToggles.lower():
            if ctx.message.author.guild_permissions.administrator == True:
                quickMode = True
                await ctx.send("Executing with quick mode enabled...")
            else:
                await ctx.send("You cannot use the quick mode toggle.")
        try:
            voice = ctx.guild.voice_client
            #await ctx.send("IDE detected! Unable to run command. Aborting.\nFeature enabled in v1.1")
            #return
            os.chdir("D:\\BaguetteBot\\AudioCache")
            text = ctx.message.content

            millisecs = round(time.time() * 1000)

            voice.stop()
            searchTerm = text.split(' ', 1)[-1]

            results = YoutubeSearch(searchTerm, max_results=1).to_dict()

            print (results)
            if len(results) == 0:
                await ctx.send(f"No results found for **{searchTerm}**")
                return

            if debugMode == True:
                await ctx.send((str ('\n\nResults = ')) + (str (results)))
            for v in results:
                id = v['id']
                result = ('https://www.youtube.com/watch?v=' + v['id'])

                my_file = Path((str ("D:\\BaguetteBot\\AudioCache\\")) + (str (id)))
                if my_file.is_file():
                    global hasVideo
                    #await ctx.send("fileExists=True")
                    hasVideo = "True"
                    print("hasvideo set to true")
                else:
                    hasVideo = "False"
                if debugMode == True:
                    await ctx.send((str ('\n\nResult = ')) + (str (result)))

                ydl_opts = {}

                global video_title

                video_title = id

                video = result

                if quickMode != True:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(video, download=False)
                        video_title = info_dict.get('title', None)

                print((str ('\n\nResult = ')) + (str (result)))
                await ctx.send((str ('Processing: `')) + (str (video_title)) + (str ("`.")))
                url = result
                text = ctx.message.content
            
            #print(id)
            if hasVideo == "True":
                print("hasvideo = true")
                my_file = Path((str ("D:\\BaguetteBot\\AudioCache\\")) + (str (id)))
                voice.play(discord.FFmpegPCMAudio(my_file))
                doneMillisecs = round(time.time() * 1000)
                nTighem = doneMillisecs - millisecs
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.3
                print("cached")
                if debugMode == True:
                    await ctx.send((str ("Playing: **")) + (video_title) + (str("** (avec `time taken: ")) + (str (nTighem)) + (str ("ms`)\n\nattrs:\nplayingFromCache")))
                else:
                    await ctx.send((str ("Playing: **")) + (video_title) + (str("** (avec `time taken: ")) + (str (nTighem)) + (str ("ms`). `c=t`,`d=f`)"))) #    c=t means cache = true. s=f means downloaded = false
            else:
                print("uncached else")
                #currenttime = datetime.time()
                
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'quiet': True,
                    'outtmpl': (id),
                    #'external-downloader': 'D:\\Downloads\\aria2c\\aria2c.exe',
                    #'external-downloader-args': '-j 16 -x 16 -s 16'
                    #'postprocessors': [{
                    #    'key': 'FFmpegExtractAudio',
                    #    'preferredcodec': 'mp3',
                    #    'preferredquality': '320',
                    #}],
                }

                #iDuration = results["duration"]
                #if iDuration > 30:
                #    await ctx.send("Video is too long.")
                #    return

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    info_dict = ydl.extract_info(result, download=False)
                    video_title = info_dict.get('title', None)

                filename = (id)
                if debugMode == True:
                    await ctx.send((str ('\n\nFilename = ')) + (filename))

                for file in os.listdir("./"):
                    if file.endswith(".part"):
                        name = file
                        print(f"File: {file}\n")
                        try:
                            os.remove(file)
                            print(f"Removed file {file}")
                            if debugMode == True:
                                await ctx.send((str (f"Successfully removed {name}")))
                        except:
                            print(f"Failed to remove file {file}")
                            if debugMode == True:
                                await ctx.send((str (f"Failed to remove {name}")))

                doneMillisecs = round(time.time() * 1000)
                try:
                    voice.play(discord.FFmpegPCMAudio(filename))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.3
                except:
                    await ctx.send("Warning! Timed out. Reconecting...")
                    channel = ctx.author.voice.channel
                    await channel.connect()       
                    voice.play(discord.FFmpegPCMAudio(filename))
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.3
                
                nTighem = doneMillisecs - millisecs

                if debugMode == True:
                    await ctx.send((str ("value nTighem = ")) + (str (nTighem)))

                name = filename
                nName = name.rsplit("-", 1)
                vName = nName[0]

                if debugMode == True:
                    await ctx.send((str ("value nName = ")) + (str (nName)))
                if debugMode == True:
                    await ctx.send((str ("value vName = ")) + (str (vName)))

                await ctx.send((str ("Playing: **")) + (video_title) + (str("** (avec `time taken: ")) + (str (nTighem)) + (str("ms`). `c=f`,`d=t`)")))
                print((str ("Playing: **")) + (video_title) + (str("** (avec `time taken: ")) + (str (nTighem)) + (str("ms`). `c=f`,`d=t`)")))
        except Exception as e:
            try:
                try:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    await yt(ctx, url)
                except:
                    await ctx.send(f"An error occured and idk what it is. It says: `{e}`. Please report this in github/baguettebot/issues or DM Draggie#3060 with your server ID.")
            except:
                await ctx.send("An error occured.")
    
#   Grave key: `
#   Bullet point: • 

#   ytstream

@client.command(help="Streams a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Streams YT audio. Sligthly buggy, may die randomly.", pass_context=True)
async def yts(ctx):
    async with ctx.typing():
        testForToggles = ctx.message.content
        debugMode = False
        if ("/d") in testForToggles.lower():
            if ctx.message.author.guild_permissions.administrator == True:
                debugMode = True
            else:
                await ctx.send("Your server administrator has disabled the option to use the debug mode toggle.")

        try:
            text = ctx.message.content
            #await ctx.send("IDE detected! Unable to run command. Aborting.\nFeature enabled in v1.1")

            searchTerm = text.split(' ', 1)[-1]

            millisecs = round(time.time() * 1000)

            results = YoutubeSearch(searchTerm, max_results=1).to_dict()

            for v in results:
                result = ('https://www.youtube.com/watch?v=' + v['id'])
                print((str ('\nresult = ')) + (str (result)))
                if debugMode == True:
                    await ctx.send((str ('DEBUG: Loading: `')) + (str (result)) + (str ("`")))
                url = result
            
                text = ctx.message.content

                YTDL_OPTIONS = {
                    'format': 'bestaudio/best',
                    'extractaudio': True,
                    'audioformat': 'mp3',
                    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                    'restrictfilenames': True,
                    'noplaylist': True,
                    'nocheckcertificate': True,
                    'ignoreerrors': False,
                    'logtostderr': False,
                    'quiet': True,
                    'no_warnings': True,
                    'default_search': 'auto',
                    'source_address': '0.0.0.0',
                }

                FFMPEG_OPTIONS = {
                    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn',
                }

                with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
                    info = ydl.extract_info(url, download=False)
                    URL = info['formats'][0]['url']

                try:
                    voice_client = ctx.guild.voice_client
                    voice_client.stop()
                except Exception:
                    channel = ctx.author.voice.channel
                    await channel.connect()

                voice_client.play(discord.FFmpegPCMAudio(URL, executable="D:\\Downloads\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\bin\\ffmpeg.exe", options=FFMPEG_OPTIONS))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
                voice_client.source.volume = 0.3
                doneMillisecs = round(time.time() * 1000)
                timeDelay = doneMillisecs - millisecs

                nname = result.rsplit("=", 1)
                #nTighem = datetime.time()
                await ctx.send((str ("Playing: ")) + (nname[1]) + (str("\n`time taken: ")) + (str (timeDelay)) + (str("ms`")))
                await ctx.send("btw: youtube playing is runing in streaming mode, this may lead to audio randomly cutting off!")
        except AttributeError:
            await ctx.send("You are not in a voice channel. You need to be in one to use audio commands.")
            return
        except:
            if debugMode == True:
                await ctx.send('DEBUG: An error cccured, most likely the bot is not in a channel already. Reconnecting...')
            channel = ctx.author.voice.channel
            await channel.connect()
            await yts(ctx)

#   Get links

@client.command(help="Gets YouTube video raw links.", brief="Gets YouTube video's and raw audio URL", pass_context=True)
async def links(ctx):
    async with ctx.typing():
        text = ctx.message.content
        searchTerm = text.split(' ', 1)[-1]

        results = YoutubeSearch(searchTerm, max_results=1).to_dict()

        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print(result)
            url = result
        
            text = ctx.message.content

            ydl_opts = {'format': 'bestaudio'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                print((str ('\n\nurl = ')) + (str (URL)))
                embed = discord.Embed()
                embed.description = ((str ("[audio url](")) + (str (URL)) + (str (")")))
                await ctx.send(embed=embed)

#            ydl_opts = {'format': 'bestvideo/best'}
#            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#
#                info = ydl.extract_info(url, download=False)
#                URL = info['formats'][0]['url']
#                embed = discord.Embed()
#                embed.description = ((str ("[video url](")) + (str (URL)) + (str (")")))
#                await ctx.send(embed=embed)

#   Pause audio

#@client.command(help="Pauses the current audio.", brief="[Audio] Pauses audio", pass_context=True)
#async def pause(ctx):    
#    voice_client = ctx.guild.voice_client
#    if voice_client.is_playing():
#        voice_client.pause()
#        await ctx.send("*✅ Paused audio!*")
#    else:
#        await ctx.send("Audio is unable to be paused")

#   Resumes audio

#@client.command(help="Resumes playing the current audio.", brief="[Audio] Resumes audio", pass_context=True)
#async def resume(ctx):    
#    voice_client = ctx.guild.voice_client
#    if voice_client.is_paused():
#        voice_client.resume()
#        await ctx.send("*✅ Resumed playing audio!*")
#    else:
#        await ctx.send("Audio is unable to be resumed")

#   Stop audio

#@client.command(help="Stops playing the current audio.", brief="[Audio] Stops audio", pass_context=True)
#async def stop(ctx):    
#    voice_client = ctx.guild.voice_client
#    voice_client.stop()
#    await ctx.send((str ("Stopped playing audio.")))
#    f = open(GlobalLogDir, "a")
#    f.write((str ("\nAUDIO COMMAND RAN -> '.stop' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
#    f.close()
#    print ((str ("\nAUDIO COMMAND RAN -> '.stop' ran by ")) + (str (ctx.message.author)))
#    return

#   join/leave voice

#@client.command(help="Joins message author's voice channel", brief="[Audio] Joins voice chat", pass_context=True)
#async def join(ctx):#    Joins
#    try:
#        channel = ctx.author.voice.channel
#        await channel.connect()
#        await ctx.send((str ("Joined voice channel *")) + (str (channel)) + (str ("*.")))
#    except:
#        await ctx.send("You are not in a voice channel, please join one before running the command.")
#        return
#    f = open(GlobalLogDir, "a")
#    f.write((str ("\nAUDIO COMMAND RAN -> '.join' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
#    f.close()
#    print ((str ("\nAUDIO COMMAND RAN -> '.join' ran by ")) + (str (ctx.message.author)))  

#@client.command(help="Leaves message author's voice channel", brief="[Audio] Leaves voice chat", pass_context=True)
#async def leave(ctx):#  Leaves
#    try:
#        channel = ctx.voice_client.channel
#        await ctx.voice_client.disconnect()
#        await ctx.send((str("Left voice channel "))+(str(channel)))
#    except:
#        await ctx.send("Can't leave a voice channel when I'm not in a voice channel..?")
#    f = open(GlobalLogDir, "a")
#    f.write((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
#    f.close()
#    print ((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (ctx.message.author)))  

#   Purge

@client.command(help="Purges a specified amount of messages", brief="Purges messages", pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'King')
async def purge(ctx):
    if ctx.message.author.id == 382784106984898560:
        async with ctx.typing():
            txt = ctx.message.content
            x = txt.split()
            print(x[1])
            y = (int (x[1])) + 1

            if (x[1]) == 1:
                await ctx.channel.purge(limit = y)
                await ctx.send(str ("Deleted ") + (x[1]) + (str (" message!")))
                f = open(GlobalLogDir, "a")
                f.write((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
                f.close()
                print ((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)))
                return  
            if y <= 21:
                await ctx.channel.purge(limit = y)
                await ctx.send(str ("Deleted ") + (x[1]) + (str (" messages!")))
                f = open(GlobalLogDir, "a")
                f.write((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
                f.close()
                print ((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)))
                return
            if (x[1]) == 69:
                await ctx.send(str ("Nice"))  
            f = open(GlobalLogDir, "a")
            f.write((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
            f.close()
            print ((str ("\nCOMMAND RAN -> '.purge' ran by ")) + (str (ctx.message.author)))
    else:
        await ctx.send("You don't have permissions for that u sussy boi")

#   i g n o r e

@client.command(help="UwU", brief="UwU", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def uwu(ctx):
    uwuwu = random.randint(1,2)
    if uwuwu == 1:
        await ctx.send(file=discord.File(r"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Assets\\Commands\\I_regret_making_this.png", filename="UwU.png"))
    if uwuwu == 2:
        await ctx.send(file=discord.File(r"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Assets\\Commands\\canvas_1.png", filename="canvas_1.png"))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.uwu' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.uwu' ran by ")) + (str (ctx.message.author)))  

#   change nickname

@client.command(help = "Changes nickname", brief = "Changes nickname for mentioned user", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def chnick(ctx):
    text = ctx.message.content
    member = ctx.message.author
    sp1 = text.split(' ', 1)[-1]
    await member.edit(nick=sp1)

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.chnick' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.chnick' ran by ")) + (str (ctx.message.author)))

#   brawl stars API

@client.command(help = "Use: .bs <PLAYER TAG IN C", brief = "Interacts with the Brawl Stars API. Type '.help bs' for usage", pass_context=True)
async def bs(ctx):
    async with ctx.typing():
        txt = ctx.message.content
        x = txt.split()
        print(x[1])
        playerTag = (x[1])
        playerTag = playerTag.upper()

        print((str ('playerTag = ') + (str (playerTag))))

        if (x[2]) == 'brawlers':
            url = ((str ('https://api.brawlstars.com/v1/players/%23')) + (str (playerTag)))
            print((str ('url = ') )+ (str (url)))
            with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\supercell_api_key.txt", encoding="utf-8") as f:
                api_key = f.read()

            
            headers = {
            'Accept': 'application/json',
            'authorization': api_key,
            }
            brawlerRequest = requests.get(url, headers=headers)
            brawlerRequestStr = (str (brawlerRequest))

            brawlerRequestStatusCode = brawlerRequest.status_code
            if brawlerRequestStatusCode == 404:
                embed=discord.Embed(description=('Supercell Servers sent this:\n\n'))
                embed.add_field(name="Response", value=brawlerRequestStr, inline=False)
                embed.set_footer(text="404 Not Found")
                await ctx.send(embed=embed)
                return

            
            print(brawlerRequest.status_code)

            path = ((str ("Z:\\#"))+(str(playerTag)) + (str(".json")))
            #print(brawlerRequest.json())

            if os.path.isfile(path):
                f = open(path, "w+")
                f.close()
        
            f = open(path, "w")
            f.write((str (brawlerRequest.json())))
            f.close()

            try:
                await ctx.send((str ('Recieved this response from Supercell Servers:\n\n' )) + (str (brawlerRequest.json())))
            except:
                await ctx.send(file=discord.File(path))

        if (x[2]) == 'battles':
            url = ((str (f'https://api.brawlstars.com/v1/players/%23{playerTag}/battlelog')))

            with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\supercell_api_key.txt", encoding="utf-8") as f:
                api_key = f.read()
            headers = {
            'Accept': 'application/json',
            'authorization': api_key,
            }
            brawlerRequest = requests.get(url, headers=headers)
            brawlerRequestStr = (str (brawlerRequest))
            brawlerRequestStatusCode = brawlerRequest.status_code
            print(brawlerRequestStr)
            path = ((str ("Z:\\#"))+(str(playerTag)) + (str(".json")))
            #print(brawlerRequest.json())

            if os.path.isfile(path):
                f = open(path, "w+")
                f.close()
        
            f = open(path, "w", encoding="UTF-8")
            f.write((str (brawlerRequest.json())))
            f.close()
            try:
                await ctx.send((str ('Recieved this response from Supercell Servers:\n\n' )) + (str (brawlerRequest.json())))
            except:
                await ctx.send(file=discord.File(path))

#   SPLIT TESTS

@client.command(brief = "test split msg str", pass_context=True)
async def testsplit(ctx):
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    await ctx.send(sp1)
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.testsplit' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.testsplit' ran by ")) + (str (ctx.message.author)))  

#   FILE TEST

@client.command(brief = "tests for file", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def testForFile(ctx):
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    print (sp1)
    my_file = Path((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Files\\")) + (str (sp1)))
    if my_file.is_file():
        await ctx.send("fileExists=True")
    else:
        await ctx.send("fileExists=False")
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.testForFile' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.testForFile' ran by ")) + (str (ctx.message.author)))  

#   Birthdays

@client.command(help = "Writes your birthday to a file. Use .birthday set [date] to set birthday, and .birthday file to get a list of birthdays.", brief = "Sets your birthday, syntax '.birthday set [your birth date]",pass_context=True)
async def birthday(ctx):
    async with ctx.typing():
        try:
            text = ctx.message.content
            syntaxErrorChecker = text.split(' ', 1)[-1]
            birthDate = text.split(' ', 2)[-1]
            x = text.split()
            if x[1] == "file":
                with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\logs\\birthdays.txt") as file:
                    birthdays = file.read()
                    embed=discord.Embed(title="All Birthdays", description=(birthdays), colour=0x00acff)
                    await ctx.send(embed=embed)
                    return
            print(x[2])
            if '/' in syntaxErrorChecker:
                await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")
                return
            if '.' in syntaxErrorChecker:
                await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")
                return

            if x[1] == "file":
                with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\logs\\birthdays.txt") as file:
                    birthdays = file.read()
                    embed=discord.Embed(title="All Birthdays", description=(birthdays), colour=0x00acff)
                    await ctx.send(embed=embed)
            if (x[1]) == "0":
                await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")

            if x[1] == "set":
                author = (str (ctx.message.author.id))
                file=open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Logs\\birthdays.txt",encoding="UTF-8").read()
                count=file.count(author)
                print (count)
                if count != 0:
                    await ctx.send("Error! You have already added your birthday to the file. Please ask an admin to remove it if you believe this is an error.")    
                    return

                f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\logs\\birthdays.txt", "a")
                f.write((str ("\n<@!")) + (str (ctx.message.author.id)) + (str (">'s birthday is on the ") + (str(birthDate))))
                f.close()
                await ctx.send((str ("\n")) + (str (ctx.message.author)) + (str ("'s birthday has been set to `") + (str(birthDate)) + (str ("`. A custom message will be sent, enjoy!"))))
        
        except Exception:
            await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")

#   DLfile  

@client.command(help = "Downloads file at specific directory.", brief = "Downloads any file on my PC (8mb max)",pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def dlfile(ctx):
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    print (sp1)
    await ctx.send(file=discord.File((str (sp1))))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.dlfile' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.dlfile' ran by ")) + (str (ctx.message.author)))  

#   Dir

@client.command(help = "Specify the directory to display all items in it.", brief = "Shows all files in my PC...",pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def dir(ctx):
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    arr = os.listdir((str (sp1)))
    embed=discord.Embed(title=(str ("Directory lookup: ")) + ((str (sp1))), description=(str (arr)) + (str ("\n\nInit by ")) + ((str ("{}".format(ctx.author.mention)))), colour=0xFF5800)
    await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.dir' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.dir' ran by ")) + (str (ctx.message.author)))  

#   Files

@client.command(help = "Lists all files in DraggieBot's file directory.", brief = "Lists available files", pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def files(ctx):
    arr = os.listdir('D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Files')
    embed = discord.Embed
    embed=discord.Embed(title="List of all files", description=(str (arr)) + (str ("\n\n Add a file by going to http://bit.ly/DraggieBotFiles.")), colour=0x00acff)
    await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.files' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.files' ran by ")) + (str (ctx.message.author)))   

#   File

@client.command(help = "Sends a file in DraggieBot's directory.", brief = "Sends files", pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def file(ctx):
    txt = ctx.message.content
    x = txt.split()
    print(x[1])
    my_file = Path((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Files\\")) + (str (x[1])))
    if my_file.is_file():
#           await ctx.send("True")
        await ctx.send(file=discord.File((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Files\\")) + (str (x[1]))))
    else:
        embed=discord.Embed(title="Error: 404", description=((str ("File ")) + (str ((x[1]))) + (str (" not found!"))), colour=0x990000)
        await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.file' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.file' ran by ")) + (str (ctx.message.author)))     

#   Drop

@client.command(help = "drop", brief = "Where we droppin?", pass_context=True)
async def drop(ctx):

    dropLocation = random.randint(1,34)

    if dropLocation == 1:
        await ctx.send("Salty Towers")
    if dropLocation == 2:
        await ctx.send("Weather Station (G7)")
    if dropLocation == 3:
        await ctx.send("Redacted Bunker (G7)")
    if dropLocation == 4:
        await ctx.send("Zero Point (E4)")
    if dropLocation == 5:
        await ctx.send("Holly Hedges")
    if dropLocation == 6:
        await ctx.send("Sweaty Sands")
    if dropLocation == 7:
        await ctx.send("Pleasant Park")
    if dropLocation == 8:
        await ctx.send("Craggy Cliffs")
    if dropLocation == 9:
        await ctx.send("Steamy Stacks")
    if dropLocation == 10:
        await ctx.send("Collosal Collisium")
    if dropLocation == 11:
        await ctx.send("Dirty Docks")
    if dropLocation == 12:
        await ctx.send("Retail Row")
    if dropLocation == 13:
        await ctx.send("Lazy Lake")
    if dropLocation == 14:
        await ctx.send("Misty Meadows")
    if dropLocation == 15:
        await ctx.send("Weeping Woods")
    if dropLocation == 16:
        await ctx.send("Slurpy Swamp")
    if dropLocation == 17:
        await ctx.send("Coral Castle")
    if dropLocation == 18:
        await ctx.send("Hunter's Haven")
    if dropLocation == 19:
        await ctx.send("Camp Cod (G8)")
    if dropLocation == 20:
        await ctx.send("Lake Canoe (G5)")
    if dropLocation == 21:
        await ctx.send("Lockie's Lighthouse (C1)")
    if dropLocation == 22:
        await ctx.send("Stealthy Stronghold")
    if dropLocation == 23:
        await ctx.send("The Orchard (F3)")
    if dropLocation == 24:
        await ctx.send("Hydro 16 (D7)")
    if dropLocation == 25:
        await ctx.send("Flush Factory (D8)")
    if dropLocation == 26:
        await ctx.send("Risky Reels (E3/4)")
    if dropLocation == 27:
        await ctx.send("Castle ruins (A3)")
    if dropLocation == 28:
        await ctx.send("Shipping containers (A3)")
    if dropLocation == 29:
        await ctx.send("Drop as soon as you can!")
    if dropLocation == 30:
        await ctx.send("Furthest place away from the bus!")
    if dropLocation == 31:
        await ctx.send("bruh...")
    if dropLocation == 32:
        await ctx.send("idk lol")
    if dropLocation == 33:
        await ctx.send("Shanty Town (B6)")
    if dropLocation == 34:
        await ctx.send("Follow someone off spawn and pickaxe them!")


    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.drop' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.drop' ran by ")) + (str (ctx.message.author)))

#   Ship

@client.command(help="Ships people. Syntax: *.ship [person1] [person2]", brief="Ships 2 people out of 100.", pass_context=True)
async def ship(ctx):
    #   LOC NAMES
    txt = ctx.message.content
    x = txt.split()
    #print(x[1])
    y = (str (x[1]))
    z = (str (x[2]))
    #   CALC RAND
    shipMaths = random.randint(1,100)

    #   BIAS!

    if y == "oliver":
        shipMaths = shipMaths + 10
        print("True - oliver y")
    if y == "Oliver":
        shipMaths = shipMaths + 10
        print("True - Oliver y")

    if z == "Oliver":
        shipMaths = shipMaths + 10
        print("True - oliver z")
    if z == "oliver":
        shipMaths = shipMaths + 10
        print("True - Oliver z")
    
    if y == "sam":
        shipMaths = shipMaths + 10
        print("True - sam y")
    if y == "Sam":
        shipMaths = shipMaths + 10
        print("True - Sam y")

    if z == "sam":
        shipMaths = shipMaths + 10
        print("True - sam z")
    if z == "Sam":
        shipMaths = shipMaths + 10
        print("True - Sam z")

    if y == "jack":
        shipMaths = shipMaths + 10
        print("True - sam y")
    if y == "Jack":
        shipMaths = shipMaths + 10
        print("True - Jack y")

    if z == "jack":
        shipMaths = shipMaths + 10
        print("True - jack z")
    if z == "Jack":
        shipMaths = shipMaths + 10
        print("True - Jack z")

    if y == "nolly":
        shipMaths = shipMaths + 10
        print("True - noll y")
    if y == "Nolly":
        shipMaths = shipMaths + 10
        print("True - Noll y")
    if z == "nolly":
        shipMaths = shipMaths + 10
        print("True - noll z")
    if z == "Nolly":
        shipMaths = shipMaths + 10
        print("True - Noll z")

    if y == "nolwenn":
        shipMaths = shipMaths + 10
        print("True - nol y")
    if y == "Nolwenn":
        shipMaths = shipMaths + 10
        print("True - Nol y")
    if z == "nolwenn":
        shipMaths = shipMaths + 10
        print("True - nol z")
    if z == "Nolwenn":
        shipMaths = shipMaths + 10
        print("True - Nol z")

    if y == "ish":
        shipMaths = shipMaths + 10
        print("True - ish y")
    if y == "Ish":
        shipMaths = shipMaths + 10
        print("True - Ish y")
    if z == "ish":
        shipMaths = shipMaths + 10
        print("True - ish z")
    if z == "Ish":
        shipMaths = shipMaths + 10
        print("True - Ish z")
    if z == "<@!757978892370706573>":
        shipMaths = shipMaths + 10

    if y == "ismail":
        shipMaths = shipMaths + 10
        print("True - ism y")
    if y == "Ismail":
        shipMaths = shipMaths + 10
        print("True - Ism y")
    if z == "ismail":
        shipMaths = shipMaths + 10
        print("True - ism z")
    if z == "Ismail":
        shipMaths = shipMaths + 10
        print("True - Ism z")
    if y == "sam":
        if z == "jack":
            shipMaths = 100
            embed=discord.Embed(title="Shipping...", description=((str ("{}".format(ctx.author.mention))) + (str (" ships **")) + (str (y)) + (str (" x ")) + (str (z)) + (str ("**!")) + (str ("\n\nResult: **")) + (str (shipMaths) + (str ("**    out of 100!")))), colour=0x00acff)
            await ctx.send(embed=embed)
            return
    if y == "jack":
        if z == "sam":
            shipMaths = 100
            embed=discord.Embed(title="Shipping...", description=((str ("{}".format(ctx.author.mention))) + (str (" ships **")) + (str (y)) + (str (" x ")) + (str (z)) + (str ("**!")) + (str ("\n\nResult: **")) + (str (shipMaths) + (str ("**    out of 100!")))), colour=0x00acff)
            await ctx.send(embed=embed)
            return

    #   LONG STRING

    embed=discord.Embed(title="Shipping...", description=((str ("{}".format(ctx.author.mention))) + (str (" ships **")) + (str (y)) + (str (" x ")) + (str (z)) + (str ("**!")) + (str ("\n\nResult: **")) + (str (shipMaths) + (str ("**    out of 100!")))), colour=0x00acff)
    await ctx.send(embed=embed)
    #   LOG
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.ship' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.ship' ran by ")) + (str (ctx.message.author)))

#   broadcast

@client.command(pass_context=True)
async def broadcast(ctx, *, msg):
    if ctx.message.author.id == 382784106984898560:
        beans = 0
        fails = 0
        for guild in client.guilds:
            print(f"Locating channel in {guild}...")
            for channel in guild.text_channels:
                if channel.name == "event-log-baguette":
                    try:
                        await channel.send(msg)
                        beans = beans + 1
                        print(f"Successfully sent message in {guild} / {channel}!")
                        print (f"Sent in {beans} servers.")
                    except Exception as e:
                        print(f"Exception {e}")
                        fails = fails + 1
                        continue
                    else:
                        break
        await ctx.send(f"Done! Broadcasted message to {beans} servers, with {fails} failures.")
    else:
        await ctx.send("You do not have permission to run this command.")

#   Command template

@client.command(help="Lots of help goes here", brief="[template command]", pass_context=True)
async def COMMAND(ctx):
    await ctx.send("Sends a message.")
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.COMMAND' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.COMMAND' ran by ")) + (str (ctx.message.author)))

#   Nolwennium mine

@client.command(help="Mines a random amount of Nolwennium.", brief="Mines Nolwennium.", pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def mine(ctx):
    global balance
    global myuuid
    global address
    channelName = ctx.message.channel.name
    channelID = ctx.message.channel.id
    serverID = ctx.message.guild.id

    if serverID == 759861456300015657:
        if channelID != 785620979300302869:
            await ctx.send("You can't do that here! Try <#785620979300302869>.")
            return

    authorID = ctx.message.author.id
    person = ctx.message.author
    address = authorID
    #   Nolwennium UPDATED LOCATION 2/11/2021: D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\

    filedir = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\{authorID}.txt")
    newNumber = random.randint(1,10)
    fee = newNumber/(random.randint(50,200))
    newNumberAfterFee = newNumber - fee
    newNumberAfterFee = round(newNumberAfterFee, 3)
    fee = round(fee, 3)

    try:
        e = open(filedir, 'r')
        balance = (float (e.read()))
        e.close()
        minedString = (f"Mined another {newNumber} <:NolwenniumCoin:846464419503931443> Nolwennium!")
    except:
        e = open(filedir, 'w+')
        e.write(str (0))
        e.close()

        e = open(filedir, 'r')
        balance = (float (e.read()))
        e.close()
        minedString = (f"Mined {newNumber} <:NolwenniumCoin:846464419503931443> Nolwennium!")
        #return
    
    #await ctx.send((str ("\n\nYour address is: ")) + (str (address)))

    minedString_existing = (f"Mined another {newNumber} <:NolwenniumCoin:846464419503931443> Nolwennium!")
    minedString_new = (f"Mined {newNumber} <:NolwenniumCoin:846464419503931443> Nolwennium!")

    roleBooster = discord.utils.find(lambda r: r.name == 'Server Booster', ctx.message.guild.roles)

    Croissants = [796777705520758795, 821405856285196350, 588081261537394730]

    embed=discord.Embed(title="⛏️ Miner ⛏️", description = minedString, colour =0x44ff44)
    embed.add_field(name="**Fees Paid**", value=f"{fee} to <@{random.choice(Croissants)}>", inline=False)
    
    balance = balance + newNumberAfterFee

    if roleBooster in person.roles:
        BoosterBonus = random.randint(5,15)
        embed.add_field(name="**Server Booster Bonus**", value=(str (BoosterBonus)) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium")))
        balance = balance + BoosterBonus

    embed.add_field(name="**Total Balance**", value=((str (round (balance, 3))) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium"))), inline=False)
    embed.set_footer(text=((str ("User ID: ")) + (str (authorID))))
    await ctx.send(embed=embed)

    f = open(filedir, 'w+')
    f.write((str (balance)))
    f.close()

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.mine' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

    #   Pay the fees

    randomcroissant = (f"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\Nolwennium\\{random.choice(Croissants)}.txt")
    try:
        e = open(randomcroissant, 'r')
        balance = (float (e.read()))
        e.close()
    except:
        e = open(randomcroissant, 'w+')
        e.write(str (0))
        e.close()

        e = open(randomcroissant, 'r')
        balance = (float (e.read()))
        e.close()

    balance = balance + fee

    f = open(randomcroissant, 'w+')
    f.write((str (balance)))
    f.close()

#   YouTube audio EPIC VERSION

#   Temporarily removed

#   ON ERROR

@client.event
async def on_slash_command_error(ctx, error):
    randomCry = random.randint(1,7)
    if randomCry == 1:
        cry = '<:AmberCry:828577834146594856>'
    if randomCry == 2:
        cry = '<:BibiByeBye:828683852939395072>'
    if randomCry == 3:
        cry = '<:ColetteCry:828683829631516732>'
    if randomCry == 4:
        cry = '<:JessieCry:828683805861740654>'
    if randomCry == 5:
        cry = '<:SpikeCry:828683779206807622>'
    if randomCry == 6:
        cry = '<:SurgeCry:828683755694063667>'
    if randomCry == 7:
        cry = '<:TaraCry:828683724286853151>'                    
    embed=discord.Embed(title=((str (cry)) + (str (" An error occured"))), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if "is not found" in str(error):
        return
    if ctx.message.content.startswith(".."):
        return
    randomCry = random.randint(1,7)
    if randomCry == 1:
        cry = '<:AmberCry:828577834146594856>'
    if randomCry == 2:
        cry = '<:BibiByeBye:828683852939395072>'
    if randomCry == 3:
        cry = '<:ColetteCry:828683829631516732>'
    if randomCry == 4:
        cry = '<:JessieCry:828683805861740654>'
    if randomCry == 5:
        cry = '<:SpikeCry:828683779206807622>'
    if randomCry == 6:
        cry = '<:SurgeCry:828683755694063667>'
    if randomCry == 7:
        cry = '<:TaraCry:828683724286853151>'                    
    embed=discord.Embed(title=((str (cry)) + (str (" An error occured"))), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)
    print (str(error))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nERROR: An error occured! Original command initialised by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))) + (str (". ERROR MESSAGE: ")) + (str(error)))
    f.close()
    f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\errors.txt", "a")
    f.write((str ("\n\nERROR: An error occured! Original command initialised by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))) + (str (".\n          : ")) + (str(error)))
    f.close()

dotenvPath = 'D:\\BaguetteBot\\draggiebot\\.env'
load_dotenv(dotenv_path=dotenvPath)
if dotenvPath != 'D:\\BaguetteBot\\draggiebot\\.env':
    print("\n\n\n\n\nRUNNING IN TEST MODE!\n\n\n\n\n")
client.run(os.getenv('TOKEN'))


#   poggerspogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpog