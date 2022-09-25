DraggieBot_version = "v1.2.9"
revision = ""

print("Importing all modules...\n")
import      discord, asyncio, os, time, random, sys, youtube_dl, requests, json, uuid, difflib, termcolor, psutil, secrets, logging, subprocess, math, openai
from        discord_slash import SlashCommand
from        discord_slash.utils.manage_commands import create_option, create_choice
from        discord.ext import commands
from        discord.errors import Forbidden#                                    CMD Prerequisite: py -3 -m pip install -U discord.py
from        dotenv import load_dotenv#                                          CMD Prerequisite: py -3 -m pip install -U python-dotenv
from        youtube_search import YoutubeSearch#                                PIP:            python -m ensurepip
from        datetime import datetime#                                           UPDATE PIP:     python -m pip install --upgrade pip
from        json import loads
from        pathlib import Path
from        io import StringIO

global voiceVolume, upvote, downvote, Croissants, draggie, hasMembersforGlobalServer, nolwenniumUserDir, roleMember, hasMember, hasAdmin, bot_events
bot_events = 0
voiceVolume = 0.3
Croissants = [796777705520758795, 821405856285196350, 588081261537394730]
croissant_names = ["ETigger_4", "Josephy Spaghetti", "tigger_4"]
tester_guilds = [384403250172133387, 759861456300015657, 833773314756968489, 921088076011425892] # Server IDs where I'm an admin so can change stuff before it reaches other servers
brigaders = [759861456300015657]
random_word = ["Expulser!", "Troubador!", "Delenda!", "Vincit1", "Consilium!", "Renovatur!", "Acheronta!", "Oderint!"]
emoji_Coins = "<:Coins:852664685270663194>"
emoji_Nolwennium = "<:NolwenniumCoin:846464419503931443>"
emoji_random_lmao = ["😂", "<a:RotatingSkull:966452197787332698>", "💀", "😳"]
emoji_loading = "<a:loading:935623554215591936>"
value_Placeholder = "TBD/tbd"
name_Nolwennium = "Nolwennium"
id_Draggie = 382784106984898560
discord_snowflake = 175928847299117063
discord_epoch = 1420070400000
YTAPI_Status = "Disabled"
SCAPI_Status = "Disabled"
audio_subsystem = "Disabled" # Modified repl.it

#   Check directories
nolwennium_checker_directory = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Nolwennium\\.rootnolwenniumdirectory"
nolwenniumDirChecker = Path(nolwennium_checker_directory)
if nolwenniumDirChecker.is_file():
    running_locally = True
    print("Running locally! Using enhanced features.")
    minified_base_directory = "D:\\Draggie Programs\\BaguetteBot\\"
    base_directory = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\"
    base_directory_minus_slash = "D:\\Draggie Programs\\BaguetteBot\\draggiebot"
    s_slash = "\\"
    json_dir = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\JSONs\\"
    temp_folder = f"Z:{s_slash}"
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'{minified_base_directory}Logs\\{DraggieBot_version}{revision}-{time.time()}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
else:
    running_locally = False
    print(f"Not running locally, coins and {name_Nolwennium} values may not be up to date and some features may be disabled")
    base_directory = "/"
    base_directory_minus_slash = ""
    s_slash = "/"
    json_dir = "JSONs/"
    temp_folder = f"Temp{s_slash}"
    minified_base_directory = "D:\\Draggie Programs\\BaguetteBot\\.useful"
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'.useful{s_slash}{DraggieBot_version}{revision}-{time.time()}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    import keep_alive
    keep_alive.keep_alive()


if running_locally:
    subprocess.Popen(['java', '-jar', f'{base_directory}GitHub\\BaguetteBot\\Lavalink.jar'])

"""
    To do:
    tbd

"""

youtube_dl.utils.bug_reports_message = lambda: ''

print("Done!\nInitialising Bot...")
global start_time
start_time = time.time()

sys.setrecursionlimit(99999999)


class roles:
    Roles_order_List = ["Citizen", "Knight", "Baron", "Viscount", "Earl", "Marquess", "Duke", "Prince", "King", "Admin"]
    Roles_Cost = [0, 25, 50, 100, 250, 500, 1000, 2500, 10000, 1000000]

    Citizen_Tier = 0

    Knight_Tier = 1

    Baron_Tier = 2

    Viscount_Tier = 3

    Earl_Tier = 4

    Marquess_Tier = 5

    Duke_Tier = 6

    Prince_Tier = 7

    King_Tier = 8

    Admin: 1000000


help_command = commands.DefaultHelpCommand(no_category='Dot Commands')


PYTHONIOENCODING = "utf-8"

client = discord.Client()
intents = discord.Intents().all()

client = discord.Client(intents=intents)
client = commands.Bot(
    command_prefix=commands.when_mentioned_or('.'),
    case_insensitive=True,
    intents=intents,
    description=f"BaguetteBot - version {DraggieBot_version}{revision} - d.py {discord.__version__}",
    help_command=help_command
    )

slash = SlashCommand(client, sync_commands=True)


def nolwenniumUserDirectory(ctx):
    global nolwenniumUserDir
    nolwenniumUserDir = f"{base_directory}Nolwennium{s_slash}{ctx.author.id}.txt"


def coinDirectory(ctx):
    global coinDir
    coinDir = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}Coins{s_slash}{ctx.author.id}.txt")


async def bot_runtime_events(event_int):
    global bot_events
    bot_events = bot_events + event_int


async def error_code(ctx, code, *note, **raw_error):
    if note:
        print(f"A manual error was encountered and here is the information: {note}")
    embed = discord.Embed()
    random_cry = ['<:AmberCry:828577834146594856>', '<:BibiByeBye:828683852939395072>', '<:ColetteCry:828683829631516732>', '<:JessieCry:828683805861740654>', '<:SpikeCry:828683779206807622>', '<:SurgeCry:828683755694063667>', '<:TaraCry:828683724286853151>']        
    error_messages = [
        "",
        "[Error 0x0000001] This command does not exist. Maybe you don't have access to it or it was removed?",
    ]

    embed = discord.Embed(
        title=(f"{random.choice(random_cry)} An error occured"), 
        description=f"**{str(error_messages[code])}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", 
        color=0x990000)

    await ctx.send(embed=embed)

    if raw_error:
        with open(f"{base_directory}errors.txt", "a") as f:
            f.write(f"\nERROR: An error occured! Original command initialised by {ctx.message.author} at {datetime.now()}. ERROR MESSAGE: {str(raw_error)}")


async def changeNolwenniumBalance(ctx, base_mined_amount):
    #   Nolwennium UPDATED LOCATION 2/11/2021: {base_directory}Nolwennium{s_slash}
    filedir = (f"{base_directory}Nolwennium{s_slash}{ctx.message.author.id}.txt")

    #   Calculate fees first, so the calculations after account for it.
    fee = base_mined_amount / random.randint(10, 40)
    newNumberAfterFee = base_mined_amount - fee
    newNumberAfterFee = round(newNumberAfterFee, 3)
    fee = round(fee, 3)

    #   Assign basic values first
    shared_guilds = ctx.author.mutual_guilds
    shared_number = 0
    SharedServerBonus = 0
    BoosterBonus = 0
    bonuses = 0

    #   Check whether the user has mined before. If so, add 'another' to the mined string. Else, create a file and just have 'Mined'
    if os.path.isfile(filedir):
        e = open(filedir, 'r')
        balance = float(e.read())
        e.close()
    else:
        e = open(filedir, 'w+')
        e.write(str(0))
        e.close()
        balance = 0

    #    Initiate the embed sequence
    embed = discord.Embed(title="⛏️ Miner ⛏️", colour=0x44ff44)
    embed.add_field(name="**Initially Mined**", value=f"{base_mined_amount} {emoji_Nolwennium} {name_Nolwennium}!")

    #   Perform first check if a user is Boosting the server. If so, then give them a big bonus.
    #   If not, check if they have Nitro. If yes, checked by an animated profile picture, encourage to use a Boost.
    if ctx.author.premium_since:
        BoosterBonus = random.randint(30, 150)
        embed.add_field(name="**Server Booster Bonus**", value=(f"{BoosterBonus} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
        balance = balance + BoosterBonus
        bonuses += BoosterBonus
    else:
        # print("Ok, the user isn't boosting.")
        if ctx.guild.id in tester_guilds:
            print("Ok, the guild is in the tester_guilds list.")
            if ctx.author.avatar_url is not None:
                if ctx.author.is_avatar_animated():
                    print("Ok, the user has nitro.")
                    embed.add_field(name="**If you were Boosting, you would have gained:**", value=(f"{random.randint(30, 150)} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
            else:
                print("Ok, the user doesn't have nitro.")

    #   Check for shared servers. If so, add a random bonus based 3x the amount shared.
    for guild in shared_guilds:
        shared_number += 1

    #   Check shared guilds. If it's only one server, i.e the current one, then encourage them to add it to another server.
    if shared_number > 1:
        SharedServerBonus = random.randint(1, (shared_number * 3))
        embed.add_field(name="**Shared Servers Bonus**", value=(f"{SharedServerBonus} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
        balance = balance + SharedServerBonus
        bonuses += SharedServerBonus
    else:
        embed.add_field(name="**Shared servers: 1**", value="Not enough servers shared for a bonus. :(", inline=False)

    #   Set the embed desription to the above mined string (determined by whether or not the user has mined before.
    #   The output will be something like "Mined another 10 Nolwennium!"
    #   As it's a description, it will be placed *above* the added fields.
    embed.description = f"Mined a total of {base_mined_amount + bonuses} {emoji_Nolwennium} {name_Nolwennium}!"

    #   Finally, show the fees, also paid to a random 'Croissant'.
    croissant_to_pay = random.randint(0, 2)
    croissant_paid = Croissants[croissant_to_pay]
    croisssant_name = croissant_names[croissant_to_pay]
    embed.add_field(name="**Fees Paid**", value=f"{fee} to **{croisssant_name}**", inline=False)

    #   'balance' takes into account existing balance, read from a file, and bonuses.
    #   'newNumberAfterFee' is calculated initially from the base amount mined.
    new_balance = balance + newNumberAfterFee

    #   Set fields and footers, then send the final compiled result.
    embed.add_field(name="**Total Balance**", value=(f"{(round (new_balance, 3))} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
    embed.set_footer(text=f"ID: {ctx.message.author.id} | Total: {bonuses} bonus + {base_mined_amount} = {bonuses + base_mined_amount}")

    await ctx.send(embed=embed)

    #   Write balance and globally log it!
    f = open(filedir, 'w+')
    f.write(str(new_balance))
    f.close()
    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write(f"COMMAND RAN -> '.mine' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()

    #   Add the fees to the aforementioned croissant
    randomcroissant = (f"{base_directory}Nolwennium{s_slash}{croissant_paid}.txt")
    try:
        e = open(randomcroissant, 'r')
        balance = float(e.read())
        e.close()
    except:
        e = open(randomcroissant, 'w+')
        e.write("0")
        e.close()

        e = open(randomcroissant, 'r')
        balance = float(e.read())
        e.close()

    balance = balance + fee

    f = open(randomcroissant, 'w+')
    f.write(str(balance))
    f.close()
    await bot_runtime_events(1)
    print(f"CURRENCY - {name_Nolwennium} > {ctx.message.author.id} has gained {newNumberAfterFee} {name_Nolwennium} (fee: {fee}). Their total is {new_balance}")


async def changeCoinBalance(message, number_to_change_by):
    await bot_runtime_events(1)
    try:
        coinDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Coins{s_slash}{message.author.id}.txt")
        serverdir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Coins")
    except:
        coinDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Coins{s_slash}{message.id}.txt")
        serverdir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Coins")

    if not os.path.exists(serverdir):
        os.makedirs(serverdir)

    try:
        f = open(coinDir, 'r')
        coins = f.read()
        f.close()

        f = open(coinDir, 'w+')
        coins = (int(coins)) + number_to_change_by
        f.close()

        with open(coinDir, 'a') as f:
            f.write(str(coins))
            f.close()

    except FileNotFoundError:   #   User not found
        await bot_runtime_events(1)
        with open(coinDir, 'a') as f:
            print(f"\nSet coin value to 1, {message.author.name} is a new user.")
            try:
                f.write('1')
                f.close()
            except Exception:
                f.write('1')
                f.close()

        sendLogsDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}sendMessages.txt")
        my_file = Path(sendLogsDir)
        if my_file.is_file():
            await bot_runtime_events(1)
            try:
                bbLogChnlId = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                embed = discord.Embed(title="User First Message", description=(f"{message.author.mention} has sent their first message. Their coins balance has been set to 1."), colour=0x00ff00)
                await bbLogChnlId.send(embed=embed)
            except Exception:
                print(f"Unable to send that a new user has joined. This server, {message.guild.name}, doesn't have a text channel called 'event-log-baguette'.")
                guild = message.author.guild
                await guild.create_text_channel('event-log-baguette')
                bbLogChnlId = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await bbLogChnlId.set_permissions(message.guild.default_role, VIEW_CHANNEL=False)
                await bbLogChnlId.send("Logging channel created. You can do whatever you want with this channel but deleting it may cause some issues in the future :)")
                embed = discord.Embed(title="User First Message", description=(f"{message.author.mention} has sent their first message. Their coins balance has been set to 1."), colour=0x00ff00)
                await bbLogChnlId.send(embed=embed)
    except ValueError:
        f.write('1')
        f.close()
    await bot_runtime_events(1)

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'audioformat': 'mp3',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'logtostderr': False,
    'quiet': False,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect True -reconnect_streamed True -reconnect_delay_max 5',
    'options': '-vn -report -loglevel debug',
}

print("Done!\nSlash commands initialising...")

###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################


@slash.slash(name="openai",
             description="Generates a text completion based on any prompt.",
             guild_ids=tester_guilds,
             options=[create_option(
                    name="prompt",
                    description="This can be as complex as you want. Add here as if you were speaking to a human.",
                    option_type=3,
                    required=True
                    ),
                    create_option(
                    name="model",
                    description="What AI model do you want to use? 1 to 4. 4 is best but slow, 1 is worse but fast to generate.",
                    option_type=4,
                    required=True
                    ),
                    create_option(
                    name="limit",
                    description="Enter the token limit to generate.",
                    option_type=4,
                    required=True
                    )
                ]
            )
async def openai_prompt(ctx, prompt: str, model: int, limit: int):
    #   await ctx.send("Generating response... <a:loading:935623554215591936>")
    allowed_users = [382784106984898560, 629321969615110154, 606583679396872239]
#   Check owner to quickly enable/disable it in case of abuse
    if ctx.author.id == 382784106984898560:
        if prompt == "disable":
            x = open(f"{base_directory}openai", "w")
            x.close()
            await ctx.send("Disabled OpenAI integration subsystem.")
            return
        if prompt == "enable":
            try:
                os.remove(f"{base_directory}openai")
            except OSError:
                await ctx.send("The subsystem is already enabled")
                return
            await ctx.send("Enabled OpenAI integration subsystem.")
            return

    if os.path.isfile(f"{base_directory}openai"):
        await ctx.send("The OpenAI subsystem has been disabled.")
        return
    if ctx.author.id not in allowed_users:
        await ctx.send("Unauthorised access, please wait for the application to be verified.")
        return
    if prompt is None:
        await ctx.send("No prompt!")
        return
    if model == 1:
        model_type = "text-ada-001"
    if model == 2:
        model_type = "text-babbage-001"
    if model == 4:
        model_type = "text-davinci-002"
    else:#  Default.
        model_type = "text-curie-001"

    #   Now defer as it may take a long time lmao
    await ctx.defer()
    with open(f"{base_directory}openai_api_key.txt", 'r', encoding="UTF-8") as api:
        openai.api_key = api.read()
    with open(f"{base_directory}openai_organisation.txt", 'r', encoding="UTF-8") as org:
        openai.organization = org.read()

    #   Get moderation dats
    response = openai.Moderation.create(input=prompt)
    print(response)
    print(response.results[0])
    output = (response.results[0].flagged)
    if output == 1:
        await ctx.send("You've sent it some really sussy things, so imma have to stop you right there... wtf!")
        return


    #   Get the actual data
    response = openai.Completion.create(
        model=model_type,
        prompt=prompt,
        temperature=0.82,
        max_tokens=limit,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    x = (response.choices[0].text)
    if len(x) > 2000:
        buffer = StringIO(x)
        f = discord.File(buffer, filename=f"{prompt}.txt")
        await ctx.send(file=f)
    print(x)
    await ctx.send(x)


@slash.slash(name="debug", description="Spits out debug info for debugging bugs")
async def test(ctx):
    await bot_runtime_events(1)
    nolwenniumUserDirectory(ctx)
    my_file = Path(nolwenniumUserDir)
    if not my_file.is_file():
        nolwenniumBal = "null"
        nolly = nolwenniumBal
    else:
        f = open(nolwenniumUserDir, 'r')
        nolwenniumBal = f.read()
        f.close()
        nolly = f"{nolwenniumBal} {emoji_Nolwennium}"
    x = False
    Admin = discord.utils.get(ctx.guild.roles, name="Admin")
    if Admin in ctx.author.roles:
        x = True
    shard_id = ctx.guild.shard_id
    await ctx.send(f"Debug info: S: {ctx.guild.id} in C: {ctx.channel.id} - A: {ctx.author.id}, hA: {x}, {name_Nolwennium}: {nolly} + l:{client.latency}s, iID: {uuid.uuid4()}, sO: {ctx.guild.owner.id}, bbPremium = False, usesEmilite: False, sID: {shard_id}")#\n<a:HmmThinkSpin:857307788572098610> *Unsure what this is?* These are just guild/channel ids, send this to Draggie#3060 if you have issues")
    #                                Server ID           Channel ID            Message author ID   HasAdmin?         NolwenniumBalance     Ping          Random UUID          Server Owner       
    await bot_runtime_events(1)
    
@slash.slash(name="Ping", description="Shows bot latency to Discord's servers, using Discord WebSocket protocol.", guild_ids=tester_guilds)
async def _ping(ctx):
    print("ping'd")
    await bot_runtime_events(1)
    GlobalLogDir=("{base_directory}GlobalLog.txt")
    startTime = round(time.time() * 1000)
    await ctx.reply("Ping: Testing connection...")
    #message = ctx.channel.last_message
    EmbedGetTime = round(time.time() * 1000)
    nTighem = EmbedGetTime - startTime

    if round(client.latency * 1000) <= 100:
        string = (f"Ping: Total message delay is **{round(client.latency *1000)}** milliseconds. (Very good!)\nAdditional logic operations took {nTighem}ms. ")
    elif round(client.latency * 1000) <= 150:
        string = (f"Ping: Total message delay is **{round(client.latency *1000)}** milliseconds. (Good)\nAdditional logic operations took {nTighem}ms. ")
    elif round(client.latency * 1000) <= 150:
        string = (f"Ping: Total message delay is **{round(client.latency *1000)}** milliseconds. (Bad)\nAdditional logic operations took {nTighem}ms. ")
    else:
        string = (f"Ping: Total message delay is **{round(client.latency *1000)}** milliseconds. (Very bad!)\nAdditional logic operations took {nTighem}ms. ")
    message = ctx.channel.last_message
    await message.edit(content=string)
    f = open(GlobalLogDir, "a", encoding="utf8")
    f.write(f"\nCOMMAND RAN -> '.ping' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    await bot_runtime_events(1)


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
    await bot_runtime_events(1)


@slash.slash(name="cuisine",
             description="Cuisine.",
             guild_ids=brigaders,
             options=[create_option(
                  name="country",
                  description="Choose country.",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(name="France", value="france"),
                      create_choice(name="Italy", value="italy")])])
async def _cuisine(ctx, country: str):
    await ctx.send(f"You chose {country}.")
    await bot_runtime_events(1)


@slash.slash(name="rgb", description="Updates rgb advisor colour.", guild_ids=tester_guilds)
async def _rgb(ctx):
    #   rgb = discord.utils.get(ctx.guild.roles, name="RGB Advisor")
    #   admin = discord.utils.get(ctx.guild.roles, name="Admin")
    #   mod = discord.utils.get(ctx.guild.roles, name="Mod")
    print(f"RGB ran by {ctx.author.name}")
    #   if rgb or mod or admin in ctx.author.roles:
    guild = ctx.guild
    colour = random.randint(1000, 16777215)
    colour = discord.Color(colour)
    role = discord.utils.get(guild.roles, name="RGB Advisor")
    await role.edit(server=guild, role=role, colour=colour, reason=f"RGB advisor role update command ran, by {ctx.author.name}")
    await ctx.send(f"{role.mention} set to colour {colour}")
    await bot_runtime_events(1)
    
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
                LoggingChannel = discord.utils.get(ctx.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)#test
                print(f"Logging Channel {LoggingChannel}")
                if LoggingChannel is None:
                    print("Creating channel")
                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False)
                    }
                    await ctx.guild.create_text_channel('event-log-baguette', overwrites=overwrites)
                LoggingChannel = discord.utils.get(ctx.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await LoggingChannel.send("**Logging enabled**")

                sendLogsDir = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}sendMessages.txt")
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
                sendLogsDir = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}sendMessages.txt")
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
            sendRedactions = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}sendRedactions.txt")
            x = open(sendRedactions, "a", encoding='utf-8')
            x.close()
            await ctx.send("Redacted messages have been enabled. Announcements showing a message's deletion will be sent in DMs and broadcasted in the channel.")
        if "redactions" in disable:
            try:
                sendRedactions = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}sendRedactions.txt")
                os.remove(sendRedactions)
                x = "enabled" if os.path.isfile(f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}sendMessages.txt") else "disabled"
                await ctx.send(f"Redacted messages have been disabled. Messages will not be sent in the channel or to DMs. Logging is {x}.")
            except Exception:
                await ctx.send("Cannot perform that function. `sendRedactions` is `disabled`")
        if "nothing" in enable and disable:
            await ctx.send("Nothing was changed.")
    else:
        await ctx.send("You are not admin, or do not have Admin as an assigned role")
    await bot_runtime_events(1)

geo1Questions = ["Give one reason why tropical storms have a seasonal pattern [1 mark]", "Suggest why some tropical storms have severe primary and secondary effects.\n\nUse Figure 3 and your own understanding. [6 marks] https://cdn.discordapp.com/attachments/895390385440952352/947549285128495154/unknown.png"]

@slash.slash(name="verify",
            description="Allow users into the private side of Baguette Brigaders.",
            guild_ids = tester_guilds,
            options = [
            create_option(
                name="user",
                description="User to allow into the private side.",
                option_type=6,
                required=True,
            )])
async def verify(ctx, user: discord.Member):
    member_role = discord.utils.get(ctx.guild.roles, name=f"Member")
    members_role = discord.utils.get(ctx.guild.roles, name=f"Members")
    unverified_private_role = discord.utils.get(ctx.guild.roles, name=f"Private Unverified")
    if member_role in ctx.author.roles:
        if member_role not in user.roles:
            await user.send(f"Hello! A kind member of Baguette Brigader's private side, {ctx.author}, has allowed you access to view its contents. Please hit the verification tick and you'll have access to it.")
            await user.remove_roles(members_role)
            await user.add_roles(unverified_private_role)
            await ctx.send(f"The user, {user.mention}, has been given access to the private side.")
        else:
            await ctx.send(f"They already have access to the private side.")
    else:
        await ctx.send("You cannot execute this. Request logged.")
    await bot_runtime_events(1)


@slash.slash(name="NameColour",
            description="Change the colour of your name!",
            guild_ids = tester_guilds,
            options = [create_option(
            name="colour",
            description="Enter the hex colour. For example, 00acff. (Just the code, not the hashtag!)",
            option_type=3,
            required=True,
            ),

            create_option(
            name="delete",
            description="do you want to delete your role? (ignores any hex code added) - ANYTHING HERE = DELETE!",
            option_type=5,
            required=False,
            )])
async def moverole(ctx, colour: str, **kwargs):
    if "delete" in kwargs:
        role = discord.utils.get(ctx.guild.roles, name=f"CC: {ctx.author.name}")
        if role is None:
            await ctx.send(f"No role to delete. `'NoneType' has no attribute 'delete'.`")
            return
        await role.delete()
        await ctx.send("Role deleted")
        return
    access = False
    roleStaff = discord.utils.get(ctx.guild.roles, name="Staff")
    if roleStaff in ctx.author.roles:
        access = True
        await ctx.send("Your highest role **Staff** is above the Custom Colour section, so your custom colour will not show")
        print(f"{ctx.author.name} has Staff")
    roleKing = discord.utils.get(ctx.guild.roles, name="King")
    if roleKing in ctx.author.roles:
        access = True
        print(f"{ctx.author.name} has King")
    roleCroissant = discord.utils.get(ctx.guild.roles, name="Croissant")
    if roleCroissant in ctx.author.roles:
        access = True
        print(f"{ctx.author.name} has Croissant")
        await ctx.send("Your highest role **Croissant** is above the Custom Colour section, so your custom colour will not show")
    if ctx.author.premium_since:
        access = True
    if access:
        print(f"Allowed user {ctx.author.name} - {ctx.author.roles}")
        number_of_roles = (len(ctx.guild.roles))
        pos = number_of_roles - 18
        role = discord.utils.get(ctx.guild.roles, name=f"CC: {ctx.author.name}")
        if role is None:
            await ctx.guild.create_role(name=f"CC: {ctx.author.name}", reason=f"Command ran by {ctx.author.name} at {datetime.now()} - Response was OK, passed role checks..")
            role = discord.utils.get(ctx.guild.roles, name=f"CC: {ctx.author.name}")
            #await ctx.send(f"Role added! at position {pos}").
        try:
            if colour != "00acff":
                try:
                    colour = int(colour, 16)
                except Exception as e:
                    await ctx.send(f"The colour inputted, {colour}, is not a valid hex code. You can find a valid one on a site like https://htmlcolorcodes.com. Make sure it's just the code, not the hashtag.")
                    return
                await role.edit(colour=discord.Colour(colour), position=int(pos), reason=f"Slash Command ran by {ctx.author.name} at {datetime.now()}.")
                await ctx.send(f"Your custom role colour has been updated to '0x{colour}' and position moved to {pos}.")
            else:
                await ctx.send("That colour has been reserved. Choose another!")
                return
        except discord.Forbidden:
            await ctx.send("You do not have permission to do that")
        except discord.HTTPException:
            await ctx.send("Failed to move role")
        except discord.InvalidArgument:
            await ctx.send("Invalid argument")
        await ctx.author.add_roles(role)
    else:
        role = discord.utils.get(ctx.guild.roles, name=f"CC: {ctx.author.name}")
        if role:
            await role.delete()
        await ctx.send("You are neither boosting the server nor have a high enough role. Boost the server in order to unlock Custom Colours!")
    await bot_runtime_events(1)

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

    async def beanery():
        if character == "Wattson":
            randomiser = random.randint(1,290)
            await ctx.send(file=discord.File(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\MaximumWattage\\wattson ({randomiser}).png", filename="SPOILER_wattson{randomiser}.png"))
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
            options=[create_option(name="term",description="Type in a term to search for. Returns an integer value.",option_type=3,required=True)])
async def _CodeSearch(ctx, term: str):
    await ctx.defer()
    message = term
    searchTerm = message.lower()
    file=open(f"{base_directory}GitHub{s_slash}BaguetteBot{s_slash}BaguetteBot.py", encoding="UTF-8").read().lower()
    num_chars = sum(1 for line in file)
    num_lines = sum(1 for line in open (f"{base_directory}GitHub{s_slash}BaguetteBot{s_slash}BaguetteBot.py", encoding='utf-8'))

    count=file.count(searchTerm)
    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{searchTerm}**' in code:", value=f"{count}", inline=False)
    embed.set_footer(text=(f"Searching {num_chars} characters in {num_lines} lines of code. Requested by {ctx.author}"))
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write(f"\nSLASH COMMAND RAN -> 'CodeSearch' ran by {ctx.author} at {str (datetime.now())}")
    f.close()
    await bot_runtime_events(1)

###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

DisabledComponents = "Unknown"
EnabledComponents = "Unknown"

if running_locally:
  GlobalLogDir=(f"{base_directory}GlobalLog.txt")
else:
  GlobalLogDir=("GlobalLog.txt")

""" BULK READ JSONS so it doesn't have to read the file every time a message is sent
    people = nolTighe (p1, g, b, T), oliver, sam (g), jack (r, g), joe (g), charlie (g), haydn, maisy, flo (a), ish, maya, boris (gl), josephTighe (p13, g, c, T)
    "g = grouped", "r = remade", "a = affiliated", "gl = global" 
"""


#	Modified in repl.it

with open(f"{json_dir}NollyMention.json", "r", encoding="utf8") as file:
    nollyWords = loads(file.read())
with open(f"{json_dir}OliverMention.json", "r", encoding="utf8") as file:
    oliverWords = loads(file.read())
with open(f"{json_dir}SamMention.json", "r", encoding="utf8") as file:
    samWords = loads(file.read())
with open(f"{json_dir}JackMention.json", "r", encoding="utf8") as file:
    jackWords = loads(file.read())
with open(f"{json_dir}JoeMention.json", "r", encoding="utf8") as file:
    joeWords = loads(file.read())
with open(f"{json_dir}HaydnMention.json", "r", encoding="utf8") as file:
    haydnWords = loads(file.read())
with open(f"{json_dir}MaisyMention.json", "r", encoding="utf8") as file:
    maisyWords = loads(file.read())
with open(f"{json_dir}BenMention.json", "r", encoding="utf8") as file:
    benWords = loads(file.read())
with open(f"{json_dir}FloMention.json", "r", encoding="utf8") as file:
    floWords = loads(file.read())
with open(f"{json_dir}IshMention.json", "r", encoding="utf8") as file:
    ishWords = loads(file.read())
with open(f"{json_dir}BorisMention.json", "r", encoding="utf8") as file:
    borisWords = loads(file.read())
with open(f"{json_dir}MayaMention.json", "r", encoding="utf8") as file:
    mayaWords = loads(file.read())
with open(f"{json_dir}JosephTigheMention.json", "r", encoding="utf8") as file:
    josephTighe = loads(file.read())
with open(f"{json_dir}CharlieMention.json", "r", encoding="utf8") as file:
    charlieSewards = loads(file.read())


@client.event
async def on_ready():
    print(f'\n\n\n\nLogged in as {client.user} - {(datetime.now())}')
    global ready_start_time, roleMember, hasMember, hasAdmin
    ready_start_time = time.time()
    if running_locally:
        try:
            client.load_extension('cogs.music')# Modified repl.it
            print("COG: Music loaded!")
        except Exception as e:
            print(f"Unable to load extension: {e}")
    log_channel = client.get_channel(838107252115374151) # Brigaders_channel
    await log_channel.send(f"Online at **{datetime.now()}**")
    f = open(GlobalLogDir, "a", encoding="utf-8")
    f.write(f"\n\nREADY at {datetime.now()}")
    f.write(' - Logged in as {0.user}'.format(client))
    f.close()
    servers = len(client.guilds)
    members = 0
    await bot_runtime_events(7)
    for guild in client.guilds:
        members += guild.member_count - 1
        print(f"{guild.name} - {guild.member_count - 1} members")
    if revision != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{revision} | .help | {servers} servers + {members} members")))
    else:
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members")))
    global draggie, general, console, upvote, downvote, hasMembersforGlobalServer
    draggie = client.get_user(382784106984898560)
    general = client.get_channel(759861456761258045)#  Brigaders_channel 
    console = client.get_channel(912429726562418698)
    guild = client.get_guild(759861456300015657)
    draggie_guild = client.get_guild(759861456300015657)
    hasMember = discord.utils.find(lambda r: r.name == 'Member', guild.roles)
    hasAdmin = discord.utils.find(lambda r: r.name == 'Admin', guild.roles)
    roleMember = discord.utils.get(guild.roles, name='Member')
    upvote = client.get_emoji(803578918488768552)
    downvote = client.get_emoji(803578918464258068)
    epic_memes = client.get_channel(809112184902778890)
    public_memes = client.get_channel(930488945144397905)

    memes_channels = [epic_memes, public_memes]
    hasMembersforGlobalServer = discord.utils.get(guild.roles, name="Members")

    await asyncio.sleep(2)
    global test__bb_voice_channel
    test__bb_voice_channel = client.get_channel(1013893596493119488)
    test_voice_time = await test__bb_voice_channel.history().flatten()

    voice_time = test_voice_time[0].content

    x = open(f'{base_directory}Servers{s_slash}759861456300015657{s_slash}Logs{s_slash}TotalUserVoiceTime.txt', 'w+')
    x.write(voice_time)
    x.close()

    for message in await epic_memes.history().flatten():
        if "upvote" not in str(message.reactions) or "downvote" not in str(message.reactions):
            #print(message.reactions)
            if ("http") in message.content.lower():
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
                print(f"Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'http' in '{message.content.lower()}'")
            if len(message.attachments) >= 1:
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
                print(f"Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'message.attachments' is greater than 1")
            else:
                print("Skipped message to react to")
        if len(message.reactions) == 0:
            if ("http") in message.content.lower() or len(message.attachments) >= 1:
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
                print(f"Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'no reactions on message' or 'has attachment'")

    print(f"Calibrated Voice Chat time to {voice_time} seconds")

    await bot_runtime_events(1)
    await StatusAutoUpdator()

async def StatusAutoUpdator():
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    if revision !="":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{revision} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
        await bot_runtime_events(1)
    else:
        await bot_runtime_events(1)
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
    print(f"Updated status - {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")
    #await asyncio.sleep(random.randint(100,500))
    await bot_runtime_events(1)
    await asyncio.sleep(60)
    await StatusAutoUpdator()

@client.event
async def on_voice_state_update(member, before, after):
    print(f"\nVoiceChatEvent in {member.guild.id} ({member.guild.name}) by {member.name} at {datetime.now()}")
    #if member.bot: #checking this before anything else will reduce unneeded file operations etc
    #    return
    await bot_runtime_events(1)
    if after.channel:
        if not os.path.isfile(f'{base_directory}Servers{s_slash}{after.channel.guild.id}{s_slash}Voice{s_slash}voice_info.txt'):
            try:
                os.mkdir(f'{base_directory}Servers{s_slash}{after.channel.guild.id}{s_slash}Voice')
            except Exception:
                print("Area already exists.")
            print(f"User joined VC in {member.guild.id} ({member.guild.name}) by {member.name} at {datetime.now()} ")
            x = open(f'{base_directory}Servers{s_slash}{after.channel.guild.id}{s_slash}Voice{s_slash}voice_info.txt', 'w')
            x.close()
    else:
        print(f"User left VC in {member.guild.id} ({member.guild.name}) by {member.name} at {datetime.now()}")
    new_user = str(member.id)

    if not before.channel: #When VC joined.
        join_time = round(time.time())
        x = open(f'{base_directory}Servers{s_slash}{after.channel.guild.id}{s_slash}Voice{s_slash}tempuserstate_{new_user}.txt', 'w')
        x.write(str(join_time))
        x.close
    if not after.channel:
        await bot_runtime_events(1)
        leave_time = round(time.time())
        x = open(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Voice{s_slash}tempuserstate_{new_user}.txt', 'r')
        start_time = int(x.read())
        x.close()
        #os.remove(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Voice{s_slash}tempuserstate_{new_user}.txt')
        time_spent = leave_time - start_time
        print(f"{member.name} just spent {time_spent} in a Voice Chat.")

        if before.channel.guild.id == 759861456300015657:
            await bot_runtime_events(1)
            print("It's in Baguette Brigaders!")

            #   Calculate the amount to add using the special formula
            coins_to_add = round(((math.sqrt(time_spent)/10))*2 + (math.sqrt(time_spent)/2))
            if time_spent < 120:
                new_time_spent = time_spent
                units = "seconds"
            else:
                new_time_spent = round(time_spent/60)
                units = "minutes"

            if time_spent > 3600:
                new_time_spent = round(time_spent/3600)
                if new_time_spent == 1:
                    units = "hour"
                else:
                    units = "hours"
                
            try:
                x = (random.randint(1,3))
                if x == 2:
                    if coins_to_add > 5:
                        if member.id == 792850689533542420:
                            return
                        string = (f"{member.mention}, you have earned an extra {coins_to_add} Coins {emoji_Coins} for spending {new_time_spent} {units} in voice!\n\n*Type `.coins` in Baguette Brigaders to see what you can buy!*")
                        await member.send(string)
                        #await draggie.send(f"[Sent to {member.mention}] {string}")
                        print(string)
                    else:
                        print(f"Not going to Stage 3 of alerting earned sum was only {coins_to_add}.")
                else:
                    print(f"Not going to Stage 2 of alerting as the number was not 2, it was {x}")
            except AttributeError:
                print("Could not send the message as the member is probably a bot or has blocked the bot.")

            await changeCoinBalance(member, coins_to_add)

        # Get total guild time spent in Voice Chat
        # Firstly, if there is not a record of voice chat time, create the file
        if not os.path.isfile(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Logs{s_slash}TotalUserVoiceTime.txt'):
            x = open(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Logs{s_slash}TotalUserVoiceTime.txt', 'w')
            x.close()
        
        #   Then, open up the file for reading.
        x = open(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Logs{s_slash}TotalUserVoiceTime.txt', 'r')
        try:
            #   Try and convert the value into an integer. If error, then the value would be zero.
            preTime = int(x.read())
        except Exception:
            preTime = 0
        x.close()

        #   Perform calculations on total time spent.
        total_guild_time_spent = preTime + time_spent
        print(f"Total time spent in VCs in {member.guild.name}: {total_guild_time_spent} seconds.")
        
        #   Write new sum to the file for later reading.
        x = open(f'{base_directory}Servers{s_slash}{before.channel.guild.id}{s_slash}Logs{s_slash}TotalUserVoiceTime.txt', 'w+')
        x.write(str(total_guild_time_spent))
        x.close()

        if before.channel.guild.id == 759861456300015657:
            await test__bb_voice_channel.send(total_guild_time_spent)

        #   Finally, send sum to me as a test.
        await draggie.send(f"The guild, {before.channel.guild.name}, now has {total_guild_time_spent} seconds total spent, thanks to {member.name}.")

@client.event
async def on_member_join(member):
    await bot_runtime_events(1)
    sendLogsDir = (f"{base_directory}Servers{s_slash}{member.guild.id}{s_slash}sendMessages.txt")
    if member.guild.id == 759861456300015657:
        #await member.send(f"Hello! Welcome to Baguette Brigaders. Whether you joined from the Vanity URL or a member invited you, welcome! Go to the rules channel for a free role!")
        print("Not welcomed user")
        #await draggie.send(f"Welcomed user {member}")
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    if revision != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{revision} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
    else:
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + {memoryUsage}%")))

@client.event
async def on_member_remove(member):
    await bot_runtime_events(1)
    sendLogsDir = (f"{base_directory}Servers{s_slash}{member.guild.id}{s_slash}sendMessages.txt")
    if os.path.isfile(sendLogsDir):
        try:
            channel = discord.utils.get(member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
            await channel.send(f"{member} has left the server.")
        except Forbidden:
            await draggie.send(f"Removed from server {member.guild.name} / {member.guild.id}")
    servers = len(client.guilds)
    members = 0
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    for guild in client.guilds:
        members += guild.member_count - 1
    if revision != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{revision} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
    else:
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
    
@client.event
async def on_raw_reaction_add(payload=None):
    await bot_runtime_events(1)
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
        role_private_unverified = discord.utils.get(guild.roles, name='Private Unverified')
        roleSMP = discord.utils.get(guild.roles, name='SMP')
        robloxDev = discord.utils.get(guild.roles, name="Roblox Developer")
        roleNew = discord.utils.get(guild.roles, name='New Baguette')
        LoggingChannel = discord.utils.get(payload.member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

        if payload is not None:
            #if payload.channel_id == 809112184902778890:
                #if payload.emoji.name == "downvote":
                #    channel = client.get_channel(809112184902778890)
                #    message = await channel.fetch_message(payload.message_id)
                #    reaction = discord.utils.get(message.reactions, emoji=payload.emoji)
                #    count = reaction.count
                #    if count > 4:
                #        await channel.send(f"{message.author.mention}'s 'epic' meme from {message.created_at.date()} was removed {random.choice(emoji_random_lmao)}")
                #        await message.author.send(f"Your 'epic' meme has been removed as it reached too many downvotes. Please only put your *best* locally grown epic memes! {random.choice(emoji_random_lmao)} {random.choice(emoji_random_lmao)}")
                #        await message.delete()
                #        return
            authorName = payload.member.name
            authorName = authorName.lower()
            if payload.message_id == birthdayID:
                await payload.member.send("You are too late to claim the birthday role, sorry. More exclusive roles will be given in the future!")
            if payload.message_id == smp2ID:
                await payload.member.add_roles(roleSMP)
                print(f"Added role to {roleMember.name}")
                await payload.member.send(f"{payload.member.mention}, you've been granted SMP Season 2 role in Baguette Brigaders! Enjoy your time on the server.")
                print(f"Sent DM to {payload.member.name}")
                
            if payload.message_id == 936320104193474630:
                print(f"Sent Roblox Message message to {payload.member}")
                await payload.member.add_roles(robloxDev)
            if payload.message_id == 931577920512725083:#
                await asyncio.sleep(5)
                member = payload.member.guild.get_member(payload.member.id)
                await payload.member.remove_roles(roleUnverified)
                if roleAllRandoms not in member.roles:
                    print("Adding roles...")
                    channel = client.get_channel(930489645014331442)
                    await member.add_roles(roleAllRandoms)
                    await member.send(f"Welcome, {member.mention}! You have been verified! Enjoy the server; thanks for being part of this special community. We look forward to having you onboard for future developments!")
                    print(f"Sent message to {member}")     
                    await LoggingChannel.send(f"{payload.member} has been verified.")
                else:
                    print("Not adding as members is already in roles.")

            if payload.message_id == 931586778245247018:
                choices = ["OK, you'll no longer see the other side.", "No longer seeing the other side. Enjoy your time on this side!", "Who likes the other side anyway, this side is better!"]
                if roleAllRandoms not in payload.member.roles:
                    await payload.member.add_roles(roleAllRandoms)
                    await LoggingChannel.send("{payload.member} has been allowed access to the other side.")
                else:
                    print(f"{payload.member.name} already has Members role, removing it.")
                    await payload.member.remove_roles(roleAllRandoms)
                    await payload.member.send(f"{random.choice(choices)}")
    
            if payload.message_id == msgID:#                VERIFICATION MESSAGE ONLY
                if str(payload.emoji) == "✅":
                    channel = client.get_channel(835200388965728276)
                    await payload.member.add_roles(roleMember)
                    await payload.member.add_roles(roleNew)
                    await channel.send(f"Welcome, {payload.member.mention}! You have been verified! Maybe check out <#759861456761258045> now?")
                    await payload.member.remove_roles(role_private_unverified)
                    await payload.member.remove_roles(roleUnverified)
                    await asyncio.sleep(8)
                    await channel.purge(limit=1)
                    print(f"And it's gone in {channel}")

            if payload.message_id == vaccinatedID:
                if str(payload.emoji) == "✅":
                    await payload.member.add_roles(roleVaccinated)
                    await LoggingChannel.send(f"{payload.member} has been granted vaccination status.")

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


    if payload.guild_id == 384403250172133387:#     Must, while reaction roles are not available for all servers.
        if payload.message_id == 907318418712170538:
            channel = client.get_channel(907318241498656850)

@client.event
async def on_reaction_remove(reaction, user):
    await bot_runtime_events(1)
    print(reaction, user)


@client.event
async def on_guild_remove(guild):
    print(f"Removed from guild {guild}")
    await draggie.send(f"DEV MODE: removed from guild {guild} ({guild.id})")

#   Client evenys

@client.event
async def on_message_delete(message):
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    sendRedactionsInChannel = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}sendRedactions.txt")
    print(f"Message deleted: '{message.content}' channel: '{message.channel.name}' server: '{message.guild.name}'")
    if message.channel.id == 825470734453047297:
        if message.author.bot == False:
            await message.channel.send(f"Stop deleting your messages in here, we're literally adding numbers, {message.author.mention}. *Their message was {message.content}*")
            return 
    if os.path.isfile(sendRedactionsInChannel):
        if message.author.id != 792850689533542420:
            await message.channel.send(f"{message.author.mention}'s message has been *redacted*.")
            user = client.get_user(int(message.author.id))
            await user.send(f"Your message, '`{message.content}`', has been ***redacted***.")
    if os.path.isfile(f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}sendMessages.txt"):
        LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        embed = discord.Embed(title=f"User's message deleted", colour=0xFF0000)
        embed.add_field(name="User", value=message.author.mention)
        embed.add_field(name='Channel', value=f"<#{message.channel.id}>")
        embed.add_field(name='Time', value=tighem)
        if message.content == "":
            embed.add_field(name='Message', value="[attachment]", inline=False)
        else:
            embed.add_field(name='Message', value=message.content, inline=False)
        await LoggingChannel.send(embed=embed)

@client.command(pass_context=True, hidden=True)
async def discorddm(ctx):
    message = ctx.message.content
    x = message.split()
    sp1 = message.split(' ', 2)[-1]
    userID = (x[1])
    user = client.get_user(int (userID))
    await user.send(f"{sp1}")
    await ctx.send(f"Successfully sent {sp1} to user {user.name}")

@client.event
async def on_message_edit(before, after):
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    sendLogsDir = (f"{base_directory}Servers{s_slash}{after.guild.id}{s_slash}sendMessages.txt")

    LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

    if LoggingChannel is not None:
        if before.content == after.content:
            embed = discord.Embed(title=f"Message modified", description=f"Embed preview added to message ([jump]({after.jump_url}))")
            await LoggingChannel.send(embed=embed)
            return

        print(f"Message updated >>> '{before.content}' changed to '{after.content}' in {after.guild.name}/{after.guild.name}")
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
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        sendLogsDir = (f"{base_directory}Servers{s_slash}{channel.guild.id}{s_slash}sendMessages.txt")
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
                """await draggie.send(f"{user.mention} has been seen **TYPING** in {channel.guild.name}! Triggered by {trigger}: `{tighem}`")"""
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
        #LoggingChannel = discord.utils.get(channel.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        #embed = discord.Embed(title=f"User typing", colour=0x00ff00)
        #embed.add_field(name='User', value=user.mention)
        #embed.add_field(name='Channel', value=f"<#{channel.id}>")
        #embed.add_field(name='Time', value=tighem)
        #await LoggingChannel.send(embed=embed)
    print(f"TYPING >>> {user.name} started typing in {channel.name} at {tighem}/{when} in {channel.guild.name}")

@client.event
async def on_user_update(before, after):
    await bot_runtime_events(1)
    if after.avatar != before.avatar:
        print(f"INFO >>> {before.name} updated their avatar, affecting {before.guild}.")

@client.event
async def on_member_ban(guild, user):
    await bot_runtime_events(1)
    print("test")

@client.event
async def on_member_update(before, after):
    #print(f"Member updated - BEFORE = {before} AFTER = {after} - {datetime.now()}")
    await bot_runtime_events(1)
    send = False
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    guild = after.guild

    if after.activity is not None:
        await bot_runtime_events(1)
    #    print(f"ACTIVITY of {after.name} has been updated to {after.activity.name} at {datetime.now()}")
        #print(str(after.activities)) modified repl.it
    if before.status != after.status:
        await bot_runtime_events(1)
        
    elif before.nick != after.nick:
        embed = discord.Embed(title=f"Changed nick", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.nick)
        embed.add_field(name='After', value=after.nick)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"Events Listener: NICK of {after} has been updated FROM {before.nick} TO {after.nick} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        staffCheck = new_role.id
        if staffCheck == 963738031863525436 or staffCheck == 930874936082452480 or staffCheck == 759861918763712542 or staffCheck == 943974413810933802:
            roleStaff = discord.utils.get(guild.roles, name=new_role.name)
            await after.remove_roles(roleStaff)
        else:
            print("Not staff role.")
        embed = discord.Embed(title=f"Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role added', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"Events Listener: ROLES of {after} has been updated: ADDED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
        if after.guild.id == 759861456300015657 or after.guild.id == 384403250172133387:
            if new_role.name == "Server Booster":
                coinDir = (f"{base_directory}Servers{s_slash}{after.guild.id}{s_slash}Coins{s_slash}{after.guild.id}.txt")
                nolwenniumUserDir = (f"{base_directory}Nolwennium{s_slash}{after.id}.txt")
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    with open(nolwenniumUserDir, 'a') as f:
                        print (f"\n[CURRENCY - {name_Nolwennium}] Set {name_Nolwennium} value to 0, new user. {after.id} - {after.name}")
                        f.write('0')
                        f.close()

                with open(nolwenniumUserDir, 'r') as f:
                    beforeBonusAmount = (float (f.read()))
                    f.close()
    
                toAdd = random.randint(100,1000)
                addedAmount = beforeBonusAmount + toAdd       

                f = open(nolwenniumUserDir, 'w+')
                f.close()

                with open(nolwenniumUserDir, 'a') as f:
                    f.write(str (addedAmount))
                    print (f"\n[CURRENCY - {name_Nolwennium}] Added balance of {toAdd} (total: {addedAmount} for boosting the server: {after.id} - {after.name}")
                    f.close()
    
                f = open(coinDir, 'r')
                coins = int(f.read())
                f.close()
                newSum = coins + 200
                f = open(coinDir, 'w+')
                f.write(str (newSum))
                f.close()
                f = open(coinDir, 'r')
                newCoins = int(f.read())
                f.close()

                await general.send(f"Thank you {after.mention} for boosting the server! You have received the Server Booster role, an exclusive name colour, and a bonus sum of Coins (total: {newCoins}) and {name_Nolwennium} (total: {addedAmount}). You can also change your name to any colour you want, see the command /namecolour for more information.")
            #await draggie.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!')                        In Brigaders Helper
            #await after.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!') <<<<<<                   In Brigaders Helper
            #print(f"Sent >>> {after.mention}, you\'ve been given the role **\"{new_role}\"** in {after.guild.name}! <<< to {after.name}")
            
    elif len(after.roles) < len(before.roles):
        new_role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title=f"Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role removed', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"Events Listener: ROLES of {after} has been updated: REMOVED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.name != after.name:
        embed = discord.Embed(title=f"Changed name", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.name)
        embed.add_field(name='After', value=after.name)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"Events Listener: NAME of {after} has been updated FROM {before.name} TO {after.name} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.discriminator != after.discriminator:
        embed = discord.Embed(title=f"Changed discriminator", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.discriminator)
        embed.add_field(name='After', value=after.discriminator)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"Events Listener: DISCRIMINATOR of {after} has been updated FROM {before.discriminator} TO {after.discriminator} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
    
    sendLogsDir = (f"{base_directory}Servers{s_slash}{after.guild.id}{s_slash}sendMessages.txt")
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

#   on message

@client.event
async def on_message(message):
    global roleMember, hasMember, hasAdmin
    await bot_runtime_events(1)
    if "UUID of player EmileTigger is d0b393de-e783-45b6-9d13-19ba56c5451e" in message.content:
        termcolor.cprint("Emile joined", 'red', attrs=['blink'])
        await asyncio.sleep(3)
        await console.send("say FRENCH Detected!!!!")
    if "EmileTigger lost connection" in message.content:
        await console.send("say Au revoir!")

    async def DLstuff():
        if len(message.attachments) < 1: # Checks if there is an attachment on the message
            return
        else: # If there is it gets the filename from message.attachments
            if message.channel.id == 930494689105309777 or message.channel.id == 930496092754284576:
                upvote = client.get_emoji(803578918488768552)
                downvote = client.get_emoji(803578918464258068)
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
            try:
                attachmentsDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Attachments{s_slash}")
                if not os.path.exists(attachmentsDir):
                    os.makedirs(f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}Attachments{s_slash}")
                    print("Made directory" + (attachmentsDir))
            except AttributeError:
                print("Attachment sent in DMs.")
                attachmentsDir = (f"{base_directory}DMs{s_slash}Attachments{s_slash}{message.author.id}{s_slash}")
                if not os.path.exists(attachmentsDir):
                    os.makedirs(f"{base_directory}DMs{s_slash}Attachments{s_slash}{message.author.id}{s_slash}")
                    print("Made directory" + (attachmentsDir))
            nameOfFile = str(message.attachments).split("filename='")[1]
            filename = str(nameOfFile).split("' ")[0]
            beans = (f"{attachmentsDir}{filename}")
            attachment = message.attachments[0]
            
            if os.path.isfile(beans):
                filename = str(nameOfFile).split("' ")[0]
                beans = (f"{attachmentsDir}{uuid.uuid4()}-name={filename}")
            await message.attachments[0].save(fp=beans)

            try:
                LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                sendLogsDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}sendMessages.txt")
                if os.path.isfile(sendLogsDir):
                    await LoggingChannel.send(f"Attachment sent in <#{message.channel.id}>: **{filename}**: {attachment.url}")
            except:
                pass

    if running_locally: #	Modified in repl.it
      await DLstuff()

    if message.author.bot:
       return
    person = message.author
    personID = message.author.id

    if not message.guild:
        if message.content.startswith(".a"):
            x = message.content.split()
            msgchannel = (x[1])
            sp1 = message.content.split(' ', 2)[-1]
            channel = client.get_channel(int (msgchannel))
            await channel.send(f"`{sp1}`")
            return
        if message.content.startswith(".sa"):
            x = message.content.split()                
            msgchannel = (x[1])
            sp1 = message.content.split(' ', 2)[-1]
            channel = client.get_channel(int (msgchannel))
            await channel.send(str (sp1))
            return
        if message.content.startswith("."):
            await message.channel.send("Please use commands in a server with me in it for them to run correctly. Sorry!")
        #await draggie.send(f"\n'{message}' DMed by {person} at {datetime.now()}")
        print(f"\n'{message.content}' DMed by {person} at {datetime.now()}")

        dmLocation = (f"{base_directory}DMs{s_slash}{personID}.txt")
        logAllMessages = open(dmLocation, "a", encoding='utf-8')
        logAllMessages.write(f"\n'{message}' DMed by {person} at {datetime.now()}")
        logAllMessages.close()
        return
            
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    serverName = message.guild.name
    serverID = message.guild.id
    channelName = message.channel.name
    channelID = message.channel.id

    filedir = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Logs{s_slash}")
    if not os.path.exists(filedir):
      if running_locally: # Modified repl.it
        os.makedirs(f"{base_directory}Servers{s_slash}{serverID}{s_slash}Logs{s_slash}")
      else:
        os.makedirs(f"{base_directory}Servers{s_slash}{serverID}{s_slash}Logs{s_slash}")

    
    try:
        with open((f"{filedir}MessageLog.txt"), "a", encoding='utf-8') as logAllMessages:
            logAllMessages.write(f"\n'{message.content}' sent by {message.author} in [{serverName}- #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")
            logAllMessages.close()
    except Exception as e:
        errorMsg = str(f"\n\n\n\nError!!!! Logging file corruption has occured!!! cc: <@382784106984898560> \n\n\n\n{e}\n\n")
        print(errorMsg)
        try:
            with open((f"{filedir}MessageLog1.txt"), "a", encoding='utf-8') as logAllMessages:
                logAllMessages.write(f"\n'{message.content}' sent by {message.author} in [{serverName}- #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")
                logAllMessages.close()
        except Exception as e:
                errorMsg = str(f"\nCRITICAL ERROR!!!! Server file corruption has occured!!! cc: <@382784106984898560>, server ID is {serverID} / {channelID}\nDM Draggie#3060 if this does not get resolved in 10 minutes\nError: {e}")
                print(errorMsg)
                await draggie.send(errorMsg)

    print(f"\n'{message.content}' sent by {message.author} in [{serverName}- #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    if message.channel.name == 'nolwennium-138':
        emoji = client.get_emoji(786177817993805844)
        await message.add_reaction(emoji)
        
    if message.channel.id == 809112184902778890 or message.channel.id == 967114002347986954:
        if ("http") in message.content.lower() or len(message.attachments) >= 1:
            print("Yes")
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

#   Coin adder.
    if message.content != ".":
        await changeCoinBalance(message, 1)

#   Generic commands.

#   Thumb, async wait for test (Part of 1.2.4)

    if message.content.startswith('.thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

#   Hi autorun

    if message.guild.id in tester_guilds:
        if message.content == ("hi"):
            await message.reply(content='hi')
            f = open(GlobalLogDir, "a")
            f.write(f"\nWORD MENTIONED -> 'hi' ran by {message.author} at {datetime.now()}")
            f.close()

        if message.content == ("Hi"):
            await message.channel.send('Hi')
            f = open(GlobalLogDir, "a")
            f.write(f"\nWORD MENTIONED -> 'Hi' said by {message.author} at {datetime.now()}")
            f.close()

# Animated emoji sender.

        if message.content.startswith('ninjarage'): #                                     ninjarage emoji animated
            await message.channel.send("<a:ninjarage:767453473133953044>")
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.ninjarage' ran by {message.author} at {datetime.now()}")
            f.close()
            print(f"\nCOMMAND RAN -> '.ninjarage' ran by {message.author} at {datetime.now()}")
        if message.content.startswith('boris'): #                                     boris emoji animated
            await message.channel.send("<a:boris:795038238799822848>")
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.boris' ran by {message.author} at {datetime.now()}")
            f.close()
            print(f"\nCOMMAND RAN -> '.boris' ran by {message.author} at {datetime.now()}")
        if message.content.startswith('Colette'): #                                     boris emoji animated
            await message.channel.send("<a:colette:790577621690875956>")
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.Colette' ran by {message.author} at {datetime.now()}")
            f.close()
            print(f"\nCOMMAND RAN -> '.Colette' ran by {message.author} at {datetime.now()}")

        if message.content.startswith("bbot://"):
            if personID == 382784106984898560:
                x = message.content.split("/")
                actual_query = (x[2])
                if actual_query == "offline":
                    await client.change_presence(status=discord.Status.invisible)
                    await message.channel.send("Status set to invisible/offline.")
                #await message.channel.send(actual_query)
                #await message.channel.send("```Executed instruction.```")
                print("Ok")
            else:
                await message.channel.send(f"```{uuid.uuid4()}_callstack/MainThread: operation rejected, traceback includes data: message.author.id is {personID}```")

    #   test

        if message.content == ('test'):
            await message.channel.send("testerino")
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.test' ran by {message.author} in {message.guild.id} at {datetime.now()}")
            f.close()

        if message.content == ('France'):
            await message.channel.purge(limit=1)
            franceRand = 0
            franceRand = secrets.randbelow(270)
            if franceRand == 50:
                await message.channel.send("You must speak French in this server only for the next hour.")
                print (franceRand)
            else:
                await message.channel.send(f"Nope. (number = {franceRand})")
                print (franceRand)
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> 'France' ran by {message.author} in {message.guild.id} at {datetime.now()}. Number randomly generated between 0 and 100: {franceRand}")
            f.close()

    #   Split message

        if message.content.startswith (".split"):
            txt = message.content
            x = txt.split()
            print(x[1])
            await message.channel.send(x[1])

    #   Send Emoji for Face!

    if message.guild.id == 759861456300015657 or message.guild.id == 384403250172133387:#     Checks whether the server ID matches Baguette Brigaders's server for privacy
        if hasMember in person.roles:
            messageContent = message.content.lower()
            #for word in messageContent.split():
            #    print("")
            #    if word in nollyWords:
            ##        await message.add_reaction("<:nolly:786177817993805844>")
            #        print(f"Matched word in message! {word}")
            #    if word in oliverWords:
            #        await message.add_reaction("<:oliver:790576109795409920>")
            #        print(f"Matched word in message! {word}")
            #    if word in jackWords:
            #        await message.add_reaction("<:jacc:786275811405070337>")
             #       print(f"Matched word in message! {word}")
            ##    if word in joeWords:
            #        await message.add_reaction("<:CuteJoe:897467228545503242>")
            ##        print(f"Matched word in message! {word}")
            #    if word in haydnWords:
            #        await message.add_reaction("<:haydn:786276584671412244>")
            #        print(f"Matched word in message! {word}")
            #    if word in maisyWords:
            #        await message.add_reaction("<:maisy:786276271809101840>")
            #        print(f"Matched word in message! {word}")
            #    if word in benWords:
            #        await message.add_reaction("<:bennybooze:788311580768075786>")
            #        print(f"Matched word in message! {word}")
            #    if word in ishWords:
            ##        await message.add_reaction("<:ish:791381704278540369>")
            #        print(f"Matched word in message! {word}")
            #    if word in mayaWords:
            #        await message.add_reaction("<:maya:785942478448230470>") 
            #        print(f"Matched word in message! {word}")
            #    if word in samWords:
            #        await message.add_reaction("<:samf:785942793280815114>")
            #        print(f"Matched word in message! {word}")
            #for word in josephTighe:
            ##    if word in messageContent:
            #        print(f"Matched word in message! {word}")
            #        integer = random.randint(1,2)#      Sets random emoji reaction as he has 2 emojis.
            #        if integer == 1:
            #            await message.add_reaction("<:hmmnotsureaboutthis:870745923171549234>")#    if random int is 1 search for and add tighe 1
            ##        if integer == 2:
            #                await message.add_reaction("<:Joseph:865213431900143656>")#    else, search for and add tighe 2#
            #for word in charlieSewards:
            #    if word in messageContent:
            #        print(f"Matched word in message! {word}")
           ##         integer = random.randint(1,2)#      Again, sets random emoji reaction as he has 2 emojis.
           #         if integer == 1:
            #            await message.add_reaction("<:charlie:903324276147499041>")
            #        if integer == 2:
            #            await message.add_reaction("<:CharlieUwU:857907947371495424>")
#
    #  here we can do global server ones because its funny

    messageContent = message.content.lower()
    for word in messageContent.split():
        if word in borisWords:
            await message.add_reaction("<:boris:785942478381121556>")
            f = open(GlobalLogDir, "a", encoding="utf8")
            f.write((str (f"\nINFO: 'boris' emoji sent, initiated by '{message.author}' at {datetime.now()}")))
            f.close()  
       
#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

    else:
        if message.guild.id != 789537159450198036:
            await client.process_commands(message)

#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

#   baguettes
    
@client.command(help="Sends up to 9 random baguette pics", brief="Sends random baguette pics", pass_context=True)
async def baguette(ctx, member: discord.Member = None):
    await ctx.send(f"Use French Cuisine bot for this and much more! The commad is `/baguette`.\nAdd it! https://ibaguette.com/api/BotInvs/FrenchCuisine&permissions=V2")

#   Cross Server Messaging

@client.command(pass_context=True, hidden=True)
async def sa(ctx):
    text = ctx.message.content
    x = text.split()
    
    msgchannel = (x[1])
    sp1 = text.split(' ', 2)[-1]
    channel = client.get_channel((int (msgchannel)))
    await channel.send(str (sp1))
    return

@client.command(help="Use .snowflake <snowflake> to convert a Discord snowflake into a DateTime object, exact and relative to the second.", brief="Converts Discord snowflake into readable date")
async def snowflake(ctx, snowflake: int):
    x = ctx.message.content.split()
    try: #      Try and change the message content after the '.snowflake' into an integer.
        unix_timestamp = ((1420070400000 + int(((f"{(snowflake):b}")[:-22]), 2)) / 1000)
        stringe = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y,%m,%d,%H,%M,%S')
        stringe = stringe.split(",")
        string_to_send = (f"Exact: <t:{round(unix_timestamp)}>:{stringe[5]}. Relative: <t:{round(unix_timestamp)}:R>.")
        await ctx.send(string_to_send)
        print(string_to_send)
    except:#    If it doesn't work, then we can deduce that a number hasn't been inputted.
        await ctx.reply("That isn't a valid integer to converrt into a date.")
    
@client.command()
async def bb_xp(ctx):
    if ctx.author.id == 382784106984898560:
        guild = client.get_guild(759861456300015657)
        for channel in guild.text_channels:
            if channel.category.id == 930186026125762570:
                messages = 0
                print(f"Now indexing <#{channel.id}>")
                await ctx.send(f"Now indexing <#{channel.id}>")
                async for message in channel.history(limit=None): # Async through the messages
                    if os.path.isfile(f"Z:{s_slash}XP{s_slash}{message.author.id}{s_slash}xp.txt"):
                        with open (f"Z:{s_slash}XP{s_slash}{message.author.id}{s_slash}xp.txt", 'r') as f:
                            xp = f.read()
                            f.close()
                        try:
                            xp_to_add = int(xp) + random.randint(20, 30)
                        except:
                            xp_to_add = 10

                        with open (f"Z:{s_slash}XP{s_slash}{message.author.id}{s_slash}xp.txt", 'w+') as f:
                            f.write(str(xp_to_add))
                            print(f"Given {xp_to_add} to {message.author.id}")

                    else:
                        os.mkdir(f"Z:{s_slash}XP{s_slash}{message.author.id}")
                        x = open(f"Z:{s_slash}XP{s_slash}{message.author.id}{s_slash}xp.txt", 'w')
                        x.write("10")
                        x.close()
                        print(f"Created {message.author.id}")
                    messages = messages + 1
                await ctx.send(f"Credited XP for {messages} messages.")
    else:
        await ctx.send("Developer only command.")

#   Elon musk

@client.command(pass_context=True, help="X Æ A-12", brief="bebe spam X Æ A-12", hidden=True)
async def ElonMusk(ctx):
    await ctx.send("X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12X Æ A-12")

#   convert

@client.command(help="Shows coin balance. If above a threshold, shows items to buy", brief="Shows your balance, and available to buy items.", pass_context=True, hidden=True)
async def convert(ctx):
    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol=ETH'
    #await ctx.send("IDE detected! Unable to run command. Aborting.")
    #return
    with open(f"{base_directory}cmc_api_key.txt", encoding="utf-8") as f:
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

#   brawlstars

@client.command(help="Displays currency options and commands", brief="Displays currency options and commands.", pass_context=True)
async def currency(ctx):
    nolwenniumUserDirectory(ctx)
    my_file = Path(nolwenniumUserDir)

    if not my_file.is_file():
        with open(nolwenniumUserDir, 'a') as f:
            print (f"\n[CURRENCY - {name_Nolwennium}] Set {name_Nolwennium} value to 0, new user. {ctx.author.id} - {ctx.author.name}")
            try:
                f.write('0')
                f.close()
            except Exception:
                f.write('0')
                f.close()

    f = open(nolwenniumUserDir, 'r')
    nolwenniumBal = round(float(f.read()), 4)
    f.close()

    message = ""
    number = 0
    for guild in ctx.author.mutual_guilds:
        message += f"`{guild.name}` \n"
        number = number + 1

    await ctx.send(f"Multiplier: 1.{number}x ({number}0%) bonus {nolwenniumBal}")
    await ctx.send(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/baguette for updates on what this will do, and for the all-new currency system. You are eligible for {nolwenniumBal} new currency points! {emoji_Nolwennium}")

@client.command(hidden=True)
async def getBBboosters(ctx):
    if ctx.author.id == 382784106984898560:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Server Booster")
        if role is None:
            await bot.say('There is no "Server Booster" role on this server!')
            return
        hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
        hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
        hasPrince = discord.utils.find(lambda r: r.name == 'Prince', ctx.message.guild.roles)
        hasKing = discord.utils.find(lambda r: r.name == 'King', ctx.message.guild.roles)
        for member in ctx.guild.members:
            coinDir = (f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}Coins{s_slash}{member.id}.txt")
            refresher = False
            if hasCitizen in member.roles:
                await member.remove_roles(hasCitizen)
                await member.send(f"Your role **Citizen** has been (temporarily) removed due to a server update. To get this role again, simply buy it from the shop in {ctx.guild.name} for free!")
                refresher = True
            if hasKnight in member.roles:
                await member.remove_roles(hasKnight)
                await member.send(f"Your role **King** has also been removed. You have been **refunded** an **additional 300 coins** to purchase new roles.")
                f = open(coinDir, 'r')
                coins = int(f.read())
                f.close()
                newSum = coins + 300
                f = open(coinDir, 'w+')
                f.write(str (newSum))
                f.close()
                refresher = True
            if hasPrince in member.roles:
                await member.remove_roles(hasPrince)
                await member.send(f"Your role **Prince** has also been removed. You have been **refunded** an **additional 1250 coins** to purchase new roles.")
                f = open(coinDir, 'r')
                coins = int(f.read())
                f.close()
                newSum = coins + 1250
                f = open(coinDir, 'w+')
                f.write(str (newSum))
                f.close()
                refresher = False
            if hasKing in member.roles:
                f = open(coinDir, 'r')
                coins = int(f.read())
                f.close()
                newSum = coins + 3000
                f = open(coinDir, 'w+')
                f.write(str (newSum))
                f.close()
                await member.remove_roles(hasKing)
                await member.send(f"Your role **King** has also been removed. You have been **refunded** an **additional 3000 coins** to purchase new roles.")
                refresher = False
            
            if refresher == True:
                await member.send(f"In case you need a refresher, the command to see your coins is `.coins`, and to buy an item, use the command `.buy <item>` in {ctx.guild.name}. Thank you for being a part of this epic community!")
            await asyncio.sleep(0.1)

            if role in member.roles:
                nolwenniumUserDir = (f"{base_directory}Nolwennium{s_slash}{member.id}.txt")
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    with open(nolwenniumUserDir, 'a') as f:
                        print (f"\n[CURRENCY - {name_Nolwennium}] Set {name_Nolwennium} value to 0, new user. {member.id} - {member.name}")
                        f.write('0')
                        f.close()

                with open(nolwenniumUserDir, 'r') as f:
                    beforeBonusAmount = (float (f.read()))
                    f.close()

                toAdd = random.randint(100,1000)
                addedAmount = beforeBonusAmount + toAdd       

                f = open(nolwenniumUserDir, 'w+')
                f.close()

                with open(nolwenniumUserDir, 'a') as f:
                    f.write(str (addedAmount))
                    print (f"\n[CURRENCY - {name_Nolwennium}] Added balance of {toAdd} (total: {addedAmount} for boosting the server: {member.id} - {member.name}")
                    f.close()

                f = open(coinDir, 'r')
                coins = int(f.read())
                f.close()
                newSum = coins + 200
                f = open(coinDir, 'w+')
                f.write(str (newSum))
                f.close()
                f = open(coinDir, 'r')
                newCoins = int(f.read())
                f.close()

                await general.send(f"Thank you {member.mention} for boosting the server! You have the **Server Booster** role, an **exclusive name colour**, and a bonus sum of Coins (total: {newCoins}) and {name_Nolwennium} (total: {addedAmount}). You can also change your name's colour **permanently** to a colour of your choice, type `/namecolour` and enter the colour you want!")

#   coins

@client.command(
    help="Shows coin balance. If above a threshold, shows items to buy", 
    brief="Shows your balance, and available to buy items.", 
    pass_context=True,
    aliases=['shop', 'rank', 'points', 'balance', 'bal', 'coin', 'nolly', 'nolwennium', 'nolwenn', 'score'],
    hidden=False
    )
async def coins(ctx):
    #   Firstly get the guild and member intent.
    if ctx.message.guild.id == 759861456300015657:
        member_role = discord.utils.get(ctx.guild.roles, name=f"Member")
        if member_role in ctx.author.roles:
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
            serverID = ctx.message.guild.id
            #print (serverID)

            coinDirectory(ctx)
            f = open(coinDir, 'r')
            coinBal = f.read()
            f.close()

            nolwenniumUserDir = (f"{base_directory}Nolwennium{s_slash}{authorID}.txt")
            my_file = Path(nolwenniumUserDir)

            if not my_file.is_file():
                with open(nolwenniumUserDir, 'a') as f:
                    print (f"\nSet {name_Nolwennium} value to 0, {authorID} is a new user.")
                    try:
                        f.write('0')
                        f.close()
                    except Exception:
                        f.write('0')
                        f.close()

            f = open(nolwenniumUserDir, 'r')
            nolwenniumBal = round(float(f.read()), 2)
            f.close()
            
            if ctx.message.guild.id == 384403250172133387 or ctx.guild.id == 759861456300015657:
                canRunCommand = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
                canRunCommand2 = discord.utils.find(lambda r: r.name == 'Admin', ctx.message.guild.roles)
                if canRunCommand or canRunCommand2 in user.roles:
                    try:
                        #	List of stuff BEFORE showing the user their balance
                        txt = ctx.message.content
                        x = txt.split()
                        word1 = (str (x[1]))

                        if word1.lower() == 'set':
                            if ctx.message.author.guild_permissions.administrator == True:
                                userID = (str (x[2]))
                                amount = (str (x[3]))
                                usersCoins = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{userID}.txt")
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
                                    await ctx.send(f"<@{userID}>'s coins have been updated from {oldCoins} {emoji_Coins} to **{newCoins}** {emoji_Coins}.")
                                if silent == True:
                                    print(f"Old coins: {oldCoins} -----> New coins: {newCoins}")
                                    await ctx.message.add_reaction('✅')
                                return
                        
                        if word1.lower() == 'add':
                            if ctx.message.author.guild_permissions.administrator == True:
                                userID = (str (x[2]))
                                amountToAdd = (str (x[3]))

                                usersCoins = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{userID}.txt")

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
                                    await ctx.send(f"<@{userID}>'s coins have been updated from {oldCoins} {emoji_Coins} to **{newCoins}** {emoji_Coins}.")
                                if silent == True:
                                    print(f"{userID}: Old coins: {oldCoins} -----> New coins: {newCoins}")
                                    await ctx.message.add_reaction('✅')
                                return
                        if word1.lower() == 'lookup':
                            if ctx.message.author.guild_permissions.administrator == True:
                                userID = (str (x[2]))

                                usersCoins = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{userID}.txt")
                                oc = open(usersCoins, 'r')
                                coinAmount = oc.read()
                                oc.close()

                                nolwenniumUserDir = (f"{base_directory}Nolwennium{s_slash}{userID}.txt")
                                my_file = Path(nolwenniumUserDir)

                                if not my_file.is_file():
                                    with open(nolwenniumUserDir, 'a') as f:
                                        print (f"\nSet{name_Nolwennium} value to 0, {userID} is a new user.")
                                        try:
                                            f.write('0')
                                            f.close()
                                        except Exception:
                                            f.write('0')
                                            f.close()

                                f = open(nolwenniumUserDir, 'r')
                                nolwenniumBal = round(float(f.read()), 2)
                                f.close()

                                if silent == False:
                                    await ctx.send(f"<@{userID}> has **{coinAmount}** coins, and **{nolwenniumBal}** {name_Nolwennium}.")
                                if silent == True:
                                    print(f"{userID}:       Coins: {coinAmount} -----> {name_Nolwennium}: {nolwenniumBal}")
                                    await ctx.message.add_reaction('✅')
                                    await ctx.author.send(f'<@{userID}> has **{coinAmount}** coins, and **{nolwenniumBal}** {name_Nolwennium}.')
                                return
                        else:
                            await ctx.send("I don't know what you mean. The correct syntaxes are:\n\n`.coins set <targetUserID> <newCoins>`\n`.coins add <targetUserID> <addedAmount>`\n`.coins lookup <targetUserID>`")

                    except Exception:#		AFTER the list of alternate options has been checked; the user just wants their balance.
                        hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
                        hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
                        hasBaron = discord.utils.find(lambda r: r.name == 'Baron', ctx.message.guild.roles)
                        hasViscount = discord.utils.find(lambda r: r.name == 'Viscount', ctx.message.guild.roles)
                        hasEarl = discord.utils.find(lambda r: r.name == 'Earl', ctx.message.guild.roles)
                        hasMarquess = discord.utils.find(lambda r: r.name == 'Marquess', ctx.message.guild.roles)
                        hasDuke = discord.utils.find(lambda r: r.name == 'Duke', ctx.message.guild.roles)
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
                        
                        next_available_role_cost = 0
                        roles_tier = -1

                        if hasCitizen in user.roles:
                            roles_tier = roles.Citizen_Tier
                        if hasKnight in user.roles:
                            roles_tier = roles.Knight_Tier
                        if hasBaron in user.roles:
                            roles_tier = roles.Baron_Tier
                        if hasViscount in user.roles:
                            roles_tier = roles.Viscount_Tier
                        if hasEarl in user.roles:
                            roles_tier = roles.Earl_Tier
                        if hasMarquess in user.roles:
                            roles_tier = roles.Marquess_Tier
                        if hasMarquess in user.roles:
                            roles_tier = roles.Marquess_Tier
                        if hasDuke in user.roles:
                            roles_tier = roles.Duke_Tier
                        if hasPrince in user.roles:
                            roles_tier = roles.Prince_Tier
                        if hasKing in user.roles:
                            roles_tier = roles.King_Tier

                        topRole_name = roles.Roles_order_List[roles_tier]
                        #await ctx.send(f"The user's top role is {topRole_name}")
                        nextRole = roles.Roles_order_List[(roles_tier + 1)]
                        next_available_role_cost = roles.Roles_Cost[(roles_tier + 1)]

                        #await ctx.send(f"the next role is {nextRole} which will cost {roles.Roles_Cost[(roles_tier + 1)]} coins. this means they are {next_available_role_cost - int(coinBal)} coins away.")

                        if roles_tier != -1:
                            roles_liste = ""

                            for i in range((roles_tier + 1)):
                                roles_liste = (f"{roles_liste}" + f"{(roles.Roles_order_List[i])}: Unlocked! 🔓\n")
                                i = i + 1
                            #await ctx.send(roles_liste)

                            f = open (nolwenniumUserDir, 'r')
                            nolwenniumBal = round(float(f.read()), 2)
                            f.close()

                            finalSum = f"{roles_liste}" + f"{nextRole}: {roles.Roles_Cost[(roles_tier + 1)]} {emoji_Coins} 🔒"

                            if "🔓" not in finalSum:
                                if f"{emoji_Coins}" not in finalSum:
                                    finalSum = f"***You have bought all possible roles! Maybe some more will come out in the future...***"
                        else:
                            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {emoji_Coins} coins and {nolwenniumBal} {emoji_Nolwennium} Nolwennium available to spend."), colour=0xFFD700)
                            embed.add_field(
                                name="Items curently available for you to buy:",
                                value=f"**Citizen**: FREE {emoji_Coins}\n\nType **.buy citizen** to start ascending through purchasable roles!",
                                inline=False
                                )
                            embed.set_footer(text=(f'Type ".buy item" to buy your selected item! For example, .buy citizen.\nYou can buy roles for Coins in this server, and use {name_Nolwennium} to run bot commands (in all servers).'))
                            await ctx.send(embed=embed)
                            return
                        
                        embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {emoji_Coins} coins and {nolwenniumBal} {emoji_Nolwennium} Nolwennium available to spend."), colour=0xFFD700)
                        embed.add_field(
                            name="Items available to buy:",
                            value=finalSum,
                            inline=False
                            )
                        if next_available_role_cost > 0:
                            embed.add_field(
                                name="Next item available to buy in:",
                                value=f"{next_available_role_cost - int(coinBal)} {emoji_Coins} Coins (**{nextRole}**)",
                                inline=False
                                )
                        elif next_available_role_cost <= 0:
                            embed.add_field(name="Buy your roles!", value=f":warning: You can afford a new role. Once bought, this will say how\n many more {emoji_Coins} Coins are needed until the next role.")

                        if serverID in tester_guilds:
                            embed.set_footer(text=(f'Type ".buy item" to buy your selected item! For example, .buy citizen.\nYou can buy roles for Coins in this server, and use {name_Nolwennium} to run bot commands (in all servers).'))
                        else:
                            embed.set_footer(text=(f"Type .buy item to buy your selected item!\nYou can buy roles for Coins, and use {name_Nolwennium} to run commands for the bot (saved across all servers)."))
                        await ctx.send(embed=embed)
                else:
                    await ctx.send("You do not have permission to access the shop interface.")
            else:
                nolwenniumUserDirectory(ctx)
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    nolly = "0"
                else:
                    f = open(nolwenniumUserDir, 'r')
                    nolwenniumBal = f.read()
                    f.close()
                    nolly = f"{nolwenniumBal} {emoji_Nolwennium}"
                await ctx.send(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/baguette for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {emoji_Nolwennium}")
        else:
            await error_code(ctx, 1)

#   buy

@client.command(help="Shows coin balance. If above a threshold, displays the list of roles the user can buy by typing .buy <role>", brief="Shows your balance, and available to buy items.", pass_context=True, hidden=True)
async def buy(ctx):
    if ctx.guild.id in tester_guilds:
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
                    determiner = determiner.lower()
                except Exception as e:
                    await ctx.send("Please enter an item to buy.")
                    return
                filedir = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{authorID}.txt")
                f = open(filedir, 'r')
                coinBal = f.read()
                f.close()

                if determiner == 'citizen':
                    hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
                    if hasCitizen in member.roles:
                        await ctx.send("You can't buy Citizen, you already have it!")
                        return
                    
                    coinBal = int(coinBal) - 1
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name="Citizen")
                    await member.add_roles(role)
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought Citizen for free! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"• Above Member in the Member List\n• Custom nickname\n• Add reactions\n• Bonus {name_Nolwennium}", inline=False)   
                    await ctx.send(embed=embed)
                    return

#           KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT

            if determiner == 'knight':
                cost = 25
                roleName = "Knight"
                hasKnight = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasKnight in member.roles:
                    await ctx.send(f"You can't buy {roleName}, you already have it!")
                    return
                        
                hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', ctx.message.guild.roles)
                if hasCitizen in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Citizen"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Create private threads", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Citizen before {roleName}.")
                    return
                return

#           BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON 

            if determiner == 'baron':
                cost = 50
                roleName = "Baron"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasBaron in member.roles:
                    await ctx.send(f"You can't buy {roleName}, you already have it!")
                    return
                
                #   Check if the person has the previous role. If not, can't buy.
                hasKnight = discord.utils.find(lambda r: r.name == 'Knight', ctx.message.guild.roles)
                if hasKnight in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Knight"))
                    await member.add_roles(role)

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Use external stickers\nBonus {name_Nolwennium}", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Knight before {roleName}.")
                    return
                return

#           VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT 

            if determiner == 'viscount':
                cost = 100
                roleName = "Viscount"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasBaron in member.roles:
                    await ctx.send("You can't buy Viscount, you already have it!")
                    return
                
                #   Check if the person has the previous role. If not, can't buy.
                hasBaron = discord.utils.find(lambda r: r.name == 'Baron', ctx.message.guild.roles)
                if hasBaron in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Use TTS messages\nUse server activities", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Baron before {roleName}.")
                    return
                return

#           EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL

            if determiner == 'earl':
                cost = 250
                roleName = "Earl"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasBaron in member.roles:
                    await ctx.send("You can't buy Earl, you already have it!")
                    return
                
                #   Check if the person has the previous role. If not, can't buy.
                hasViscount = discord.utils.find(lambda r: r.name == "Viscount", ctx.message.guild.roles)
                if hasViscount in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Viscount"))
                    await member.add_roles(role)

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Add and edit server events", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Viscount before {roleName}.")
                    return
                return

#           MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS 

            if determiner == 'marquess':
                cost = 500
                roleName = "Marquess"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasBaron in member.roles:
                    await ctx.send("You can't buy Earl, you already have it!")
                    return
                
                #   Check if the person has the previous role. If not, can't buy.
                hasEarl = discord.utils.find(lambda r: r.name == 'Earl', ctx.message.guild.roles)
                if hasEarl in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Access to history of <#865291106459844609>\nAccess to #deleted-channel", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Earl before {roleName}.")
                    return
                return

#           DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE 

            if determiner == 'duke':
                cost = 1000
                roleName = "Duke"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasBaron in member.roles:
                    await ctx.send("You can't buy Earl, you already have it!")
                    return
                
                #   Check if the person has the previous role. If not, can't buy.
                hasMarquess = discord.utils.find(lambda r: r.name == 'Marquess', ctx.message.guild.roles)
                if hasMarquess in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await ctx.send(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Marquess"))

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"View server statistics\nMute members\nManage threads", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"You must buy Marquess before {roleName}.")
                    return
                return
        
#           PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE 

            if determiner == 'prince':
                cost = 2500
                roleName = "Prince"
                hasPrince = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasPrince in member.roles:
                    await ctx.send("You can't buy Prince, you already have it!")
                    return
                
                hasDuke = discord.utils.find(lambda r: r.name == 'Duke', ctx.message.guild.roles)
                if hasDuke in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        await ctx.send(f"You do not have enough Coins to buy {roleName}.")
                        return
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Duke"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Move members in voice channels\nAccess to #deleted-channel\nUse Priority speaker in voice chat\nChange others' nicknames\nTime out members\nAdd emojis and stickers\nAdd custom channels", inline=False)   
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("You must buy Knight before Prince.")
                return

#           KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING 

            if determiner == 'king':
                cost = 10000
                roleName = "King"
                hasKing = discord.utils.find(lambda r: r.name == roleName, ctx.message.guild.roles)
                if hasKing in member.roles:
                    await ctx.send("You can't buy King, you already have it!")
                    return
                
                hasPrince = discord.utils.find(lambda r: r.name == 'Prince', ctx.message.guild.roles)
                if hasPrince in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest < 0:
                        await ctx.send("You do not have enough Coins to buy King.")
                        return
                    coinBal = int(coinBal) - cost
                    f = open(filedir, 'w+')
                    f.close()
                    with open(filedir, 'a') as f:
                        f.write(str (coinBal))
                        f.close()
                    role = discord.utils.get(ctx.message.guild.roles, name="King")
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Prince"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought King for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", value=f"Deafen members\nPin and manage messages\nAccess to #deleted-channel\nAccess to history of #deleted-channel\nAdd webhooks\nAdd bots\nAdd channels", inline=False)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("You must buy Prince before King.")
                return
            
            if determiner == 'admin':
                await ctx.send("Required role missing (`Croissant`, `Staff`)")
            else:
                await ctx.send(f"**{determiner}** isn't a valid item to buy. Try `Citizen/Knight/Baron/Viscount/Earl/Marquess/Duke/Prince/King/Admin`!")
        else:
            await error_code(ctx, 1)
    else:
        nolwenniumUserDirectory(ctx)
        my_file = Path(nolwenniumUserDir)
        if not my_file.is_file():
            nolly = "0"
        else:
            f = open(nolwenniumUserDir, 'r')
            nolwenniumBal = f.read()
            f.close()
            nolly = f"{nolwenniumBal} {emoji_Nolwennium}"
        await ctx.send(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/baguette for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {emoji_Nolwennium}")

#   Get messages

@client.command(pass_context=True, hidden=True)
async def getMessages(ctx):
    if ctx.message.author.id == 382784106984898560:
        x = ctx.message.content.split()
        userID = int((x[1]))

        user1 = await client.fetch_user(userID)

        dmchannel = await user1.create_dm() # "Create" a DM
        async for message in dmchannel.history(limit=30): # Async through the messages
            await ctx.send(f"{message.author.name}: `{message.content}`")

#   Voice Channel Bitrate

@client.command(help="Changes voice channel bitrate. Syntax '.bitrate [channelID] [bitrateInBits]'.", brief="Changes voice channel bitrate.", pass_context=True)
async def bitrate(ctx):
    text = ctx.message.content
    x = text.split()
    channelID = (int (x[1]))
    bitrate = (int (x[2]))
    vchannel = client.get_channel(channelID)
    await vchannel.edit(bitrate=(bitrate), reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")

#   offline status for replit

@client.command(help="Turns status to offline/invisible", brief="[Status] Turns invisible", hidden=True)
async def offline(ctx):
    await client.change_presence(status=discord.Status.invisible)
    await ctx.send("Status set to invisible/offline.")

@client.command(help="Turns status to offline/invisible", brief="[Status] Turns invisible", hidden=True)
async def online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.send("Status set to online.")

@client.command(hidden=True)
async def variable(ctx):
    if ctx.author.id == id_Draggie:
        x = ctx.message.content.split()
        word1 = (str (x[1]))
        word2 = (str (x[2]))
        await ctx.send(f"Set {word1} to value {word2}.")
        word1 = word2

#   yn

@client.command(help="Randomly answers yes or no.", brief="Ask me a yes/no question.", pass_context=True, hidden=True)
async def yn(ctx):
    list_test = ["No!", "Of course not!", "Certainly not.", "Definitely not!", "Obviously not.", "Nah!", "Nope.", 
                "Yes!", "Obviously!", "Of course!", "Certainly!",  "Definitely!",  "Without a shadow of a doubt!", "Yessir!"]
    await ctx.send(random.choice(list_test))

    print (f"\nCOMMAND RAN -> '.yn' ran by {ctx.message.author}")
    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.yn' ran by {ctx.message.author} at {datetime.now()}")
    f.close()

#   setdelay

@client.command(help="Sets slow mode.", brief="Sets slow mode. Syntax = .setdelay [delayInSec]", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def setdelay(ctx):
    txt = ctx.message.content
    x = txt.split()
    sp1 = (str (x[1]))
    
    await ctx.channel.edit(slowmode_delay=sp1, reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")

    embed = discord.Embed
    embed=discord.Embed(title="Edited channel info!", description=(f"Set the slowmode delay in this channel to {sp1} seconds!"), colour=0x228B22)
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write(f"\nCOMMAND RAN -> '.setdelay {sp1}' ran by {ctx.message.author} in channel {ctx.channel.mention} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.setdelay {sp1}' ran by {ctx.message.author} in channel {ctx.channel.mention} at {datetime.now()}")

#	Brawl Stars Music

@client.command(help="Plays random Brawl Stars music. This command requires the user to be in a voice channel. Also triggered by typing .r", brief="[Audio] Repeatedly plays Brawl Stars music.", aliases=['r'], pass_context=True, hidden=True)
async def radio(ctx):
    channel = ctx.author.voice.channel
    serverName = ctx.message.guild.name
    testForToggles = ctx.message.content
    debugMode = False
    if ("/d") in testForToggles.lower():
        if ctx.message.author.guild_permissions.administrator == True:
            debugMode = True
        else:
            await ctx.send("Your server administrator has disabled the option to use the debug mode toggle.")
    def after_audio():
        voice_client = ctx.guild.voice_client
        randomnumber = random.randint(1,69)
        musicDir = (f"D:{s_slash}App Files{s_slash}Brawl Music{s_slash}py{s_slash}music_{randomnumber}.ogg")
        voice_client.play(discord.FFmpegPCMAudio(source=musicDir), after=lambda e: after_audio())
        print(f"RADIO: Playing 'music_{randomnumber} in [{serverName} / {channel}] Debug data: in after_audio")
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
            musicDir = (f"D:{s_slash}App Files{s_slash}Brawl Music{s_slash}py{s_slash}music_{randomnumber}.ogg")
            voice_client.play(discord.FFmpegPCMAudio(source=musicDir), after=lambda e: after_audio())
            print(f"RADIO: Playing 'music_{randomnumber}' in [{serverName}/{channel}] Debug data: in BaguetteBot v1.2.py/funcion/playtheaudio/try")
            if debugMode == True:
                await ctx.channel.send(f"```RADIO: Playing 'music_{randomnumber}' in [{serverName} / {channel}] Debug data: in BaguetteBot v1.2.py/funcion/playtheaudio/try```")
            await ctx.message.add_reaction('<a:AnimatedTick:956621591108804652>')

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
        await ctx.send(f"£ {GBP} is equal to {vAmount} vbucks (using tier 1 of vbuck purchase).")
    if vTier == (float ("2")):
        vAmount = (int (vTier2)) * (int (vAmount))
        await ctx.send(f"£ {GBP} is equal to {vAmount} vbucks (using tier 2 of vbuck purchase).")
        print (vAmount)
    if vTier == (float ("3")):
        vAmount = (int (vTier3)) * (int (vAmount))
        await ctx.send(f"£ {GBP} is equal to {vAmount} vbucks (using tier 3 of vbuck purchase).")
        print (vAmount)
    if vTier == (float ("4")):
        vAmount = (int (vTier4)) * (int (vAmount))
        await ctx.send(f"£ {GBP} is equal to {vAmount} vbucks (using tier 4 of vbuck purchase).")
        print (vAmount)

#   Vbucks USD

@client.command(hidden=True)
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

    if vTier == "1":
        vAmount = (int (vTier1USD)) * (int (vAmount))
        await ctx.send(f"${USD} is equal to {vAmount} vbucks (using tier 1 of vbuck purchase)")
        print (vAmount)
    if vTier == "2":
        vAmount = (int (vTier2USD)) * (int (vAmount))
        await ctx.send(f"${USD} is equal to {vAmount} vbucks (using tier 2 of vbuck purchase)")
        print (vAmount)
    if vTier == "3":
        vAmount = (int (vTier3USD)) * (int (vAmount))
        await ctx.send(f"${USD} is equal to {vAmount} vbucks (using tier 3 of vbuck purchase)")
        print (vAmount)
    if vTier == "4":
        vAmount = (int (vTier4USD)) * (int (vAmount))
        await ctx.send(f"${USD} is equal to {vAmount} vbucks (using tier 4 of vbuck purchase)")
        print (vAmount)

#   Face

@client.command(help="Allows face.", brief="Allows face.", pass_context=True, hidden=True)
async def face(ctx):
    if ctx.guild.id == 759861456300015657:
        await ctx.send("Face allowed. Please wait for the next DraggieBot version for your setting to be applied. This may take an hour. If your face is not already added, please go to #emoji-nominations channel to add or modify it! :)")
        f = open(GlobalLogDir, "a")
        f.write(f"\nCOMMAND RAN -> '.face' ran by {ctx.message.author} at {datetime.now()}")
        f.close()
        print (f"\nCOMMAND RAN -> '.face' ran by {ctx.message.author} at {datetime.now()}")


@client.command(hidden=True)
async def saveanddelete(ctx):
    if ctx.author.id == 382784106984898560:
        channel = ctx.channel
        count = 0
        errors = 0
        attachments = 0
        error_details = []
        tighe1 = round(time.time() * 1000)
        await ctx.message.add_reaction('<a:AnimatedTick:956621591108804652>')
        async for message in channel.history(limit=None):
            if len(message.attachments) < 1: # Checks if there is an attachment on the message
                with open((f"{temp_folder}{channel.name}_log.txt"), "a", encoding='utf-8') as logAllMessages:
                    logAllMessages.write(f"\n'{message.content}' sent by {message.author} at {(message.created_at)}")
                    print(f"\n'{message.content}' sent by {message.author}")
                    logAllMessages.close()
                    count = count + 1
            else: # If there is it gets the filename from message.attachments
                try:
                    attachmentsDir = (f"{temp_folder}{message.channel.name}{s_slash}Attachments{s_slash}")
                    if not os.path.exists(attachmentsDir):
                        os.makedirs(f"{temp_folder}{message.channel.name}{s_slash}Attachments{s_slash}")
                        print("Made directory" + (attachmentsDir))
                    nameOfFile = str(message.attachments).split("filename='")[1]
                    filename = str(nameOfFile).split("' ")[0]
                    beans = (f"{attachmentsDir}{filename}")
                    attachment = message.attachments[0]
                    
                    if os.path.isfile(beans):
                        filename = str(nameOfFile).split("' ")[0]
                        beans = (f"{attachmentsDir}{uuid.uuid4()}-name={filename}")
                    await message.attachments[0].save(fp=beans)
                    await message.delete()

                    #LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                    #sendLogsDir = (f"{base_directory}Servers{s_slash}{message.guild.id}{s_slash}sendMessages.txt")
                    #if os.path.isfile(sendLogsDir):
                        #await LoggingChannel.send(f"Attachment sent in <#{message.channel.id}>: **{filename}**: {attachment.url}")
                    count = count + 1
                    attachments = attachments + 1
                except Exception as e:
                    errors = errors + 1
                    error_details.append(e)
        tighe2 = round(time.time() * 1000)
        nTighe = tighe2 - tighe1
        await draggie.send(f"Counted {count} messages and {attachments} attachments ({errors} errors) in {nTighe}ms in server {message.guild.name}. Deleted <#{message.channel.id}> (#{message.channel.name})")
        if error_details != []:
            await draggie.send(f"Error info: {error_details}")
        await ctx.send("Deleting this channel in 5 seconds unless interrupted.")
        await asyncio.sleep(5)
        await message.channel.delete()

@client.command(hidden=True, brief="Saves channel messages")
async def save_messages(ctx):
    if ctx.author.id == 382784106984898560:
        channel = ctx.channel
        count = 0
        errors = 0
        attachments = 0
        error_details = []
        tighe1 = round(time.time() * 1000)
        await ctx.message.delete()

        def line_prepender(filename, line, content1):
            if not os.path.isfile(filename):
                with open(filename, 'w+') as e:
                    e.write(f"\n\nGenerated at {datetime.now()}. Requested by {ctx.author.name} in {ctx.message.guild.name}.")
            with open(filename, 'r+', encoding="utf-8") as fp:
                lines = fp.readlines()     # lines is list of line, each element '...\n'
                lines.insert(0, content1)  # you can use any index if you know the line index
                fp.seek(0)                 # file pointer locates at the beginning to write the whole file again
                fp.writelines(lines)       # write whole lists again to the same file
        message_total = ""
        async for message in channel.history(limit=None):
            if len(message.attachments) < 1: # Checks if there is an attachment on the message
                if "https" not in message.content:
                    line_prepender(f"Z:{s_slash}{channel.name}_log.txt", 1, f"\n>> MESSAGE: Sent at {(message.created_at)} by {message.author}: '{message.content}'")
                    count = count + 1
                else:
                    line_prepender(f"Z:{s_slash}{channel.name}_log.txt", 1, f"\n>> LINK:    Sent at {(message.created_at)} by {message.author}: {message.content}")
            else: # If there is it gets the filename from message.attachments
                try:
                    with open((f"Z:{s_slash}{channel.name}_log.txt"), "a", encoding='utf-8') as logAllMessages:
                        line_prepender(f"Z:{s_slash}{channel.name}_log.txt", 1, f"\n>> MEDIA:   Sent at {(message.created_at)} by {message.author}: {message.attachments[0].url}")
                    attachmentsDir = (f"Z:{s_slash}{message.channel.name}{s_slash}Attachments{s_slash}")
                    if not os.path.exists(attachmentsDir):
                        os.makedirs(f"Z:{s_slash}{message.channel.name}{s_slash}Attachments{s_slash}")
                        print("Made directory" + (attachmentsDir))
                    nameOfFile = str(message.attachments).split("filename='")[1]
                    filename = str(nameOfFile).split("' ")[0]
                    beans = (f"{attachmentsDir}{filename}")
                    if os.path.isfile(beans):
                        filename = str(nameOfFile).split("' ")[0]
                        beans = (f"{attachmentsDir}{uuid.uuid4()}-name={filename}")
                    await message.attachments[0].save(fp=beans)
                    count = count + 1
                    attachments = attachments + 1
                except Exception as e:
                    errors = errors + 1
                    error_details.append(e)
            message_total = f"{message.content} {message_total}"
        print(f"'{message_total}'")
        tighe2 = round(time.time() * 1000)
        nTighe = tighe2 - tighe1
        await draggie.send(f"Counted {count} messages and {attachments} attachments ({errors} errors) in {nTighe}ms in server {message.guild.name}. Deleted <#{message.channel.id}> (#{message.channel.name})")
        if error_details != []:
            await draggie.send(f"Error info: {error_details}")

#   brawlstars

@client.command(help="?", brief="?", pass_context=True, hidden=True)
async def BrawlStars(ctx):
    if ctx.guild.id == 759861456300015657:
        num_lines = sum(1 for line in open ("C:{s_slash}Users{s_slash}Draggie{s_slash}iCloudDrive{s_slash}iCloud~is~workflow~my~workflows{s_slash}Brawl Stars Counter.txt"))
        await ctx.send(f"I have opened Brawl Stars ***{num_lines}***  times since the 19th October 2020.")
        f = open(GlobalLogDir, "a")
        f.write(f"\nCOMMAND RAN -> '.lines' ran by {ctx.message.author} at {datetime.now()}")
        f.close()

#   log search

@client.command(help="Searches log for term. Syntax .log [term]", brief="Searches server's message log for term.", pass_context=True)
async def log(ctx):
    message = ctx.message.content
    searchTerm = message.split(' ', 1)[-1]
    searchTerm = searchTerm.lower()
    serverID = ctx.message.guild.id
    serverName = ctx.message.guild.name
    file=open((f"{base_directory}Servers{s_slash}{serverID}{s_slash}Logs{s_slash}MessageLog.txt"),encoding="UTF-8").read().lower()
    count=file.count(searchTerm)

    count = count - 1
    
    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{searchTerm}**':", value=f"{count}", inline=False)
    embed.set_footer(text=f"Not case sensitive. Does not account for bot messages. Searching in server {serverID}/{serverName}.")
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.log' ran by {ctx.message.author} at {datetime.now()}")
    f.close()

@slash.slash(name="stats", description="Useful bot statistics.")
async def _stats(ctx):
    await bot_runtime_events(1)
    if round(client.latency * 1000) <= 100:
        pingColour = (0x44ff44)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xffd000)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xff6600)
    else:
        pingColour = (0x990000)

    fileSizeBytes = os.path.getsize(f'{base_directory}GitHub{s_slash}BaguetteBot{s_slash}BaguetteBot.py')

    num_lines = sum(1 for line in open (f"{base_directory}GitHub{s_slash}BaguetteBot{s_slash}BaguetteBot.py", encoding='utf-8'))
    secsOrMins1 = "seconds"
    current_time = time.time()
    uptimeInSeconds = int(round(current_time - start_time))

    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    secsOrMins2 = "seconds"
    if uptimeInSeconds > 60:
        uptimeInSeconds = int(round(uptimeInSeconds / 60))
        secsOrMins2 = "minutes"

    real_uptimeInSeconds = int(round(current_time - ready_start_time))

    ping = round(client.latency * 1000)

    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    DIR = 'D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\AudioCache\\'
    cachedVideos = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

    embed = discord.Embed(title="_**Bot Stats**_\n", colour=pingColour)
    embed.add_field(name="CPU Usage", value=f"{cpuPercentage}%")  
    embed.add_field(name="RAM Usage", value=f"{memoryUsage}%")  
    embed.add_field(name="Lines of Code", value=f"{num_lines} lines")    
    embed.add_field(name="File Size", value=(f"{fileSizeBytes} bytes"))    
    embed.add_field(name="**Uptime:**", value=(f"{uptimeInSeconds} {secsOrMins2} ({real_uptimeInSeconds}s ago)"))
    embed.add_field(name="**Ping:**", value=(f"{ping} ms"))
    embed.add_field(name="**Videos Loaded:**", value=cachedVideos)
    embed.add_field(name="**Servers :**", value=(servers))
    embed.add_field(name="**Total Members:**", value=members)
    embed.add_field(name="**Bot Events**", value=bot_events)
    embed.add_field(name="**Bot Events/sec:**", value=f"{round((bot_events / real_uptimeInSeconds), 3)}")
    embed.add_field(name="**Debug Mode:**", value="Disabled")
    embed.add_field(name="**Command Logging:**", value="Enabled")
    embed.add_field(name="**Message Logging:**", value="Enabled")
    embed.add_field(name="**Voice Channels:**", value="Enabled")
    embed.add_field(name="**YouTube Player:**", value=YTAPI_Status)
    embed.add_field(name="**Audio Subsystem:**", value=audio_subsystem)
    embed.add_field(name="**Supercell API:**", value=SCAPI_Status)

    embed.set_footer(text=(f"\nDraggieBot.py | {DraggieBot_version}"))
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a", encoding="UTF-8")
    f.write(f"\nSLASH COMMAND RAN -> '.stats' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()

async def handleLeaveVoiceChat(ctx):
    voice_client = ctx.guild.voice_client
    if not voice_client:
        await ctx.send("Nothing to leave.")

#   epic

@client.command(pass_context=True, brief = "[Audio] Plays Text to Speech voice in voice chat.", hidden=True)
async def tts(ctx):
    txt = ctx.message.content
    x = txt.split()

    try:
        locale = (str (x[1]))
        speed = (str (x[2]))
        inputText = txt.split(' ', 3)[-1]
    except IndexError:
        await ctx.send("```.tts <locale> <speed> <inputText>\n^^^^^^^^^^^^^\nlocale, speed, inputText are required arguments which are missing```")
        return

    if any(word in '[]#?/\|£$%^&*=+}{`¬<>' for word in inputText):
        return(await ctx.send(f"Cannot do that, your TTS word contains an incompatible character"))
    else:
        query_string = f"https://www.google.com/speech-api/v1/synthesize?text={inputText}&enc=mpeg&lang={locale}&speed={speed}&client=lr-language-tts&use_google_only_voices=1"
        #await ctx.send(query_string)

        r = requests.get(query_string)
        print(f"Satus {r.status_code}")
        x = uuid.uuid4()
        with open(f'Z:\\{x}.MP3', 'wb') as f:
            f.write(r.content)

        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        
        voice_client.play(discord.FFmpegPCMAudio(source=f'Z:\\{x}.MP3', executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe",))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)

#   play

@client.command(help="Plays audio at specified directory.", brief="[Audio] Plays audio at directory", pass_context=True, hidden=True)
async def sfx(ctx):
    tighe1 = round(time.time() * 1000)
    txt = ctx.message.content
    x = txt.split()

    term = x[1]
    if "french" in term.lower():
        toPlay = f"{base_directory}ExternalAssets\\QuickAudio\\FrenchAccordion"
    elif "end2" in term.lower():
        toPlay = f"{base_directory}ExternalAssets\\QuickAudio\\NightNight2"
    elif "seasonx" in term.lower():
        toPlay = f"{base_directory}ExternalAssets\\QuickAudio\\SeasonX.weba"
    elif "seasonx" in term.lower():
        toPlay = f"{base_directory}ExternalAssets\\QuickAudio\\BrawlidaysOrchestral"
    else:
        await ctx.send(f"No valid sound file found for *{term}*.\n```french, end2, seasonx, brawlidays```")
        return

    try:
        f = open(f"{base_directory}Servers{s_slash}{ctx.guild.id}{s_slash}Preferences{s_slash}Voice_Chat_Volume.txt", "r")
        x = f.read()
        f.close()
        volume = (float(x))
    except FileNotFoundError:
        await setVolume(ctx)

    voice_client = await connectToGuildChannel(ctx)
    voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe", source=(toPlay)))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = volume


    tighe2 = round(time.time() * 1000)

    nTighe = tighe2 - tighe1
    ping = round(client.latency * 1000)
    tot = nTighe + ping

    await ctx.send(f"Executed, delay = **{tot}ms** (**{nTighe}ms** processing + Discord API **{ping}ms**)")

    f = open(GlobalLogDir, "a")
    f.write(f"\nAUDIO COMMAND RAN -> '.sfx' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nAUDIO COMMAND RAN -> '.sfx' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

@client.command(help="Plays audio at specified directory.", brief="[Audio] Plays audio at directory", pass_context=True, hidden=True)
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
            f.write(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
            f.close()
            print(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

        except:
            channel = ctx.author.voice.channel
            await channel.connect()
            await playdir(ctx)

#   play

@client.command(help="Sends what is written to the message log.", brief="Sends what is written to the message log in the channel.", pass_context=True)
async def message(ctx):
    await ctx.send(f"\n'{ctx.message.content}' sent by {ctx.message.author} in [{ctx.message.guild.name} - #{ctx.channel.name}] at {datetime.now()}")

#   Stream YT

@client.command(help="Streams youtube audio into voice channel.", brief="Plays YouTube video", pass_context=True, hidden=True)
async def url(ctx, url: str):
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(URL))
    await ctx.send("Streaming audio")

#   download

@client.command(help="Downloads a youtube video.", brief="Downloads an entire YouTube video", pass_context=True)
async def download(ctx, url: str):
    async with ctx.typing():
        os.chdir("D:\\Draggie Programs\\BaguetteBot\\youtube-dl")
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


@client.command(hidden=True, brief="Backup server emojis", help="Backs up your server emojis. This will be retrievable soon.")
async def emojis(ctx):
    if ctx.message.author.id == 382784106984898560:
        message = (ctx.message.content).split()
        try:
            guild_id = int((message[1]))
            newGuild = client.get_guild(guild_id)
            await ctx.send(f"Getting emojis for {newGuild.id} // {newGuild.name}")
            emoji_list = []
            emojis = 0
            for emoji in newGuild.emojis:
                emojis += 1
                emoji_list.append(f"{emoji.name} - {emoji.url}") 
                x = requests.get(emoji.url)
                emoji_exturl = emoji.url._url
                emoji_exturl = emoji_exturl.split(".")
                extension = (emoji_exturl[1])

                if os.path.exists(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}'):
                    with open(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}{emoji.name}.{extension}', 'wb') as f:
                        f.write(x.content)
                        print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
                else:
                    os.mkdir(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}')
                    print(f"Made emoji directory for {newGuild.id} // {newGuild.name}")
                    with open(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}{emoji.name}.{extension}', 'wb') as f:
                        f.write(x.content)
                        print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
            try:
                await ctx.send(emoji_list)
            except Exception as e:
                await ctx.send(f"Probably too many emojis. `{e}`")
            await ctx.send("Done!")

        except Exception:
            await ctx.send("Running on all guilds")
            emojis = 0
            guilds = 0
            for guild in client.guilds:
                guilds += 1
                newGuild = client.get_guild(guild.id)
                await ctx.send(f"Getting emojis for {newGuild.id} // {newGuild.name}")
                emoji_list = []
                for emoji in newGuild.emojis:
                    emojis += 1
                    emoji_list.append(f"{emoji.name} - {emoji.url}") 
                    x = requests.get(emoji.url)
                    emoji_exturl = emoji.url._url
                    emoji_exturl = emoji_exturl.split(".")
                    extension = (emoji_exturl[1])

                    if os.path.exists(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}'):
                        with open(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}{emoji.name}.{extension}', 'wb') as f:
                            f.write(x.content)
                            print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
                    else:
                        os.mkdir(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}')
                        print(f"Made emoji directory for {newGuild.id} // {newGuild.name}")
                        with open(f'{base_directory}Servers{s_slash}{newGuild.id}{s_slash}Emojis{s_slash}{emoji.name}.{extension}', 'wb') as f:
                            f.write(x.content)
                            print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
                try:
                    if str(emoji_list) == "[]":
                        print(f"No emojis in guild {newGuild.id}")
                    else:
                        await ctx.send(emoji_list)
                except Exception as e:
                    await ctx.send(f"Probably too many emojis. `{e}`")
            await ctx.send(f"Done! Archived {emojis} from {guilds} guilds.")
    
#   Invite link

@client.command(hidden=True)
async def create_invite(ctx):
    if ctx.message.author.id == 382784106984898560:
        txt = ctx.message.content
        x = txt.split()
        channel = int(x[1])
        channel = client.get_channel(channel)
        link = await channel.create_invite(max_age = 69)
        await ctx.send(f"Channel invite link: {link}")
    else:
        await draggie.send("Error 5: `command reserved for bot developer(s)`")

@client.command(hidden=True)
async def addroles(ctx):
    if ctx.message.author.id == 382784106984898560 or ctx.message.author.id == 606583679396872239 or ctx.message.author.id == 854323313631559680:
        await ctx.message.delete()
        member = ctx.message.author
        for r in ctx.guild.roles:
            try:
                await ctx.author.add_roles(r)
                await member.send(f"Good: **`{r.name}` given** to {member}")
            except Exception as e:
                await member.send(f"Error: **`{r.name}` couldn't be given** to {member}: {e}")
        await member.send(f"Successfully gave {member} all the roles I could!")

@client.command(help="Edit your BaguetteBot preferences here. Change DMs, role notifications, Coins earning and more.", brief="Edit your BaguetteBot preferences.")
async def preferences(ctx):
    await ctx.send("You have no special preferences loaded. <@382784106984898560> please code this")

@client.command(hidden = True)
async def adaptor(ctx):
    if ctx.message.author.id == 382784106984898560:
        txt = ctx.message.content
        x = txt.split()
        server = int(x[1])
        sp1 = txt.split(' ', 2)[-1]
        guild = await client.fetch_guild(server)
        await guild.edit(name=sp1, reason=f"Command ran at {datetime.now()} - the command given was {ctx.message.content}.")
    else:
        await ctx.send("Error 5: `command reserved for bot developer(s)`")

#   YouTube search, download, convert, play.

@client.command(help="Downloads a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Searches for and plays YouTube video", pass_context=True, hidden=True)
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
            os.chdir("D:\\Draggie Programs\\BaguetteBot\\AudioCache")
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
                await ctx.send(f"\n\nResults = {results}")
            for v in results:
                id = v['id']
                result = ('https://www.youtube.com/watch?v=' + v['id'])

                my_file = Path("D:\\Draggie Programs\\BaguetteBot\\AudioCache\\{id}")
                if my_file.is_file():
                    global hasVideo
                    hasVideo = "True"
                    print("hasvideo set to true")
                else:
                    hasVideo = "False"
                if debugMode == True:
                    await ctx.send(f"\n\nResult = {result}")

                ydl_opts = {}

                global video_title

                video_title = id

                video = result

                if quickMode != True:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(video, download=False)
                        video_title = info_dict.get('title', None)

                print(f"\n\nResult = {result}")
                await ctx.send(f"Processing: `{video_title}`.")
                url = result
                text = ctx.message.content
            
            #print(id)
            if hasVideo == "True":
                print("hasvideo = true")
                my_file = Path(f"D:\\Draggie Programs\\BaguetteBot\\AudioCache\\{id}")
                voice.play(discord.FFmpegPCMAudio(my_file))
                doneMillisecs = round(time.time() * 1000)
                nTighem = doneMillisecs - millisecs
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.3
                print("cached")
                if debugMode == True:
                    await ctx.send(f"Playing: **{video_title}** (avec `time taken: {nTighem}ms`)\n\nattrs:\nplayingFromCache")
                else:
                    await ctx.send(f"Playing: **{video_title}** (avec `time taken: {nTighem}ms`). `c=t`,`d=f`)") #    c=t means cache = true. s=f means downloaded = false
            else:
                print("uncached else")
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
                    await ctx.send(f"Filename = {filename}")

                for file in os.listdir("./"):
                    if file.endswith(".part"):
                        name = file
                        print(f"File: {file}\n")
                        try:
                            os.remove(file)
                            print(f"Removed file {file}")
                            if debugMode == True:
                                await ctx.send(f"Successfully removed {name}")
                        except:
                            print(f"Failed to remove file {file}")
                            if debugMode == True:
                                await ctx.send(f"Failed to remove {name}")

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
                    await ctx.send(f"value nTighem = {nTighem}")

                name = filename
                nName = name.rsplit("-", 1)
                vName = nName[0]

                if debugMode == True:
                    await ctx.send(f"value nName = {nName}")
                if debugMode == True:
                    await ctx.send(f"value vName = {vName}")

                await ctx.send(f"Playing: **{video_title}** (avec `time taken: {nTighem}ms`). `c=f`,`d=t`)")
                print(f"Playing: **{video_title}** (avec `time taken: {nTighem}ms`). `c=f`,`d=t`)")
        except Exception as e:
            try:
                try:
                    channel = ctx.author.voice.channel
                    await channel.connect()
                    await yt(ctx, url)
                except:
                    await ctx.send(f"An unhandlable error occured! Error message: `{e}`. Please report this in github/baguettebot/issues or DM Draggie#3060 with your server ID.")
            except:
                await ctx.send("An error occured.")
    
#   Grave key: `
#   Bullet point: • 

#   ytstream

@client.command(help="Streams a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Streams YT audio. Sligthly buggy, may die randomly.", pass_context=True, hidden=True)
async def yts(ctx):
    async with ctx.typing():
        text = ctx.message.content
        searchTerm = text.split(' ', 1)[-1]
        millisecs = round(time.time() * 1000)
        results = YoutubeSearch(searchTerm, max_results=1).to_dict()
        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print(f"\nresult = {result}")
            url = result
            text = ctx.message.content

            print("Got YTDL_OPTIONS")
            with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                print(f"\n\n{URL}\n\n")
            print("Extracted info")

            voice_client = await connectToGuildChannel(ctx)
            volume = await getServerVoiceVolume(ctx)

            print("Called volume and voiceclient")

            source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
            voice_client.play(source)    
            voice_client.is_playing()
            #voice_client.play(discord.FFmpegPCMAudio(URL, options=FFMPEG_OPTIONS, executable="D:\\Downloads\\FFMPEG\\bin\\ffmpeg.exe"))
            #voice_client.source = discord.PCMVolumeTransformer(voice_client.source, volume=volume)

            
            doneMillisecs = round(time.time() * 1000)
            timeDelay = doneMillisecs - millisecs
            video_title = info.get('title')
            
            duration = round((info.get('duration'))/60, 2)

            embed=discord.Embed(title="Playing audio", description=f"**[{video_title}]({info.get('webpage_url')})**", colour=0x228B22)
            embed.add_field(name="Channel", value=f"[{info.get('channel')}]({info.get('channel_url')})")
            embed.add_field(name="Duration", value=f"{duration}  minutes")
            embed.add_field(name="Views", value=f"{info.get('view_count')}")
            embed.add_field(name="Likes", value=f"{info.get('like_count')}")
            embed.add_field(name="Time taken", value=f"{timeDelay}ms")
            embed.add_field(name="Audio bitrate", value=f"{info.get('abr')} kbps")
            embed.set_thumbnail(url=(info.get('thumbnail')))
            await ctx.send(embed=embed)
            print("Send embed")

            
#   Get links

@client.command(help="Gets YouTube video raw links.", brief="Gets YouTube video's and raw audio URL", pass_context=True, hidden=True)
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
                print(f"\n\nurl = {URL}")
                embed = discord.Embed()
                embed.description = (f"[audio url]({URL})")
                await ctx.send(embed=embed)


@client.command(hidden=True)
async def create_voice_chat(ctx):
    text = ctx.message.content
    x = text.split()
    category_id = int(x[1])
    chat_name = text.split(' ', 2)[-1]
    category = discord.utils.get(ctx.guild.categories, id=category_id)
    await ctx.guild.create_voice_channel(name=chat_name, category=category, bitrate=ctx.guild.bitrate_limit, reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")
    await ctx.reply(f"Ok! I created the voice chat **{chat_name}** in category **{category.name}**. The bitrate was set to the server's max, at {round(ctx.guild.bitrate_limit/1000)}kbps.")

@client.command(hidden=True)
async def max_bitrate(ctx):
    x = ""
    try:
        text = (ctx.message.content).split()
        specific_bitrate = int(text[1])
    except Exception:
        pass

    for channel in ctx.guild.voice_channels:
        try:
            if 'specific_bitrate' not in locals():
                if channel.bitrate is not ctx.guild.bitrate_limit:
                    await channel.edit(bitrate=ctx.guild.bitrate_limit, reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")
                    x = f"Set the bitrate of **<#{channel.id}>** to **{round(ctx.guild.bitrate_limit/1000)}** kbps.\n{x}"
                else:
                    x = f"Bitrate of **<#{channel.id}>** is at the maximum bitrate.\n{x}"
            else:
                try:
                    await channel.edit(bitrate=specific_bitrate, reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")
                    x = f"Set the bitrate of **<#{channel.id}>** to **{specific_bitrate/1000}** kbps.\n{x}"
                except:
                    x = f"Error changing the bitrate of **<#{channel.id}>** to **{specific_bitrate}** bps.  (The server limit is between 8000 and {ctx.guild.bitrate_limit}, maybe that's why?)\n{x}"

        except Exception:
            await ctx.send(f"Could not edit the information of <#{channel.id}>. Maybe the bot doesn't have good permissions?")
    await ctx.reply(x)
    if x == "":
        await ctx.send("Nothing happened.")

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
#    f.write(f"\nAUDIO COMMAND RAN -> '.stop' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
#    f.close()
#    print(f"\nAUDIO COMMAND RAN -> '.stop' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
#    return

#   join/leave voice

@client.command(help="Joins message author's voice channel", brief="[Audio] Joins voice chat", pass_context=True, hidden=True)
async def join(ctx):#    Joins
    await ctx.reply("• You need to be in a Voice Chat to play audio.\n• You don't need to make me join - search for any audio and I'll play it automatically.") if not ctx.author.voice else await ctx.reply("You don't need to make me join: search for any audio and I'll play it automatically.")
    
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

@client.command(help="Purges a specified amount of messages", brief="Delets x messages", pass_context=True)
#@commands.has_any_role('Admin', 'Mod', 'King')
async def purge(ctx):
    if ctx.message.author.id == 382784106984898560:
        async with ctx.typing():
            txt = ctx.message.content
            x = txt.split()
            print(x[1])
            y = (int (x[1])) + 1
            current_time_for_deletes = time.time()
            async for message in ctx.message.channel.history(limit=y):
                if len(message.attachments) < 1: # Checks if there is an attachment on the message
                    with open((f"Z:\\{message.channel.id}_log{current_time_for_deletes}.txt"), "a", encoding='utf-8') as logAllMessages:
                        logAllMessages.write(f"\n'{message.content}' sent by {message.author} at {(message.created_at)}", encoding="UTF-8")
                        print(f"\n'{message.content}' sent by {message.author}")
                        logAllMessages.close()
                else: # If there is it gets the filename from message.attachments
                    attachmentsDir = (f"Z:\\{message.channel.id}\\Attachments\\")
                    if not os.path.exists(attachmentsDir):
                        os.makedirs(f"Z:\\{message.channel.id}\\Attachments\\")
                        print("Made directory" + (attachmentsDir))
                    nameOfFile = str(message.attachments).split("filename='")[1]
                    filename = str(nameOfFile).split("' ")[0]
                    beans = (f"{attachmentsDir}{filename}")
                    if os.path.isfile(beans):
                        filename = str(nameOfFile).split("' ")[0]
                        beans = (f"{attachmentsDir}{uuid.uuid4()}-name={filename}")
                        await message.attachments[0].save(fp=beans)
            if (x[1]) == 1:
                await ctx.channel.purge(limit = y)
                await ctx.send(f"Deleted {x[1]} message!")
            else:
                await ctx.channel.purge(limit = y)
                await ctx.send(f"Deleted {x[1]} messages!")
                f = open(GlobalLogDir, "a")

            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.purge' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
            f.close()
            print(f"\nCOMMAND RAN -> '.purge' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
            return  
    else:
        await ctx.send("You don't have permissions for that u sussy boi")

#   i g n o r e

@client.command(help="UwU", brief="UwU", pass_context=True, hidden=True)
@commands.has_any_role('Admin', 'Mod')
async def uwu(ctx):
    uwuwu = random.randint(1,2)
    if uwuwu == 1:
        await ctx.send(file=discord.File(f"{base_directory}Assets\\Commands\\I_regret_making_this.png", filename="UwU.png"))
    if uwuwu == 2:
        await ctx.send(file=discord.File(f"{base_directory}Assets\\Commands\\canvas_1.png", filename="canvas_1.png"))
    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.uwu' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.uwu' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

#   change nickname

@client.command(help = "Changes nickname", brief = "Changes nickname for mentioned user", pass_context=True, hidden=True)
@commands.has_any_role('Admin', 'Mod')
async def chnick(ctx):
    text = ctx.message.content
    member = ctx.message.author
    sp1 = text.split(' ', 1)[-1]
    await member.edit(nick=sp1, reason=f"Command ran by {ctx.message.author.name} at {datetime.now()} - the command was {ctx.message.content}.")

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.chnick' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.chnick' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

#   brawl stars API

@client.command(help = "Use: .bs <PLAYER TAG>", brief = "Interacts with the Brawl Stars API. Type '.help bs' for usage", pass_context=True, hidden=True)
async def bs(ctx):
    async with ctx.typing():
        txt = ctx.message.content
        x = txt.split()
        print(x[1])
        playerTag = (x[1])
        playerTag = playerTag.upper()

        print(f'playerTag = {playerTag}')

        if (x[2]) == 'brawlers':
            url = (f'https://api.brawlstars.com/v1/players/%23{playerTag}')
            print(f'url = {url}')
            with open(f"{base_directory}supercell_api_key.txt", encoding="utf-8") as f:
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

            path = (f"Z:\\#{playerTag}.json")
            if os.path.isfile(path):
                f = open(path, "w+")
                f.close()
            f = open(path, "w")
            f.write((str (brawlerRequest.json())))
            f.close()

            try:
                await ctx.send(f'Recieved this response from Supercell Servers:\n\n{brawlerRequest.json()}')
            except:
                await ctx.send(file=discord.File(path))

        if (x[2]) == 'battles':
            url = (f'https://api.brawlstars.com/v1/players/%23{playerTag}/battlelog')

            with open(f"{base_directory}supercell_api_key.txt", encoding="utf-8") as f:
                api_key = f.read()
            headers = {
            'Accept': 'application/json',
            'authorization': api_key,
            }
            brawlerRequest = requests.get(url, headers=headers)
            brawlerRequestStr = (str (brawlerRequest))
            brawlerRequestStatusCode = brawlerRequest.status_code
            print(brawlerRequestStr)
            path = (f"Z:\\#{playerTag}.json")

            if os.path.isfile(path):
                f = open(path, "w+")
                f.close()
        
            f = open(path, "w", encoding="UTF-8")
            f.write((str (brawlerRequest.json())))
            f.close()
            try:
                await ctx.send(f'Recieved this response from Supercell Servers:\n\n{brawlerRequest.json()}')
            except:
                await ctx.send(file=discord.File(path))

#   Birthdays

@client.command(help = "Writes your birthday to a file. Use .birthday set [date] to set birthday, and .birthday file to get a list of birthdays.", brief = "Sets your birthday, syntax '.birthday set [your birth date]", pass_context=True, hidden=True)
async def birthday(ctx):
    async with ctx.typing():
        try:
            text = ctx.message.content
            syntaxErrorChecker = text.split(' ', 1)[-1]
            birthDate = text.split(' ', 2)[-1]
            x = text.split()
            if x[1] == "file":
                with open(f"{base_directory}logs{s_slash}birthdays.txt") as file:
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
                with open(f"{base_directory}logs{s_slash}birthdays.txt") as file:
                    birthdays = file.read()
                    embed=discord.Embed(title="All Birthdays", description=(birthdays), colour=0x00acff)
                    await ctx.send(embed=embed)
            if (x[1]) == "0":
                await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")

            if x[1] == "set":
                author = (str (ctx.message.author.id))
                file=open(f"{base_directory}Logs{s_slash}birthdays.txt",encoding="UTF-8").read()
                count=file.count(author)
                print (count)
                if count != 0:
                    await ctx.send("Error! You have already added your birthday to the file. Please ask an admin to remove it if you believe this is an error.")    
                    return

                f = open(f"{base_directory}logs{s_slash}birthdays.txt", "a")
                f.write(f"\n<@!{ctx.message.author.id}>'s birthday is on the {birthDate}")
                f.close()
                await ctx.send(f"\n{ctx.message.author}'s birthday has been set to `{birthDate}`. A custom message will be sent, enjoy!")
        
        except Exception:
            await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")

#   Dir

@client.command(help = "Specify the directory to display all items in it.", brief = "Shows all files in my PC...",pass_context=True, hidden=True)
@commands.has_any_role('Admin', 'Mod', 'Prince')
async def dir(ctx):
    if ctx.guild.id == 759861456300015657:
        text = ctx.message.content
        sp1 = text.split(' ', 1)[-1]
        arr = os.listdir((str (sp1)))
        embed=discord.Embed(title=f"Directory lookup: {sp1}", description=f"{arr}\n\nInit by {ctx.author.mention}", colour=0xFF5800)
        await ctx.send(embed=embed)
        f = open(GlobalLogDir, "a")
        f.write(f"\nCOMMAND RAN -> '.dir' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
        f.close()
        print(f"\nCOMMAND RAN -> '.dir' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

#   Drop

@client.command(help = "drop", brief = "Gets random Fortnite location.", pass_context=True, hidden=True)
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
    f.write(f"\nCOMMAND RAN -> '.drop' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.drop' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

#   Roleperms command

@client.command(help="Gets all roles with that permission.", brief="Gets all roles with that permission", pass_context=True)
async def roleperms(ctx):
    x = ctx.message.content.split()
    permLookup = (str (x[1]).lower())
    rolesWithPerm = []
    roles = [r for r in ctx.guild.roles if any(p[1] and p[0] == f"{permLookup}" for p in r.permissions)]
    for name in roles:
        rolesWithPerm.append(name.mention)
    
    rolesWithPerm = list(reversed(rolesWithPerm))
    total = len(rolesWithPerm)
    roleNum = len(ctx.guild.roles)
    rolesWithPerm = (str(rolesWithPerm)).replace("'", "")
    if rolesWithPerm == '[]':
        await ctx.send(f"No roles have that permission. Check out permissions here to find a valid permission: https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags")
    else:
        embed=discord.Embed(title=f"All roles with permission '{permLookup}'", description=(f"{rolesWithPerm}"), colour=0x00acff)
        embed.set_footer(text=f"Total: {total} of {roleNum}\nThis only shows permissions which have been specifically enabled for that role\nMentioning users or roles in an embed like this does not send a ping to anyone.")
        await ctx.send(embed=embed)

#   Ship

@client.command(help="Ships things. Syntax: *.ship [person1] [person2]", brief="Ships x and y out of 100.", pass_context=True, hidden=True)
async def ship(ctx):
    txt = ctx.message.content
    x = txt.split()
    y = (str (x[1]))
    z = (str (x[2]))
    #   CALC RAND
    calculation = random.randint(1,100)

    embed=discord.Embed(title="Shipping...", description=(f"{ctx.author.mention} ships **{y} x {z}**!\n\nResult: **{calculation}** out of 100!"), colour=0x00acff)
    await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a")
    f.write(f"COMMAND RAN -> '.ship' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"COMMAND RAN -> '.ship' ran by {ctx.message.author} in {ctx.guild.id} at {datetime.now()}")

#   broadcast

@client.command(pass_context=True, hidden=True)
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

#   Nolwennium mine

@client.command(help=f"Mines a random amount of {name_Nolwennium}.", brief=f"Mines {name_Nolwennium}.", pass_context=True)
@commands.cooldown(1, 29, commands.BucketType.user)
async def mine(ctx):
    print(f"CURRENCY - {name_Nolwennium} > {ctx.author} is mining")
    global balance
    global myuuid
    global address

    newNumber = random.randint(-5, 99)
    
    await changeNolwenniumBalance(ctx, newNumber)

#   YouTube audio EPIC VERSION

#    removed

#   ON ERROR

@client.event
async def on_slash_command_error(ctx, error):
    await bot_runtime_events(1)
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
    embed=discord.Embed(title=(f"{cry} An error occured"), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    await bot_runtime_events(1)
    if "is not found" in str(error):
        print(f"Command returned an error but will be returned. Server: {ctx.guild.name}, error message = {error}")
        return
    if "on cooldown" in str(error):
        await ctx.send(f"{error}.")
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
    embed=discord.Embed(title=(f"{cry} An error occured"), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)
    print (str(error))
    f = open(GlobalLogDir, "a")
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.message.author} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()
    f = open(f"{base_directory}errors.txt", "a")#	Modified in repl.it
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.message.author} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()

if running_locally:
    dotenvPath = 'D:\\Draggie Programs\\BaguetteBot\\draggiebot\\.env'
    load_dotenv(dotenv_path=dotenvPath)
    client.run(os.getenv('TOKEN'))
else:
    client.run(os.getenv('TOKEN'))

#   poggerspogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpog