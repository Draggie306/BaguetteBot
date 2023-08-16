DRAGGIEBOT_VERSION = "v1.3.9"
BUILD = "a" # use / in commit message
BETA_BOT = False

"""
Naming scheme:
DRAGGIEBOT_VERSION: current version with features: <alpha/release>.<major>.<minor>
BUILD: hotfixes descending alphabetically. Always 'dev' if in branch 'dev', followed by '/<comitted_revision>'
BETA_BOT: True if bot is in beta mode else False
"""

print("Importing all modules...\n")
import      discord, os, time, random, sys, requests, json, psutil, logging, openai, subprocess, wavelink, traceback, asyncio, uuid, math
import      yt_dlp as youtube_dl
from        dotenv import load_dotenv
from        discord.ext import commands#                                        CMD Prerequisite:   py -3 -m pip install -U discord.py
from        datetime import datetime#                                           CMD Prerequisite:   py -3 -m pip install -U python-dotenv
from        pathlib import Path#                                                UPDATE PIP:         python -m pip install --upgrade pip
from        discord import app_commands#                                        PIP:                python -m ensurepip
from        typing import Optional
from        wavelink.ext import spotify
import      matplotlib.pyplot as plt

print("Defining main variables...")
global VOICE_VOLUME, upvote, downvote, CROISSANTS, draggie, hasMembersforGlobalServer, nolwenniumUserDir, rolePrivate, hasPrivate, hasAdmin, bot_events
bot_events = 0
VOICE_VOLUME = 65
CROISSANTS = [796777705520758795, 821405856285196350, 588081261537394730]
CROISSANT_NAMES = ["ETigger_4", "Josephy Spaghetti", "tigger_4"]
TESTER_GUILD_IDS = [384403250172133387, 759861456300015657, 833773314756968489, 921088076011425892] # Server IDs where I'm an admin so can change stuff before it reaches other servers
BRIGADERS = 759861456300015657
RANDOM_WORD = ["Expulser!", "Troubador!", "Delenda!", "Vincit!", "Consilium!", "Renovatur!", "Acheronta!", "Oderint!"]
EMOJI_COINS = "<:Coins:852664685270663194>"
EMOJI_NOLWENNIUM = "<:NolwenniumCoin:846464419503931443>"
EMOJI_RANDOM_LMAO = ["😂", "<a:RotatingSkull:966452197787332698>", "💀", "😳"]
EMOJI_LOADING = "<a:loading:935623554215591936>"
EMOJI_TICK_ANIMATED = "<a:AnimatedTick:956621591108804652>"
EMOJI_CROSS_ANIMATED = "<a:AnimatedCross:956621593113665536>"
EMOJI_UPVOTE = "<:upvote:803578918488768552>"
EMOJI_DOWNVOTE = "<:downvote:803578918464258068>"
VALUE_PLACEHOLDER = "TBD/tbd"
NAME_NOLWENNIUM = "Nolwennium"
ID_DRAGGIE = 382784106984898560
DISCORD_EPOCH = 1420070400000
YTAPI_STATUS = "Enabled: yt-dl"
SCAPI_STATUS = "Disabled"
AUDIO_SUBSYSTEM = "Wavelink"
IDK_WHAT_U_MEAN = ("I don't know what you mean. Please use **buy/set/lookup** in the `operation` Choice. Make sure the `target_user` Choice is a valid user ID. The `mod_value` Choice does not need to have any conditional arguments if `operation` is `lookup`.")
YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': 'True', 'youtube-skip-dash-manifest': 'True'}
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
youtube_dl.utils.bug_reports_message = lambda: ''

sys.setrecursionlimit(99999999)

PYTHONIOENCODING = "utf-8"


class Roles:
    ROLES_LIST = ["Citizen", "Knight", "Baron", "Viscount", "Earl", "Marquess", "Duke", "Prince", "King", "Admin"]
    ROLES_LIST_ID = [795738020967743491, 796360098108538901, 943259355619418163, 943259337185435699, 943259319821021194, 943259291484295218, 943259217123496028, 796362374827343923, 796362553541656576, 943974413810933802]
    ROLES_COSTS = [0, 25, 50, 100, 250, 500, 1000, 2500, 10000, 1000000]

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


global start_time
start_time = time.time()

print("Checking directories...")

#   Check directories
NOLWENNIUM_CHECK_DIR = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Nolwennium\\.rootnolwenniumdirectory"
NOLWENNIUM_DIR_CHECKER = Path(NOLWENNIUM_CHECK_DIR)
if NOLWENNIUM_DIR_CHECKER.is_file():
    running_locally = True
    print("Running locally! Using enhanced features.")
    MINIFIED_BASE_DIR = "D:\\Draggie Programs\\BaguetteBot\\"
    BASE_DIR = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\"
    BASE_DIR_MINUS_SLASH = "D:\\Draggie Programs\\BaguetteBot\\draggiebot"
    S_SLASH = "\\"
    JSON_DIR = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\JSONs\\"
    if BETA_BOT:
        print("Beta Bot mode is on! This should only print in development situations. Switching directories...")
        MINIFIED_BASE_DIR = "D:\\Draggie Programs\\BetaBaguetteBot\\"
        BASE_DIR = "D:\\Draggie Programs\\BetaBaguetteBot\\draggiebot\\"
        BASE_DIR_MINUS_SLASH = "D:\\Draggie Programs\\BetaBaguetteBot\\draggiebot"
        S_SLASH = "\\"
        JSON_DIR = "D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\JSONs\\"
    TEMP_FOLDER = f"Z:{S_SLASH}"
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'{MINIFIED_BASE_DIR}Logs\\{DRAGGIEBOT_VERSION}{BUILD}-{time.time()}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    GlobalLogDir = (f"{BASE_DIR}GlobalLog.txt")
else:
    running_locally = False
    print(f"Not running locally, coins and {NAME_NOLWENNIUM} values may not be up to date and some features may be disabled")
    BASE_DIR = "/"
    BASE_DIR_MINUS_SLASH = ""
    S_SLASH = "/"
    JSON_DIR = "JSONs/"
    TEMP_FOLDER = f"Temp{S_SLASH}"
    MINIFIED_BASE_DIR = "D:\\Draggie Programs\\BaguetteBot\\.useful"
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'.useful{S_SLASH}{DRAGGIEBOT_VERSION}{BUILD}-{time.time()}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    GlobalLogDir = ("GlobalLog.txt")
    import keep_alive       # This is only in BaguetteBot's Replit page to run 24/7.
    keep_alive.keep_alive()


with open(f"{BASE_DIR_MINUS_SLASH}\\spotify_api_key.txt", 'r') as spapi:
    spotify_id = spapi.read()
with open(f"{BASE_DIR_MINUS_SLASH}\\spotify_client_id.txt", 'r') as spcid:
    spotify_client_id = spcid.read()

if running_locally:
    if BETA_BOT:
        subprocess.Popen(['java', '-jar', f'{BASE_DIR}GitHub\\BaguetteBot\\Lavalink-3.7.8.jar'])
    else:
        #subprocess.Popen(['java', '-jar', f'{BASE_DIR}GitHub\\BaguetteBot\\LavalinkOSHIv6-languagefix.jar'])
        subprocess.Popen(['java', '-jar', f'{BASE_DIR}GitHub\\BaguetteBot\\Lavalink-3.7.8.jar'])

process = subprocess.Popen(['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE)
git_head_hash = process.communicate()[0].strip()
print(git_head_hash)

print("Creating bot instance...")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

client = discord.Client(intents=intents)
client = commands.Bot(
    command_prefix=commands.when_mentioned_or('.'),
    case_insensitive=True,
    intents=intents,
    description=f"BaguetteBot - version {DRAGGIEBOT_VERSION}{BUILD} - d.py {discord.__version__}",
    help_command=commands.DefaultHelpCommand(no_category='Below is a list of legacy .<commands> - please use the new Slash Commands menu to see a description of all my commands!')
)


###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

print("Done! Slash commands initialising...")


@client.tree.command(name="help", description="Everything you need to know about BaguetteBot")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="BaguetteBot Help", description="Everything you need to know about BaguetteBot", color=0x00acff)
    embed.add_field(name="Commands", value="Preview my commands by typing in `/` and clicking the BaguetteBot icon", inline=False)
    embed.add_field(name="Support", value="Join the support server [here](https://discord.gg/GfetCXH)", inline=False)
    embed.add_field(name="Invite", value="Invite BaguetteBot to your server [here](https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands). Feel free to select the permissions you want BaguetteBot to have.", inline=False)
    embed.add_field(name="Source Code", value="BaguetteBot is open source! You can find the source code [here](https://github.com/Draggie306/BaguetteBot/blob/main/BaguetteBot.py)", inline=False)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Commands List", url="https://github.com/Draggie306/BaguetteBot/blob/main/README.md", style=discord.ButtonStyle.link))
    view.add_item(discord.ui.Button(label="Support", url="https://discord.gg/GfetCXH", style=discord.ButtonStyle.link))
    view.add_item(discord.ui.Button(label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands", style=discord.ButtonStyle.link))
    view.add_item(discord.ui.Button(label="Source Code", url="https://github.com/Draggie306/BaguetteBot/blob/main/BaguetteBot.py", style=discord.ButtonStyle.link))
    await interaction.response.send_message(embed=embed, view=view)


async def report(interaction: discord.Interaction, message: discord.Message):
    report_channel = client.get_channel(957409071655419914)
    embed = discord.Embed(title="Message Reported", description=f"Reported by {interaction.user.mention} in {interaction.channel.mention}:\n```{message.content}```({message.jump_url})", color=0x00ff00)
    await report_channel.send(embed=embed)
    await interaction.response.send_message("Message reported successfully.")

report_context_menu = app_commands.ContextMenu(
    name='Report Message',
    callback=report,
)
client.tree.add_command(report_context_menu)


async def warn(interaction: discord.Interaction, member: discord.Member):
    if interaction.user.guild_permissions.kick_members:
        # log the warn given to JSON database:
        # it has "_count" and "reasons", "time" as keys.
        reason = f"Warned from context menu at: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        user_dir = f"database/warns/{member.id}.json"
        if os.path.exists(user_dir):
            with open(user_dir) as f:
                data = json.load(f)
        else:
            data = {"_count": 0, "reasons": [], "time": []}
        data["_count"] += 1
        data["reasons"].append(reason)
        data["time"].append(str(time.time()))
        with open(user_dir, "w+") as f:
            json.dump(data, f, indent=4)
        # send the warn to the user.
        await member.send(f"You have been warned in {interaction.guild.name} for the following reason:\n```{reason}```")
        await interaction.response.send_message(f"User warned successfully for the following reason:\n```{reason}```")
    else:
        await interaction.response.send_message("You do not have permission to warn users.")

warn_ctx_menu = app_commands.ContextMenu(
    name='Quick Warn User',
    callback=warn,
)
client.tree.add_command(warn_ctx_menu)


@client.tree.command(name="devtest", description="Developer testing commands.")
async def devtest(interaction: discord.Interaction):
    # Read data from JSON file
    try:
        with open('Z:\\testfile.txt') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return await interaction.response.send_message("No developer test file found, cannot load data.", ephemeral=True)
    # Extract the data for each category
    dates = [d['date'] for d in data]
    messages_sent = [d['messages_sent'] for d in data]
    messages_received = [d['messages_received'] for d in data]
    time_spent_voice = [d['time_spent_voice'] for d in data]

    # Create the bar chart
    fig, ax = plt.subplots()
    bar_width = 0.2
    bar_x = range(len(data))

    ax.bar(bar_x, messages_sent, bar_width, label='Messages Sent')
    ax.bar([x + bar_width for x in bar_x], messages_received, bar_width, label='Messages Received')
    ax.bar([x + 2 * bar_width for x in bar_x], time_spent_voice, bar_width, label='Time Spent in Voice Chat')

    # Add labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Discord Chat Stats')
    ax.set_xticks([x + bar_width for x in bar_x], dates)
    ax.legend()

    # Show plot
    plt.savefig("Z:\\discord_chart.png")
    # plt.show()
    await interaction.response.send_message(file=discord.File("Z:\\discord_chart.png"))


@client.tree.command(name="command-2")
@app_commands.guilds(discord.Object(id=384403250172133387))
async def my_private_command(interaction: discord.Interaction) -> None:
    """ /command-2 """
    await interaction.response.send_message("Hello from private command!", ephemeral=True)


@client.tree.command()
async def my_command(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello from my command!")


@client.tree.command(name="sync-commands", description="[Admin] Sync edited client tree commands to Discord servers")
async def sync(interaction: discord.Interaction) -> None:
    await slash_log(interaction)
    if interaction.user.id == 382784106984898560:
        await interaction.response.defer() # Defer due to rate limiting being annoying sometimes grr
        x = await client.tree.sync()
        print(x)
        await interaction.followup.send(f"Synced client tree commands. {x}") # Must use interaction.followup.send after a defer
    else:
        await interaction.response.send_message("This is bot admin only.")


@client.tree.command(name="stats", description="[Info] Just a few useful bot statistics.")
async def stats(interaction: discord.Interaction) -> None:
    await slash_log(interaction)
    await bot_runtime_events(1)
    if round(client.latency * 1000) <= 100:
        pingColour = (0x44ff44)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xffd000)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xff6600)
    else:
        pingColour = (0x990000)

    fileSizeBytes = os.path.getsize(f'{BASE_DIR}GitHub{S_SLASH}BaguetteBot{S_SLASH}BaguetteBot.py')

    num_lines = sum(1 for line in open(f"{BASE_DIR}GitHub{S_SLASH}BaguetteBot{S_SLASH}BaguetteBot.py", encoding='utf-8'))
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
        if guild.member_count:
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
    embed.add_field(name="**YouTube Player:**", value=YTAPI_STATUS)
    embed.add_field(name="**Audio Subsystem:**", value=AUDIO_SUBSYSTEM)
    embed.add_field(name="**Supercell API:**", value=SCAPI_STATUS)

    embed.set_footer(text=(f"\nBaguetteBot.py | {DRAGGIEBOT_VERSION}/{BUILD} | discord.py {discord.__version__} | made by draggie"))
    await interaction.response.send_message(embed=embed)

    with open(GlobalLogDir, "a", encoding="UTF-8") as f:
        f.write(f"\nSLASH COMMAND RAN -> '.stats' ran by {interaction.user.id} in {interaction.guild_id} at {datetime.now()}")


@client.tree.command(name="invite", description="[Info] Get the invite link for the bot.")
async def invite(interaction: discord.Interaction) -> None:
    await slash_log(interaction)
    invite_link = "https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands"
    await interaction.response.send_message(f"You can invite me to your server with this link: {invite_link}. Enjoy all the features of BaguetteBot!\n\nIf you need help, join the support server: https://discord.gg/GfetCXH")


# namecolour for nitro boosters
# Now in BaguetteBrigadersHelper.py

#   baguettes


@client.tree.command(name="baguette", description="[Social] Sends a random baguette image.")
async def baguette(interaction: discord.Interaction) -> None:
    await slash_log(interaction)
    return await interaction.response.send_message("Use French Cuisine bot for this and much more! The commad is `/baguette`.\nAdd it! https://ibaguette.com/api/BotInvs/FrenchCuisine&permissions=V2")


@client.tree.command(name="snowflake", description="[Utility] Convert a Discord snowflake into a DateTime object, accurate to the second.")
@app_commands.describe(flake="Input the snowflake here, something like '382784106984898560'.")
async def snowflake(interaction: discord.Interaction, flake: str) -> None:
    await slash_log(interaction)
    snowflake = int(flake)
    try: #      Try and change the message content after the '.snowflake' into an integer.
        unix_timestamp = ((1420070400000 + int(((f"{(snowflake):b}")[:-22]), 2)) / 1000)
        stringe = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y,%m,%d,%H,%M,%S')
        stringe = stringe.split(",")
        string_to_send = (f"Exact: <t:{round(unix_timestamp)}>:{stringe[5]}. Relative: <t:{round(unix_timestamp)}:R>.")
        await interaction.response.send_message(string_to_send)
        print(string_to_send)
    except Exception:#    If it doesn't work, then we can deduce that a number hasn't been inputted.
        await interaction.response.send_message("That isn't a valid integer to convert into a date.")


@client.tree.command(name="meme-stats", description="[Social] Get some detailed analytics about the Baguette Brigaders Epic Memes Channel")
async def meme_analysis(interaction: discord.Interaction):
    await interaction.response.send_message(f"*FETCHing Discord API Data. Please wait...* {EMOJI_LOADING}")
    try:
        start_time = time.time()
        channel = client.get_channel(809112184902778890)
        if channel.type == discord.ChannelType.private:
            return
        if channel is not None and channel.type == discord.ChannelType.text:
            messages = []
            total_messages = 0
            meme_messages = 0

            async for message in channel.history(limit=None):
                total_messages = total_messages + 1
                if message.reactions:
                    print("Adding message to messages")
                    messages.append(message)
                    meme_messages = meme_messages + 1
                else:
                    print("Skipping message as no reactions")

            async def most_posts():
                author_scores = {}
                for message in messages:
                    upvote_count = 0
                    downvote_count = 0
                    for reaction in message.reactions:
                        if hasattr(reaction.emoji, 'name'):
                            if reaction.emoji.name == 'upvote':
                                upvote_count = reaction.count
                            elif reaction.emoji.name == 'downvote':
                                downvote_count = reaction.count

                    total_score = upvote_count - downvote_count

                    author_id = message.author.id
                    author_scores.setdefault(author_id, []).append(total_score)

                organised_user_scores = []
                for author_id, score_list in author_scores.items():
                    average_score = sum(score_list) / len(score_list)
                    organised_user_scores.append({'author_id': author_id, 'avg_score': average_score, 'posts': len(score_list)})

                organised_user_scores = sorted(organised_user_scores, key=lambda x: x['posts'], reverse=True)
                return organised_user_scores

            async def most_upvoted() -> str:
                calculated_messages = []

                for message in messages:
                    upvote_count = 0
                    downvote_count = 0
                    for reaction in message.reactions:
                        print(f"For message reaction in reactions: {reaction}")
                        if hasattr(reaction.emoji, 'name'):
                            if reaction.emoji.name == 'upvote':
                                upvote_count = reaction.count
                            elif reaction.emoji.name == 'downvote':
                                downvote_count = reaction.count

                    calculated_messages.append({"data": message, "id": message.id, "jump_url": message.jump_url, "upvotes": upvote_count, "downvotes": downvote_count, "total_score": upvote_count - downvote_count})

                most_upvoted = sorted(calculated_messages, key=lambda x: x['upvotes'], reverse=True)
                print(most_upvoted)
                return most_upvoted

            async def most_downvoted() -> list:
                calculated_messages = []

                for message in messages:
                    upvote_count = 0
                    downvote_count = 0
                    for reaction in message.reactions:
                        print(f"For message reaction in reactions: {reaction}")
                        if hasattr(reaction.emoji, 'name'):
                            if reaction.emoji.name == 'upvote':
                                upvote_count = reaction.count
                            elif reaction.emoji.name == 'downvote':
                                downvote_count = reaction.count

                    calculated_messages.append({"data": message, "id": message.id, "jump_url": message.jump_url, "upvotes": upvote_count, "downvotes": downvote_count, "total_score": upvote_count - downvote_count})

                downvote_count = sorted(calculated_messages, key=lambda x: x['downvotes'], reverse=True)
                print(downvote_count)
                return downvote_count

            downvote_count = await most_downvoted()
            most_post = await most_posts()
            most_upvote = await most_upvoted()

            embed = discord.Embed(title="Meme Stats")
            embed.add_field(name=f"{EMOJI_UPVOTE} Most Upvoted Posts {EMOJI_UPVOTE}", value=f"**<:NumberOne:1092556140556066837> [{most_upvote[0]['upvotes']} upvotes by {most_upvote[0]['data'].author.mention}]({most_upvote[0]['jump_url']}).**\n[{most_upvote[1]['upvotes']} upvotes by {most_upvote[1]['data'].author.mention}]({most_upvote[1]['jump_url']})\n[{most_upvote[2]['upvotes']} upvotes by {most_upvote[2]['data'].author.mention}]({most_upvote[2]['jump_url']})", inline=False)
            embed.add_field(name=F"{EMOJI_DOWNVOTE} Most Downvoted Posts {EMOJI_DOWNVOTE}", value=f"**<:NumberOne:1092556140556066837> [{downvote_count[0]['downvotes']} downvotes by {downvote_count[0]['data'].author.mention}]({downvote_count[0]['jump_url']}).**\n[{downvote_count[1]['downvotes']} downvotes by {downvote_count[1]['data'].author.mention}]({downvote_count[1]['jump_url']})\n[{downvote_count[2]['downvotes']} downvotes by {downvote_count[2]['data'].author.mention}]({downvote_count[2]['jump_url']})", inline=False)
            embed.add_field(name="📈 Most Posts", value=f"**<:NumberOne:1092556140556066837> {most_post[0]['posts']} posts, by <@{most_post[0]['author_id']}>. (Avg. upvotes/post: {round(most_post[0]['avg_score'], 2) })**\n{most_post[1]['posts']}, by <@{most_post[1]['author_id']}>\n{most_post[2]['posts']}, by <@{most_post[2]['author_id']}>", inline=False)
            embed.set_footer(text=('⚠️ This feature is currently in beta and is currently being worked on, please say your suggestions!'))

            await interaction.edit_original_response(content="", embed=embed)
    except Exception as e:
        await interaction.edit_original_response(content=f"Error **{e}**: ```python\n{traceback.format_exc()}```")


@client.tree.command(name="coins", description="[Social] Shows coin balance. If above a threshold, shows items to buy!")
@app_commands.guild_only()
@app_commands.describe(operation="[Admin Only] set/add/lookup.", target_user="[Admin Only] Enter the user id for the operation to target", amount="[Admin Only] Use this as the value for the operation")
@app_commands.choices(operation=[
    app_commands.Choice(name="Set", value="Set"),
    app_commands.Choice(name="Add", value="Add"),
    app_commands.Choice(name="Lookup", value="Lookup")
])
async def coins(interaction: discord.Interaction, operation: Optional[app_commands.Choice[str]] = None, target_user: Optional[discord.Member] = None, amount: Optional[int] = None) -> None:
    await slash_log(interaction)
    if interaction.guild and interaction.guild_id in TESTER_GUILD_IDS:
        print(operation, target_user, amount)
        member_role = discord.utils.get(interaction.guild.roles, id=806481292392267796)
        staff_role = discord.utils.get(interaction.guild.roles, id=963738031863525436)
        owner_role = discord.utils.get(interaction.guild.roles, id=759861763247570946)
        if member_role in interaction.user.roles or staff_role in interaction.user.roles or owner_role in interaction.user.roles:
            print(interaction.user.id)
            authorID = interaction.user.id
            # await ctx.send("Coins earned before 30/07/2021 are not available to use. This is a known bug and will be fixed later. You have not lost any Coins, but you cannot buy anything with your old balance. New Coins will be added to your old Coins.")
            userID = authorID
            user = interaction.user
            serverID = interaction.guild_id
            # print (serverID)

            coinBal = await get_coins(serverID, interaction.user.id)

            nolwenniumUserDir = (f"{BASE_DIR}Nolwennium{S_SLASH}{authorID}.txt")
            my_file = Path(nolwenniumUserDir)

            if not my_file.is_file():
                with open(nolwenniumUserDir, 'w+') as f:
                    print(f"\nSet {NAME_NOLWENNIUM} value to 0, {authorID} is a new user.")
                    try:
                        f.write('0')
                        f.close()
                    except Exception:
                        f.write('0')
                        f.close()

            with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                nolwennium_bal = round(float(nolwennium_balance_file.read()), 2)
                nolwennium_balance_file.close()

            if serverID == 384403250172133387 or serverID == 759861456300015657:
                canRunCommand = member_role
                canRunCommand2 = discord.utils.find(lambda r: r.id == 759861763247570946, interaction.guild.roles)
                if canRunCommand or canRunCommand2 in user.roles:
                    if operation:
                        # List of stuff BEFORE showing the user their balance
                        if not operation or not target_user:
                            return await interaction.response.send_message(IDK_WHAT_U_MEAN)
                        word1 = operation
                        userID = int(target_user.id)

                        if interaction.user.guild_permissions.administrator is True:
                            if word1.value == 'Set':
                                if not amount or not userID:
                                    return await interaction.response.send_message(IDK_WHAT_U_MEAN)
                                users_coins = (f"{BASE_DIR}Servers{S_SLASH}{serverID}{S_SLASH}Coins{S_SLASH}{userID}.txt")
                                old_coins = await get_coins(interaction.guild_id, userID)
                                with open(users_coins, 'w+') as f:
                                    f.write(str(amount))
                                new_coins = await get_coins(interaction.guild_id, userID)
                                return await interaction.response.send_message(f"Successfully set the user's coins from {old_coins} to **{new_coins}**.")
                            elif word1.value == 'Add':
                                if not amount or not userID:
                                    return await interaction.response.send_message(IDK_WHAT_U_MEAN)
                                added_balance = update_coins(interaction.guild_id, userID, amount)
                                return await interaction.response.send_message(f"Successfully added {amount} Coins to the user. They now have **{added_balance}**!")
                            elif word1.value == 'Lookup':
                                if not userID:
                                    return await interaction.response.send_message(IDK_WHAT_U_MEAN)
                                users_coins = get_coins(interaction.guild_id, userID)
                                if users_coins is None:
                                    return await interaction.response.send_message(f"<@{userID}> has not started earning Coins yet.")
                                return await interaction.response.send_message(f"<@{userID}> has **{users_coins}** Coins.")

                            else:
                                return await interaction.response.send_message(IDK_WHAT_U_MEAN)

                        else:
                            await interaction.response.send_message("You don't have full administrator privileges to run this command. Try `/coins` without any added options?")

                    else: # If no operation is specified, show the user their balance
                        hasCitizen = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[0], interaction.guild.roles)
                        hasKnight = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[1], interaction.guild.roles)
                        hasBaron = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[2], interaction.guild.roles)
                        hasViscount = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[3], interaction.guild.roles)
                        hasEarl = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[4], interaction.guild.roles)
                        hasMarquess = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[5], interaction.guild.roles)
                        hasDuke = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[6], interaction.guild.roles)
                        hasPrince = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[7], interaction.guild.roles)
                        hasKing = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[8], interaction.guild.roles)
                        hasAdmin = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[9], interaction.guild.roles)

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

                        next_available_role_cost = 0
                        roles_tier = -1

                        if hasCitizen in user.roles:
                            roles_tier = Roles.Citizen_Tier
                        if hasKnight in user.roles:
                            roles_tier = Roles.Knight_Tier
                        if hasBaron in user.roles:
                            roles_tier = Roles.Baron_Tier
                        if hasViscount in user.roles:
                            roles_tier = Roles.Viscount_Tier
                        if hasEarl in user.roles:
                            roles_tier = Roles.Earl_Tier
                        if hasMarquess in user.roles:
                            roles_tier = Roles.Marquess_Tier
                        if hasMarquess in user.roles:
                            roles_tier = Roles.Marquess_Tier
                        if hasDuke in user.roles:
                            roles_tier = Roles.Duke_Tier
                        if hasPrince in user.roles:
                            roles_tier = Roles.Prince_Tier
                        if hasKing in user.roles:
                            roles_tier = Roles.King_Tier

                        nextRole = Roles.ROLES_LIST[(roles_tier + 1)]
                        next_available_role_cost = Roles.ROLES_COSTS[(roles_tier + 1)]

                        # await interaction.response.send_message(f"the next role is {nextRole} which will cost {roles.ROLES_COSTS[(roles_tier + 1)]} coins. this means they are {next_available_role_cost - int(coinBal)} coins away.")

                        if roles_tier != -1:
                            roles_liste = ""

                            for i in range((roles_tier + 1)):
                                roles_liste = (f"{roles_liste}" + f"{(Roles.ROLES_LIST[i])}: Unlocked! 🔓\n")
                                i = i + 1
                            # await interaction.response.send_message(roles_liste)

                            with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                                nolwennium_balance = round(float(nolwennium_balance_file.read()), 2)
                                nolwennium_balance_file.close()

                            finalSum = f"{roles_liste}" + f"{nextRole}: {Roles.ROLES_COSTS[(roles_tier + 1)]} {EMOJI_COINS} 🔒"

                            if "🔓" not in finalSum:
                                if f"{EMOJI_COINS}" not in finalSum:
                                    finalSum = "***You have bought all possible roles! Maybe some more will come out in the future...***"
                        else:
                            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {EMOJI_COINS} coins and {nolwennium_bal} {EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)
                            embed.add_field(
                                name="Items curently available for you to buy:",
                                value=f"**Citizen**: FREE {EMOJI_COINS}\n\nType </buy:1057428586610573359> `item:citizen` to start ascending through purchasable roles!",
                                inline=False)
                            embed.set_footer(text=(f'Type </buy:1057428586610573359> to buy your selected item! For example, </buy:1057428586610573359> `item:citizen`.\nYou can buy roles for Coins in this server, and use {NAME_NOLWENNIUM} to run bot commands (in all servers).'))
                            await interaction.response.send_message(embed=embed)
                            return

                        embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {EMOJI_COINS} coins and {nolwennium_bal} {EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)
                        embed.add_field(
                            name="Items available to buy:",
                            value=finalSum,
                            inline=False
                        )
                        if next_available_role_cost > 0:
                            embed.add_field(
                                name="Next item available to buy in:",
                                value=f"{next_available_role_cost - int(coinBal)} {EMOJI_COINS} Coins (**{nextRole}**)",
                                inline=False
                            )
                        elif next_available_role_cost <= 0:
                            embed.add_field(name="Buy your roles!", value=f":warning: You can afford a new role. Once bought, this will say how\n many more {EMOJI_COINS} Coins are needed until the next role.")

                        embed.set_footer(text=(f'Type </buy:1057428586610573359> `item` to buy your selected item! For example, </buy:1057428586610573359> `item:citizen`.\nYou can buy roles for Coins in this server, and use {NAME_NOLWENNIUM} to run bot commands (saved across all servers).'))

                        x = await get_user_settings(interaction.user.id)

                        view = discord.ui.View()
                        if x['can_use_shop_section_2'] == 'true':
                            view.add_item(CoinsButtons2(label="View Page 2", style=discord.ButtonStyle.blurple))

                        await interaction.response.send_message(embed=embed, view=view)
                else:
                    await interaction.response.send_message("You do not have permission to access the shop interface.")
            else:
                nolwenniumUserDirectory(interaction)
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    nolly = "0"
                else:
                    with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                        nolwennium_balance = nolwennium_balance_file.read()
                        nolwennium_balance_file.close()
                    nolly = f"{nolwennium_balance} {EMOJI_NOLWENNIUM}"
                await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check https://ibaguette.com/discord for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {EMOJI_NOLWENNIUM}")
        else:
            await error_code(interaction, 1)


#   buy


@client.tree.command(name="buy", description="[Social] Shows your balance, and available to buy items.")
@app_commands.guild_only()
@app_commands.choices(item=[
    app_commands.Choice(name="Citizen", value="Citizen"),
    app_commands.Choice(name="Knight", value="Knight"),
    app_commands.Choice(name="Baron", value="Baron"),
    app_commands.Choice(name="Viscount", value="Viscount"),
    app_commands.Choice(name="Earl", value="Earl"),
    app_commands.Choice(name="Marquess", value="Marquess"),
    app_commands.Choice(name="Duke", value="Duke"),
    app_commands.Choice(name="Prince", value="Prince"),
    app_commands.Choice(name="King", value="King") # ,
    # app_commands.Choice(name="Emperor", value="Emperor"),
    # app_commands.Choice(name="Legend", value="Legend"),
    # app_commands.Choice(name="God", value="God"),
])
@app_commands.describe(item="Enter the item to buy here")
async def buy(interaction: discord.Interaction, item: app_commands.Choice[str]) -> None:
    await slash_log(interaction)
    if not interaction.guild:
        return await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
    if interaction.guild_id in TESTER_GUILD_IDS:
        canRunCommand = rolePrivate
        owner = discord.utils.find(lambda r: r.name == 'Owner', interaction.guild.roles)
        staff = discord.utils.find(lambda r: r.name == 'Staff', interaction.guild.roles)
        can_access_shop_ui = False
        if owner in interaction.user.roles:
            print("Owner is in the roles list")
            await interaction.channel.send("> Note: you already have owner permissions, this overrides the shop's items, permissions, and perks")
            can_access_shop_ui = True
        if staff in interaction.user.roles:
            print("Staff is in the roles list")
            await interaction.channel.send("> Note: already have staff permissions, this overrides the shop's items, permissions, and perks")
            can_access_shop_ui = True
        if canRunCommand in interaction.user.roles:
            print("Member is in the list")
            can_access_shop_ui = True
        if can_access_shop_ui:
            member = await interaction.guild.fetch_member(interaction.user.id)
            item_name = item.value.lower()

            coinBal = await get_coins(interaction.guild_id, interaction.user.id)

            if item_name == 'citizen':
                cost = 1
                hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                if hasCitizen in member.roles:
                    await interaction.response.send_message("You can't buy Citizen, you already have it!")
                    return

                coinBal = int(coinBal) - cost
                update_coins(interaction.guild_id, interaction.user.id, -cost)

                role = discord.utils.get(interaction.guild.roles, name="Citizen")
                await member.add_roles(role)
                embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought Citizen for free! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                embed.add_field(name="Perks",
                                value=f"• Above Member in the Member List\n• Custom nickname\n• Add reactions\n• Bonus {NAME_NOLWENNIUM}",
                                inline=False
                                )
                await interaction.response.send_message(embed=embed)
                return

#           KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT

            if item_name == 'knight':
                cost = 25
                roleName = "Knight"
                hasKnight = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasKnight in member.roles:
                    await interaction.response.send_message(f"You can't buy {roleName}, you already have it!")
                    return

                hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                if hasCitizen in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Citizen"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Create private threads",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Citizen before {roleName}.")
                    return
                return

#           BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON

            if item_name == 'baron':
                cost = 50
                roleName = "Baron"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasBaron in member.roles:
                    await interaction.response.send_message(f"You can't buy {roleName}, you already have it!")
                    return

                #   Check if the person has the previous role. If not, can't buy.
                hasKnight = discord.utils.find(lambda r: r.name == 'Knight', interaction.guild.roles)
                if hasKnight in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Knight"))
                    await member.add_roles(role)

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value=f"Everything in Citizen, and:\n• Use external stickers\n• Increased Coins earning\n• Bonus {NAME_NOLWENNIUM}",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Knight before {roleName}.")
                    return
                return

#           VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT

            if item_name == 'viscount':
                cost = 100
                roleName = "Viscount"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasBaron in member.roles:
                    await interaction.response.send_message("You can't buy Viscount, you already have it!")
                    return

                #   Check if the person has the previous role. If not, can't buy.
                hasBaron = discord.utils.find(lambda r: r.name == 'Baron', interaction.guild.roles)
                if hasBaron in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Everything in Baron, and:\n• Use TTS messages\n• Use server activities",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Baron before {roleName}.")
                    return
                return

#           EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL

            if item_name == 'earl':
                cost = 250
                roleName = "Earl"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasBaron in member.roles:
                    await interaction.response.send_message("You can't buy Earl, you already have it!")
                    return

                #   Check if the person has the previous role. If not, can't buy.
                hasViscount = discord.utils.find(lambda r: r.name == "Viscount", interaction.guild.roles)
                if hasViscount in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    if role is not None:
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Viscount")) # Remove previous role
                        await member.add_roles(role)
                    else:
                        print(f"Role '{roleName}' not found")

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Everything in Viscount, and:\n• Add and edit server events",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Viscount before {roleName}.")
                    return
                return

#           MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS

            if item_name == 'marquess':
                cost = 500
                roleName = "Marquess"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasBaron in member.roles:
                    await interaction.response.send_message("You can't buy Earl, you already have it!")
                    return

                #   Check if the person has the previous role. If not, can't buy.
                hasEarl = discord.utils.find(lambda r: r.name == 'Earl', interaction.guild.roles)
                if hasEarl in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Everything in Earl, and:\n• View detailed server statistics\n• Access to some more stuff, you'll figure it out",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Earl before {roleName}.")
                    return
                return

#           DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE

            if item_name == 'duke':
                cost = 1000
                roleName = "Duke"
                #   Check if the person already has the role.
                hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasBaron in member.roles:
                    await interaction.response.send_message("You can't buy Earl, you already have it!")
                    return
                #   Check if the person has the previous role. If not, can't buy.
                hasMarquess = discord.utils.find(lambda r: r.name == 'Marquess', interaction.guild.roles)
                if hasMarquess in member.roles:
                    #   Tests balance if user can afford the new role.
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        requiredAmount = cost - int(coinBal)
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    #   If the balance is adequate, allow the purchase.
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Marquess"))

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Everything in Marquess, and:\n• Mute members\n• Manage threads\n• View private threads\n• Access to history of <#1035684553546809456>",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Marquess before {roleName}.")
                    return
                return

#           PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINC

            if item_name == 'prince':
                cost = 2500
                roleName = "Prince"
                hasPrince = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasPrince in member.roles:
                    await interaction.response.send_message("You can't buy Prince, you already have it!")
                    return

                hasDuke = discord.utils.find(lambda r: r.name == 'Duke', interaction.guild.roles)
                if hasDuke in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest <= 0:
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Duke"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value="Everything in Duke, and:\n• Move members in voice channels\n• Use Priority speaker in voice chat\n• Change others' nicknames\n• Time out members if they are being annoying\n• Add emojis and stickers\n• Add custom channels",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("You must buy Knight before Prince.")
                return

#           KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING

            if item_name == 'king':
                cost = 10000
                roleName = "King"
                hasKing = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                if hasKing in member.roles:
                    await interaction.response.send_message("You can't buy King, you already have it!")
                    return

                hasPrince = discord.utils.find(lambda r: r.name == 'Prince', interaction.guild.roles)
                if hasPrince in member.roles:
                    coinBalTest = int(coinBal) - cost
                    if coinBalTest < 0:
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                        return
                    coinBal = int(coinBal) - cost
                    update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name="King")
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Prince"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought King for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value=f"Everything in Prince, and:\n• Deafen members\n• Pin and manage messages\n• Add custom webhooks\n• Add custom bots\n• Add into Other Channels and define permissions",
                                    inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("You must buy Prince before King.")
                return

            if item_name == 'admin':
                await error_code(interaction, 1)
            else:
                await interaction.response.send_message(f"**{item_name}** isn't a valid item to buy. Try `Citizen/Knight/Baron/Viscount/Earl/Marquess/Duke/Prince/King/Admin`!")
        else:
            await error_code(interaction, 1)
    else:
        nolwenniumUserDir = nolwenniumUserDirectory(interaction)
        my_file = Path(nolwenniumUserDir)
        if not my_file.is_file():
            nolly = "0"
        else:
            f = open(nolwenniumUserDir, 'r')
            nolwennium_bal = f.read()
            f.close()
            nolly = f"{nolwennium_bal} {EMOJI_NOLWENNIUM}"
        await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/GfetCXH for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {EMOJI_NOLWENNIUM}")


#   setdelay

@client.tree.command(name="slowmode", description="[Utility] Sets the slowmode in a channel.")
@app_commands.describe(seconds="Input seconds here.")
async def setdelay(interaction: discord.Interaction, seconds: int):
    await slash_log(interaction)
    if not interaction.user.guild_permissions.manage_channels:
        return await interaction.response.send_message("You are missing the required guild persmission: `manage_channels`.")
    try:
        seconds = int(seconds)
    except ValueError:
        return await interaction.response.send_message(f"Invalid integer: {seconds}")

    if seconds == 0:
        await interaction.channel.edit(slowmode_delay=seconds, reason=f"Slash Command ran by {interaction.user.name} ({interaction.user.id}) at {datetime.now()}.")
        return await interaction.response.send_message("Removed slowmode from this channel.")
    else:
        await interaction.channel.edit(slowmode_delay=seconds, reason=f"Slash Command ran by {interaction.user.name} ({interaction.user.id}) at {datetime.now()}.")

    embed = discord.Embed(title="Edited channel info!", description=(f"Set the slowmode delay in this channel to {seconds} seconds!"), colour=0x228B22)
    await interaction.response.send_message(embed=embed)

    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write(f"\nCOMMAND RAN -> '.setdelay {seconds}' ran by {interaction.user} in channel {interaction.channel.mention} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.setdelay {seconds}' ran by {interaction.user} in channel {interaction.channel.mention} at {datetime.now()}")


# Clear roles

@client.tree.command(name="clearroles", description="[Utility] Clears all roles from a user.")
@app_commands.describe(user="User to clear roles from")
async def clearroles(interaction: discord.Interaction, user: discord.Member):
    await slash_log(interaction)
    await interaction.response.defer()
    if not interaction.user.guild_permissions.administrator:
        return await interaction.followup.send("You must be a server administrator to use this command.")

    await interaction.followup.send(f"Clearing roles from **{user.name}**...")

    role_count = 0
    errors = 0
    for role in user.roles:
        try:
            await user.remove_roles(role)
            role_count += 1
        except Exception:
            errors += 1
            pass

    await interaction.followup.send(f"Removed {role_count} roles from **{user.name}** with {errors} errors.")


# Copy Roles from one user to another

@client.tree.command(name="copyroles", description="[Utility] Copy roles from one user to another.")
@app_commands.describe(user1="User to copy roles from", user2="User to copy roles to")
async def copyroles(interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):
    await slash_log(interaction)
    await interaction.response.defer()
    if not interaction.user.guild_permissions.administrator:
        return await interaction.followup.send("You must be an administrator to use this command.")

    if user1 == user2:
        return await interaction.followup.send("You can't copy roles from a user to themselves!")

    await interaction.followup.send(f"Copying roles from {user1.mention} to {user2.mention}...")

    role_count = 0
    errors = 0
    for role in user1.roles:
        try:
            await user2.add_roles(role)
            role_count += 1
        except Exception:
            # await interaction.followup.send(f"Failed to copy role `{role.name}` ({role.id}) from `{user1.name}` to `{user2.name}` due to error: {e}")
            errors += 1
            pass

    embed = discord.Embed(title="Roles copied!", description=(f"{role_count} roles copied from `{user1.name}` to `{user2.name}`! There were {errors} errors."), colour=0x228B22)
    await interaction.response.send_message(embed=embed)


# EmojiArchiver


@client.tree.command(name="emoji-backup", description="[Utility] Backs up all your server emojis. This will be retrievable soon.")
@app_commands.describe(guild_id="Enter server ID to grab emojis from")
async def emojis(interaction: discord.Interaction, guild_id: str):
    await slash_log(interaction)
    if not interaction.user.guild_permissions.manage_emojis_and_stickers:
        return await interaction.response.send_message("You are missing the required guild persmission: `manage_emojis_and_stickers`.")

    newGuild = client.get_guild(int(guild_id))
    if newGuild is None:
        return await interaction.response.send_message("Unable to get that guild's data.")
    await interaction.response.send_message(f"Getting emojis for {newGuild.id} // {newGuild.name}")
    emoji_list = []
    emojis = 0
    for emoji in newGuild.emojis:
        emojis += 1
        emoji_list.append(f"{emoji.name} - {emoji.url}")
        x = requests.get(emoji.url)
        emoji_exturl = emoji.url
        emoji_exturl = emoji_exturl.split(".")
        extension = (emoji_exturl[3])

        if os.path.exists(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}'):
            with open(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}{emoji.name}.{extension}', 'wb') as f:
                f.write(x.content)
                print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
        else:
            os.mkdir(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}')
            print(f"Made emoji directory for {newGuild.id} // {newGuild.name}")
            with open(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}{emoji.name}.{extension}', 'wb') as f:
                f.write(x.content)
                print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")

    await interaction.followup.send(f"Done! Saved {emojis} emojis.")

    if interaction.user.id == 382784106984898560:
        await interaction.response.send_message("Running on all guilds")
        emojis = 0
        guilds = 0
        for guild in client.guilds:
            guilds += 1
            newGuild = client.get_guild(guild.id)
            if not newGuild:
                return await interaction.response.send_message("Unable to get that guild's data.")
            await interaction.followup.send(f"Getting emojis for {newGuild.id} // {newGuild.name}")
            emoji_list = []
            for emoji in newGuild.emojis:
                emojis += 1
                emoji_list.append(f"{emoji.name} - {emoji.url}")
                x = requests.get(emoji.url)
                emoji_exturl = emoji.url
                emoji_exturl = emoji_exturl.split(".")
                extension = (emoji_exturl[1])

                if os.path.exists(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}'):
                    with open(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}{emoji.name}.{extension}', 'wb') as f:
                        f.write(x.content)
                        print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
                else:
                    os.mkdir(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}')
                    print(f"Made emoji directory for {newGuild.id} // {newGuild.name}")
                    with open(f'{BASE_DIR}Servers{S_SLASH}{newGuild.id}{S_SLASH}Emojis{S_SLASH}{emoji.name}.{extension}', 'wb') as f:
                        f.write(x.content)
                        print(f"Saved emoji {emoji.name} ({extension.upper()}) // {newGuild.name}")
            try:
                if str(emoji_list) == "[]":
                    print(f"No emojis in guild {newGuild.id}")
                else:
                    await interaction.followup.send(emoji_list)
            except Exception as e:
                await interaction.followup.send(f"Probably too many emojis. `{e}`")
        await interaction.followup.send(f"Done! Archived {emojis} from {guilds} guilds.")


#   Get messages

@client.tree.command(name="get_messages", description="[Admin Only] Get direct messages sent to a user object")
@app_commands.describe(id="User id to objectify")
async def get_messages(interaction: discord.Interaction, id: str):
    await slash_log(interaction)
    if interaction.user.id == 382784106984898560:
        user1 = await client.fetch_user(int(id))

        dmchannel = await user1.create_dm() # "Create" a DM
        async for message in dmchannel.history(limit=30): # Async through the messages
            await interaction.response.send_message(f"{message.author.name}: `{message.content}`")

#   log search


@client.tree.command(name="logsearch", description="[Utility] Search the message history for a term. Returns how many times it was sent.")
@app_commands.describe(term="String to search the log for")
async def log(interaction: discord.Interaction, term: str):
    await slash_log(interaction)
    if not interaction.user.guild_permissions.view_audit_log:
        return await interaction.response.send_message("You are missing the required guild persmission: `view_audit_log`.")
    serverID = interaction.guild_id

    if not interaction.guild:
        return await interaction.response.send_message("This cannot be used in DMs.")

    else:
        serverName = interaction.guild.name

    file = open((f"{BASE_DIR}Servers{S_SLASH}{serverID}{S_SLASH}Logs{S_SLASH}MessageLog.txt"),encoding="UTF-8").read().lower()
    count = file.count(term)

    count = count - 1

    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{term}**':", value=f"{count}", inline=False)
    embed.set_footer(text=f"Not case sensitive. Does not account for bot messages. Searching in server {serverID}/{serverName}.")
    await interaction.response.send_message(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.log' ran by {interaction.user} at {datetime.now()}")
    f.close()


@client.tree.command(name="volume", description="[Voice] Change the audio player's volume or lock it.")
@app_commands.describe(percentage=f"Enter the volume in percentage to play. The default is {VOICE_VOLUME}%. Values above 1000 don't work.", lock="[Manage Server] Would you this volume to be locked? ('True' be specified each time.)")
async def volume(interaction: discord.Interaction, percentage: int, lock: bool = False):
    await slash_log(interaction)
    if not interaction.guild:
        return await interaction.response.send_message("This cannot be used in DMs.")
    try:
        volume_float = int(percentage)
    except Exception:
        return await interaction.response.send_message(f"Unable to convert {volume_float} into a valid percentage.")

    str_to_send = ""

    if volume_float > 1000:
        volume_float = 1000

    if not os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt"):
        with open(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'w') as f:
            f.write(str(VOICE_VOLUME))
            print(f"[VOICE_VOLUME]       Created a directory for guild_id {interaction.guild_id}")

    vc: wavelink.Player = interaction.guild.voice_client
    if vc is None:
        return await interaction.response.send_message("Not currently in a voice channel.")

    if lock:
        if not interaction.user.guild_permissions.manage_guild:
            return await interaction.response.send_message("You are trying to lock a voice channel without having the right priviliges: `manage_guild`.")
        with open(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'w+') as file:
            file.write(str(volume_float))
        with open(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_IsLocked.txt", 'w') as file:
            file.close()

        if vc.is_playing():
            await vc.set_volume(volume_float)

        return await interaction.response.send_message(f"{EMOJI_TICK_ANIMATED} Locked the voice chat volume to {volume_float}% for this server.")

    if os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_IsLocked.txt"):
        if interaction.user.guild_permissions.manage_guild:
            return await interaction.response.send_message("You can't modify the volume as it has been locked. Change the value of `lock` to `True` when using `/volume` to toggle it off again.")
        else:
            return await interaction.response.send_message("You can't modify the volume as it has been locked by a guild manager.")

    voice_client = interaction.guild.voice_client

    if voice_client is not None:
        if voice_client.is_playing():
            voice_client.volume = volume_float

    with open(f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'w+') as file:
        file.write(str(volume_float))
        print(f"[VOICE_VOLUME]       Written to {interaction.guild_id} file: {str(volume_float)}")
        str_to_send = (f"{str_to_send}\n{EMOJI_TICK_ANIMATED} Set the server's voice percentage to: **{volume_float}%.**")

    vc: wavelink.Player = interaction.guild.voice_client or await interaction.user.voice.channel.connect(cls=wavelink.Player)
    if vc.is_playing():
        volume = await get_server_voice_volume(interaction.guild.id)
        volume = (volume) # as Wavelink uses native percentages
        await vc.set_volume(volume)
        str_to_send = f"{str_to_send}\nNOTE: An experimental, faster HD player, Wavelink, is being used to handle audio, so it may take an extra few seconds to normalise audio output."

    await interaction.response.send_message(str_to_send)


@client.tree.command(name="gpt", description="[Social] Get GPT-3 to respond to your prompt.")
@app_commands.describe(prompt="What do you want GPT3 to generate? 'Write a story about...', 'Summarise the relationship...'", model="1, 2, 3 or 4: 4 is the most capable but slowest.", limit="Max tokens to generate. Up to 4080 including the input.", dm="Do you want me to DM you the result? (Doesn't work for longer stuff)", temperature="[Advanced] 0-100. Controls randomness, zero = deterministic & repetitive.", top_p="0-100. Controls diversity, 50 = half the liklihood-weighted options considered.", frequency_penalty="0-200. Penalises repeated tokens. 200 = low chance to repeat lines.", presence_penalty="0-200. Penalises repeated tokens. 200 = high chance to talk about new topics")
async def gpt(interaction: discord.Interaction, prompt: str, model: int, limit: int, dm: Optional[bool] = False, temperature: Optional[int] = None, top_p: Optional[int] = None, frequency_penalty: Optional[int] = None, presence_penalty: Optional[int]=None):
    # await ctx.send("Generating response... <a:loading:935623554215591936>")
    await slash_log(interaction)
    print(f"/ [GPT-3]     Prompt '{prompt}' entered by {interaction.user.id} ({interaction.user.name}) in {interaction.guild_id}. Model: {model} // Limit: {limit}")
    if not temperature:
        temperature = 0.69
    else:
        temperature = temperature / 100

    if not top_p:
        top_p = 0.95
    else:
        top_p = top_p / 100

    if not frequency_penalty:
        frequency_penalty = 0
    else:
        frequency_penalty = frequency_penalty / 100

    if not presence_penalty:
        presence_penalty = 0
    else:
        presence_penalty = presence_penalty / 100

    if not dm:
        dm = False

    if os.path.isfile(f"{BASE_DIR}openai_disabled.txt"):
        return await interaction.response.send_message("The OpenAI subsystem has been disabled.")

    if prompt is None:
        return await interaction.response.send_message("No prompt!")

    if model == 1:
        model_type = "text-ada-001"
    if model == 2:
        model_type = "text-babbage-001"
    if model == 4:
        model_type = "text-davinci-002"
    else:#  Default.
        model_type = "text-curie-001"

    #   Now defer as it may take a long time lmao
    await interaction.response.defer()

    with open(f"{BASE_DIR}openai_api_key.txt", 'r') as f:
        openai_key = f.read()
    openai.api_key = openai_key

    response = openai.Moderation.create(
        input=prompt,
    )
    print(response)
    print(response.results[0])
    output = (response.results[0].flagged)
    if output == 1:
        return await interaction.followup.send("You've sent it some really sussy things, so imma have to stop you right there... wtf!")

    #   Get the actual data

    try:
        response = openai.Completion.create(
            model=model_type,
            prompt=prompt,
            temperature=temperature,
            max_tokens=limit,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
    except Exception as e:
        await interaction.followup.send(e)

    response_content = (response.choices[0].text)
    print(response_content)

    mod_response = openai.Moderation.create(
        input=response_content,
    )
    print(mod_response)
    print(mod_response.results[0])
    output = (mod_response.results[0].flagged)

    if output == 1:
        with open(f"Z:\\{interaction.user.id}_gpt.txt", 'w+') as f:
            f.write(response_content)
        view = discord.ui.View()
        view.add_item(SusButton(label="See Sussiness", style=discord.ButtonStyle.red))
        return await interaction.followup.send("The output of the request was a little too suspicious. If you *really* want to see it, then click the button.", view=view)

    if len(response_content) > 1900:
        chunks = [response_content[i:i+1900] for i in range(0, len(response_content), 1900)]
        print(len(chunks))

        if dm:
            for chunk in chunks:
                await interaction.user.send(chunk)
            await interaction.followup.send("I've sent the result in your DMs!")
            for chunk in chunks:
                await draggie.send(chunk)
        else:
            for chunk in chunks:
                await interaction.followup.send(chunk)

    if dm:
        await interaction.user.send(response_content)
        await interaction.followup.send("I've sent the result in your DMs!")
        await draggie.send(x)
    else:
        await interaction.followup.send(response_content)


@client.tree.command(name="stop", description="[Voice] Stops everything in Voice Chat, clears the queue, disconnects.")
async def stop(interaction: discord.Interaction):
    await slash_log(interaction)
    if not interaction.user.guild_permissions.stream:
        return await interaction.response.send_message("You are missing the required guild persmission: `stream`.")
    voice_client = interaction.guild.voice_client
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc:
        return await interaction.response.send_message("Currently not in a voice chat channel. Please disconnect and reconnect me if you believe this is an error.")
    if vc.is_playing():
        vc.autoplay = False
        await vc.stop()
        vc.queue.clear()
        await vc.disconnect()
        return await interaction.response.send_message("Stopped playing audio, stopped the queue and disconnected.\n*Using `/pause` or `/skip` will not clear the queue.*")
    if voice_client is not None:
        vc.autoplay = False
        voice_client.stop()
        return await interaction.response.send_message("Stopped playing audio.")
    else:
        return await interaction.response.send_message(f"There is no currently active voice client in the guild id {interaction.guild_id}")


@client.tree.command(name="leave", description="[Voice] Leaves the voice channel.")
async def leave(interaction: discord.Interaction):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc:
        return await interaction.response.send_message("I'm not in a Voice Channel.")
    if not interaction.user.guild_permissions.moderate_members:
        return await interaction.response.send_message("You are missing the required guild persmission: `moderate_members`.")
    await vc.disconnect()
    await interaction.response.send_message(f"Left the voice channel {vc.channel}")


@client.tree.command(name="bitrates", description="[Utility] Set all Voice Channel bitrates")
@app_commands.describe(bitrate="Enter specific bitrate, in bytes/sec. Leave blank or 0 to default to max")
async def bitrates(interaction: discord.Interaction, bitrate: Optional[str]):
    await slash_log(interaction)
    if not interaction.guild:
        return await interaction.response.send_message("This command can only be used in a server.")
    if not interaction.user.guild_permissions.manage_channels:
        return await interaction.response.send_message("You are missing the required guild persmission: `manage_channels`.")

    if bitrate is not None:
        try:
            specific_bitrate = int(bitrate)
        except ValueError:
            return await interaction.response.send_message("Invalid bitrate")

    x = ""
    for channel in interaction.guild.voice_channels:
        try:
            if 'specific_bitrate' not in locals():
                if channel.bitrate is not interaction.guild.bitrate_limit:
                    await channel.edit(bitrate=interaction.guild.bitrate_limit, reason=f"Command ran by {interaction.user.name} at {datetime.now()}")
                    x = f"Set the bitrate of **<#{channel.id}>** to **{round(interaction.guild.bitrate_limit/1000)}** kbps.\n{x}"
                else:
                    x = f"Bitrate of **<#{channel.id}>** is at the maximum bitrate.\n{x}"
            else:
                try:
                    await channel.edit(bitrate=specific_bitrate, reason=f"Command ran by {interaction.user.name} at {datetime.now()}")
                    x = f"Set the bitrate of **<#{channel.id}>** to **{specific_bitrate/1000}** kbps.\n{x}"
                except Exception:
                    x = f"Error changing the bitrate of **<#{channel.id}>** to **{specific_bitrate}** bps. (The server limit is between 8000 and {interaction.guild.bitrate_limit}, maybe that's why?)\n{x}"

        except Exception:
            x = f"Could not edit the information of <#{channel.id}>. Maybe the bot doesn't have good permissions?\n{x}"
            await interaction.response.send_message(x)
    await interaction.response.send_message(x)
    if x == "":
        await interaction.response.send_message("Nothing happened.")

#   Pause/resume audio


@client.tree.command(name="pause", description="[Voice] Pauses or resumes audio being played")
async def pause(interaction: discord.Interaction):
    await slash_log(interaction)
    if not interaction.guild:
        return await interaction.response.send_message("This command can only be used in a server.")
    vc = interaction.guild.voice_client
    if not vc:
        return await interaction.response.send_message("Audio is unable to be paused because there is no audio to pause")
    if not vc._paused:
        await vc.pause()
        await interaction.response.send_message("*✅ Paused the current audio playing!*")
    elif vc._paused:
        await vc.resume()
        await interaction.response.send_message("*✅ Resumed playing the audio!*")
    else:
        await interaction.response.send_message("Audio is unable to be paused")

#   Nolwennium mine


@client.tree.command(name="mine", description="[Social] Mines some globalCurrency which can be used to do cool stuff!")
@app_commands.checks.cooldown(1, 29, key=lambda i: (i.user.id))
async def mine(interaction: discord.Interaction):
    await slash_log(interaction)
    print(f"CURRENCY - {NAME_NOLWENNIUM} > {interaction.user.id} is mining")

    base_mined_amount = random.randint(-5, 88)

    #   Nolwennium UPDATED LOCATION 2/11/2021: {BASE_DIR}Nolwennium{S_SLASH}
    filedir = (f"{BASE_DIR}Nolwennium{S_SLASH}{interaction.user.id}.txt")

    #   Calculate fees first, so the calculations after account for it.
    fee = base_mined_amount / random.randint(10, 40)
    newNumberAfterFee = base_mined_amount - fee
    newNumberAfterFee = round(newNumberAfterFee, 3)
    fee = round(fee, 3)

    #   Assign basic values first
    shared_guilds = interaction.user.mutual_guilds
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
    embed.add_field(name="**Initially Mined**", value=f"{base_mined_amount} {EMOJI_NOLWENNIUM} {NAME_NOLWENNIUM}!")

    #   Perform first check if a user is Boosting the server. If so, then give them a big bonus.
    #   If not, check if they have Nitro. If yes, checked by an animated profile picture, encourage to use a Boost.
    if interaction.user.premium_since:
        BoosterBonus = random.randint(30, 150)
        embed.add_field(name="**Server Booster Bonus**", value=(f"{BoosterBonus} {EMOJI_NOLWENNIUM} {NAME_NOLWENNIUM}"), inline=False)
        balance = balance + BoosterBonus
        bonuses += BoosterBonus
    else:
        print("Ok, the user doesn't have nitro.")

    #   Check for shared servers. If so, add a random bonus based 3x the amount shared.
    for guild in shared_guilds:
        shared_number += 1

    #   Check shared guilds. If it's only one server, i.e the current one, then encourage them to add it to another server.
    if shared_number > 1:
        SharedServerBonus = random.randint(1, (shared_number * 3))
        embed.add_field(name="**Shared Servers Bonus**", value=(f"{SharedServerBonus} {EMOJI_NOLWENNIUM} {NAME_NOLWENNIUM}"), inline=False)
        balance = balance + SharedServerBonus
        bonuses += SharedServerBonus
    else:
        embed.add_field(name="**Shared servers: 1**", value="Not enough servers shared for a bonus. :(", inline=False)

    #   Set the embed desription to the above mined string (determined by whether or not the user has mined before.
    #   The output will be something like "Mined another 10 Nolwennium!"
    #   As it's a description, it will be placed *above* the added fields.
    embed.description = f"Mined a total of {base_mined_amount + bonuses} {EMOJI_NOLWENNIUM} {NAME_NOLWENNIUM}!"

    #   Finally, show the fees, also paid to a random 'Croissant'.
    croissant_to_pay = random.randint(0, 2)
    croissant_paid = CROISSANTS[croissant_to_pay]
    croisssant_name = CROISSANT_NAMES[croissant_to_pay]
    embed.add_field(name="**Fees Paid**", value=f"{fee} to **{croisssant_name}**", inline=False)

    #   Check for bonuses, new in 1.2.10

    bonus_perks = ["5 Gems", "Golden Treasure Chest", "Engraved Diamond", "Polished Diamond", "Crown", "Tiara", "Stick", "Rubber Duck", "Encrusted Ring", "Golden Ring", "Old Bracelet", "Necklace"]
    bonus_perk_reward = ["500", "2000", "10000", "12000", "13500", "7500", "1", "25", "6000", "7500", "3500", "2500"]

    randomiser = random.randint(0, 100)
    print("Randomiser:", randomiser)
    if randomiser < 30:
        luck = random.randint(0, 250)
        if luck <= 50:
            print("Luck", luck)
            luck = random.randint(0, 11)
            bonus_perk = bonus_perks[luck]
            bonus_perk_reward = bonus_perk_reward[luck]
            embed.add_field(name="***You found rare loot!***", value=f"**{bonus_perk}**: {bonus_perk_reward} bonus {NAME_NOLWENNIUM}!")
            balance = balance + int(bonus_perk_reward)
            bonuses = bonuses + int(bonus_perk_reward)

    #   'balance' takes into account existing balance, read from a file, and bonuses.
    #   'newNumberAfterFee' is calculated initially from the base amount mined.
    new_balance = balance + newNumberAfterFee

    #   Set fields and footers, then send the final compiled result.
    embed.add_field(name="**Total Balance**", value=(f"{(round (new_balance, 3))} {EMOJI_NOLWENNIUM} {NAME_NOLWENNIUM}"), inline=False)
    embed.set_footer(text=f"ID: {interaction.user.id} | Bonuses ({bonuses}) + base: ({base_mined_amount}) = {bonuses + base_mined_amount}")

    await interaction.response.send_message(embed=embed)

    #   Write balance and globally log it!
    with open(filedir, 'w+') as f:
        f.write(str(new_balance))
        f.close()
    with open(GlobalLogDir, "a", encoding='utf-8') as f:
        f.write(f"COMMAND RAN -> '.mine' ran by {interaction.user} in {interaction.guild.id} at {datetime.now()}")
        f.close()

    #   Add the fees to the aforementioned croissant
    randomcroissant = (f"{BASE_DIR}Nolwennium{S_SLASH}{croissant_paid}.txt")
    try:
        with open(randomcroissant, 'r') as e:
            balance = float(e.read())
    except Exception:
        with open(randomcroissant, 'w+') as e:
            e.write("0")
            e.close()

        with open(randomcroissant, 'r') as e:
            balance = float(e.read())
            e.close()

    balance = balance + fee

    with open(randomcroissant, 'w+') as f:
        f.write(str(balance))
    await bot_runtime_events(1)
    print(f"CURRENCY - {NAME_NOLWENNIUM} > {interaction.user.id} has gained {newNumberAfterFee} {NAME_NOLWENNIUM} (fee: {fee}). Their total is {new_balance}")

#   yn


@client.tree.command(name="yes-no", description="[Social] Randomly answers yes or no.")
async def yn(interaction: discord.Interaction):
    await slash_log(interaction)
    list_test = ["No!", "Of course not!", "Certainly not.", "Definitely not!", "Obviously not.", "Nah!", "Nope.", "Hell nah...",
                 "Yes!", "Obviously!", "Of course!", "Certainly!", "Definitely!", "Without a shadow of a doubt!", "Yessir!"]
    await interaction.response.send_message(random.choice(list_test))

    print(f"\nCOMMAND RAN -> '.yn' ran by {interaction.user}")
    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.yn' ran by {interaction.user} at {datetime.now()}")
    f.close()

#   brawlstars


@client.tree.command(name="brawl-stats", description="[Dev] File reading test for BaguetteBot devs.")
async def brawlstats(interaction: discord.Interaction):
    await slash_log(interaction)
    num_lines = sum(1 for line in open(f"C:{S_SLASH}Users{S_SLASH}Draggie{S_SLASH}iCloudDrive{S_SLASH}iCloud~is~workflow~my~workflows{S_SLASH}Brawl Stars Counter.txt"))
    await interaction.response.send_message(f"I have opened Brawl Stars ***{num_lines}***  times since the 19th October 2020.")
    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.lines' ran by {interaction.user} at {datetime.now()}")
    f.close()


#   vbuck calc


@client.tree.command(name="vbucks", description="[Social] Calculates GBP -> V-Bucks")
@app_commands.describe(amount="Enter the amount of £££ that should be converted into vbonks", tier="Enter the tier of purchase. 1 is the cheapest V-Bucks option, wile 4 is the most expensive")
async def vbucks(interaction: discord.Interaction, amount: str, tier: Optional[int]):
    await slash_log(interaction)
    tier = 0 if tier is None else tier
    try:
        vAmount = (float(amount))
        gbp = amount
    except ValueError:
        return await interaction.response.send_message(f"Inappropriate integer: {amount}/{tier}")

    vTier1 = (float(154.083205))
    vTier2 = (float(175.109443))
    vTier3 = (float(192.381685))
    vTier4 = (float(210.970464))

    if tier == 1:
        vAmount = round(vTier1 * vAmount)
        await interaction.response.send_message(f"£{gbp} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 1 of vbuck purchase)")
        print(vAmount)
    if tier == 2:
        vAmount = round(vTier2 * vAmount)
        await interaction.response.send_message(f"£{gbp} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 2 of vbuck purchase)")
        print(vAmount)
    if tier == 3:
        vAmount = round(vTier3 * vAmount)
        await interaction.response.send_message(f"£{gbp} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 3 of vbuck purchase)")
        print(vAmount)
    if tier == 4:
        vAmount = round(vTier4 * vAmount)
        await interaction.response.send_message(f"£{gbp} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 4 of vbuck purchase)")
        print(vAmount)
    else:
        vAmount_LowerBounds = int(vTier1 * vAmount)
        vAmount_UpperBounds = int(vTier4 * vAmount)
        await interaction.response.send_message(f"£{gbp} may be between **{format(vAmount_LowerBounds, ',')}** and **{format(vAmount_UpperBounds, ',')}** V-Bucks depending on which V-Bucks package(s) you choose to buy")

#   Vbucks USD


@client.tree.command(name="vbucks-usd", description="[Social] Calculates USD -> V-Bucks")
@app_commands.describe(amount="Enter the amount of $$$ that should be converted into vbonks", tier="Enter the tier of purchase. 1 is the cheapest V-Bucks option, wile 4 is the most expensive")
async def vbucks_usd(interaction: discord.Interaction, amount: str, tier: Optional[int]):
    await slash_log(interaction)
    tier = 0 if tier is None else tier
    try:
        vAmount = (float(amount))
        usd = amount
    except ValueError:
        return await interaction.response.send_message(f"Inappropriate integer: {amount}/{tier}")

    vTier1usd = 125.156446
    vTier2usd = 140.070035
    vTier3usd = 156.298843
    vTier4usd = 168.771096

    if tier == 1:
        vAmount = round(vTier1usd * vAmount)
        await interaction.response.send_message(f"${usd} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 1 of vbuck purchase)")
        print(vAmount)
    if tier == 2:
        vAmount = round(vTier2usd * vAmount)
        await interaction.response.send_message(f"${usd} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 2 of vbuck purchase)")
        print(vAmount)
    if tier == 3:
        vAmount = round(vTier3usd * vAmount)
        await interaction.response.send_message(f"${usd} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 3 of vbuck purchase)")
        print(vAmount)
    if tier == 4:
        vAmount = round(vTier4usd * vAmount)
        await interaction.response.send_message(f"${usd} is equal to **{format(vAmount, ',')}** V-Bucks (using tier 4 of vbuck purchase)")
        print(vAmount)
    else:
        vAmount_LowerBounds = int(vTier1usd * vAmount)
        vAmount_UpperBounds = int(vTier4usd * vAmount)
        await interaction.response.send_message(f"${usd} may be between **{format(vAmount_LowerBounds, ',')}** and **{format(vAmount_UpperBounds, ',')}** V-Bucks depending on which V-Bucks package(s) you choose to buy")


@client.tree.command(name="settings", description="[Info] Edit a ton of the bot's settings here. [Ephemeral]")
async def settings(interaction: discord.Interaction):
    await slash_log(interaction)
    user_settings_json_path = f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json"
    # Check if the file exists
    if not os.path.isfile(user_settings_json_path):
        with open(user_settings_json_path, 'w') as f:
            json.dump(default_configfile, f)

    # Read the JSON file
    with open(user_settings_json_path, 'r') as f:
        settings = json.load(f)

    string = "This message has buttons!"

    embed = discord.Embed(title="BaguetteBot Settings", description="Use the buttons to interact and change these settings. These apply to all servers.")
    view = discord.ui.View()

    for key, value in settings['user_settings'].items():
        string = (f"{string}\n{key}: {value}")
        if key == "send_generalised_dms":
            key = "Send General DMs"
        if key == "get_dm_notification_for_role_addition":
            key = "Role Addition Messages"
        if key == "get_dm_notification_for_role_removal":
            key = "Role Removal Messages"
        if key == "get_dm_notification_for_coin_threshold":
            key = "Coin Amount Messages"
        if key == "reminders_for_voice_time":
            key = "Voice Time Coin Reminders"
        if key == "participate_in_experiments":
            key = "Allow User Experiments"
        if key == "can_use_shop_section_2":
            key = "View Shop Sections"
        if key == "contribute_to_statistics":
            key = "User Analytics"
        embed.add_field(name=key, value="🔴 Disabled" if value == "false" else "🟢 Enabled")

        style = discord.ButtonStyle.green if value == "true" else discord.ButtonStyle.red
        view.add_item(OptionButton(label=key, style=style))

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

#   vbuck calc


@client.tree.command(name="terms", description="[Info] Views the iBaguette Terms of Service which governs this bot.")
async def terms(interaction: discord.Interaction):
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="iBaguette Terms of Service", style=discord.ButtonStyle.link, url="https://terms.ibaguette.com"))
    view.add_item(discord.ui.Button(label="iBaguette Privacy Policy", style=discord.ButtonStyle.link, url="https://privacy.ibaguette.com"))
    await interaction.response.send_message("Press the button below to see iBaguette Terms of Service and Privacy Policy.", view=view, ephemeral=True)


@client.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(f"There was a generic client tree error when running that command.\n{error}\n{traceback.format_exc()}", ephemeral=True)
    else:
        await interaction.response.send_message(f"There was a generic client tree error when running that command.\n{error}", ephemeral=True)
        print(traceback.format_exc())
        raise error
    print(f"[Tree/ERROR]      {error}")


@client.tree.command(name="dev_settings", description="Dev settings panel")
async def dev_settings(interaction: discord.Interaction):
    # save_user_settings(interaction.user.id)
    await interaction.response.send_message("Done")


@client.tree.command(name="join", description="[Voice] Joins the Voice Channel you are in.")
async def join(interaction: discord.Interaction):
    if not interaction.guild:
        return await interaction.response.send_message("You can't use this command in DMs.")
    if interaction.user.voice is None or interaction.user.voice.channel is None:
        return await interaction.response.send_message("You aren't in a Voice Channel.")

    else:
        channel = interaction.user.voice.channel
        await channel.connect(cls=wavelink.Player)
        await interaction.response.send_message(f"Joined <#{channel.id}>")


@client.tree.command(name="play", description="[Voice] Plays/queues audio that you want in the current Voice Chat.")
@app_commands.describe(search="What YouTube video/Spotify track/playlist would you like to search for?", seek="Time in seconds you want to seek to?", dev_stuff="[DevMode] Load all types of Wavelink PlayableTrack args")
async def play(interaction: discord.Interaction, search: str, seek: Optional[int], dev_stuff: Optional[bool] = False):
    await slash_log(interaction)
    """Play a song with the given search query.

    If not connected, connect to our voice channel.
    """
    if dev_stuff:
        search = "https://www.youtube.com/watch?v=TseSndeG6pg"

    if interaction.user.voice is None:
        return await interaction.response.send_message("You're not in a voice channel! Please join one to use this command.", ephemeral=True)
    try:
        vc = interaction.guild.voice_client or await interaction.user.voice.channel.connect(cls=wavelink.Player)
        vc.autoplay = True
    except IndexError:
        return await interaction.response.send_message("Nodes are still being connected, please wait a minute...")
    except Exception:
        return await interaction.response.send_message("Can't get the nodes! Please wait a minute...")

    await interaction.response.defer()

    tracks = False

    vc.guild_interaction = interaction

    async def play_track(search_video, type: Optional[str] = None, offset: Optional[int] = False) -> None:
        print(f"[PlayCommand] [PlayTrack] Video title: {search_video}")
        if offset:
            print(f"Offset: {offset}s")
        total_duration = 0
        if type == "spotify_playlist": # Spotify playlists need special handling as there are multiple songs.
            # await interaction.followup.send(f"{EMOJI_LOADING} Processing...")
            for track in search_video:
                await play_track(track, type="processed_playlist")
                total_duration = total_duration + track.duration
            tracklen = len(tracks)
            remaining_tracks = len(vc.queue)
            string_to_send = (f'Added {tracklen} Spotify tracks to the queue. There are now {remaining_tracks} tracks in the queue. (~{await duration_to_time(round(total_duration))})')

            embed = discord.Embed(title="Added Tracks!", description=string_to_send)
            view = discord.ui.View()
            view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
            view.add_item(discord.ui.button(label="Next ▶️", style=discord.ButtonStyle.blurple))

            embed.set_footer(text=random.choice(["You can play YouTube playlists, Spotify playlists and more!", "You can queue as many tracks as you want!", "You can seek through tracks before they play my using the `seek` parameter in the Slash Command.", "You can change and lock volumes by using /volume.", "Use the buttons to pause, start, seek and cycle through the queue."]))
            embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else None, url="https://discord.com/invite/F5Vu9PhXMr")
            return await interaction.followup.send(embed=embed)

        if type == "yt_playlist": # YT playlists need special handling as there are multiple songs.
            for track in search_video.tracks:
                await play_track(track, type="processed_playlist")
                total_duration = total_duration + track.duration
            tracklen = len(search_video.tracks)
            remaining_tracks = len(vc.queue)

            string_to_send = (f'Added {tracklen} YouTube videos from the playlist into the queue. There are now {remaining_tracks} tracks in the queue. (~{await duration_to_time(round(total_duration/1000))})') # wavelink >v2 now in millis
            embed = discord.Embed(title="Added Tracks!", description=string_to_send)
            return await interaction.followup.send(embed=embed, ephemeral=True)

        # End of playlist content #

        # If the bot has been initialised by using /join

        if not hasattr(vc, "queue"):
            search_video: wavelink.YouTubeTrack = await wavelink.YouTubeTrack.search(search, return_first=True)
            print("Playing youtube track")
            vc.play(search_video)
            # await vc.play(search_video.source)
            await interaction.followup.send("Please use </play:1057428586761556090> to start playing sounds!", ephemeral=True)

        # If the bot isn't doing anything.

        if vc.queue.is_empty and not vc.is_playing(): # This is the most commonly used embed!
            volume = await get_server_voice_volume(interaction.guild_id)
            await vc.set_volume(volume)
            await vc.play(search_video)
            if offset:
                offset = ((int(offset)) * 1000)
                await vc.seek(offset)

            # See if the player is looping.

            looping = ""
            if vc.queue.loop:
                looping = "Looping current"
            if vc.queue.loop_all:
                looping = "Looping queue"
            else:
                looping = "Disabled"

            # Construct embed

            embed = discord.Embed(title="Now playing", description=f"[{search_video.title}]({search_video.uri})")
            try:
                embed.set_image(url=search_video.thumbnail)
            except Exception:
                embed.add_field(name="Thumbnail", value="<unable to get.>")

            embed.add_field(name="Creator", value=search_video.author)
            embed.add_field(name="Time Left", value=f"<t:{int(time.time()) + int(search_video.duration / 1000)}:R>")
            # embed.add_field(name="Time left", value=await duration_to_time(int(search_video.duration / 1000)))
            embed.add_field(name="Looping", value=looping)
            embed.add_field(name="Tracks Remaining", value=vc.queue.count)

            embed.set_footer(text=random.choice(["You can play YouTube playlists, Spotify playlists and more!", "You can queue as many tracks as you want!", "You can seek through tracks before they play my using the `seek` parameter in the Slash Command.", "You can change and lock volumes by using /volume.", "Use the buttons to pause, start, seek and cycle through the queue."]))
            embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else None, url="https://discord.com/invite/F5Vu9PhXMr")

            # Add the buttons

            view = discord.ui.View()
            view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))

            x = await interaction.followup.send(embed=embed, view=view)
            vc.play_controls_message = x

        # or else, the bot is playing something, we can put it into the queue.

        else:
            print("[PlayCommand]    Adding standard item to the queue")
            total_duration = 0
            for track in vc.queue:
                try:
                    if hasattr(track, "duration"): # Spotify tracks only
                        total_duration += track.length
                    else:
                        total_duration += track.client['info']['length']
                except Exception as e:
                    print(f"[ERROR] [PlayCommand]   Unable to get a good duration for {track}! {e}")
                    pass
            if not vc.current: # Check if not playing with queue
                ph = 0
            else:
                ph = vc.current.length
            total_duration = total_duration + ph - vc.last_position # Add the current track length
            print(total_duration)
            await vc.queue.put_wait(search_video)
            if not type == 'processed_playlist':
                return await interaction.followup.send(f'Successfully added ``{search_video.title}`` to the queue. This will play after **{len(vc.queue)}** more tracks have finished, which will be in **~{await duration_to_time(round(total_duration/1000))}**.', ephemeral=True) # wavelink >v2 time now millis

    # end of function play_track()

    if dev_stuff:
        try:
            string = ""
            await vc.set_volume(10)
            string = f"{string}\n[DevPlayCommand]    Volume set: success"
            print("[DevPlayCommand]    Initialising quick developer stuff")
            string = f"{string}\n[DevPlayCommand]    Initialising quick developer stuff"
            found_youtube_video_test_track: wavelink.YouTubeTrack = await wavelink.YouTubeTrack.search("https://www.youtube.com/watch?v=TseSndeG6pg", return_first=True)
            await play_track(found_youtube_video_test_track)
            print("[DevPlayCommand]    YouTube Track process successful")
            string = f"{string}\n[DevPlayCommand]    YouTube Track: success"

            spotify_test_track = await spotify.SpotifyTrack.search(query="https://open.spotify.com/track/61nFtmbCsaND1HZXGpieb0?si=6c3922890b94497a")
            await play_track(spotify_test_track)
            print("[DevPlayCommand]     Spotify Track process successful")
            string = f"{string}\n[DevPlayCommand]    Spotify Track: success"

            async for track in spotify.SpotifyTrack.iterator(query="https://open.spotify.com/playlist/0PBUTgtoa4crppyaqSXkNG?si=1c88a454b6ec4dbb"):
                await play_track(track)
            print("[DevPlayCommand]     Spotify Playlist process successful")
            string = f"{string}\n[DevPlayCommand]    Spotify Playlist: success"

            yt_playlist_test_tracks = await wavelink.YouTubePlaylist.search("https://www.youtube.com/playlist?list=PL5xtnB--9zERtoI-yN_t0YlWtaFmx10eu")
            await play_track(yt_playlist_test_tracks, "yt_playlist")
            print("[DevPlayCommand]     YouTube Playlist process successful")
            string = f"{string}\n[DevPlayCommand]    YouTube Playlist: success"

            return await interaction.followup.send(f"Looks like all tracks have been queued successfully. No errors have been detected with adding any type of track.```py\nTraceback: {traceback.format_exc()} (NoError)``` ```{string}```")
        except Exception as e:
            return await interaction.followup.send(f"```py\n{traceback.format_exc()}```\n> **{e}**")

    # End of added dev stuff.

    if "open.spotify.com/playlist" in search:
        print("[PlayCommand] Processing: Spotify Playlist")
        async for track in spotify.SpotifyTrack.iterator(query=search): # Needs some work still
            await play_track(track)
    elif "open.spotify.com/track" in search:
        print("[PlayCommand] Processing: Spotify Track")
        search = await spotify.SpotifyTrack.search(query=search, return_first=True)
        print("[PlayCommand] Spotify track process successful")
        return await play_track(search)

    elif "youtu" in search:
        node = wavelink.NodePool.get_node()
        if "playlist" in search:
            print("[PlayCommand]    Processing: YouTube Playlist")
            tracks = await wavelink.YouTubePlaylist.search(search)
            print(tracks)
            return await play_track(tracks, "yt_playlist")

        try:
            if "&" in search:
                print(f"[PlayCommand]   '&' detected in search string: {search}")
                search = search.split("&")[0]

            search_video = await node.get_tracks(cls=wavelink.Player, query=search) # do some cool fancy stuff to get the url

        except Exception as e:
            print(f"An error occurred: {e}")
            return await interaction.followup.send(f"An error occurred! Sorry about that. Here is the message: ```py\n{traceback.format_exc()}\n```\n> **{e}**")

        try:
            print("[PlayCommand]    Playing detected YouTube track")
            return await play_track((search_video[0]), None, seek)
        except IndexError:
            print(f"[PlayCommand]   Valid IndexError: No valid video found: {search}")
            return await interaction.followup.send(f"No valid video was found with the search term: {search}")
        except Exception as e:
            print(f"[PlayCommand]   Error: {e}")
            return await interaction.followup.send(f"An error occurred! Sorry about that. Here is the message: ```py\n{traceback.format_exc()}\n```\n> **{e}**")

    else:
        try:
            print(f"[PlayCommand]   Searching standard YouTube track for term: {search}")
            search_video: wavelink.YouTubeTrack = await wavelink.YouTubeTrack.search(search, return_first=True)
        except wavelink.exceptions.NoTracksError as e:
            print(f"[PlayCommand]   Valid IndexError: No valid video found: {search}")
            return await interaction.followup.send(f"There was no valid YouTube track for this search term. Please make sure the video is public.\n> `{e}`")
        except Exception as e:
            return await interaction.followup.send(f"An error occurred! Sorry about that. Here is the message: ```py\n{traceback.format_exc()}\n```\n> **{e}**")

    try:
        print(f"[PlayCommand]   Final try/except block entered for track: {search_video}")
        await play_track(search_video, None, seek)
    except Exception as e:
        print(f"[Error]     An error occurred: {e}")
        print(traceback.format_exc())
        return await interaction.followup.send(f"An error occurred! Sorry about that. Here is the message: ```py\n{traceback.format_exc()}\n```\n> **{e}**")


@client.tree.command(name="clearqueue", description="[Voice] Clear the current queue!")
async def clear_queue(interaction: discord.Interaction): # Not fully tested
    await slash_log(interaction)
    if not interaction.user.guild_permissions.manage_channels:
        return await interaction.response.send_message("You are missing the required guild persmission: `manage_channels`.", ephemeral=True, delete_after=10)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc:
        return await interaction.response.send_message("I am not in a voice channel! Use </play:1057428586761556090> to play a track.", ephemeral=True, delete_after=10)
    if not vc.queue:
        return await interaction.response.send_message("Nothing is queued! Use </play:1057428586761556090> to queue a track.", ephemeral=True, delete_after=10)
    else:
        await vc.queue.clear()
        return await interaction.response.send_message("Cleared all queued tracks.", delete_after=15)


@client.tree.command(name="filter", description="[Beta/Voice] Select and use special Voice Chat Sound Filters!")
@app_commands.describe(filter="Enter the string of the filter to add", dev_mode="enable dev mode?")
async def filter(interaction: discord.Interaction, filter: Optional[str] = None, dev_mode: Optional[bool] = False):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc or not vc.is_playing():
        return await interaction.response.send_message("Nothing is playing! Use </play:1057428586761556090> to play a track.", ephemeral=True, delete_after=10)
    await interaction.response.send_message("This command is currently work in progress and is scheduled to release in v1.4. Please check back later. You can check for updates on the support server: https://discord.gg/GfetCXH.", ephemeral=True, delete_after=10)


@client.tree.command(name="loop", description="[Voice] Loop the current audio, or all the queue.")
@app_commands.describe(queue="Want to loop the entire queue?")
async def loop(interaction: discord.Interaction, queue: Optional[bool] = False):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc or not vc.is_playing():
        return await interaction.response.send_message("Nothing is playing! Use </play:1057428586761556090> to play a track.", ephemeral=True, delete_after=10)
    if vc.guild.id not in TESTER_GUILD_IDS:
        return await interaction.response.send_message(f"{EMOJI_CROSS_ANIMATED} Sorry, but it looks like this server is not a Premium server. Please contact the developer if you believe this is an issue.", delete_after=10)
    if not vc or not vc.is_playing():
        return await interaction.response.send_message("Nothing is playing. Use </play:1057428586761556090> to play some stuff!", ephemeral=True)

    if not queue:
        if vc.queue.loop:
            vc.queue.loop = False
            return await interaction.response.send_message("Looping disabled.", delete_after=10)
        else:
            vc.queue.loop = True
            return await interaction.response.send_message("The current track has been set to loop.", delete_after=10)

    if queue:
        if vc.queue.loop_all:
            vc.queue.loop_all = False
            return await interaction.response.send_message("Looping all disabled.", delete_after=10)
        else:
            vc.queue.loop_all = True
            return await interaction.response.send_message("All tracks in the history queue have been set to loop.", delete_after=10)


@client.tree.command(name="seek", description="[Voice] Seeks to a position in the current track.")
@app_commands.describe(position="Enter the time in seconds to seek to")
async def seek(interaction: discord.Interaction, position: int):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc or not vc.is_playing():
        return await interaction.response.send_message("Nothing is playing! Queue tracks with </play:1057428586761556090>", ephemeral=True)
    await vc.seek(position * 1000)
    print(f"[SeekCommand]   Seeking to {position * 1000}ms")
    return await interaction.response.send_message(f"Seeked to {position*1000}ms.", delete_after=5)
    # return await interaction.response.send_message(f"Seeked to {position*1000}ms.")


@client.tree.command(name="shuffle", description="[Voice] Shuffles all queued tracks.")
async def shuffle(interaction: discord.Interaction):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if vc is None:
        return await interaction.response.send_message("There is nothing to shuffle. Add a track to the queue with ", ephemeral=True)
    random.shuffle(vc.queue._queue)
    await interaction.response.send_message("The queue has been shuffled. Now you don't know what will be played next ;)", delete_after=15)
    print(vc.queue._queue)


@client.tree.command(name="queue", description="[Voice] Get details about the queue.") # migrated
async def queue(interaction: discord.Interaction):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if not vc:
        return await interaction.response.send_message("There is no current voice chat activity in this guild.", ephemeral=True)
    embed = discord.Embed(title=f"Queue for {interaction.guild.name} ({len(vc.queue)} songs)")
    embed.add_field(name="• Currently Playing", value=f"**{vc._source.title}** ({await duration_to_time(vc._source.length)})", inline=False)
    if vc.queue._queue[0] is not None:
        embed.add_field(name="• Next up", value=f"{vc.queue._queue[0]}", inline=False)
    else:
        embed.add_field(name="• Next up", value="Nothing yet.")
    embed.add_field(name="• Settings", value=f"Volume: {vc.volume}% | Playing from: <@{client._BotBase__tree.client.application_id}> | Latency: {round(client.latency * 1000, 4)}ms", inline=False)
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="skip", description="[Voice] Skips the current track playing.")
async def skip(interaction: discord.Interaction):
    await slash_log(interaction)
    vc: wavelink.Player = interaction.guild.voice_client
    if vc is not None:
        if not vc.queue.is_empty:
            await vc.stop()
            total_duration = 0
            for track in vc.queue:
                total_duration += track.duration
            await interaction.response.send_message(f"Now playing: **{vc.queue[0]}**. There are {len(vc.queue)-1} songs left.")
        else:
            await vc.stop()
            await interaction.response.send_message("No songs remain in the queue. Stopped the player.")
    else:
        await interaction.response.send_message("I'm not in a Voice Channel.")


"""@client.tree.command(name="purge", description="[Utility] Purges a specified amount of messages")
async def purge(interaction: discord.Interaction, amount: int):
    if interaction.user.id == 382784106984898560:
        current_time_for_deletes = time.time()
        async for message in interaction.message.channel.history(limit=amount):
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
        await interaction.channel.purge(limit=amount, oldest_first=True)
        await interaction.response.send_message(f"Deleted {amount} message!")

        f = open(GlobalLogDir, "a")
        f.write(f"\nCOMMAND RAN -> '.purge' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")
        f.close()
        print(f"\nCOMMAND RAN -> '.purge' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")
        return
    else:
        await interaction.response.send_message("You don't have permissions for that u sussy boi")
"""

@client.tree.command(name="uwu", description="UwU")
@commands.has_any_role('Admin', 'Mod')
async def uwu(interaction: discord.Interaction):
    return await interaction.response.send_message("UwU!\n*why was I asked to make this command*")

###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

print("All Slash Commands initialised.")

print("Initialising Lavalink and music functions...")


async def get_server_voice_volume(guild_id: int) -> int:
    """Returns the volume of a guild chosen by its members.\n
    Must include parameter of the guild id\n
    Returns an percentage as an integer. You can divide this by 100 if you want a float."""
    if not os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt"):
        os.makedirs(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences", exist_ok=True)
        with open(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'w+') as f:
            f.write(str(VOICE_VOLUME))
    with open(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'r') as file:
        volume = file.read()
    print(f"[VoiceVolQuery]      Server {guild_id} has a volume of {volume}%")
    return int(volume)


async def connect_nodes():
    """Connect to our Lavalink nodes."""
    await client.wait_until_ready()
    node: wavelink.Node = wavelink.Node(uri='http://localhost:2333', password='youshallnotpass')
    print("[Wavelink] Connecting nodes")
    await wavelink.NodePool.connect(client=client, nodes=[node], spotify=spotify.SpotifyClient(client_id=spotify_client_id, client_secret=spotify_id))


async def on_wavelink_node_ready(node: wavelink.Node):
    """Event fired when a node has finished connecting."""
    print(f"Node: <{node}> is ready!")


async def on_wavelink_track_end(vc: wavelink.Player, track: Optional[str] = None, reason: Optional[str] = None):
    if reason == "REPLACED":
        return
    if reason == "LOAD_FAILED":
        print("Load failed")

    interaction = vc.player.guild_interaction

    if len(vc.player.queue._queue) == 0: # If there is no more tracks in the queue
        if hasattr(vc.player, "loop"): # there might be looping in the queue
            if vc.player.loop or vc.player.loop_all:
                # return await interaction.followup.send(content="Looping track!", ephemeral=True)
                print("Looping track!")
        if hasattr(vc.player.queue, "loop"):
            if vc.player.queue.loop or vc.player.queue.loop_all:
                # return await interaction.followup.send(content="Looping track!", ephemeral=True)
                print("Looping all tracks!")

        if not vc.reason or vc.reason == "STOPPED":
            return await interaction.followup.send(content="Finished playing all audio!", ephemeral=True)

        # await interaction.delete_original_response()
        return await interaction.followup.send(content="Finished playing all audio!")

    next_track = vc.player.queue._queue[0]
    embed = discord.Embed(title="[on_wavelink_track_end] Edited Playing track", description=f"[{next_track.title}]({next_track.uri})")

    try:
        if hasattr(next_track, "images"):
            embed.set_image(url=next_track.images[0]) # Spotify images
        else:
            embed.set_image(url=next_track.thumbnail)
    except Exception as e:
        print(e)
        embed.add_field(name="Thumbnail", value="<unable to get.>")

    previous_item = await get_wavelink_queue_previous_item(vc)
    if hasattr(next_track, "artists"):
        artists_str = ', '.join(previous_item.artists)
    else:
        artists_str = next_track.author

    # Check if the queue is looping

    looping = ""
    if hasattr(vc, "loop"):
        if vc.queue.loop:
            looping = "Looping current"
        if vc.queue.loop_all:
            looping = "Looping queue"
        else:
            looping = "Disabled"
    else:
        try:
            if vc.player.queue.loop:
                looping = "Looping current"
            if vc.player.queue.loop_all:
                looping = "Looping queue"
            else:
                looping = "Disabled"
        except Exception as e:
            print(e)
            looping = "Unknown"

    embed.add_field(name="Creator", value=artists_str)
    embed.add_field(name="Real Time Left", value=f"<t:{int(time.time()) + int(previous_item.duration / 1000)}:R>")
    # embed.add_field(name="Time left", value=await duration_to_time(int((next_track.duration / 1000)))) # Wavelink >v2: Duration is now in millis
    embed.add_field(name="Looping", value=looping)
    embed.add_field(name="Tracks Remaining", value=await get_wavelink_queue_length(vc))
    embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else None, url="https://discord.com/invite/F5Vu9PhXMr")
    embed.set_footer(text=random.choice(["You can play YouTube playlists, Spotify playlists and more!", "You can queue as many tracks as you want!", "You can seek through tracks before they play my using the `seek` parameter in the Slash Command.", "You can change and lock volumes by using /volume.", "Use the buttons to pause, start, seek and cycle through the queue."]))

    view = discord.ui.View()
    view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
    view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.green))
    view.timeout = None

    await interaction.edit_original_response(embed=embed, view=view)


async def get_wavelink_queue_previous_item(player):
    """
    Returns the last track in the queue for simplicity\n
    Returns `None` if nothing there.
    """
    if hasattr(player, "queue"): # catches wavelink stopped events
        if len(player.queue._queue) == 0:
            return None
        else:
            return player.queue._queue[0]
    else:
        if len(player.player.queue._queue) == 0:
            return None
        else:
            return player.player.queue._queue[0]


async def get_wavelink_queue_length(player):
    """
    Returns the length of the queue for simplicity\n
    """
    if hasattr(player, "queue"):
        if len(player.queue._queue) == 0:
            return None
        else:
            return len(player.queue._queue)
    else:
        if len(player.player.queue._queue) == 0:
            return None
        else:
            return len(player.player.queue._queue)


async def get_wavelink_queue_next_item(player):
    """
    Returns the last track in the queue for simplicity\n
    Returns `None` if nothing there.
    """
    if len(player.queue._queue) == 0:
        return None
    else:
        return player.queue._queue[0]


print("Initialising Discord.py v2 Button classes...")


class CoinsButtons2(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle):
        super().__init__(label=label, style=style)

    async def callback(self, interaction):
        view = discord.ui.View()
        view.timeout = None

        # Coin balance

        coinBal = await get_coins(interaction.guild_id, interaction.user.id)
        nolwennium_bal = await get_nolwennium(interaction)
        view = discord.ui.View()

        if self.label == "View Page 2":
            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {EMOJI_COINS} coins and {nolwennium_bal} {EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)

            base_json = {
                'currentBoosts': [],
                'used_boosts': 0,
            }

            current_boosts_path = f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Coins{S_SLASH}{interaction.user.id}_boosted.json"
            if os.path.isfile(current_boosts_path):
                with open(current_boosts_path, 'r') as boosts_file:
                    boosts_json = json.load(boosts_file)
                    boosts_file.close()

                    # Remove expired boosts
                    current_time = datetime.now()
                    current_boosts = []
                    for boost in boosts_json['currentBoosts']:
                        expiration_time = datetime.strptime(boost['expirationTime'], '%Y-%m-%d %H:%M:%S.%f')
                        if expiration_time > current_time:
                            current_boosts.append(boost)
                    boosts_json['currentBoosts'] = current_boosts

                    # Display currently active boosts
                    if len(current_boosts) > 0:
                        active_boosts_string = '\n'.join([f"{boost['name']} ({boost['multiplier']}x) until {boost['expirationTime']}" for boost in current_boosts])
                        embed.add_field(
                            name="Currently active Boosts",
                            value=active_boosts_string,
                            inline=False
                        )

            # Define the available boosts
            boosts = [
                {
                    'name': '2x Coins for 1 hour',
                    'multiplier': 3,
                    'duration': 1,
                    'unit': 'hours',
                    'price': 50
                },
                {
                    'name': '2x Coins for 1 day',
                    'multiplier': 2,
                    'duration': 1,
                    'unit': 'days',
                    'price': 100
                },
                {
                    'name': '3x Coins for 7 days',
                    'multiplier': 5,
                    'duration': 7,
                    'unit': 'days',
                    'price': 1500
                },
                # Add more boosts here
            ]

            # Display available boosts
            available_boosts_string = '\n'.join([f"{boost['name']} ({boost['multiplier']}x) for {boost['duration']} {boost['unit']} - {boost['price']} coins" for boost in boosts])

            for i in boosts:
                embed.add_field(
                    name=i["name"],
                    value=f"Multiplier: {i['multiplier']}x\nDuration: {i['duration']} {i['unit']}\n**Price: {i['price']} Coins**",
                    inline=False
                )

            # Add buttons for each available boost
            for boost in boosts:
                button_label = f"{boost['name']}"
                view.add_item(CoinsButtons2(style=discord.ButtonStyle.blurple, label=button_label))

            embed.set_footer(text=('Use the buttons below to buy what you want.'))

            await interaction.response.edit_message(embed=embed, view=view)

        if self.label == "2x Coins for 1 day":
            data = {
                'name': '2x Coins for 1 day',
                'multiplier': 2,
                'duration': 1,
                'unit': 'days',
                'price': 100
            }

            # Load the current boosts from the JSON file
            current_boosts_path = f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Coins{S_SLASH}{interaction.user.id}_boosted.json"
            boosts_json = {'currentBoosts': []}
            if os.path.isfile(current_boosts_path):
                with open(current_boosts_path, 'r') as boosts_file:
                    boosts_json = json.load(boosts_file)
                    boosts_file.close()

            # Check if the user has enough coins to purchase the boost
            if coinBal < data['price']:
                await interaction.response.send_message(f"You don't have enough coins to purchase this boost. You need {data['price'] - coinBal} more.", ephemeral=True)
                return

            # Calculate the expiration time for the boost
            current_time = datetime.now()
            if data['unit'] == 'seconds':
                expiration_time = current_time + datetime.timedelta(seconds=data['duration'])
            elif data['unit'] == 'minutes':
                expiration_time = current_time + datetime.timedelta(minutes=data['duration'])
            elif data['unit'] == 'hours':
                expiration_time = current_time + datetime.timedelta(hours=data['duration'])
            elif data['unit'] == 'days':
                expiration_time = current_time + datetime.timedelta(days=data['duration'])
            else:
                # Handle unknown boost unit
                expiration_time = current_time

            # Add the boost to the currentBoosts list in the JSON file
            boosts_json['currentBoosts'].append({
                'name': data['name'],
                'multiplier': data['multiplier'],
                'expirationTime': expiration_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            })

            # Deduct the price of the boost from the user's coins
            coinBal -= data['price']

            # Save the updated JSON file and update the embed and view
            with open(current_boosts_path, 'w') as boosts_file:
                json.dump(boosts_json, boosts_file)
                boosts_file.close()

            update_coins(interaction.guild_id, interaction.user.id, data['price'])

            await interaction.response.send_message(f"You have purchased the **{data['name']}** boost! You will now earn {data['multiplier']}x multiplier!")


class PlayButton(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, disabled: Optional[bool] = False, emoji: Optional[discord.PartialEmoji] = None):
        super().__init__(label=label, style=style, disabled=disabled, emoji=emoji)

    async def callback(self, interaction):
        view = discord.ui.View()
        view.timeout = None
        if not interaction.user.voice:
            return await interaction.response.send_message(content="You must be in the voice chat in order to use the music buttons!", ephemeral=True)
        vc = interaction.guild.voice_client or await interaction.user.voice.channel.connect(cls=wavelink.Player)
        if not vc:
            return await interaction.response.send_message("There is no active player in this guild", ephemeral=True)
        embed = None

        await interaction.response.defer() # do this to fix button not working - as seen in discord.py server: https://canary.discord.com/channels/336642139381301249/1094719114473381979/1095232120978411652

        vc.just_skipped = False # this is used to precent the embed message being edited multiple times if a skip has occurred due to it stopping, which triggers on_wavelink_track_end and also occurs at the end of this function

        # Button: Pause/Play alternating.

        if self.label == "Pause":
            if not vc._paused:
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple, disabled=True))
                view.add_item(PlayButton(label="Resume", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple, disabled=True))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple, disabled=True))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple, disabled=True))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple, disabled=True))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple, disabled=True))
                await vc.pause()
                # await interaction.response.edit_message(view=view)
            else:
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Resume", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                await vc.resume()
        elif self.label == "Resume":
            if vc._paused:
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                await vc.resume()
                # await interaction.response.edit_message(view=view)

        # Button: Skipping

        elif self.label == "Skip ▶️":
            view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
            if hasattr(vc, 'isPlayingFromQueue') and hasattr(vc, 'isPlayingFromQueue'):
                vc.isPlayingFromQueueLength = vc.isPlayingFromQueueLength - 1
                if vc.isPlayingFromQueue:
                    try:
                        await vc.play(vc.queue.history._queue[(len(vc.queue.history._queue)) - vc.isPlayingFromQueueLength])
                    except IndexError:
                        await vc.stop()
                        vc.isPlayingFromQueue = False
                else:
                    vc.just_skipped = True
                    await vc.stop()
                    await interaction.channel.send("Skipped audio.", delete_after=5)

            else:
                vc.just_skipped = True
                await vc.stop()
                await interaction.channel.send("Skipped audio.", delete_after=5)

        # Button: Restart

        elif self.label == "Restart":
            if vc.is_playing:
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                await vc.seek(0)
            else:
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.red))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                await vc.seek(0)

        # Button: Skip 10 seconds

        elif self.label == "+10s":
            if vc.is_playing():
                currentPos = vc.position
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                # print(f"[dev] currentPos: {await duration_to_time(currentPos)}")
                await vc.seek((currentPos + 10000)) # Wavelink v2: Positions are now in millis.

        # Button: Minus 10 seconds

        elif self.label == "-10s":
            if vc.is_playing():
                currentPos = vc.position
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                if currentPos - 10 <= 0:
                    await vc.seek(0)
                else:
                    await vc.seek((currentPos - 10000)) # Wavelink v2: Positions are now in millis.

        # Button: Shuffling

        elif self.label == "Shuffle":
            if vc.is_playing():
                currentPos = vc.position
                view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
                view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.green))
                view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
                vc: wavelink.Player = interaction.guild.voice_client
                if vc is None:
                    return await interaction.followup.send("There is nothing to shuffle")
                random.shuffle(vc.queue._queue)
                return await interaction.followup.send(f"{EMOJI_TICK_ANIMATED} Shuffled the **{len(vc.queue)}** queued tracks.", ephemeral=True)

        # Button: Previous

        elif self.label == "◀️ Previous": # !!! Sometimes this will replay the existing track. Need stack trace to fix it. I don't know why.
            vc.isPlayingFromQueue = True
            if hasattr(vc, 'isPlayingFromQueueLength'):
                if vc.isPlayingFromQueueLength <= 0:
                    vc.isPlayingFromQueueLength = 1
                vc.isPlayingFromQueueLength = vc.isPlayingFromQueueLength + 1
            else:
                vc.isPlayingFromQueueLength = 1
            try:
                await vc.play(vc.queue.history._queue[(len(vc.queue.history._queue)) - vc.isPlayingFromQueueLength])
            except IndexError: # catch dequeue index out of range!
                return await interaction.response.send_message(content="There is nothing behind this item in the queue.", ephemeral=True)
            except Exception as e:
                await interaction.channel.send(f"An error occurred! Sorry about that. Resetting queue. Here is the message: ```py\n{traceback.format_exc()}\n```\n> **{e}**")
                vc.isPlayingFromQueueLength = 0
                vc.isPlayingFromQueue = False
            view.add_item(PlayButton(label="◀️ Previous", style=discord.ButtonStyle.green))
            view.add_item(PlayButton(label="Pause", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Restart", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="-10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="+10s", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Shuffle", style=discord.ButtonStyle.blurple))
            view.add_item(PlayButton(label="Skip ▶️", style=discord.ButtonStyle.blurple))
            x = vc.queue.history._queue
            print(len(x))
            for i in x:
                print(i)

        if not vc.just_skipped:
            if not vc.current:
                return await interaction.response.edit_message(content="Finished playing.")
            embed = discord.Embed(title="Playing track", description=f"[{vc.current.title}]({vc.current.uri})")
            try:
                embed.set_image(url=vc._current.thumbnail)
                print("...")
            except Exception:
                embed.add_field(name="Thumbnail", value="<unable to get from current interaction url>")

            # Check if looping is enabled

            looping = ""
            if vc.queue.loop:
                looping = "Looping current"
            if vc.queue.loop_all:
                looping = "Looping queue"
            else:
                looping = "Disabled"

            # Construct embed

            embed.add_field(name="Creator", value=vc.current.author)
            embed.add_field(name="Real Time Left", value=f"<t:{int(time.time()) + (int(vc.current.duration / 1000) - int(vc.last_position / 1000))}:R>")
            # embed.add_field(name="Time left", value=await duration_to_time(int((vc.current.duration / 1000) - (vc.last_position / 1000)))) # Wavelink >v2: Duration is now in millis
            embed.add_field(name="Looping", value=looping)
            embed.add_field(name="Tracks Remaining", value=vc.queue.count)
            embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else None, url="https://discord.com/invite/F5Vu9PhXMr")
            embed.set_footer(text=random.choice(["You can play YouTube playlists, Spotify playlists and more!", "You can queue as many tracks as you want!", "You can seek through tracks before they play my using the `seek` parameter in the Slash Command.", "You can change and lock volumes by using /volume.", "Use the buttons to pause, start, seek and cycle through the queue."]))
            # view.add_item(PlayButton(label="info: unknown event", style=discord.ButtonStyle.red, disabled=True))

            await interaction.followup.edit_message(embed=embed, view=view, message_id=interaction.message.id)
        else:
            print("Not doing anything - just skipped!")


class AcceptToSButtons(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle):
        super().__init__(label=label, style=style)

    async def callback(self, interaction):
        if not os.path.isfile(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json"):
            first_save_user_settings(interaction.user.id)
        with open(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json", 'r') as f:
            settings = json.load(f)
        with open(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json", 'w') as f:
            settings['accepted_tos'] = 'true'
            json.dump(settings, f)
            await interaction.response.edit_message(content="iBaguette Terms of Service have been accepted! Please rerun the command. To change your preferences, use `/settings`.")
            return print(f"> [TermsAccepted]  ToS accepted by {interaction.user.id}. They can now run Slash Commands. Event occurred at {datetime.now()}")


async def slash_log(interaction):
    print(f"/ [SlashCommand]   {interaction.data['name']} ran by {interaction.user.id} ({interaction.user.name} at {datetime.now()})")
    if not os.path.isfile(f"{BASE_DIR}Users\\JSONSettings{S_SLASH}{interaction.user.id}.json"):
        view = discord.ui.View()
        view.add_item(AcceptToSButtons(label="Accept ToS", style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="View ToS", style=discord.ButtonStyle.link, url="https://terms.ibaguette.com/#discord-bots"))
        return await interaction.response.send_message("You must accept the iBaguette Terms of Service and BaguetteBot supplemental Terms of Service once before using a Slash Command.", view=view, ephemeral=True)
    else:
        with open(f"{BASE_DIR}Users\\JSONSettings{S_SLASH}{interaction.user.id}.json", 'r') as json_file:
            json_data = json.load(json_file)
            if not json_data['accepted_tos'] == 'true':
                view = discord.ui.View()
                view.add_item(AcceptToSButtons(label="Accept ToS", style=discord.ButtonStyle.success))
                view.add_item(discord.ui.Button(label="View ToS", style=discord.ButtonStyle.link, url="https://terms.ibaguette.com/#discord-bots"))
                return await interaction.response.send_message("You must accept the iBaguette Terms of Service and BaguetteBot supplemental Terms of Service once before using a Slash Command.", view=view, ephemeral=True)
            else:
                pass
    with open(GlobalLogDir, 'a', encoding="utf-8") as file:
        file.write(f"/ [SlashCommand]      {interaction.data['name']} ran by {interaction.user.id} ({interaction.user.name} at {datetime.now()})\n")


class SusButton(discord.ui.Button): # For the GPT interaction
    def __init__(self, label: str, style: discord.ButtonStyle):
        super().__init__(label=label, style=style)

    async def callback(self, interaction):
        user_id = interaction.user.id
        if os.path.isfile(f"Z:\\{user_id}_gpt.txt"):
            with open(f"Z:\\{user_id}_gpt.txt", 'r') as f:
                content = f.read()
                view = discord.ui.View()
                # view.add_item(SusButton(label="See Sussiness", style=discord.ButtonStyle.red))
                await interaction.response.edit_message(content=content, view=view)


class OptionButton(discord.ui.Button): # For the settings interaction
    def __init__(self, label: str, style: discord.ButtonStyle):
        super().__init__(label=label, style=style)

    async def callback(self, interaction):
        with open(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json", 'r') as f:
            settings = json.load(f)

        def enableanddisable(self, text: str):
            if settings['user_settings'][text] == "false":
                print(f"/ [UserSettings] {text} is being changed to True for user {interaction.user.id}")
                settings['user_settings'][text] = "true"
            elif settings['user_settings'][text] == "true":
                print(f"/ [UserSettings] {text} is being changed to False for user {interaction.user.id}")
                settings['user_settings'][text] = "false"

            with open(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json", 'w') as f:
                json.dump(settings, f)

        if self.label == "Send General DMs":
            enableanddisable(self, "send_generalised_dms")
        if self.label == "Role Addition Messages":
            enableanddisable(self, "get_dm_notification_for_role_addition")

        if self.label == "Role Removal Messages":
            enableanddisable(self, "get_dm_notification_for_role_removal")
        if self.label == "Coin Amount Messages":
            enableanddisable(self, "get_dm_notification_for_coin_threshold")

        if self.label == "Voice Time Coin Reminders":
            enableanddisable(self, "reminders_for_voice_time")
        if self.label == "Allow Bot Experiments":
            enableanddisable(self, "participate_in_experiments")

        if self.label == "View Shop Sections":
            enableanddisable(self, "can_use_shop_section_2")
        if self.label == "Contribute to Statistics":
            enableanddisable(self, "can_use_shop_section_2")

        string = "This message has buttons!"

        with open(f"{BASE_DIR}Users{S_SLASH}JSONSettings{S_SLASH}{interaction.user.id}.json", 'r') as f:
            settings = json.load(f)

        embed = discord.Embed(title="BaguetteBot Settings", description="Use the buttons to interact and change these settings. These apply to all servers.")
        view = discord.ui.View()
        for key, value in settings['user_settings'].items():
            string = (f"{string}\n{key}: {value}")
            if key == "send_generalised_dms":
                key = "Send General DMs"
            if key == "get_dm_notification_for_role_addition":
                key = "Role Addition Messages"
            if key == "get_dm_notification_for_role_removal":
                key = "Role Removal Messages"
            if key == "get_dm_notification_for_coin_threshold":
                key = "Coin Amount Messages"
            if key == "reminders_for_voice_time":
                key = "Voice Time Coin Reminders"
            if key == "participate_in_experiments":
                key = "Allow Bot Experiments"
            if key == "can_use_shop_section_2":
                key = "View Shop Sections"
            if key == "contribute_to_statistics":
                key = "User Analytics"

            embed.add_field(name=key, value="🔴 Disabled" if value == "false" else "🟢 Enabled")
            style = discord.ButtonStyle.green if value == "true" else discord.ButtonStyle.red
            view.add_item(OptionButton(label=key, style=style))

        await interaction.response.edit_message(embed=embed, view=view)


print("Done! Defining functions")


async def StatusAutoUpdator():
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    await client.change_presence(activity=discord.Game(name=(f"/help | {servers} servers, {members} users | CPU {cpuPercentage}% + RAM {memoryUsage}% | {DRAGGIEBOT_VERSION}{BUILD}")))
    print(f"[SelfStatus]        /help | {servers} servers, {members} users | CPU {cpuPercentage}% + RAM {memoryUsage}% | {DRAGGIEBOT_VERSION}{BUILD}")
    # await asyncio.sleep(random.randint(100,500))
    await bot_runtime_events(1)
    await asyncio.sleep(60)
    await StatusAutoUpdator()


async def wip_command():
    messages_sent = 0
    messages_received = 0

    def save_to_json():
        global messages_sent, messages_received
        current_day = datetime.now().day
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
                last_day = data["day"]
                if last_day != current_day:
                    data = {
                        "messages_sent": messages_sent,
                        "messages_received": messages_received,
                        "time_spent_voice": time_spent_voice(),
                        "day": current_day
                    }
                    messages_sent = 0
                    messages_received = 0
                    with open("data.json", "w") as json_file:
                        json.dump(data, json_file)
        except Exception:
            data = {
                "messages_sent": messages_sent,
                "messages_received": messages_received,
                "time_spent_voice": time_spent_voice(),
                "day": current_day
            }
            messages_sent = 0
            messages_received = 0
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)

    schedule.every(1).minutes.do(save_to_json)

    while True:
        schedule.run_pending()
        time.sleep(1)

async def get_user_settings(user_id) -> dict:
    """Returns a JSON dict with the user's settings."""
    if os.path.isfile(f"{BASE_DIR}Users\\JSONSettings{S_SLASH}{user_id}.json"):
        with open(f"{BASE_DIR}Users\\JSONSettings{S_SLASH}{user_id}.json", "r") as file:
            json_data = json.load(file)

        if json_data['accepted_tos'] == 'true':
            settings = json_data['user_settings']
            return settings
        else:
            return None
    else:
        print(f"[GetUserSettings]   No valid user settings file for user id {user_id}")
        first_save_user_settings(user_id)
        await get_user_settings(user_id)

# Define the default file layout
default_configfile = {
    "user_settings": {
        "send_generalised_dms": "false",
        "get_dm_notification_for_role_addition": "false",
        "get_dm_notification_for_role_removal": "false",
        "get_dm_notification_for_coin_threshold": "false",
        "reminders_for_voice_time": "false",
        "participate_in_experiments": "false",
        "can_use_shop_section_2": "false",
        "contribute_to_statistics": "true",
    },
    "accepted_tos": "false",
    "config_version": "1",
}


# Function to save the user settings to a JSON file
def first_save_user_settings(user_id):
    # Read the existing JSON file, if it exists
    filepath = f"{BASE_DIR}Users\\JSONSettings{S_SLASH}{user_id}.json"
    # Read the JSON file
    if not os.path.exists(filepath):
        # Create the file with default values
        with open(filepath, 'w') as f:
            json.dump(default_configfile, f)
    else:
        os.remove(filepath)
        with open(filepath, 'w') as f:
            json.dump(default_configfile, f)


async def handleLeaveVoiceChat(ctx):
    voice_client = ctx.guild.voice_client
    if not voice_client:
        await ctx.send("Nothing to leave.")


def nolwenniumUserDirectory(ctx):
    nolwenniumUserDir = f"{BASE_DIR}Nolwennium{S_SLASH}{ctx.user.id}.txt"
    return nolwenniumUserDir


async def get_nolwennium(ctx):
    nolwenniumUserDir = nolwenniumUserDirectory(ctx)
    with open(nolwenniumUserDir, 'r') as f:
        nolwennium_balance = f.read()
        f.close()
    return nolwennium_balance


async def get_coins(server_id: int, user_id: int) -> int:
    """Gets a user's coins. The `server_id` and `user_id` as integers must be provided."""
    coin_dir = f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins{S_SLASH}{user_id}.txt"
    if not os.path.exists(coin_dir):
        return None
    with open(coin_dir, 'r') as f:
        balance = int(f.read())
    print(f"[CoinsQuery]    Balance called for {user_id} in {server_id}. (Balance: {balance})")
    return balance


def update_coins(server_id: int, user_id: int, coins_calc: int) -> int:
    """Gets then updates a user's coins. The `server_id` and `user_id` as integers must be provided.\n
    The amount of coins to add/subtract as an integer must be added too.\n
    Returns new amount of Coins."""
    coin_dir = f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins{S_SLASH}{user_id}.txt"
    if not os.path.exists(f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins"):
        os.makedirs(f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins")
    multiplication_amount = 1
    if os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins{S_SLASH}{user_id}_boosted.json"):
        with open(f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins{S_SLASH}{user_id}_boosted.json", 'r') as f:
            info = json.load(f)
            expiration_time = info['currentBoosts'][0]['expirationTime']
            expiration_datetime = datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f')
            # Compare the expiration time to the current time
            if expiration_datetime > datetime.now():
                # The boost is still active
                multiplication_amount = info['currentBoosts'][0]['multiplier']
            else:
                os.remove(f"{BASE_DIR}Servers{S_SLASH}{server_id}{S_SLASH}Coins{S_SLASH}{user_id}_boosted.json")
                print(f"[CoinsUpdate]       Removed User Bonus File for user {user_id}")
    mode = 'r+' if os.path.exists(coin_dir) else 'w+'

    with open(coin_dir, mode) as file:
        balance = int(file.read()) if mode == "r+" else 0
        print(f"[CoinsUpdate]       Balance queried for {user_id} in {server_id}. (Balance: {balance})")
        new_balance = balance + (coins_calc * multiplication_amount)
        print(f"[CoinsUpdate]       The new balance for {user_id} is {new_balance}.")
        file.seek(0)
        file.write(str(new_balance))
    return new_balance


async def bot_runtime_events(event_int):
    global bot_events
    bot_events = bot_events + event_int


class error_messages:
    codes = [
        ["You do not have the facilities to use this, big man", "You don't have the correct permissions", "[Error 1] You do not have the required permissions", "You can't run this command."],
        ["A critical error occured and this command cannot continue [this server is not compatible with this command]", ""],
        ["Critical error whilst in Voice Chat"]
    ]


async def error_code(interaction, code: int, *note: str, **raw_error: Exception):
    if note:
        print(f"A manual error was encountered and here is the information: {note}")
    embed = discord.Embed()
    random_cry = ['<:AmberCry:828577834146594856>', '<:BibiByeBye:828683852939395072>', '<:ColetteCry:828683829631516732>', '<:JessieCry:828683805861740654>', '<:SpikeCry:828683779206807622>', '<:SurgeCry:828683755694063667>', '<:TaraCry:828683724286853151>']

    embed = discord.Embed(
        title=(f"{random.choice(random_cry)} An error occured"),
        description=f"**{str(random.choice(error_messages.codes[code]))}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.",
        color=0x990000)

    try:
        await interaction.response.send_message(embed=embed)
    except app_commands.errors.CommandInvokeError:
        await interaction.followup.send(embed=embed)

    if raw_error:
        with open(f"{BASE_DIR}errors.txt", "a") as f:
            f.write(f"\nERROR: An error occured! Original command initialised by {interaction.user} at {datetime.now()}. ERROR MESSAGE: {str(raw_error)}")


async def get_current_seconds_bandwidth() -> list:
    """
    Gets network bandwidth used in the last second. Useful for seeing if the network is being throttled.\n
    Returns a list, index `0` is Uploaded Megabytes, index `1` is Downloaded Megabytes.
    """

    # Store the previous values for comparison
    prev_net_data = psutil.net_io_counters(pernic=False, nowrap=True)

    # Wait for one second
    await asyncio.sleep(1)

    # Get the current network data
    net_data = psutil.net_io_counters(pernic=False, nowrap=True)

    # Calculate the network usage over the last second
    bytes_sent = net_data.bytes_sent - prev_net_data.bytes_sent
    bytes_recv = net_data.bytes_recv - prev_net_data.bytes_recv

    # Convert the usage to megabytes
    megabytes_sent = (bytes_sent / 1024 / 1024) * 10
    megabytes_recv = (bytes_recv / 1024 / 1024) * 10

    print("Total network usage:")
    print(f"Megabytes sent: {megabytes_sent}")
    print(f"Megabytes received: {megabytes_recv}")
    return [f"{megabytes_sent}", f"{megabytes_recv}"]


async def duration_to_time(duration: int, format: Optional[int] = None) -> str:
    """
    Enter the duration in seconds as the argument and the function
    will return a prettified string based on the time :)\n
    e.g. 23 hours 6 minutes, 4 minutes 45 seconds, etc.
    """
    print(f"[FunctionUsed]  'duration_to_time(duration:{duration})' used.")
    # Convert duration to seconds
    seconds = int(duration)

    # If the duration is greater than or equal to an hour, print the duration in hours and minutes
    if seconds >= 3600:
        hours = seconds / 3600
        minutes = (seconds % 3600) / 60
        if hours == 0:
            return f"{int(minutes)} minutes"
        elif minutes == 0:
            return f"{int(hours)} hours"
        else:
            return f"{int(hours)} hours {int(minutes)} minutes"

    # If the duration is greater than or equal to a minute, print the duration in minutes and seconds
    elif seconds >= 60:
        minutes = seconds / 60
        seconds = seconds % 60
        if minutes == 0:
            return f"{int(seconds)} seconds"
        elif seconds == 0:
            return f"{int(minutes)} minutes"
        else:
            return f"{int(minutes)} minutes {int(seconds)} seconds"

    # Otherwise, print the duration in seconds
    else:
        return f"{seconds} seconds"


async def generic_operation_complete_message(interaction, timer, message: Optional[str] = None):
    """Pass in the interaction and the current time using something like `timer = time.perf_counter()`"""
    execution_time = time.perf_counter() - timer
    embed = discord.Embed(title=message, description=f"Operation completed successfully ({round((execution_time), 6)}s)\n")
    await interaction.response.send_message(embed=embed)


""" BULK READ JSONS so it doesn't have to read the file every time a message is sent
    people = nolTighe (p1, g, b, T), oliver, sam (g), jack (r, g), joe (g), charlie (g), haydn, maisy, flo (a), ish, maya, boris (gl), josephTighe (p13, g, c, T)
    "g = grouped", "r = remade", "a = affiliated", "gl = global"
"""

with open(f"{JSON_DIR}NollyMention.json", "r", encoding="utf8") as file:
    nollyWords = json.loads(file.read())
with open(f"{JSON_DIR}OliverMention.json", "r", encoding="utf8") as file:
    oliverWords = json.loads(file.read())
with open(f"{JSON_DIR}SamMention.json", "r", encoding="utf8") as file:
    samWords = json.loads(file.read())
with open(f"{JSON_DIR}JackMention.json", "r", encoding="utf8") as file:
    jackWords = json.loads(file.read())
with open(f"{JSON_DIR}JoeMention.json", "r", encoding="utf8") as file:
    joeWords = json.loads(file.read())
with open(f"{JSON_DIR}HaydnMention.json", "r", encoding="utf8") as file:
    haydnWords = json.loads(file.read())
with open(f"{JSON_DIR}MaisyMention.json", "r", encoding="utf8") as file:
    maisyWords = json.loads(file.read())
with open(f"{JSON_DIR}BenMention.json", "r", encoding="utf8") as file:
    benWords = json.loads(file.read())
with open(f"{JSON_DIR}FloMention.json", "r", encoding="utf8") as file:
    floWords = json.loads(file.read())
with open(f"{JSON_DIR}IshMention.json", "r", encoding="utf8") as file:
    ishWords = json.loads(file.read())
with open(f"{JSON_DIR}BorisMention.json", "r", encoding="utf8") as file:
    borisWords = json.loads(file.read())
with open(f"{JSON_DIR}MayaMention.json", "r", encoding="utf8") as file:
    mayaWords = json.loads(file.read())
with open(f"{JSON_DIR}JosephTigheMention.json", "r", encoding="utf8") as file:
    josephTighe = json.loads(file.read())
with open(f"{JSON_DIR}CharlieMention.json", "r", encoding="utf8") as file:
    charlieSewards = json.loads(file.read())


#   Client events

print("Initialising client events...")


@client.event
async def on_ready():
    print("Bot started!")
    print(f'\n\n\n\n[ReadyUp]       Logged in as {client.user} - {(datetime.now())}')
    global ready_start_time, rolePrivate, hasPrivate, hasAdmin
    ready_start_time = time.time()
    await client.tree.sync()
    print("COG: Music loaded!")
    with open(GlobalLogDir, "a", encoding="utf-8") as f:
        f.write(f"\n\nREADY at {datetime.now()}")
        f.write(' - Logged in as {0.user}'.format(client))
    servers = len(client.guilds)
    members = 0
    await bot_runtime_events(7)
    for guild in client.guilds:
        members += guild.member_count - 1
        print(f"{guild.name} - {guild.member_count - 1} members")
    await client.change_presence(activity=discord.Game(name=(f"/help | {servers} servers, {members} users | {DRAGGIEBOT_VERSION}{BUILD}")))
    global draggie, general, console, upvote, downvote, hasMembersforGlobalServer
    draggie = client.get_user(382784106984898560)
    general = client.get_channel(759861456761258045)#  Brigaders_channel
    console = client.get_channel(912429726562418698)
    guild = client.get_guild(759861456300015657)
    draggie_guild = client.get_guild(759861456300015657)
    hasPrivate = discord.utils.find(lambda r: r.name == 'Private', guild.roles)
    hasAdmin = discord.utils.find(lambda r: r.name == 'Admin', guild.roles)
    rolePrivate = discord.utils.get(guild.roles, id=806481292392267796)
    upvote = client.get_emoji(803578918488768552)
    downvote = client.get_emoji(803578918464258068)
    epic_memes = client.get_channel(809112184902778890)
    public_memes = client.get_channel(930488945144397905)
    memes_channels = [epic_memes, public_memes]
    ready_up_channel = client.get_channel(1099008145092788254)
    if BETA_BOT:
        await ready_up_channel.send(f"Beta Bot is now online at {datetime.now()}")
    else:
        await ready_up_channel.send(f"Bot is now online at {datetime.now()}")
    hasMembersforGlobalServer = discord.utils.get(guild.roles, name="Members")

    await asyncio.sleep(2)
    global test__bb_voice_channel
    test__bb_voice_channel = client.get_channel(1013893596493119488)

    it = test__bb_voice_channel.history()
    test_voice_time = await anext(it)

    voice_time = test_voice_time.content

    with open(f'{BASE_DIR}Servers{S_SLASH}759861456300015657{S_SLASH}Logs{S_SLASH}TotalUserVoiceTime.txt', 'w+') as x:
        x.write(voice_time)

    client.loop.create_task(connect_nodes())
    client.add_listener(on_wavelink_node_ready, 'on_wavelink_node_ready')
    client.add_listener(on_wavelink_track_end, 'on_wavelink_track_end')

    if BETA_BOT:
        return

    for channel in memes_channels:
        async for message in channel.history():
            if "upvote" not in str(message.reactions) or "downvote" not in str(message.reactions):
                # print(message.reactions)
                if ("http") in message.content.lower():
                    await message.add_reaction(upvote)
                    await message.add_reaction(downvote)
                    print(f"[ReadyUp]       Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'http' in '{message.content.lower()}'")
                if len(message.attachments) >= 1:
                    await message.add_reaction(upvote)
                    await message.add_reaction(downvote)
                    print(f"[ReadyUp]       Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'message.attachments' is greater than 1")
                else:
                    print("[ReadyUp]        Skipped message to react to")
            if len(message.reactions) == 0:
                if ("http") in message.content.lower() or len(message.attachments) >= 1:
                    await message.add_reaction(upvote)
                    await message.add_reaction(downvote)
                    print(f"[ReadyUp]       Added Upvote and Downvote reactions to a message sent by {message.author} {message.id}.\nReason: 'no reactions on message' or 'has attachment'")

    for file in os.listdir("D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice"):
        if file != "voice_info.txt":
            file = file.split("_")
            file = file[1].split(".")
            file = str(file[0])
            person = guild.get_member(int(file)) # Get member object from guild ID
            try:
                if not person.voice:
                    os.remove(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice\\tempuserstate_{file}.txt")
                    print(f"[ReadyUp]       Deleted a temporary voice file on readying up. Name: {file} // ({person})")
                else:
                    print(f"[ReadyUp]       Kept temporary voice file, as the person is still in a voice chat. ({person.name})")
            except AttributeError:
                os.remove(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice\\tempuserstate_{file}.txt")

    voice_chat_category = discord.utils.get(guild.categories, id=759861456761258048)

    for VoiceChannel in voice_chat_category.channels:
        for Member in VoiceChannel.members:
            print(f"[ReadyUpVoice]      {Member.id} is in a Voice Chat.")
            if not os.path.isfile(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice\\tempuserstate_{Member.id}.txt"):
                with open(f"{BASE_DIR}Servers{S_SLASH}{guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{Member.id}.txt", "w+") as new_synced_user_from_offline:
                    join_time = str(round(time.time()))
                    new_synced_user_from_offline.write(join_time)
                    new_synced_user_from_offline.close()
                    print(f"[ReadyUpVoice]      Written {join_time} to {BASE_DIR}Servers{S_SLASH}{guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{Member.id}.txt")
            else:
                print(f"[ReadyUpVoice]      Path to Voice Time file already exists. {BASE_DIR}Servers{S_SLASH}{guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{Member.id}.txt")

    print(f"[ReadyUp]       Calibrated Voice Chat time to {voice_time} seconds")

    await bot_runtime_events(1)
    await StatusAutoUpdator()


@client.event
async def on_voice_state_update(member, before, after):
    print(f"[VoiceChatEvent]    Occurred in {member.guild.id} ({member.guild.name}) by {member.name} at {datetime.now()}")
    # if member.bot: #checking this before anything else will reduce unneeded file operations etc
    #    return
    await bot_runtime_events(1)
    if after.channel:
        if member.id == 382784106984898560:
            if before.channel is not None:
                if before.channel.id == 1045032578190684181:
                    if after.channel.id != 1045032578190684181:
                        channel = client.get_channel(1045032578190684181)
                        await member.move_to(channel)
        if not os.path.isfile(f'{BASE_DIR}Servers{S_SLASH}{after.channel.guild.id}{S_SLASH}Voice{S_SLASH}voice_info.txt'):
            try:
                os.makedirs(f'{BASE_DIR}Servers{S_SLASH}{after.channel.guild.id}{S_SLASH}Voice', exist_ok=True)
            except Exception as e:
                print("[VoiceChatJoin]    Error creating voice folder: " + str(e))
            print(f"[VoiceChatJoin]    User {member.name} joined VC in {member.guild.id} ({member.guild.name}) at {datetime.now()} ")

            with open(f'{BASE_DIR}Servers{S_SLASH}{after.channel.guild.id}{S_SLASH}Voice{S_SLASH}voice_info.txt', 'w') as f:
                f.close() #  Create the file
    else:
        print(f"[VoiceChatLeave]    User {member.name} left VC in {member.guild.id} ({member.guild.name}) at {datetime.now()}")
        # Check if the member is the only one in the voice channel
        # if guild.voice_client
        if len(before.channel.members) == 1:
            # Leave the voice channel
            if before.channel.guild.voice_client is not None:
                await asyncio.sleep(30) #   Wait a few seconds in case people rejoin.
                if len(before.channel.members) == 1:
                    await before.channel.guild.voice_client.disconnect()
                    await before.channel.send("Automatically left this Voice Channel as all other members have left!")
    new_user = str(member.id)

    if not before.channel: #When VC joined.
        join_time = round(time.time())
        with open(f'{BASE_DIR}Servers{S_SLASH}{after.channel.guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{new_user}.txt', 'w') as x:
            x.write(str(join_time))
    if not after.channel:
        await bot_runtime_events(1)
        leave_time = round(time.time())
        with open(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{new_user}.txt', 'r') as x:
            start_time = int(x.read())
        os.remove(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Voice{S_SLASH}tempuserstate_{new_user}.txt')
        time_spent = leave_time - start_time
        print(f"[VoiceChatLeave]    {member.name} just spent {time_spent}s in a Voice Chat.")

        if before.channel.guild.id == 759861456300015657:
            await bot_runtime_events(1)
            print("[VoiceChatLeave]     Occured in Baguette Brigaders!")

            #   Calculate the amount to add using the special formula
            #   Formula generated by GPT
            if time_spent < 300:   # 5 minutes in seconds
                coins_to_add = 0
            elif time_spent < 3600:   # 1 hour in seconds
                coins_to_add = round(40 * (1 - math.exp(-(time_spent - 300) / 120)))
            elif time_spent < 18000:   # 5 hours in seconds
                coins_to_add = round(40 * (1 - math.exp(-3300 / 120)) + 5 * math.log(time_spent / 3600))
            else:
                coins_to_add = round(40 * (1 - math.exp(-3300 / 120)) + 5 * math.log(5))

            if time_spent < 120:
                new_time_spent = time_spent
                units = "seconds"
            else:
                new_time_spent = round(time_spent / 60)
                units = "minutes"

            if time_spent > 3600:
                new_time_spent = round(time_spent / 3600)
                if new_time_spent == 1:
                    units = "hour"
                else:
                    units = "hours"

            try:
                x = (random.randint(1, 4))
                if x == 2:
                    if coins_to_add > 10:
                        if member.id == 792850689533542420:
                            return
                        settings = await get_user_settings(member.id)
                        if settings is not None:
                            if settings['reminders_for_voice_time'] == "true":
                                string = (f"{member.mention}, you have earned an extra {coins_to_add} Coins {EMOJI_COINS} for spending {new_time_spent} {units} in voice!\n\n*Type `/coins` in Baguette Brigaders to see what you can buy!*")
                                print(f"[VoiceChatEvent]    Member leaving has subscribed to Voice Reminders. Message sent: {string}")
                        else:
                            print("[VoiceChatEvent]    Member has not specified their Settings preferences.")
                    else:
                        print(f"[VoiceChatEvent]    CoinBal Not going to Stage 3 of alerting earned sum was only {coins_to_add}.")
                else:
                    print(f"Not going to Stage 2 of alerting as the number was not 2, it was {x}")
            except AttributeError:
                print("Could not send the message as the member is probably a bot or has blocked the bot.")

            update_coins(member.guild.id, member.id, coins_to_add)

        # Get total guild time spent in Voice Chat
        # Firstly, if there is not a record of voice chat time, create the file
        if not os.path.isfile(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Logs{S_SLASH}TotalUserVoiceTime.txt'):
            os.makedirs(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Logs{S_SLASH}', exist_ok=True)
            with open(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Logs{S_SLASH}TotalUserVoiceTime.txt', 'w') as x:
                x.write("0")

        #   Then, open up the file for reading.
        with open(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Logs{S_SLASH}TotalUserVoiceTime.txt', 'r') as x:
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
        x = open(f'{BASE_DIR}Servers{S_SLASH}{before.channel.guild.id}{S_SLASH}Logs{S_SLASH}TotalUserVoiceTime.txt', 'w+')
        x.write(str(total_guild_time_spent))
        x.close()

        if not BETA_BOT:
            #   Finally, send sum to me as a test.
            if before.channel.guild.id == 759861456300015657:
                await test__bb_voice_channel.send(total_guild_time_spent)
                await draggie.send(f"The guild, {before.channel.guild.name}, now has {total_guild_time_spent} seconds total spent, thanks to {member.name}.")


@client.event
async def on_member_join(member):
    await bot_runtime_events(1)
    print(f"[MemberJoined]  on_member_join triggered: Member: {member.name} ({member.id}) in guild {member.guild.name} ({member.guild.id}).")
    guild_id = member.guild.id
    member_id = member.id

    # If member's coin balance already exists in the server, remove it as they are rejoining.
    if os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Coins{S_SLASH}{member_id}.txt"):
        os.remove(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Coins{S_SLASH}{member_id}.txt")
        print("[MemberJoined]  Member's coin balance already exists in the server, so it was removed.")
    else:
        print("[MemberJoined]  Member's coin balance does not exist in the server. They are joining for the first time.")

    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    await client.change_presence(activity=discord.Game(name=(f"/help | {servers} servers, {members} users | CPU {cpuPercentage}% + RAM {memoryUsage}% | {DRAGGIEBOT_VERSION}{BUILD}")))


@client.event
async def on_member_remove(member):
    await bot_runtime_events(1)
    sendLogsDir = (f"{BASE_DIR}Servers{S_SLASH}{member.guild.id}{S_SLASH}sendMessages.txt")
    if os.path.isfile(sendLogsDir):
        try:
            channel = discord.utils.get(member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
            await channel.send(f"[MemberLeave]  {member} has left the server.")
        except Forbidden:
            await draggie.send(f"[SelfRemove]   Removed from server {member.guild.name} / {member.guild.id}")
    servers = len(client.guilds)
    members = 0
    cpuPercentage = psutil.cpu_percent()
    memoryUsage = psutil.virtual_memory().percent
    for guild in client.guilds:
        members += guild.member_count - 1
        await client.change_presence(activity=discord.Game(name=(f"/help | {servers} servers, {members} users | CPU {cpuPercentage}% + RAM {memoryUsage}% | {DRAGGIEBOT_VERSION}{BUILD}")))


@client.event
async def on_raw_reaction_add(payload=None):
    print(f"[ReactionAdd]   Reaction '{payload.emoji.name}' added in {payload.guild_id} ({payload.member.guild.name}) by {payload.member.name}. ({payload.emoji.url})")
    await bot_runtime_events(1)
    if payload.guild_id == 759861456300015657:#     Must, while reaction roles are not available for all servers.
        msgID = 835227251695288391
        vaccinatedID = 895386703144034364
        smp2ID = 912012054414630973
        birthdayID = 892114380005715978
        birthday2ID = 1024404603866988704
        guild = discord.utils.get(client.guilds, id=BRIGADERS)
        roleAllRandoms = discord.utils.get(guild.roles, id=930186230442905620)
        rolePrivate = discord.utils.get(guild.roles, id=806481292392267796)
        roleVaccinated = discord.utils.get(guild.roles, name='Vaccinated ✅')
        roleUnverified = discord.utils.get(guild.roles, id=980885916317003846)
        role_private_unverified = roleUnverified
        roleSMP = discord.utils.get(guild.roles, name='SMP')
        role_birthday_2 = discord.utils.get(guild.roles, id=1024395360023629834)
        robloxDev = discord.utils.get(guild.roles, name="Roblox Developer")
        roleNew = discord.utils.get(guild.roles, name='New Baguette')
        LoggingChannel = discord.utils.get(payload.member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

        if payload is not None:
            authorName = payload.member.name
            authorName = authorName.lower()
            if payload.message_id == birthdayID or payload.message_id == birthday2ID:
                await payload.member.send("You are too late to claim the birthday role, sorry. More exclusive roles will be given in the future!")
            if payload.message_id == smp2ID:
                await payload.member.add_roles(roleSMP)
                print(f"[ReactionRole]  Added role to {payload.member.name}")
                await payload.member.send(f"{payload.member.mention}, you've been granted SMP Season 2 role in Baguette Brigaders! Enjoy your time on the server.")
                print(f"[ReactionRole]  Sent DM to {payload.member.name}")
            if payload.message_id == 1024404603866988704:
                await payload.member.add_roles(role_birthday_2)
                await payload.member.send("You've claimed the Brigadeux role permanently! Enjoy!")

            if payload.message_id == 936320104193474630:
                print(f"[ReactionRole]  Sent Roblox Message message to {payload.member}")
                await payload.member.add_roles(robloxDev)
            if payload.message_id == 931577920512725083:#
                await asyncio.sleep(5)
                member = payload.member.guild.get_member(payload.member.id)
                await payload.member.remove_roles(roleUnverified)
                if roleAllRandoms not in member.roles:
                    print("[ReactionRole]  Adding roles...")
                    channel = client.get_channel(930489645014331442)
                    await member.add_roles(roleAllRandoms)
                    await member.send(f"Welcome, {member.mention}! You have been verified! Enjoy the server; thanks for being part of this special community. We look forward to having you onboard for future developments!")
                    print(f"[ReactionRole]  Sent message to {member}")
                    await LoggingChannel.send(f"{payload.member} has been verified.")
                else:
                    print("[ReactionRole]  Not adding as members is already in roles.")

            if payload.message_id == 931586778245247018:
                choices = ["OK, you'll no longer see the other side.", "No longer seeing the other side. Enjoy your time on this side!", "Who likes the other side anyway, this side is better!"]
                if roleAllRandoms not in payload.member.roles:
                    await payload.member.add_roles(roleAllRandoms)
                    await LoggingChannel.send(f"{payload.member} has been allowed access to the other side.")
                else:
                    print(f"[ReactionRole]  {payload.member.name} already has Members role, removing it.")
                    await payload.member.remove_roles(roleAllRandoms)
                    await payload.member.send(f"{random.choice(choices)}")

            if payload.message_id == msgID:#                VERIFICATION MESSAGE ONLY
                if str(payload.emoji) == "✅":
                    channel = client.get_channel(835200388965728276)
                    # await payload.member.add_roles(rolePrivate)
                    await payload.member.add_roles(roleNew)
                    # await channel.send(f"Welcome, {payload.member.mention} to the private side! You have been verified! Maybe check out <#759861456761258045> now? Assign some roles in <#970339131500662835> such as your sixth form/college! Also, we have our own currency and shop system, so I'll leave that for you to find. Enjoy!", delete_after=10)
                    await channel.send(f"{payload.member.mention} your request to join the private side has been submitted! I wish you luck with your application. It is now being reviewed.", delete_after=10)
                    # await payload.member.remove_roles(role_private_unverified)
                    # await payload.member.remove_roles(roleUnverified)
                    print(f"[ReactionRole]  And it's gone in {channel}")

            if payload.message_id == vaccinatedID:
                if str(payload.emoji) == "✅":
                    await payload.member.add_roles(roleVaccinated)
                    await LoggingChannel.send(f"[ReactionRole]  {payload.member} has been granted vaccination status.")

    if payload.guild_id == 384403250172133387:#     Must, while reaction roles are not available for all servers.
        if payload.message_id == 907318418712170538:
            channel = client.get_channel(907318241498656850)


@client.event
async def on_reaction_remove(reaction, user):
    await bot_runtime_events(1)
    print(reaction, user)


@client.event
async def on_guild_join(guild):
    print(f"[GuildJoin]   Joined guild {guild}")
    await draggie.send(f"DEV MODE: joined guild {guild} ({guild.id})")


@client.event
async def on_guild_remove(guild):
    print(f"[GuildRemove]   Removed from guild {guild}")
    await draggie.send(f"DEV MODE: removed from guild {guild} ({guild.id})")


@client.event
async def on_message_delete(message):
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    sendRedactionsInChannel = (f"{BASE_DIR}Servers{S_SLASH}{message.guild.id}{S_SLASH}sendRedactions.txt")
    print(f"[MessageDeletion]   Message deleted: '{message.content}' channel: '{message.channel.name}' server: '{message.guild.name}'")
    if message.channel.id == 825470734453047297:
        if message.author.bot is False:
            print(f"Stop deleting your messages in here, we're literally adding numbers, {message.author.mention}. *Their message was {message.content}*")
            return
    if os.path.isfile(sendRedactionsInChannel):
        if message.author.id != 792850689533542420:
            await message.channel.send(f"{message.author.mention}'s message has been *redacted*.")
            user = client.get_user(int(message.author.id))
            await user.send(f"Your message, '`{message.content}`', has been ***redacted***.")
    if os.path.isfile(f"{BASE_DIR}Servers{S_SLASH}{message.guild.id}{S_SLASH}sendMessages.txt"):
        LoggingChannel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
        embed = discord.Embed(title="User's message deleted", colour=0xFF0000)
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
    user = client.get_user(int(userID))
    await user.send(f"{sp1}")
    await ctx.send(f"Successfully sent {sp1} to user {user.name}")


@client.event
async def on_message_edit(before, after):
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    if not after.guild:
        return print("[Mod/Edits]       Message edited in a non guild channel or ephemeral message")
    sendLogsDir = (f"{BASE_DIR}Servers{S_SLASH}{after.guild.id}{S_SLASH}sendMessages.txt")

    LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

    if LoggingChannel is not None and not BETA_BOT:
        if before.content == after.content:
            embed = discord.Embed(title="Message modified", description=f"Embed preview added to message ([jump]({after.jump_url}))")
            await LoggingChannel.send(embed=embed)
            return

        print(f"Message updated >>> '{before.content}' changed to '{after.content}' in {after.guild.name}/{after.guild.name}")
        if os.path.isfile(sendLogsDir):
            embed = discord.Embed(title="Message edited")
            embed.add_field(name='User', value=after.author.mention)
            embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
            embed.add_field(name='Time', value=tighem)
            if before.content == '' and after.content == '':
                embed.add_field(name="Data", value='<attachment sent>', inline=False)
                await LoggingChannel.send(embed=embed)
                return
            embed.add_field(name="Message before", value=before.content, inline=False)
            embed.add_field(name="Message after", value=after.content, inline=False)
            try:
                await LoggingChannel.send(embed=embed)
            except discord.HTTPException:
                embed = discord.Embed(title="Message edited")
                embed.add_field(name='User', value=after.author.mention)
                embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
                embed.add_field(name='Time', value=tighem)
                embed.add_field(name="Message before", value="[too big to preview]", inline=False)
                embed.add_field(name="Message after", value="[too big to preview]", inline=False)
                embed.add_field(name="Jump", value=f"([Go to new message]({after.jump_url}))", inline=False)
            return
        if before == after:
            embed = discord.Embed(title="Message state changed")
            embed.add_field(name='User', value=after.author.mention)
            embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
            embed.add_field(name='Time', value=tighem)
            case_a = str(before)
            case_b = str(after)
            output_list = [li for li in difflib.ndiff(case_a, case_b) if li[0] != ' ']
            embed.add_field(name='Modified strings (beta)', value=output_list, inline=False)
            if not BETA_BOT:
                await LoggingChannel.send(embed=embed)
            return


@client.event
async def on_typing(channel, user, when):
    await bot_runtime_events(1)
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    if not channel.guild:
        await draggie.send(f"{user.mention} ({user}) is DMing me")
        print(f"[UserTypingDM]        {user.name} is DMing")
        return
    print(f"[UserTyping]        {user.name} started typing in '{channel.guild.name} - {channel.name}' at {tighem}/{when}")


@client.event
async def on_user_update(before, after):
    await bot_runtime_events(1)
    if after.avatar != before.avatar:
        print(f"[AvatarUpdate]      {before.name} updated their avatar, to {after.avatar.url}. (from {before.avatar.url})")


@client.event
async def on_member_ban(guild, user):
    await bot_runtime_events(1)
    print("test")


@client.event
async def on_presence_update(before, after):
    if after.activity is not None:
        await bot_runtime_events(1)
        # print(f"[UserActivity]      {after.name} has been updated to \"{after.activity.name}\" in {after.guild.name} at {datetime.now()}")
        # print(str(after.activities)) modified repl.it
    if before.status != after.status:
        await bot_runtime_events(1)
        # print(f"[UserPresence]      {after.name} has been updated to \"{after.status}\" in {after.guild.name} at {datetime.now()}")#    This is only used for debugging, and is not stored for more than 24 hours.
        #   This data may be stored, anonymised (i.e dissociated from the user), for longer than this time


@client.event
async def on_member_update(before, after):
    # print(f"Member updated - BEFORE = {before} AFTER = {after} - {datetime.now()}")
    await bot_runtime_events(1)
    send = False
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    guild = after.guild
    if before.nick != after.nick:
        embed = discord.Embed(title="Changed nick", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.nick)
        embed.add_field(name='After', value=after.nick)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"[NickChange]        The nickname of {after} has been updated FROM {before.nick} TO {after.nick} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        staffCheck = new_role.id
        if staffCheck == 963738031863525436 or staffCheck == 930874936082452480 or staffCheck == 759861918763712542 or staffCheck == 943974413810933802:
            roleStaff = discord.utils.get(guild.roles, name=new_role.name)
            await after.remove_roles(roleStaff)
        else:
            print("Not staff role.")
        embed = discord.Embed(title="Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role added', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"[RoleAdd]       ROLES of {after} has been updated: ADDED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
        if after.guild.id == 759861456300015657 or after.guild.id == 384403250172133387:
            if new_role.name == "Server Booster":
                nolwenniumUserDir = (f"{BASE_DIR}Nolwennium{S_SLASH}{after.id}.txt")
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    with open(nolwenniumUserDir, 'a') as f:
                        print(f"\n[CURRENCY - {NAME_NOLWENNIUM}] Set {NAME_NOLWENNIUM} value to 0, new user. {after.id} - {after.name}")
                        f.write('0')
                        f.close()

                with open(nolwenniumUserDir, 'r') as f:
                    beforeBonusAmount = (float(f.read()))
                    f.close()

                toAdd = random.randint(100, 1000)
                addedAmount = beforeBonusAmount + toAdd

                f = open(nolwenniumUserDir, 'w+')
                f.close()

                with open(nolwenniumUserDir, 'a') as f:
                    f.write(str(addedAmount))
                    print(f"\n[CURRENCY - {NAME_NOLWENNIUM}] Added balance of {toAdd} (total: {addedAmount} for boosting the server: {after.id} - {after.name}")
                    f.close()

                new_coins = update_coins(after.guild.id, after.id, 100)

                await general.send(f"Thank you {after.mention} for boosting the server! You have received the Server Booster role, an exclusive name colour, and a bonus sum of Coins (total: {new_coins}) and {NAME_NOLWENNIUM} (total: {addedAmount}). You can also change your name to any colour you want, see the command /namecolour for more information.")
            # await draggie.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!')                        In Brigaders Helper

        settings = await get_user_settings(after.id)
        if settings:
            if settings['get_dm_notification_for_role_addition'] == "true":
                await after.send(f'{after.mention}, you\'ve been given the role **"{new_role}"** in {after.guild.name}!')
                print(f"[SendDirectMessage] {after.mention}, you\'ve been given the role **\"{new_role}\"** in {after.guild.name}! <<< to {after.name}")

    elif len(after.roles) < len(before.roles):
        new_role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title="Changed roles", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Role removed', value=new_role)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"[RoleRemove]    ROLES of {after} has been updated: REMOVED {new_role} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")
        settings = await get_user_settings(after.id)
        if settings['get_dm_notification_for_role_removal'] == "true":
            await after.send(f'{after.mention}, you\'ve been removed from the role **"{new_role}"** in {after.guild.name}!')
            print(f"[SendDirectMessage] {after.mention}, you\'ve been removed from the6 role **\"{new_role}\"** in {after.guild.name}! <<< to {after.name}")

    elif before.name != after.name:
        embed = discord.Embed(title="Changed name", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.name)
        embed.add_field(name='After', value=after.name)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"[NameChange]    NAME of {after} has been updated FROM {before.name} TO {after.name} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    elif before.discriminator != after.discriminator:
        embed = discord.Embed(title="Changed discriminator", colour=0x5865F2)
        embed.add_field(name='User', value=before.mention)
        embed.add_field(name='Before', value=before.discriminator)
        embed.add_field(name='After', value=after.discriminator)
        embed.add_field(name='Date/Time', value=tighem)
        send = True
        print(f"[TagChange]     DISCRIMINATOR of {after} has been updated FROM {before.discriminator} TO {after.discriminator} - in [{after.guild.id} or {after.guild.name}] at {datetime.now()}")

    sendLogsDir = (f"{BASE_DIR}Servers{S_SLASH}{after.guild.id}{S_SLASH}sendMessages.txt")
    if os.path.isfile(sendLogsDir):
        if send is True:
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
                except Exception:
                    print(f"unable to send message in server {guild.name} / {guild.id}")
                    await draggie.send(f"unable to send message in server {guild.name} / {guild.id}")
                LoggingChannel = discord.utils.get(after.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

            await LoggingChannel.send(embed=embed)
    else:
        send = False
        return


@client.event
async def on_slash_command_error(ctx, error):
    await bot_runtime_events(1)
    random_cry_list = ['<:AmberCry:828577834146594856>', '<:BibiByeBye:828683852939395072>', '<:ColetteCry:828683829631516732>', '<:JessieCry:828683805861740654>', '<:SpikeCry:828683779206807622>', '<:SurgeCry:828683755694063667>', '<:TaraCry:828683724286853151>']
    embed = discord.Embed(title=(f"{random.choice(random_cry_list)} An error occured"), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    print("error!")
    await bot_runtime_events(1)
    if "is not found" in str(error):
        print(f"Command returned an error but will be returned. Server: {ctx.guild.name}, error message = {error}")
        return
    if "on cooldown" in str(error):
        await ctx.send(f"{error}.")
        return
    if ctx.message.content.startswith(".."):
        return
    random_cry_list = ['<:AmberCry:828577834146594856>', '<:BibiByeBye:828683852939395072>', '<:ColetteCry:828683829631516732>', '<:JessieCry:828683805861740654>', '<:SpikeCry:828683779206807622>', '<:SurgeCry:828683755694063667>', '<:TaraCry:828683724286853151>']
    embed = discord.Embed(title=(f"{random.choice(random_cry_list)} An error occured"), description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.", color=0x990000)
    await ctx.send(embed=embed)
    print(str(error))
    f = open(GlobalLogDir, "a")
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.author} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()
    f = open(f"{BASE_DIR}errors.txt", "a")#	Modified in repl.it
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.user} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()


#   on message


@client.event
async def on_message(message):
    global rolePrivate, hasPrivate, hasAdmin, upvote, downvote
    await bot_runtime_events(1)
    if "UUID of player EmileTigger is d0b393de-e783-45b6-9d13-19ba56c5451e" in message.content:
        termcolor.cprint("Emile joined", 'red', attrs=['blink'])
        await asyncio.sleep(3)
        await console.send("say FRENCH Detected!!!!")
    if "EmileTigger lost connection" in message.content:
        await console.send("say Au revoir!")
    if "382784106984898560" in message.content and "help" in message.content.lower():
        await message.reply("Here's a simple way to fix your problem:", file=discord.File("D:\\Draggie Programs\\valorant-uninstall-launcher-fuck-valorant-valorass-gif.gif"))

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
                attachmentsDir = (f"{BASE_DIR}Servers{S_SLASH}{message.guild.id}{S_SLASH}Attachments{S_SLASH}")
                if not os.path.exists(attachmentsDir):
                    os.makedirs(f"{BASE_DIR}Servers{S_SLASH}{message.guild.id}{S_SLASH}Attachments{S_SLASH}")
                    print("Made directory" + (attachmentsDir))
            except AttributeError:
                print("Attachment sent in DMs.")
                attachmentsDir = (f"{BASE_DIR}DMs{S_SLASH}Attachments{S_SLASH}{message.author.id}{S_SLASH}")
                if not os.path.exists(attachmentsDir):
                    os.makedirs(f"{BASE_DIR}DMs{S_SLASH}Attachments{S_SLASH}{message.author.id}{S_SLASH}")
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
                sendLogsDir = (f"{BASE_DIR}Servers{S_SLASH}{message.guild.id}{S_SLASH}sendMessages.txt")
                if os.path.isfile(sendLogsDir):
                    await LoggingChannel.send(f"Attachment sent in <#{message.channel.id}>: **{filename}**: {attachment.url}")
            except Exception:
                pass

    if message.author.bot:
        return
    if running_locally: #	Modified in repl.it
        await DLstuff()
    person = message.author
    personID = message.author.id

    if not message.guild:
        if message.content.startswith(".a"):
            x = message.content.split()
            msgchannel = (x[1])
            sp1 = message.content.split(' ', 2)[-1]
            channel = client.get_channel(int(msgchannel))
            await channel.send(f"`{sp1}`")
            return
        if message.content.startswith(".sa"):
            x = message.content.split()
            msgchannel = (x[1])
            sp1 = message.content.split(' ', 2)[-1]
            channel = client.get_channel(int(msgchannel))
            await channel.send(str(sp1))
            return
        if message.content.startswith("."):
            await message.channel.send("Please use commands in a server with me in it for them to run correctly. Sorry!")
        # await draggie.send(f"\n'{message}' DMed by {person} at {datetime.now()}")
        print(f"\n'{message.content}' DMed by {person} at {datetime.now()}")

        dmLocation = (f"{BASE_DIR}DMs{S_SLASH}{personID}.txt")
        logAllMessages = open(dmLocation, "a", encoding='utf-8')
        logAllMessages.write(f"\n'{message}' DMed by {person} at {datetime.now()}")
        logAllMessages.close()
        return

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    serverName = message.guild.name
    serverID = message.guild.id
    channelName = message.channel.name
    channelID = message.channel.id

    filedir = (f"{BASE_DIR}Servers{S_SLASH}{serverID}{S_SLASH}Logs{S_SLASH}")
    if not os.path.exists(filedir):
        if running_locally: # Modified repl.it
            os.makedirs(f"{BASE_DIR}Servers{S_SLASH}{serverID}{S_SLASH}Logs{S_SLASH}")
        else:
            os.makedirs(f"{BASE_DIR}Servers{S_SLASH}{serverID}{S_SLASH}Logs{S_SLASH}")

    try:
        with open((f"{filedir}MessageLog.txt"), "a", encoding='utf-8') as logAllMessages:
            logAllMessages.write(f"\n'{message.content}' sent by {message.author} in [{serverName} - #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")
            logAllMessages.close()
    except Exception as e:
        errorMsg = str(f"\n\n\n\nError!!!! Logging file corruption has occured!!! cc: <@382784106984898560> \n\n\n\n{e}\n\n")
        print(errorMsg)
        try:
            with open((f"{filedir}MessageLog1.txt"), "a", encoding='utf-8') as logAllMessages:
                logAllMessages.write(f"\n'{message.content}' sent by {message.author} in [{serverName} - #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")
                logAllMessages.close()
        except Exception as e:
            errorMsg = str(f"\nCRITICAL ERROR!!!! Server file corruption has occured!!! cc: <@382784106984898560>, server ID is {serverID} / {channelID}\nDM Draggie#3060 if this does not get resolved in 10 minutes\nError: {e}")
            print(errorMsg)
            await draggie.send(errorMsg)

    print(f"\n[MessageSent]     '{message.content}' sent by {message.author} in [{serverName} - #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    if message.channel.name == 'nolwennium-138':
        emoji = client.get_emoji(786177817993805844)
        await message.add_reaction(emoji)

    if message.content.lower() == ("ratio") or "+ ratio" in message.content.lower():
        await message.add_reaction(upvote)
        await message.add_reaction(downvote)

    if message.reference:
        if "ratio" == message.content.lower():
            await message.add_reaction(upvote)
            await message.add_reaction(downvote)

    if message.channel.id == 809112184902778890 or message.channel.id == 967114002347986954 or message.channel.id == 930488945144397905:
        if ("http") in message.content.lower() or len(message.attachments) >= 1:
            print("Adding reactions to message as it contains a link or attachment")
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
        update_coins(message.guild.id, message.author.id, 1)

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

    if message.guild.id in TESTER_GUILD_IDS:
        if message.content.lower() == ("hi"):
            await message.reply(content=(random.choice(["Hi", "hi", "Hey", "hey", "hi how r u?", "Hello there!", "Hello", "hello", "hello!", "Bonjour.", "Heyyyyy", "Hi, how are you?", "Hello! How are you today?", "Yo!", "What's up?"])))
            f = open(GlobalLogDir, "a")
            f.write(f"\nWORD MENTIONED -> 'hi' ran by {message.author} at {datetime.now()}")
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
                # await message.channel.send(actual_query)
                # await message.channel.send("```Executed instruction.```")
                print("Ok")
            else:
                await message.channel.send(f"```{uuid.uuid4()}_callstack/MainThread: operation rejected, traceback includes data: message.author.id is {personID}```")

    #   test

        if message.content == ('test'):
            await message.channel.send("testerino")
            f = open(GlobalLogDir, "a")
            f.write(f"\nCOMMAND RAN -> '.test' ran by {message.author} in {message.guild.id} at {datetime.now()}")
            f.close()

    #   Split message

        if message.content.startswith(".split"):
            txt = message.content
            x = txt.split()
            print(x[1])
            await message.channel.send(x[1])

#  here we can do global server ones because its funny

    messageContent = message.content.lower()
    for word in messageContent.split():
        if word in borisWords:
            await message.add_reaction("<:boris:785942478381121556>")
            f = open(GlobalLogDir, "a", encoding="utf8")
            f.write((str(f"\nINFO: 'boris' emoji sent, initiated by '{message.author}' at {datetime.now()}")))
            f.close()

#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete

    else:
        if message.guild.id != 789537159450198036:
            await client.process_commands(message)

#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete

#   Dot Commands.

#   Cross Server Messaging


print("Done! Initialising legacy Dot Commands...")


@client.command(pass_context=True, hidden=True)
async def sa(ctx):
    if ctx.message.author.id == 382784106984898560:
        text = ctx.message.content
        x = text.split()
        msgchannel = (x[1])
        sp1 = text.split(' ', 2)[-1]
        channel = client.get_channel((int(msgchannel)))
        await channel.send(str(sp1))
        return

#   currency


@client.command(help="Displays currency options and commands", brief="Displays currency options and commands.", pass_context=True)
async def currency(ctx):
    nolwenniumUserDir = nolwenniumUserDirectory(ctx)
    my_file = Path(nolwenniumUserDir)

    if not my_file.is_file():
        with open(nolwenniumUserDir, 'a') as f:
            print(f"\n[CURRENCY - {NAME_NOLWENNIUM}] Set {NAME_NOLWENNIUM} value to 0, new user. {ctx.author.id} - {ctx.author.name}")
            try:
                f.write('0')
                f.close()
            except Exception:
                f.write('0')
                f.close()

    f = open(nolwenniumUserDir, 'r')
    nolwennium_bal = round(float(f.read()), 4)
    f.close()

    message = ""
    number = 0
    for guild in ctx.author.mutual_guilds:
        message += f"`{guild.name}` \n"
        number = number + 1

    await ctx.send(f"Multiplier: 1.{number}x ({number}0%) bonus {nolwennium_bal}")
    await ctx.send(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/GfetCXH for updates on what this will do, and for the all-new currency system. You are eligible for {nolwennium_bal} new currency points! {EMOJI_NOLWENNIUM}")


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
    if ctx.author.id == ID_DRAGGIE:
        x = ctx.message.content.split()
        word1 = (str(x[1]))
        word2 = (str(x[2]))
        await ctx.send(f"Set {word1} to value {word2}.")
        word1 = word2


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
                with open((f"{TEMP_FOLDER}{channel.name}_log.txt"), "a", encoding='utf-8') as logAllMessages:
                    logAllMessages.write(f"\n'{message.content}' sent by {message.author} at {(message.created_at)}")
                    print(f"\n'{message.content}' sent by {message.author}")
                    logAllMessages.close()
                    count = count + 1
            else: # If there is it gets the filename from message.attachments
                try:
                    attachmentsDir = (f"{TEMP_FOLDER}{message.channel.name}{S_SLASH}Attachments{S_SLASH}")
                    if not os.path.exists(attachmentsDir):
                        os.makedirs(f"{TEMP_FOLDER}{message.channel.name}{S_SLASH}Attachments{S_SLASH}")
                        print("Made directory" + (attachmentsDir))
                    nameOfFile = str(message.attachments).split("filename='")[1]
                    filename = str(nameOfFile).split("' ")[0]
                    beans = (f"{attachmentsDir}{filename}")

                    if os.path.isfile(beans):
                        filename = str(nameOfFile).split("' ")[0]
                        beans = (f"{attachmentsDir}{uuid.uuid4()}-name={filename}")
                    await message.attachments[0].save(fp=beans)
                    await message.delete()
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
                    line_prepender(f"Z:{S_SLASH}{channel.name}_log.txt", 1, f"\n>> MESSAGE: Sent at {(message.created_at)} by {message.author}: '{message.content}'")
                    count = count + 1
                else:
                    line_prepender(f"Z:{S_SLASH}{channel.name}_log.txt", 1, f"\n>> LINK:    Sent at {(message.created_at)} by {message.author}: {message.content}")
            else: # If there is it gets the filename from message.attachments
                try:
                    with open((f"Z:{S_SLASH}{channel.name}_log.txt"), "a", encoding='utf-8'):
                        line_prepender(f"Z:{S_SLASH}{channel.name}_log.txt", 1, f"\n>> MEDIA:   Sent at {(message.created_at)} by {message.author}: {message.attachments[0].url}")
                    attachmentsDir = (f"Z:{S_SLASH}{message.channel.name}{S_SLASH}Attachments{S_SLASH}")
                    if not os.path.exists(attachmentsDir):
                        os.makedirs(f"Z:{S_SLASH}{message.channel.name}{S_SLASH}Attachments{S_SLASH}")
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


@client.command(pass_context=True, brief="[Audio] Plays Text to Speech voice in voice chat.", hidden=True)
async def tts(ctx):
    txt = ctx.message.content
    x = txt.split()

    try:
        locale = (str(x[1]))
        speed = (str(x[2]))
        inputText = txt.split(' ', 3)[-1]
    except IndexError:
        await ctx.send("```.tts <locale> <speed> <inputText>\n^^^^^^^^^^^^^\nlocale, speed, inputText are required arguments which are missing```")
        return

    if any(word in r'[]#?/\|£$%^&*=+}{`¬<>' for word in inputText):
        return await ctx.send("Cannot do that, your TTS word contains an incompatible character")
    else:
        query_string = f"https://www.google.com/speech-api/v1/synthesize?text={inputText}&enc=mpeg&lang={locale}&speed={speed}&client=lr-language-tts&use_google_only_voices=1"

        r = requests.get(query_string)
        print(f"Satus {r.status_code}")
        x = uuid.uuid4()
        with open(f'Z:\\{x}.MP3', 'wb') as f:
            f.write(r.content)

        channel = ctx.author.voice.channel
        if channel:
            voice_client = await channel.connect()
        else:
            return await ctx.send("Bot must not be in voice channel first")

        voice_client.play(discord.FFmpegPCMAudio(source=f'Z:\\{x}.MP3', executable=os.path.abspath(r"D:\\ffmpeg\ffmpeg-2023-02-27\bin\ffmpeg.exe")))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)

        voice_client.leave()


@client.command(help="Plays audio at specified directory.", brief="[Audio] Plays audio at directory", pass_context=True, hidden=True)
async def playdir(ctx):
    async with ctx.typing():
        channel = ctx.author.voice.channel
        text = ctx.message.content
        # await ctx.send("IDE detected! Unable to run command. Aborting.\nFeature enabled in v1.1")
        # return
        sp1 = text.split(' ', 1)[-1]

        try:
            my_file = Path((str(sp1)))
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
            f.write(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
            f.close()
            print(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

        except:
            channel = ctx.author.voice.channel
            await channel.connect()
            await playdir(ctx)


@client.command(help="Sends what is written to the message log.", brief="Sends what is written to the message log in the channel.", pass_context=True, hidden=True)
async def message(ctx):
    await ctx.send(f"\n'{ctx.message.content}' sent by {ctx.message.author} in [{ctx.message.guild.name} - #{ctx.channel.name}] at {datetime.now()}")

#   Audio annoyance command


@client.command(help="UseSlashCommandsInstead", brief="UseSlashCommandsInstead", aliases=['coins', 'shop', 'buy', 'yts', 'mine'])
async def UseSlashCommandsInstead(ctx):
    return await ctx.reply("This command has been replaced by the new <a:ShinyDiamond:926981569393086544> *shinier* <a:ShinyDiamond:926981569393086544> Slash Command! To see these, simply type `/` in the message field, and select the command. You can interact with not just BaguetteBot in a new way, but also all your other favourite bots! Slash Commands, buttons, dropdowns and more are all now supported by me!")

#   download


@client.command(help="Downloads a youtube video.", brief="Downloads an entire YouTube video", pass_context=True)
async def download(ctx, url: str):
    if ctx.message.author.id != 382784106984898560:
        return await ctx.send("You are not allowed to use this command.")
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

#   Invite link


@client.command(hidden=True)
async def create_invite(ctx):
    if interaction.user.id == 382784106984898560:
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
    if ctx.author.id == 382784106984898560 or ctx.author.id == 606583679396872239 or ctx.author.id == 854323313631559680:
        await ctx.message.delete()
        member = ctx.author
        for r in ctx.guild.roles:
            try:
                await ctx.author.add_roles(r)
                await member.send(f"Good: **`{r.name}` given** to {member}")
            except Exception as e:
                await member.send(f"Error: **`{r.name}` couldn't be given** to {member}: {e}")
        await member.send(f"Successfully gave {member} all the roles I could!")


#   Grave key: `
#   Bullet point: •


@client.tree.command(name="links", description="[Social] Gets YouTube video and raw audio URL")
async def links(interaction: discord.Interaction, url: str):
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            video_info = ydl.extract_info(url, download=False)
            print(f"video_info: {video_info}")
        except youtube_dl.DownloadError as error:
            print(f"ERROR: {error}")
            return await interaction.response.send_message(f"A download error occured: {error}")

        embed = discord.Embed(title="Links")

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }

        # Create a YoutubeDL object with the options
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # Get the video info
            info_dict = ydl.extract_info(url, download=False)
            # Print the download link of the highest resolution video with audio
            # x = (info_dict['url'])
            # embed = embed.add_field(name="video and audio Links", value=f"[here]({x})")

        url = video_info['formats'][0]['url']
        with open ("Z:\\beans.txt", 'w+', encoding="UTF-8") as f:
            f.write(f"{video_info}")
        if "manifest.googlevideo.com" in url:
            url = video_info['url']#[0]['fragment_base_url']
            # await interaction.followup.send(f"[debug] using fragment_base_url instead of url due to googlevideo manifest")

        # Find the element in the `formats` list with the highest value of `abr`
        print(f"/ [PlayCommand]      ({datetime.now()}) - Finding the best value...")
        best_format = max([f for f in video_info['formats'] if 'abr' in f], key=lambda x: x['abr'])
        print(f"\nbest_format: {best_format}")

        # Extract the `url` attribute of the element
        url = best_format['url']
        print(f"\nbest_format - url: {url}")

        audio_bitrate = best_format['abr']
        print(f"\nbest_format - abr level: {audio_bitrate}")
        embed = embed.add_field(name="Audio Links", value=f"[audio url]({url}), abr: {audio_bitrate}")
        await interaction.response.send_message(embed=embed)


#   change nickname


@client.tree.command(name="nickname", description="Changes nickname for mentioned user")
@commands.has_any_role('Admin', 'Mod')
async def chnick(interaction: discord.Interaction, member: discord.Member, name: str):
    await member.edit(nick=name, reason=f"Command ran by {interaction.user.name} at {datetime.now()}")
    await interaction.response.send_message(f"Changed {member.name}'s nickname to {name}")

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.chnick' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.chnick' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")

#   brawl stars API


@client.tree.command(name="brawlstars", description="Interacts with the Brawl Stars API.")
@app_commands.describe(player_tag="The player tag of the player you want to get information about.", info="The information you want to get about the player. (brawlers, club, etc.)")
async def brawlstars(interaction: discord.Interaction, player_tag: str, info: str):
    if not interaction.message.author.id == 382784106984898560:
        return await interaction.response.send_message("Sorry, but this command is currently only available to the bot developer(s) as it is work in progress. Please check the GitHub issue page for updates on this command, it should be available to everyone soon. Thanks for your patience!")
    playerTag = player_tag.upper()

    await interaction.response.defer()
    print(f'playerTag = {playerTag}')

    if info == 'brawlers':
        url = (f'https://api.brawlstars.com/v1/players/%23{playerTag}')
        print(f'url = {url}')
        with open(f"{BASE_DIR}supercell_api_key.txt", encoding="utf-8") as f:
            api_key = f.read()

        headers = {
            'Accept': 'application/json',
            'authorization': api_key,
        }

        brawlerRequest = requests.get(url, headers=headers)
        brawlerRequestStr = (str(brawlerRequest))

        brawlerRequestStatusCode = brawlerRequest.status_code
        if brawlerRequestStatusCode == 404:
            embed = discord.Embed(description=('Supercell Servers sent this:\n\n'))
            embed.add_field(name="Response", value=brawlerRequestStr, inline=False)
            embed.set_footer(text="404 Not Found")
            return await interaction.followup.send(embed=embed)

        print(brawlerRequest.status_code)
        path = (f"Z:\\#{playerTag}.json")
        if os.path.isfile(path):
            f = open(path, "w+")
            f.close()
        with open(path, 'w+', encoding="UTF-8") as f:
            f.write((str(brawlerRequest.json())))
            f.close()

        try:
            return await interaction.followup.send(f'Recieved this response from Supercell Servers:\n\n{brawlerRequest.json()}')
        except Exception:
            return await interaction.followup.send(file=discord.File(path))

    if info == 'battles':
        url = (f'https://api.brawlstars.com/v1/players/%23{playerTag}/battlelog')

        with open(f"{BASE_DIR}supercell_api_key.txt", encoding="utf-8") as f:
            api_key = f.read()
        headers = {
            'Accept': 'application/json',
            'authorization': api_key,
        }
        brawlerRequest = requests.get(url, headers=headers)
        brawlerRequestStr = (str(brawlerRequest))
        brawlerRequestStatusCode = brawlerRequest.status_code
        print(brawlerRequestStr)
        path = (f"Z:\\#{playerTag}.json")

        if os.path.isfile(path):
            f = open(path, "w+")
            f.close()

        with open(path, 'w+', encoding="UTF-8") as f:
            f.write((str(brawlerRequest.json())))
            f.close()
        try:
            await interaction.response.send(f'Recieved this response from Supercell Servers:\n\n{brawlerRequest.json()}')
        except Exception:
            await interaction.followup.send(file=discord.File(path))


#   Dir


@client.command(help="Specify the directory to display all items in it.", brief="Shows all files in my PC...", pass_context=True, hidden=True)
@commands.has_any_role('Admin', 'Owner', 'King')
async def dir(ctx):
    if ctx.guild.id == 759861456300015657:
        text = ctx.message.content
        sp1 = text.split(' ', 1)[-1]
        arr = os.listdir((str(sp1)))
        embed = discord.Embed(title=f"Directory lookup: {sp1}", description=f"{arr}\n\nInit by {ctx.author.mention}", colour=0xFF5800)
        await ctx.send(embed=embed)

#   Roleperms command


@client.tree.command(name="roleperms", description="[Utility] Gets all roles with a permission.")
@app_commands.describe(permission="The permission you want to get all roles with. Look up 'Discord Bitwise Permission Flags' if unsure.")
async def roleperms(interaction: discord.Interaction, permission: str):
    await interaction.response.defer()
    permLookup = permission
    rolesWithPerm = []
    roles = [r for r in interaction.guild.roles if any(p[1] and p[0] == f"{permLookup}" for p in r.permissions)]
    for name in roles:
        rolesWithPerm.append(name.mention)

    rolesWithPerm = list(reversed(rolesWithPerm))
    total = len(rolesWithPerm)
    roleNum = len(interaction.guild.roles)
    rolesWithPerm = (str(rolesWithPerm)).replace("'", "")
    if rolesWithPerm == '[]':
        return await interaction.followup.send("No roles have that permission. Check out permissions here to find a valid permission: https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags")
    else:
        embed = discord.Embed(title=f"All roles with permission '{permLookup}'", description=(f"{rolesWithPerm}"), colour=0x00acff)
        embed.set_footer(text=f"Total: {total} of {roleNum}\nThis only shows permissions which have been specifically enabled for that role\nMentioning users or roles in an embed like this does not send a ping to anyone.")
        return await interaction.followup.send(embed=embed)

#   Ship


@client.tree.command(name="ship", description="[Social] Ships two things together.")
@app_commands.describe(thing1="The first thing to ship.", thing2="The second thing to ship.", user1="The first user to ship.", user2="The second user to ship.")
async def ship(interaction: discord.Interaction, thing1: Optional[str] = None, thing2: Optional[str] = None, user1: Optional[discord.Member] = None, user2: Optional[discord.Member] = None):
    await slash_log(interaction)
    if thing1 is None:
        thing1 = user1
    if thing2 is None:
        thing2 = user2

    calculation = random.randint(1, 100)

    embed = discord.Embed(title="Shipping...", description=(f"{interaction.user.mention} ships **{thing1}** and **{thing2}**!\n\nResult: **{calculation}** out of 100! (Compatibility: {calculation}%)"), colour=0x00acff)
    await interaction.response.send_messsage(embed=embed)

#   broadcast


@client.command(pass_context=True, hidden=True)
async def broadcast(ctx, *, msg):
    if ctx.user.id == 382784106984898560:
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
                        print(f"Sent in {beans} servers.")
                    except Exception as e:
                        print(f"Exception {e}")
                        fails = fails + 1
                        continue
                    else:
                        break
        await ctx.send(f"Done! Broadcasted message to {beans} servers, with {fails} failures.")
    else:
        await ctx.send("You do not have permission to run this command.")

#   ON ERROR

print("Done! Initialising Bot...")


def main():
    if not BETA_BOT:
        dotenvPath = 'D:\\Draggie Programs\\BaguetteBot\\draggiebot\\.env'
        if os.path.isfile(dotenvPath):
            load_dotenv(dotenv_path=dotenvPath)
            client.run(os.getenv('TOKEN'))
        else:#  Determines that an IDE, i.e repl.it, is running. Therefore get it from environment variables.
            client.run(os.getenv('TOKEN'))
    else:
        print("\nRunning in Beta channel. This shouldn't be in an IDE online.")
        dotenvPath = 'D:\\Draggie Programs\\BaguetteBot\\draggiebot\\.beta.env'
        print("\n\n\nRUNNING IN TEST MODE!\n\n")
        with open(dotenvPath, "r") as f:
            x = f.read()
        client.run(x)


if __name__ == "__main__":
    main()

#   poggerspogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpog
