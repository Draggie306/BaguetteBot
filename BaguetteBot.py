DraggieBot_version = "v1.3"
build = ""
beta_bot = False

"""
To complete:
Shop page 2 with buttons (Convert nolwennium, custom name (1000 coins), buy multipliers???)
"""

print("Importing all modules...\n")
import      discord, asyncio, os, time, random, sys, youtube_dl, requests, json, uuid, difflib, termcolor, psutil, secrets, logging, subprocess, math, openai
#from        discord_slash import SlashCommand
#from        discord_slash.utils.manage_commands import create_option, create_choice
from        discord.ext import commands
#from        discord.ui import Select, Button, View
from        discord.errors import Forbidden#                                    CMD Prerequisite: py -3 -m pip install -U discord.py
from        dotenv import load_dotenv#                                          CMD Prerequisite: py -3 -m pip install -U python-dotenv
from        youtube_search import YoutubeSearch#                                PIP:            python -m ensurepip
from        datetime import datetime#                                           UPDATE PIP:     python -m pip install --upgrade pip
from        json import loads
from        pathlib import Path
from        io import StringIO
from        discord import app_commands
from        typing import Literal, Optional

global voiceVolume, upvote, downvote, Croissants, draggie, hasMembersforGlobalServer, nolwenniumUserDir, rolePrivate, hasPrivate, hasAdmin, bot_events
bot_events = 0
voiceVolume = 0.3
Croissants = [796777705520758795, 821405856285196350, 588081261537394730]
croissant_names = ["ETigger_4", "Josephy Spaghetti", "tigger_4"]
tester_guilds = [384403250172133387, 759861456300015657, 833773314756968489, 921088076011425892] # Server IDs where I'm an admin so can change stuff before it reaches other servers
brigaders = [759861456300015657]
random_word = ["Expulser!", "Troubador!", "Delenda!", "Vincit!", "Consilium!", "Renovatur!", "Acheronta!", "Oderint!"]
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
idk_what_u_mean = ("I don't know what you mean. Please use **buy/set/lookup** in the `operation` Choice. Make sure the `target_id` Choice is a valid user ID. The `mod_value` Choice does not need to have any conditional arguments if `operation` is `lookup`.")

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
    handler = logging.FileHandler(filename=f'{minified_base_directory}Logs\\{DraggieBot_version}{build}-{time.time()}.log', encoding='utf-8', mode='w')
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
    handler = logging.FileHandler(filename=f'.useful{s_slash}{DraggieBot_version}{build}-{time.time()}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    import keep_alive
    keep_alive.keep_alive()


#if running_locally:
#    subprocess.Popen(['java', '-jar', f'{base_directory}GitHub\\BaguetteBot\\Lavalink.jar'])

intents = discord.Intents().all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

client = discord.Client(intents=intents)
client = commands.Bot(
    command_prefix=commands.when_mentioned_or('.'),
    case_insensitive=True,
    intents=intents,
    description=f"BaguetteBot - version {DraggieBot_version}{build} - d.py {discord.__version__}",
    help_command=commands.DefaultHelpCommand(no_category='Dot Commands')
    )


print("Done!\nSlash commands initialising...")


###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

"""@client.tree.command(name="nsfw", description="haha yes")
async def nsfw(interaction: discord.Interaction, fruits: Literal['Wattson', 'Chun-Li', 'Do not click me']):
    button_watt = Button(label="Wattson", style=discord.ButtonStyle.red, emoji="⚡")
    button_chun = Button(label="Chun-Li", style=discord.ButtonStyle.blurple, emoji="🍑")
    button_sus = Button(label="Do not click me", url="ibaguette.com")


    await interaction.response.send_message(f'Your favourite fruit is {fruits}.')

    select = Select(options=[
        discord.SelectOption(label="Wattson", emoji="⚡", description="My gal Wattson Apex legen"),
        discord.SelectOption(label="Chun-Li", emoji="🍑", description="No way right now lmao")
    ])

    view = View()
    view.add_item(button_watt, button_chun, button_sus)"""

@client.tree.command(name="command-2")
@app_commands.guilds(discord.Object(id=384403250172133387))
async def my_private_command(interaction: discord.Interaction):
    """ /command-2 """
    await interaction.response.send_message("Hello from private command!", ephemeral=True)

@client.tree.command()
async def my_command(interaction: discord.Interaction) -> None:
  await interaction.response.send_message("Hello from my command!")

@client.tree.command(name="sync-commands", description="[Admin] Sync edited client tree commands to Discord servers")
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 382784106984898560:
        await interaction.response.defer() # Defer due to rate limiting being annoying sometimes grr
        x = await client.tree.sync()
        print(x)
        await interaction.followup.send(f"Synced client tree commands. {x}") # Must use interaction.followup.send after a defer
    else:
        await interaction.response.send_message("This is bot admin only.")


@client.tree.command(name="stats", description="Just a few useful bot statistics.")
async def stats(interaction: discord.Interaction):
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
    await interaction.response.send_message(embed=embed)

    with open(GlobalLogDir, "a", encoding="UTF-8") as f:
        f.write(f"\nSLASH COMMAND RAN -> '.stats' ran by {interaction.user.id} in {interaction.guild_id} at {datetime.now()}")

#   baguettes
    
@client.tree.command(name="baguette", description="Sends a random baguette image.")
async def baguette(interaction: discord.Interaction):
    await interaction.response.send_message(f"Use French Cuisine bot for this and much more! The commad is `/baguette`.\nAdd it! https://ibaguette.com/api/BotInvs/FrenchCuisine&permissions=V2")


@client.tree.command(name="snowflake", description="Convert a Discord snowflake into a DateTime object, accurate to the second.")
@app_commands.describe(flake="Input the snowflake here, something like '382784106984898560'.")
async def snowflake(interaction: discord.Interaction, flake: str):
    snowflake = int(flake)
    try: #      Try and change the message content after the '.snowflake' into an integer.
        unix_timestamp = ((1420070400000 + int(((f"{(snowflake):b}")[:-22]), 2)) / 1000)
        stringe = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y,%m,%d,%H,%M,%S')
        stringe = stringe.split(",")
        string_to_send = (f"Exact: <t:{round(unix_timestamp)}>:{stringe[5]}. Relative: <t:{round(unix_timestamp)}:R>.")
        await interaction.response.send_message(string_to_send)
        print(string_to_send)
    except:#    If it doesn't work, then we can deduce that a number hasn't been inputted.
        await interaction.response.send_message("That isn't a valid integer to convert into a date.")

#   coins

@commands.Cog.listener("on_app_command_error")
async def get_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    await interaction.response.send_message(f'An error occured: {error}')

@client.tree.command(name="coins", description="Shows coin balance. If above a threshold, shows items to buy!", )
@app_commands.describe(operation="[Admin Only] set/add/lookup.", target_id="[Admin Only] Enter the user id for the operation to target", mod_value="[Admin Only] Use this as the value for the operation")
async def coins(interaction: discord.Interaction, operation: Optional[str], target_id: Optional[str], mod_value: Optional[str]):
    if interaction.guild_id == 759861456300015657:
        print(operation,target_id,mod_value)
        member_role = discord.utils.get(interaction.guild.roles, name=f"Member")
        staff_role = discord.utils.get(interaction.guild.roles, id=963738031863525436)
        owner_role = discord.utils.get(interaction.guild.roles, id=759861763247570946)
        if member_role in interaction.user.roles or staff_role in interaction.user.roles or owner_role in interaction.user.roles:
            print(interaction.user.id)
            authorID = interaction.user.id
            #await ctx.send("Coins earned before 30/07/2021 are not available to use. This is a known bug and will be fixed later. You have not lost any Coins, but you cannot buy anything with your old balance. New Coins will be added to your old Coins.")
            userID = authorID
            user = interaction.user
            serverID = interaction.guild_id
            #print (serverID)

            coinBal = await get_coins(serverID, interaction.user.id)

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

            with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                nolwennium_bal = round(float(nolwennium_balance_file.read()), 2)
                nolwennium_balance_file.close()
            
            if serverID == 384403250172133387 or serverID == 759861456300015657:
                canRunCommand = discord.utils.find(lambda r: r.name == 'Member', interaction.guild.roles)
                canRunCommand2 = discord.utils.find(lambda r: r.name == 'Owner', interaction.guild.roles)
                if canRunCommand or canRunCommand2 in user.roles:
                    try:
                        #	List of stuff BEFORE showing the user their balance
                        word1 = operation
                        userID = target_id
                        amount = mod_value

                        if interaction.user.guild_permissions.administrator == True:
                            if word1.lower() == 'set':
                                if not amount or userID:
                                    return await interaction.response.send_message(idk_what_u_mean)
                                users_coins = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{userID}.txt")
                                old_coins = get_coins(interaction.guild_id, interaction.user.id)
                                with open(users_coins, 'w+') as f:
                                    f.write(str(amount))
                                new_coins = get_coins(interaction.guild_id, interaction.user.id)
                                return await interaction.response.send_message(f"Successfully set the user's coins from {old_coins} to **{new_coins}**.")
                            
                            if word1.lower() == 'add':
                                if not amount or userID:
                                    return await interaction.response.send_message(idk_what_u_mean)
                                added_balance = update_coins(interaction.guild_id, interaction.user.id, int(amount))
                                return await interaction.response.send_message(f"Successfully added {amount} Coins to the user. They now have **{added_balance}**!")

            
                            if word1.lower() == 'lookup':
                                if not amount or userID:
                                    return await interaction.response.send_message(idk_what_u_mean)
                                return await interaction.response.send_message(f"<@{userID}> has **{get_coins(interaction.guild_id, interaction.user.id)}** Coins.")
                            else:
                                return await interaction.response.send_message(idk_what_u_mean)

                        else:
                            await interaction.response.send_message("You don't have full administrator privileges to run this command. Try `/coins` without any added options?")

                    except Exception:#		AFTER the list of alternate options has been checked; the user just wants their balance.
                        hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                        hasKnight = discord.utils.find(lambda r: r.name == 'Knight', interaction.guild.roles)
                        hasBaron = discord.utils.find(lambda r: r.name == 'Baron', interaction.guild.roles)
                        hasViscount = discord.utils.find(lambda r: r.name == 'Viscount', interaction.guild.roles)
                        hasEarl = discord.utils.find(lambda r: r.name == 'Earl', interaction.guild.roles)
                        hasMarquess = discord.utils.find(lambda r: r.name == 'Marquess', interaction.guild.roles)
                        hasDuke = discord.utils.find(lambda r: r.name == 'Duke', interaction.guild.roles)
                        hasPrince = discord.utils.find(lambda r: r.name == 'Prince', interaction.guild.roles)
                        hasKing = discord.utils.find(lambda r: r.name == 'King', interaction.guild.roles)
                        hasAdmin = discord.utils.find(lambda r: r.name == 'Admin', interaction.guild.roles)

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
                            await interaction.response.send_message("**WARNING! This server has not been optimised for this command, errors may be encountered.**")
                        
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
                        #await interaction.response.send_message(f"The user's top role is {topRole_name}")
                        nextRole = roles.Roles_order_List[(roles_tier + 1)]
                        next_available_role_cost = roles.Roles_Cost[(roles_tier + 1)]

                        #await interaction.response.send_message(f"the next role is {nextRole} which will cost {roles.Roles_Cost[(roles_tier + 1)]} coins. this means they are {next_available_role_cost - int(coinBal)} coins away.")

                        if roles_tier != -1:
                            roles_liste = ""

                            for i in range((roles_tier + 1)):
                                roles_liste = (f"{roles_liste}" + f"{(roles.Roles_order_List[i])}: Unlocked! 🔓\n")
                                i = i + 1
                            #await interaction.response.send_message(roles_liste)

                            with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                                nolwennium_balance = round(float(nolwennium_balance_file.read()), 2)
                                nolwennium_balance_file.close()

                            finalSum = f"{roles_liste}" + f"{nextRole}: {roles.Roles_Cost[(roles_tier + 1)]} {emoji_Coins} 🔒"

                            if "🔓" not in finalSum:
                                if f"{emoji_Coins}" not in finalSum:
                                    finalSum = f"***You have bought all possible roles! Maybe some more will come out in the future...***"
                        else:
                            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {emoji_Coins} coins and {nolwennium_bal} {emoji_Nolwennium} Nolwennium available to spend."), colour=0xFFD700)
                            embed.add_field(
                                name="Items curently available for you to buy:",
                                value=f"**Citizen**: FREE {emoji_Coins}\n\nType **.buy citizen** to start ascending through purchasable roles!",
                                inline=False
                                )
                            embed.set_footer(text=(f'Type ".buy item" to buy your selected item! For example, .buy citizen.\nYou can buy roles for Coins in this server, and use {name_Nolwennium} to run bot commands (in all servers).'))
                            await interaction.response.send_message(embed=embed)
                            return
                        
                        embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {emoji_Coins} coins and {nolwennium_bal} {emoji_Nolwennium} Nolwennium available to spend."), colour=0xFFD700)
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
                        await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("You do not have permission to access the shop interface.")
            else:
                nolwenniumUserDirectory(interaction)
                my_file = Path(nolwenniumUserDir)
                if not my_file.is_file():
                    nolly = "0"
                else:
                    with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                        nolwennium_balance = f.read()
                        nolwennium_balance_file.close()
                    nolly = f"{nolwennium_balance} {emoji_Nolwennium}"
                await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check https://ibaguette.com/discord for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {emoji_Nolwennium}")
        else:
            await error_code(interaction, 1)

#   buy

@client.tree.command(name="buy", description="Shows your balance, and available to buy items.")
@app_commands.describe(item="Enter the item to buy here")
async def buy(interaction:discord.Interaction, item: str):
    if interaction.guild_id in tester_guilds:
        canRunCommand = discord.utils.find(lambda r: r.name == 'Member', interaction.guild.roles)
        owner = discord.utils.find(lambda r: r.name == 'Owner', interaction.guild.roles)
        staff = discord.utils.find(lambda r: r.name == 'Staff', interaction.guild.roles)
        can_access_shop_ui = False
        """
        if owner in interaction.user.roles:
            print("Owner is in the roles list")
            await interaction.response.send_message("You already have owner permissions, this overrides the shop's items")
            can_access_shop_ui = True
        if staff in interaction.user.roles:
            print("Staff is in the roles list")
            await interaction.response.send_message("You already have staff permissions, this overrides the shop's items")
            can_access_shop_ui = True"""
        if canRunCommand in interaction.user.roles:
            print("Member is in the list")
            can_access_shop_ui = True
        if can_access_shop_ui:
            member = interaction.user
            authorID = interaction.user.id
            serverID = interaction.guild_id
            determiner = item.lower()

            filedir = (f"{base_directory}Servers{s_slash}{serverID}{s_slash}Coins{s_slash}{authorID}.txt")
            coinBal = get_coins(interaction.guild_id, interaction.user.id)

            if determiner == "2":
                await extended_shop(interaction)

            if determiner == 'citizen':
                cost = 1
                hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                if hasCitizen in member.roles:
                    await interaction.response.send_message("You can't buy Citizen, you already have it!")
                    return
                
                coinBal = int(coinBal) - cost
                await update_coins(interaction.guild_id, interaction.user.id, -cost)
    
                role = discord.utils.get(interaction.guild.roles, name="Citizen")
                await member.add_roles(role)
                embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought Citizen for free! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                embed.add_field(name="Perks", 
                    value=f"• Above Member in the Member List\n• Custom nickname\n• Add reactions\n• Bonus {name_Nolwennium}", 
                    inline=False)   
                await interaction.response.send_message(embed=embed)
                return

#           KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT

            if determiner == 'knight':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Citizen"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Create private threads", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Citizen before {roleName}.")
                    return
                return

#           BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON 

            if determiner == 'baron':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Knight"))
                    await member.add_roles(role)

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                            value=f"Everything in Citizen, and:\n• Use external stickers\n• Increased Coins earning\n• Bonus {name_Nolwennium}", 
                            inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Knight before {roleName}.")
                    return
                return

#           VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT 

            if determiner == 'viscount':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Baron, and:\n• Use TTS messages\n• Use server activities", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Baron before {roleName}.")
                    return
                return

#           EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL

            if determiner == 'earl':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)
                    
                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Viscount"))
                    await member.add_roles(role)

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Viscount, and:\n• Add and edit server events", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Viscount before {roleName}.")
                    return
                return

#           MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS 

            if determiner == 'marquess':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)
                    
                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Baron"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Earl, and:\n• View detailed server statistics\n• Access to some more stuff, you'll figure it out", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Earl before {roleName}.")
                    return
                return

#           DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE 

            if determiner == 'duke':
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
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)
                    
                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Marquess"))

                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Marquess, and:\n• Mute members\n• Manage threads\n• View private threads\n• Access to history of <#1035684553546809456>", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(f"You must buy Marquess before {roleName}.")
                    return
                return
        
#           PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE 

            if determiner == 'prince':
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
                        await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}.")
                        return
                    coinBal = int(coinBal) - cost
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)
                    
                    role = discord.utils.get(interaction.guild.roles, name=roleName)
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Duke"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Duke, and:\n• Move members in voice channels\n• Use Priority speaker in voice chat\n• Change others' nicknames\n• Time out members if they are being annoying\n• Add emojis and stickers\n• Add custom channels", 
                        inline=False)   
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("You must buy Knight before Prince.")
                return

#           KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING 

            if determiner == 'king':
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
                        await interaction.response.send_message("You do not have enough Coins to buy King.")
                        return
                    coinBal = int(coinBal) - cost
                    await update_coins(interaction.guild_id, interaction.user.id, -cost)
                    
                    role = discord.utils.get(interaction.guild.roles, name="King")
                    await member.add_roles(role)
                    await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Prince"))
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought King for {cost} {emoji_Coins}! Remaining balance: {coinBal} {emoji_Coins}"), colour=0xFFD700)
                    embed.add_field(name="Perks", 
                        value=f"Everything in Prince, and:\n• Deafen members\n• Pin and manage messages\n• Add custom webhooks\n• Add custom bots\n• Add into Other Channels and define permissions", 
                        inline=False)
                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message("You must buy Prince before King.")
                return
            
            if determiner == 'admin':
                await interaction.response.send_message("Required role missing")
            else:
                await interaction.response.send_message(f"**{determiner}** isn't a valid item to buy. Try `Citizen/Knight/Baron/Viscount/Earl/Marquess/Duke/Prince/King/Admin`!")
        else:
            await error_code(interaction, 1)
    else:
        nolwenniumUserDirectory(interaction)
        my_file = Path(nolwenniumUserDir)
        if not my_file.is_file():
            nolly = "0"
        else:
            f = open(nolwenniumUserDir, 'r')
            nolwennium_bal = f.read()
            f.close()
            nolly = f"{nolwennium_bal} {emoji_Nolwennium}"
        await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/baguette for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {emoji_Nolwennium}")

#   setdelay

@client.tree.command(name="slowmode", description="Sets the slowmode in a channel.")
@app_commands.describe(seconds="Input seconds here.")
async def setdelay(interaction: discord.Interaction, seconds:str):
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

    embed=discord.Embed(title="Edited channel info!", description=(f"Set the slowmode delay in this channel to {seconds} seconds!"), colour=0x228B22)
    await interaction.response.send_message(embed=embed)

    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write(f"\nCOMMAND RAN -> '.setdelay {seconds}' ran by {interaction.user} in channel {interaction.channel.mention} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.setdelay {seconds}' ran by {interaction.user} in channel {interaction.channel.mention} at {datetime.now()}")

# EmojiArchiver

@client.tree.command(name="emoji-backup", description="Backs up all your server emojis. This will be retrievable soon.")
@app_commands.describe(guild_id="Enter server ID to grab emojis from")
async def emojis(interaction:discord.Interaction, guild_id: str):
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

    #try:
    #    await interaction.followup.send("Saved all emojis")
    #except Exception as e:
    #    await interaction.followup.send(f"Probably too many emojis. `{e}`")
    await interaction.followup.send(f"Done! Saved {emojis} emojis.")

    if interaction.user.id == 382784106984898560:
        await interaction.response.send_message("Running on all guilds")
        emojis = 0
        guilds = 0
        for guild in client.guilds:
            guilds += 1
            newGuild = client.get_guild(guild.id)
            await interaction.followup.send(f"Getting emojis for {newGuild.id} // {newGuild.name}")
            emoji_list = []
            for emoji in newGuild.emojis:
                emojis += 1
                emoji_list.append(f"{emoji.name} - {emoji.url}") 
                x = requests.get(emoji.url)
                emoji_exturl = emoji.url
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
                    await interaction.followup.send(emoji_list)
            except Exception as e:
                await interaction.followup.send(f"Probably too many emojis. `{e}`")
        await interaction.followup.send(f"Done! Archived {emojis} from {guilds} guilds.")


#   Get messages

@client.tree.command(name="get_messages", description="[Admon Only] Get direct messages sent to a user object")
@app_commands.describe(id="User id to objectify")
async def get_messages(interaction: discord.Interaction, id:str):
    if interaction.user.id == 382784106984898560:
        user1 = await client.fetch_user(int(id))

        dmchannel = await user1.create_dm() # "Create" a DM
        async for message in dmchannel.history(limit=30): # Async through the messages
            await interaction.response.send_message(f"{message.author.name}: `{message.content}`")

#   log search

@client.tree.command(name="logsearch", description="Search the message history for a term. Returns how many times it was sent.")
@app_commands.describe(term="String to search the log for")
async def log(interaction:discord.Interaction, term:str):
    if not interaction.user.guild_permissions.view_audit_log:
        return await interaction.response.send_message("You are missing the required guild persmission: `view_audit_log`.")
    serverID = interaction.guild_id
    
    if not interaction.guild:
        return await interaction.response.send_message("This cannot be used in DMs.")
    
    else:
        serverName = interaction.guild.name
    
    file=open((f"{base_directory}Servers{s_slash}{serverID}{s_slash}Logs{s_slash}MessageLog.txt"),encoding="UTF-8").read().lower()
    count=file.count(term)

    count = count - 1
    
    embed = discord.Embed()
    embed.add_field(name=f"Occurences of '**{term}**':", value=f"{count}", inline=False)
    embed.set_footer(text=f"Not case sensitive. Does not account for bot messages. Searching in server {serverID}/{serverName}.")
    await interaction.response.send_message(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.log' ran by {interaction.user} at {datetime.now()}")
    f.close()

#   ytstream

@client.tree.command(name="play", description="[Audio] Streams YT audio. Sligthly buggy, may die randomly.")
@app_commands.describe(video="What video would you like to search for and play?")
async def play(interaction:discord.Interaction, video:str):
    """This uses `youtube-dl` to extract and get links to a searched term. If the search term is a link with a video ID,
    it will extract straight to that ID. If not, it will search for the most liely video.\n
    When it has found a matching video, its formats are extracted. It then uses list comprehension to filter out any 
    elements in the formats list that do not have the `abr` (audio bitrate) key to prevent errors. The resulting list 
    is then passed to the `max` function. The `max` function then returns the element with the highest value of `abr`, 
    as to get the best quality audio to stream into the `VoiceChannel`. This ensures that the `KeyError` error will not 
    occur, since the list only contains elements that have the `abr`     key."""
    print(f"[SlashCommand] 'play' ran by {interaction.user.id} in {interaction.guild_id}. The search term was '{video}'.")
    if not interaction.user.guild_permissions.stream:
        return await interaction.response.send_message("You are missing the required guild persmission: `stream`.")
    await interaction.response.defer() # Defer due to rate limiting being annoying sometimes grr
    if not interaction.user.id == 382784106984898560:
        return await interaction.response.send_message("Please wait for the official release of BaguetteBot!")
    try:
        voice_client = interaction.guild.voice_client
        voice_client.stop()
    except Exception:
        if not interaction.user.voice:
            return await interaction.followup.send("You aren't in a Voice Channel.")
        channel = interaction.user.voice.channel
        await channel.connect()
        voice_client = interaction.guild.voice_client

    #await interaction.followup.send(f"[debug] Called volume and voiceclient: {voice_client}")
    print(f"[debug] Called volume and voiceclient: {voice_client}")

    searchTerm = video
    millisecs = round(time.time() * 1000)
    if "?v=" in searchTerm:
        vid_id = searchTerm[searchTerm.find("v=")+2:searchTerm.find("v=")+13]
        result = (f'https://www.youtube.com/watch?v={vid_id}')
    else:
        results = YoutubeSearch(searchTerm, max_results=1).to_dict()
        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print(f"\nresult = {result}")
        
    url = result

    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True', 'youtube-skip-dash-manifest': 'True'}

    print("Got YDL_OPTIONS")
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            video_info = ydl.extract_info(url, download=False)
        except youtube_dl.DownloadError as error:
            return await interaction.response.send_message(f"A download error occured: {error}")

        url = video_info['formats'][0]['url']
        with open ("Z:\\beans.txt", 'w+', encoding="UTF-8") as f:
            f.write(f"{video_info}")
        if "manifest.googlevideo.com" in url:
            url = video_info['url']#[0]['fragment_base_url']
            #await interaction.followup.send(f"[debug] using fragment_base_url instead of url due to googlevideo manifest")
            
        # Find the element in the `formats` list with the highest value of `abr`
        print("Finding the best value...")
        info = video_info
        best_format = max([f for f in info['formats'] if 'abr' in f], key=lambda x: x['abr'])

        # Extract the `url` attribute of the element
        url = best_format['url']

        audio_bitrate = best_format['abr']
    
        #await interaction.followup.send(f"[debug] `{url}`")
        print(f"\n\n{url}\n\n")

    print("Extracted info")
    #await interaction.followup.send("[debug] Extracted info")

    #voice_client = await connectToGuildChannel(ctx)
    #volume = await getServerVoiceVolume(ctx)

    try:
        source = discord.FFmpegPCMAudio(source=url)
        #voice_client.source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
        source = discord.PCMVolumeTransformer(source, volume=0.5)
    except Exception as error:
        print(error)
        await interaction.followup.send(f"[debug] An unexpected error has occured and audio cannot proceed to be played: {error}")
    
    voice_client.play(source)    
    voice_client.is_playing()

    #voice_client.play(discord.FFmpegPCMAudio(URL, options=FFMPEG_OPTIONS, executable="D:\\Downloads\\FFMPEG\\bin\\ffmpeg.exe"))
    

    doneMillisecs = round(time.time() * 1000)
    timeDelay = doneMillisecs - millisecs
    video_title = info.get('title')
    
    duration = await duration_to_time(info.get('duration'))

    embed=discord.Embed(title="Playing audio", description=f"**[{video_title}]({info.get('webpage_url')})**", colour=0x228B22)
    embed.add_field(name="Channel", value=f"[{info.get('channel')}]({info.get('channel_url')})")
    embed.add_field(name="Duration", value=duration)
    embed.add_field(name="Views", value=format(int(info.get('view_count')), ","))
    embed.add_field(name="Likes", value=f"{info.get('like_count')}")
    embed.add_field(name="Time taken", value=f"{timeDelay}ms")
    embed.add_field(name="Audio bitrate", value=f"{audio_bitrate} kbps")
    embed.set_thumbnail(url=(info.get('thumbnail')))
    #if int(duration) > 300:
    #    embed.add_field(name="⚠️ Warning", value=f"This video is very long, and may not work properly. If there is no audio, please use another video.", inline=True)
    await interaction.followup.send(embed=embed)
    print("Send embed")

@client.tree.command(name="stop", description="Stops whatever is going on in voice chat")
async def stop(interaction:discord.Interaction):
    if not interaction.user.guild_permissions.stream:
        return await interaction.response.send_message("You are missing the required guild persmission: `stream`.")
    voice_client = interaction.guild.voice_client
    voice_client.stop()
    await interaction.response.send_message((str ("Stopped playing audio.")))
    f = open(GlobalLogDir, "a")
    f.write(f"\nAUDIO COMMAND RAN -> '.stop' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")
    f.close()
    print(f"\nAUDIO COMMAND RAN -> '.stop' ran by {interaction.user} in {interaction.guild_id} at {datetime.now()}")
    return

@client.tree.command(name="bitrates", description="Edit all Voice Channel bitrates")
@app_commands.describe(bitrate="Enter specific bitrate, in bytes/sec. Leave blank or 0 to default to max")
async def bitrates(interaction:discord.Interaction, bitrate: Optional[str]):
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
                except:
                    x = f"Error changing the bitrate of **<#{channel.id}>** to **{specific_bitrate}** bps. (The server limit is between 8000 and {interaction.guild.bitrate_limit}, maybe that's why?)\n{x}"

        except Exception:
            x = f"Could not edit the information of <#{channel.id}>. Maybe the bot doesn't have good permissions?\n{x}"
            await interaction.response.send_message(f"")
    await interaction.response.send_message(x)
    if x == "":
        await interaction.response.send_message("Nothing happened.")

#   Pause/resume audio

@client.tree.command(name="pause", description="[Audio] Pauses or resumes audio being played")
async def pause(interaction:discord.Interaction):    
    voice_client = interaction.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await interaction.response.send_message("*✅ Paused the current audio playing!*")
    if voice_client.is_paused():
        voice_client.resume()
        await interaction.response.send_message("*✅ Resumed playing the audio!*")
    else:
        await interaction.response.send_message("Audio is unable to be paused")

#@client.tree.command(name="settings", description="Edit your BaguetteBot preferences here. Change DMs, role notifications, Coins earning and more.")
#async def settings(interaction:discord.Interaction):
#    await interaction.response.send_message("You have no special preferences loaded. <@382784106984898560> please code this")

#   Nolwennium mine

@client.tree.command(name="mine", description=f"Mines some globalCurrency which can be used to do cool stuff!")
@commands.cooldown(1, 29, commands.BucketType.user)
async def mine(interaction:discord.Interaction):
    print(f"CURRENCY - {name_Nolwennium} > {interaction.user.id} is mining")

    base_mined_amount = random.randint(-5, 88)

    #   Nolwennium UPDATED LOCATION 2/11/2021: {base_directory}Nolwennium{s_slash}
    filedir = (f"{base_directory}Nolwennium{s_slash}{interaction.user.id}.txt")

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
    embed.add_field(name="**Initially Mined**", value=f"{base_mined_amount} {emoji_Nolwennium} {name_Nolwennium}!")

    #   Perform first check if a user is Boosting the server. If so, then give them a big bonus.
    #   If not, check if they have Nitro. If yes, checked by an animated profile picture, encourage to use a Boost.
    if interaction.user.premium_since:
        BoosterBonus = random.randint(30, 150)
        embed.add_field(name="**Server Booster Bonus**", value=(f"{BoosterBonus} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
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
            embed.add_field(name="***You found rare loot!***", value=f"**{bonus_perk}**: {bonus_perk_reward} bonus {name_Nolwennium}!")
            balance = balance + int(bonus_perk_reward)
            bonuses = bonuses + int(bonus_perk_reward)

    #   'balance' takes into account existing balance, read from a file, and bonuses.
    #   'newNumberAfterFee' is calculated initially from the base amount mined.
    new_balance = balance + newNumberAfterFee

    #   Set fields and footers, then send the final compiled result.
    embed.add_field(name="**Total Balance**", value=(f"{(round (new_balance, 3))} {emoji_Nolwennium} {name_Nolwennium}"), inline=False)
    embed.set_footer(text=f"ID: {interaction.user.id} | Bonuses ({bonuses}) + base: ({base_mined_amount}) = {bonuses + base_mined_amount}")

    await interaction.response.send_message(embed=embed)

    #   Write balance and globally log it!
    f = open(filedir, 'w+')
    f.write(str(new_balance))
    f.close()
    f = open(GlobalLogDir, "a", encoding='utf-8')
    f.write(f"COMMAND RAN -> '.mine' ran by {interaction.user} in {interaction.guild.id} at {datetime.now()}")
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
    print(f"CURRENCY - {name_Nolwennium} > {interaction.user.id} has gained {newNumberAfterFee} {name_Nolwennium} (fee: {fee}). Their total is {new_balance}")


#   yn

@client.tree.command(name="yes-no", description="Randomly answers yes or no.")
async def yn(interaction:discord.Interaction):
    list_test = ["No!", "Of course not!", "Certainly not.", "Definitely not!", "Obviously not.", "Nah!", "Nope.", "Hell nah...", 
                "Yes!", "Obviously!",   "Of course!",       "Certainly!",       "Definitely!",  "Without a shadow of a doubt!", "Yessir!"]
    await interaction.response.send_message(random.choice(list_test))

    print (f"\nCOMMAND RAN -> '.yn' ran by {interaction.user}")
    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.yn' ran by {interaction.user} at {datetime.now()}")
    f.close()

#   brawlstars

@client.tree.command(name="brawlstars", description="?")
async def BrawlStars(interaction:discord.Interaction):
    if interaction.guild_id == 759861456300015657:
        num_lines = sum(1 for line in open (f"C:{s_slash}Users{s_slash}Draggie{s_slash}iCloudDrive{s_slash}iCloud~is~workflow~my~workflows{s_slash}Brawl Stars Counter.txt"))
        await interaction.response.send_message(f"I have opened Brawl Stars ***{num_lines}***  times since the 19th October 2020.")
        f = open(GlobalLogDir, "a")
        f.write(f"\nCOMMAND RAN -> '.lines' ran by {interaction.user} at {datetime.now()}")
        f.close()


#   vbuck calc

@client.tree.command(name="vbucks", description="Calculates GBP -> V-Bucks")
async def vbucks(interaction:discord.Interaction):
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

@client.tree.command(name="vbucks-usd", description="Converts USD into VBucks")
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

@client.tree.command(name="settings", description="Edit a ton of the bot's settings here. [Ephemeral]")
async def settings(interaction:discord.Interaction):
    user_settings_json_path = f"{base_directory}Users{s_slash}JSONSettings{s_slash}{interaction.user.id}.json"
    # Check if the file exists
    if not os.path.exists(user_settings_json_path):
        # Create the file with default values
        with open(user_settings_json_path, 'w') as f:
            json.dump(default_user_settings, f)

    # Read the JSON file
    with open(user_settings_json_path, 'r') as f:
        settings = json.load(f)

    string = "This message has buttons!"

    embed=discord.Embed(title="BaguetteBot Settings", description="Use the buttons to interact and change these settings. These apply to all servers.")
    view=discord.ui.View()

    for key, value in settings.items():
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

        style=discord.ButtonStyle.green if value == "true" else discord.ButtonStyle.red
        view.add_item(OptionButton(label=key, style=style))
        #OptionButton(label=key, style=style)

    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)



###########################################################################################################################################################
#   Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands Slash Commands
###########################################################################################################################################################

print("Done!\nDefining function and constants...")



class OptionButton(discord.ui.Button):  
    def __init__(self, label:str, style:discord.ButtonStyle):
        super().__init__(label=label, style = style)
    async def callback(self, interaction):
        try:
            with open(f"{base_directory}Users{s_slash}JSONSettings{s_slash}{interaction.user.id}.json", 'r') as f:
                settings = json.load(f)
        except FileNotFoundError:
            with open(f"{base_directory}Users{s_slash}JSONSettings{s_slash}{interaction.user.id}.json", 'w') as f:
                json.dump(default_user_settings, f)
            
        def enableanddisable(self, text: str):
            if settings[text] == "false":
                print(f"[UserSettings] {text} is being changed to True for user {interaction.user.id}")
                settings[text] = "true"
            elif settings[text] == "true":
                print(f"[UserSettings] {text} is being changed to False for user {interaction.user.id}")
                settings[text] = "false"
            
            with open(f"{base_directory}Users{s_slash}JSONSettings{s_slash}{interaction.user.id}.json", 'w') as f:
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
    
        with open(f"{base_directory}Users{s_slash}JSONSettings{s_slash}{interaction.user.id}.json", 'r') as f:
            settings = json.load(f)

        embed=discord.Embed(title="BaguetteBot Settings", description="Use the buttons to interact and change these settings. These apply to all servers.")
        view=discord.ui.View()
        for key, value in settings.items():
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
            if key == "User Analytics":
                key = "contribute_to_statistics"
    
            embed.add_field(name=key, value="🔴 Disabled" if value == "false" else "🟢 Enabled")
            style=discord.ButtonStyle.green if value == "true" else discord.ButtonStyle.red
            view.add_item(OptionButton(label=key, style=style))
        
        await interaction.response.edit_message(embed=embed, view=view)

#   extended shop for buy command below

async def extended_shop(ctx):
    embed = discord.Embed(title="*EXTENDED SHOP*", description=(f"Welcome to the extended shop."), colour=0xFFD700)

    f = open(coinDir, 'r')
    coinBal = f.read()
    f.close()
    f = open(nolwenniumUserDir, 'r')
    nolwennium_bal = f.read()
    f.close()

    embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {emoji_Coins} coins and {nolwennium_bal} {emoji_Nolwennium} Nolwennium available to spend."), colour=0xFFD700)
                            
    await ctx.send(embed=embed)



# Define the default user settings
default_user_settings = {
    "send_generalised_dms": "false",
    "get_dm_notification_for_role_addition": "false",
    "get_dm_notification_for_role_removal": "false",
    "get_dm_notification_for_coin_threshold": "false",
    "reminders_for_voice_time": "false",
    "participate_in_experiments": "false",
    "can_use_shop_section_2": "true",
    "contribute_to_statistics": "true",
}

# Function to save the user settings to a JSON file
def save_user_settings(user_id, settings):
    # Read the existing JSON file, if it exists
    filepath = f"{base_directory}Users\\{user_id}"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Set the default values for any keys that are not present in the settings dictionary
    for key, value in default_user_settings.items():
        settings.setdefault(key, value)

    # Add the user ID and settings to the dictionary
    data[user_id] = settings

    # Write the dictionary to a JSON file
    with open(filepath, "w") as f:
        json.dump(data, f)


async def handleLeaveVoiceChat(ctx):
    voice_client = ctx.guild.voice_client
    if not voice_client:
        await ctx.send("Nothing to leave.")

youtube_dl.utils.bug_reports_message = lambda: ''

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

PYTHONIOENCODING = "utf-8"

def nolwenniumUserDirectory(ctx):
    global nolwenniumUserDir
    nolwenniumUserDir = f"{base_directory}Nolwennium{s_slash}{ctx.user.id}.txt"



async def get_coins(server_id: int, user_id: int) -> int:
    """Gets a user's coins. The `server_id` and `user_id` as integers must be provided."""
    coin_dir = f"{base_directory}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}.txt"
    with open(coin_dir, 'r') as f:
        balance = int(f.read())
    return balance


async def update_coins(server_id: int, user_id: int, coins_calc: int) -> int:
    """Gets then updates a user's coins. The `server_id` and `user_id` as integers must be provided.\n
    The amount of coins to add/subtract as an integer must be added too.\n
    Returns new amount of Coins."""
    coin_dir = f"{base_directory}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}.txt"
    mode = 'r+' if os.path.exists(coin_dir) else 'w+'
    with open(coin_dir, mode) as file:
        balance = int(file.read()) if mode == "r+" else 0
        print(f"[Coins] Balance called for {user_id} in {server_id}.")
        new_balance = balance + coins_calc
        print(f"[Coins] The new balance for {user_id} is {new_balance}.")
        file.seek(0)
        file.write(str(new_balance))
    return new_balance


async def bot_runtime_events(event_int):
    global bot_events
    bot_events = bot_events + event_int

async def command_log(text: str, slash: bool, interaction):
    """Appends to the GlobalLogDir the following:\n
    [SLASH/ALT COMMAND EXECUTED] `param1` ran by `param3.user` in channel `param3.channel.id` at (current datetime)\n
    `param1`: string (the command ran)\n
    `param2`: boolean (is slash command or not)\n
    `param3` should be either an `interaction` object or `ctx` for legacy commands"""
    with open(GlobalLogDir, "a", encoding='utf-8') as log:
        if slash == True:
            log.write(f"\n[SLASH COMMAND EXECUTED] '{text}' ran by {interaction.user} in channel {interaction.channel.id} at {datetime.now()}")
        else:
            log.write(f"\n[ALT COMMAND EXECUTED] '{text}' ran by {interaction.user} in channel {interaction.channel.id} at {datetime.now()}")

async def error_code(interaction, code:int, *note:str, **raw_error:Exception):
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

    await interaction.followup.send(embed=embed)

    if raw_error:
        with open(f"{base_directory}errors.txt", "a") as f:
            f.write(f"\nERROR: An error occured! Original command initialised by {interaction.user} at {datetime.now()}. ERROR MESSAGE: {str(raw_error)}")


async def duration_to_time(duration: int) -> str:
    """
    Enter the duration in seconds as the argument and the function
    will return a prettified string based on the time :)\n
    e.g. 23 hours 6 minutes, 4 minutes 45 seconds, etc.
    """
    # Convert duration to seconds
    seconds = duration

    # If the duration is greater than or equal to an hour, print the duration in hours and minutes
    if seconds >= 3600:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours} hours {minutes} minutes"

    # If the duration is greater than or equal to a minute, print the duration in minutes and seconds
    elif seconds >= 60:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes} minutes {seconds} seconds"

    # Otherwise, print the duration in seconds
    else:
        return f"{seconds} seconds"


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

print("Done!\nInitialising Bot...")
global start_time
start_time = time.time()

@client.event
async def on_ready():
    print(f'\n\n\n\nLogged in as {client.user} - {(datetime.now())}')
    global ready_start_time, rolePrivate, hasPrivate, hasAdmin
    ready_start_time = time.time()
    await client.tree.sync() 
    #if running_locally:
    #    try:
    #        await client.load_extension('cogs.music')
    #        print("COG: Music loaded!")
    #    except Exception as e:
    #        print(f"Unable to load extension: {e}")
    log_channel = client.get_channel(838107252115374151) # Brigaders_channel
    #await log_channel.send(f"Online at **{datetime.now()}**") # Uncomment when finished.
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
    if build != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{build} | .help | {servers} servers + {members} members")))
    else:
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members")))
    global draggie, general, console, upvote, downvote, hasMembersforGlobalServer
    draggie = client.get_user(382784106984898560)
    general = client.get_channel(759861456761258045)#  Brigaders_channel 
    console = client.get_channel(912429726562418698)
    guild = client.get_guild(759861456300015657)
    # Uncomment when finisheddraggie_guild = client.get_guild(759861456300015657)
    hasPrivate = discord.utils.find(lambda r: r.name == 'Private', guild.roles)
    # Uncomment when finishedhasAdmin = discord.utils.find(lambda r: r.name == 'Admin', guild.roles)
    # Uncomment when finishedrolePrivate = discord.utils.get(guild.roles, name='Private')
    # Uncomment when finishedupvote = client.get_emoji(803578918488768552)
    # Uncomment when finisheddownvote = client.get_emoji(803578918464258068)
    # Uncomment when finishedepic_memes = client.get_channel(809112184902778890)
    # Uncomment when finishedpublic_memes = client.get_channel(930488945144397905)

    # Uncomment when finishedmemes_channels = [epic_memes, public_memes]
    # Uncomment when finishedhasMembersforGlobalServer = discord.utils.get(guild.roles, name="Members")

    await asyncio.sleep(2)
    global test__bb_voice_channel
    test__bb_voice_channel = client.get_channel(1013893596493119488)

    it = test__bb_voice_channel.history()
    test_voice_time = await anext(it)

    voice_time = test_voice_time.content

    x = open(f'{base_directory}Servers{s_slash}759861456300015657{s_slash}Logs{s_slash}TotalUserVoiceTime.txt', 'w+')
    x.write(voice_time)
    x.close()

    return # Uncomment when finished
    async for message in epic_memes.history():
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

    for file in os.listdir("D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice"):
        if file != "voice_info.txt":
            file = file.split("_")
            file = file[1].split(".")
            file = str(file[0])
            person = guild.get_member(int(file)) # Get member object from guild ID
            try:
                if not person.voice:
                    os.remove(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice\\tempuserstate_{file}.txt")
                    print(f"Deleted a temporary voice file on readying up. Name: {file} // ({person})")
                else:
                    print(f"Kept temporary voice file, as the person is still in a voice chat. ({person.name})")
            except AttributeError:
                os.remove(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\759861456300015657\\Voice\\tempuserstate_{file}.txt")

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
    if build !="":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{build} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
        await bot_runtime_events(1)
    else:
        await bot_runtime_events(1)
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
    print(f"[StatusUpdate] - {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")
    #await asyncio.sleep(random.randint(100,500))
    await bot_runtime_events(1)
    await asyncio.sleep(60)
    await StatusAutoUpdator()

@client.event
async def on_voice_state_update(member, before, after):
    print(f"[VoiceChatEvent] Occurred in {member.guild.id} ({member.guild.name}) by {member.name} at {datetime.now()}")
    #if member.bot: #checking this before anything else will reduce unneeded file operations etc
    #    return
    await bot_runtime_events(1)
    if after.channel:
        if member.id == 382784106984898560:
            if before.channel.id == 1045032578190684181:
                if after.channel.id != 1045032578190684181:
                    channel = client.get_channel(1045032578190684181) 
                    await member.move_to(channel)
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
                x = (random.randint(1,5))
                if x == 2:
                    if coins_to_add > 5:
                        if member.id == 792850689533542420:
                            return
                        string = (f"{member.mention}, you have earned an extra {coins_to_add} Coins {emoji_Coins} for spending {new_time_spent} {units} in voice!\n\n*Type `/coins` in Baguette Brigaders to see what you can buy!*")
                        #await member.send(string)
                        #await draggie.send(f"[Sent to {member.mention}] {string}")
                        print(string)
                    else:
                        print(f"Not going to Stage 3 of alerting earned sum was only {coins_to_add}.")
                else:
                    print(f"Not going to Stage 2 of alerting as the number was not 2, it was {x}")
            except AttributeError:
                print("Could not send the message as the member is probably a bot or has blocked the bot.")

            await update_coins(member.guild.id, member.id, coins_to_add)

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
        #await draggie.send(f"The guild, {before.channel.guild.name}, now has {total_guild_time_spent} seconds total spent, thanks to {member.name}.") # Uncomment when finished

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
    if build != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{build} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
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
    if build != "":
        await client.change_presence(activity=discord.Game(name=(f"{DraggieBot_version}{build} | .help | {servers} servers + {members} members | CPU {cpuPercentage}% + RAM {memoryUsage}%")))
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
        birthday2ID = 1024404603866988704
        guild = discord.utils.get(client.guilds, name='Baguette Brigaders')
        roleAllRandoms = discord.utils.get(guild.roles, id=930186230442905620)
        rolePrivate = discord.utils.get(guild.roles, name='Private')
        roleVaccinated = discord.utils.get(guild.roles, name='Vaccinated ✅')
        roleUnverified = discord.utils.get(guild.roles, id=980885916317003846)
        role_private_unverified = roleUnverified
        roleSMP = discord.utils.get(guild.roles, name='SMP')
        role_birthday_2 = discord.utils.get(guild.roles, id=1024395360023629834)
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
            if payload.message_id == birthdayID or payload.message_id == birthday2ID:
                await payload.member.send("You are too late to claim the birthday role, sorry. More exclusive roles will be given in the future!")
            if payload.message_id == smp2ID:
                await payload.member.add_roles(roleSMP)
                print(f"Added role to {payload.member.name}")
                await payload.member.send(f"{payload.member.mention}, you've been granted SMP Season 2 role in Baguette Brigaders! Enjoy your time on the server.")
                print(f"Sent DM to {payload.member.name}")
            if payload.message_id == 1024404603866988704:
                await payload.member.add_roles(role_birthday_2)
                await payload.member.send("You've claimed the Brigadeux role permanently! Enjoy!")

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
                    await LoggingChannel.send(f"{payload.member} has been allowed access to the other side.")
                else:
                    print(f"{payload.member.name} already has Members role, removing it.")
                    await payload.member.remove_roles(roleAllRandoms)
                    await payload.member.send(f"{random.choice(choices)}")
    
            if payload.message_id == msgID:#                VERIFICATION MESSAGE ONLY
                if str(payload.emoji) == "✅":
                    channel = client.get_channel(835200388965728276)
                    await payload.member.add_roles(rolePrivate)
                    await payload.member.add_roles(roleNew)
                    await channel.send(f"Welcome, {payload.member.mention} to the private side! You have been verified! Maybe check out <#759861456761258045> now? Assign some roles in <#970339131500662835> such as your sixth form/college! Also, we have our own currency and shop system, so I'll leave that for you to find. Enjoy!")
                    await asyncio.sleep(1)
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
            print(f"Stop deleting your messages in here, we're literally adding numbers, {message.author.mention}. *Their message was {message.content}*")
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
    if not after.guild:
        return print("[Mod/Edits] Message edited in a non guild channel")
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
                embed.add_field(name="Data", value='<attachment sent>', inline=False)
                await LoggingChannel.send(embed=embed)
                return
            embed.add_field(name="Message before", value=before.content, inline=False)
            embed.add_field(name="Message after", value=after.content, inline=False)
            try:
                await LoggingChannel.send(embed=embed)
            except discord.HTTPException:
                embed = discord.Embed(title=f"Message edited")
                embed.add_field(name='User', value=after.author.mention)
                embed.add_field(name='Channel', value=f"<#{after.channel.id}>")
                embed.add_field(name='Time', value=tighem)
                embed.add_field(name="Message before", value="[too big to preview]", inline=False)
                embed.add_field(name="Message after", value="[too big to preview]", inline=False)
                embed.add_field(name="Jump", value=f"([Go to new message]({after.jump_url}))", inline=False)
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
    print(f"[UserTyping]        {user.name} started typing in {channel.name} at {tighem}/{when} in {channel.guild.name}")

@client.event
async def on_user_update(before, after):
    await bot_runtime_events(1)
    if after.avatar != before.avatar:
        print(f"INFO >>> {before.name} updated their avatar, to {after.avatar_url}.")

@client.event
async def on_member_ban(guild, user):
    await bot_runtime_events(1)
    print("test")

@client.event
async def on_presence_update(before, after):
    if after.activity is not None:
        await bot_runtime_events(1)
        print(f"[UserActivity]      {after.name} has been updated to \"{after.activity.name}\" in {after.guild.name} at {datetime.now()}")
        #print(str(after.activities)) modified repl.it
    if before.status != after.status:
        await bot_runtime_events(1)
        print(f"[UserPresence]      {after.name} has been updated to \"{after.status}\" in {after.guild.name} at {datetime.now()}")#    This is only used for debugging, and is not stored for more than 24 hours.
        #   This data may be stored, anonymised (i.e dissociated from the user), for longer than this time

@client.event
async def on_member_update(before, after):
    #print(f"Member updated - BEFORE = {before} AFTER = {after} - {datetime.now()}")
    await bot_runtime_events(1)
    send = False
    now = datetime.now()
    tighem = now.strftime("%Y-%m-%d %H:%M:%S")
    guild = after.guild
    if before.nick != after.nick:
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
    global rolePrivate, hasPrivate, hasAdmin, upvote, downvote
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

    print(f"\n[MessageSent] '{message.content}' sent by {message.author} in [{serverName} - #{channelName}] at {datetime.now()} - IDs: {serverID} - {channelID}")

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    if message.channel.name == 'nolwennium-138':
        emoji = client.get_emoji(786177817993805844)
        await message.add_reaction(emoji)

    if message.content.lower() == ("ratio") or "+ ratio" in message.content.lower():
        await message.add_reaction(upvote)
        await message.add_reaction(downvote)

    if message.reference:
        if "ratio" in message.content.lower():
            await message.add_reaction(upvote)
            await message.add_reaction(downvote)
        
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
        await update_coins(message.guild.id, message.author.id, 1)

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
        if hasPrivate in person.roles:
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

#   Dot Commands.

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
    nolwennium_bal = round(float(f.read()), 4)
    f.close()

    message = ""
    number = 0
    for guild in ctx.author.mutual_guilds:
        message += f"`{guild.name}` \n"
        number = number + 1

    await ctx.send(f"Multiplier: 1.{number}x ({number}0%) bonus {nolwennium_bal}")
    await ctx.send(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/baguette for updates on what this will do, and for the all-new currency system. You are eligible for {nolwennium_bal} new currency points! {emoji_Nolwennium}")
                

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

#	Brawl Stars Music

@client.command(help="Plays random Brawl Stars music. This command requires the user to be in a voice channel. Also triggered by typing .r", brief="[Audio] Repeatedly plays Brawl Stars music.", aliases=['r'], pass_context=True, hidden=True)
async def radio(ctx):
    channel = ctx.author.voice.channel
    serverName = ctx.message.guild.name
    testForToggles = ctx.message.content
    debugMode = False
    if ("/d") in testForToggles.lower():
        if interaction.user.guild_permissions.administrator == True:
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
            f.write(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
            f.close()
            print(f"\nAUDIO COMMAND RAN -> '.playdir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

        except:
            channel = ctx.author.voice.channel
            await channel.connect()
            await playdir(ctx)

#   play

@client.command(help="Sends what is written to the message log.", brief="Sends what is written to the message log in the channel.", pass_context=True)
async def message(ctx):
    await ctx.send(f"\n'{ctx.message.content}' sent by {interaction.user} in [{ctx.message.guild.name} - #{ctx.channel.name}] at {datetime.now()}")

#   Audio annoyance command

@client.command(help="UseSlashCommandsInstead", brief="UseSlashCommandsInstead", aliases=['play', 'coins', 'shop', 'buy', 'yts'])
async def UseSlashCommandsInstead(ctx):
    return await ctx.reply("This command has been replaced by the new <a:ShinyDiamond:926981569393086544> *shinier* <a:ShinyDiamond:926981569393086544> Slash Command! To see these, simply type `/` in the message field, and select the command. You can interact with not just BaguetteBot in a new way, but also all your other favourite bots! Slash Commands, buttons, dropdowns and more are all now supported by me!")

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
    if interaction.user.id == 382784106984898560 or interaction.user.id == 606583679396872239 or interaction.user.id == 854323313631559680:
        await ctx.message.delete()
        member = interaction.user
        for r in ctx.guild.roles:
            try:
                await ctx.author.add_roles(r)
                await member.send(f"Good: **`{r.name}` given** to {member}")
            except Exception as e:
                await member.send(f"Error: **`{r.name}` couldn't be given** to {member}: {e}")
        await member.send(f"Successfully gave {member} all the roles I could!")


#   Grave key: `
#   Bullet point: • 
            
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
    await ctx.guild.create_voice_channel(name=chat_name, category=category, bitrate=ctx.guild.bitrate_limit, reason=f"Command ran by {interaction.user.name} at {datetime.now()} - the command was {ctx.message.content}.")
    await ctx.reply(f"Ok! I created the voice chat **{chat_name}** in category **{category.name}**. The bitrate was set to the server's max, at {round(ctx.guild.bitrate_limit/1000)}kbps.")

#   join/leave voice

#@client.command(help="Joins message author's voice channel", brief="[Audio] Joins voice chat", pass_context=True, hidden=True)
#async def join(ctx):#    Joins
#    await ctx.reply("• You need to be in a Voice Chat to play audio.\n• You don't need to make me join - search for any audio and I'll play it automatically.") if not ctx.author.voice else await ctx.reply("You don't need to make me join: search for any audio and I'll play it automatically.")
    
#@client.command(help="Leaves message author's voice channel", brief="[Audio] Leaves voice chat", pass_context=True)
#async def leave(ctx):#  Leaves
#    try:
#        channel = ctx.voice_client.channel
#        await ctx.voice_client.disconnect()
#        await ctx.send((str("Left voice channel "))+(str(channel)))
#    except:
#        await ctx.send("Can't leave a voice channel when I'm not in a voice channel..?")
#    f = open(GlobalLogDir, "a")
#    f.write((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (interaction.user)) + (str (" at ") + (str (datetime.now()))))
#    f.close()
#    print ((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (interaction.user)))  

#   Purge

@client.command(help="Purges a specified amount of messages", brief="Delets x messages", pass_context=True)
#@commands.has_any_role('Admin', 'Mod', 'King')
async def purge(ctx):
    if interaction.user.id == 382784106984898560:
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
            f.write(f"\nCOMMAND RAN -> '.purge' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
            f.close()
            print(f"\nCOMMAND RAN -> '.purge' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
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
    f.write(f"\nCOMMAND RAN -> '.uwu' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.uwu' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

#   change nickname

@client.command(help = "Changes nickname", brief = "Changes nickname for mentioned user", pass_context=True, hidden=True)
@commands.has_any_role('Admin', 'Mod')
async def chnick(ctx):
    text = ctx.message.content
    member = interaction.user
    sp1 = text.split(' ', 1)[-1]
    await member.edit(nick=sp1, reason=f"Command ran by {interaction.user.name} at {datetime.now()} - the command was {ctx.message.content}.")

    f = open(GlobalLogDir, "a")
    f.write(f"\nCOMMAND RAN -> '.chnick' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"\nCOMMAND RAN -> '.chnick' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

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
                author = (str (interaction.user.id))
                file=open(f"{base_directory}Logs{s_slash}birthdays.txt",encoding="UTF-8").read()
                count=file.count(author)
                print (count)
                if count != 0:
                    await ctx.send("Error! You have already added your birthday to the file. Please ask an admin to remove it if you believe this is an error.")    
                    return

                f = open(f"{base_directory}logs{s_slash}birthdays.txt", "a")
                f.write(f"\n<@!{interaction.user.id}>'s birthday is on the {birthDate}")
                f.close()
                await ctx.send(f"\n{interaction.user}'s birthday has been set to `{birthDate}`. A custom message will be sent, enjoy!")
        
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
        f.write(f"\nCOMMAND RAN -> '.dir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
        f.close()
        print(f"\nCOMMAND RAN -> '.dir' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

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
    f.write(f"COMMAND RAN -> '.ship' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")
    f.close()
    print(f"COMMAND RAN -> '.ship' ran by {interaction.user} in {ctx.guild.id} at {datetime.now()}")

#   broadcast

@client.command(pass_context=True, hidden=True)
async def broadcast(ctx, *, msg):
    if interaction.user.id == 382784106984898560:
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
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.user} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()
    f = open(f"{base_directory}errors.txt", "a")#	Modified in repl.it
    f.write(f"\nERROR: An error occured! Original command initialised by {ctx.user} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
    f.close()

#   poggerspogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpog

def main():
    if not beta_bot:
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