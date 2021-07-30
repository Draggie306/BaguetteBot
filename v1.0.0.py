DraggieBot_version = "v1-TEST"

print("Importing all modules...\n")
import      discord
from        discord import Embed
from        discord.ext import commands   
from        discord import ext
from        discord.errors import ClientException #     CMD Prequisite: py -3 -m pip install -U discord.py
from        dotenv import load_dotenv #                 CMD Prequisite: py -3 -m pip install -U python-dotenv
import      os#                                         PIP:            python -m ensurepip  
import      os.path#                                    UPDATE PIP:     python -m pip install --upgrade pip
import      youtube_dl
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
from        youtube_search import YoutubeSearch
from        requests.auth import HTTPBasicAuth
from        gc import enable
import      kahoot
import      json
import      subprocess
from        mcstatus import MinecraftServer
print("Done!\nInitialising Bot...")

sys.setrecursionlimit(99999999)

global voiceVolume
voiceVolume = 1

global start_time
start_time = time.time()

PYTHONIOENCODING="utf-8"

client = discord.Client()
#print (">>> client = discord.Client()")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix='.', case_insensitive=True)
#print (">>> client = commands.Bot prefix '.'")

DisabledComponents = "Unknown"
EnabledComponents = "Unknown"

GlobalLogDir=("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\GlobalLog.txt")

@client.event
async def on_ready():
    print('\n\n\n\nLogged in as {0.user}'.format(client))

    global ready_start_time
    ready_start_time = time.time()

    channel = client.get_channel(836678479520333917)
    await channel.send((str ("Online at **")) + (str (datetime.now()) + (str ("**"))))

    f = open(GlobalLogDir, "a")
    f.write((str ("\n\nREADY at ")) + (str (datetime.now())))
    f.write(' - Logged in as {0.user}'.format(client))
    f.close()
    await client.change_presence(activity=discord.Game(name=("{} | .help | <:nolly:786177817993805844>".format(DraggieBot_version))))

@client.event
async def on_member_join(member):
    channel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
    await channel.send(member, "has joined the server")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
    await channel.send(member, "has left the server")

@client.event
async def on_raw_reaction_add(payload=None):
    msgID = 843155071570149427
    guild = discord.utils.get(client.guilds, name='Baguette brigaders baccup')
    roleMember = discord.utils.get(guild.roles, name='Member')
    roleUnverified = discord.utils.get(guild.roles, name='Unverified')
    roleNew = discord.utils.get(guild.roles, name='New Baguette')

    if payload is not None:
        if payload.message_id == msgID:
            if str(payload.emoji) == "✅":
                person = payload.member
                serverName = payload.member.guild.name

                channel = client.get_channel(843155040926826507)
                await payload.member.add_roles(roleMember)
                await payload.member.add_roles(roleNew)
                #	Sends message in channel before removing the permission for it
                await channel.send((str ("Welcome, ")) + (str (payload.member.mention)) + (str ("! You have been verified! Maybe check out <#759861456761258045> now?")))
                print("Sent message")
                LoggingChannel = discord.utils.get(payload.member.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)
                await LoggingChannel.send((str (payload.member)) + (str (" has been verified.")))

                await payload.member.remove_roles(roleUnverified)
                await asyncio.sleep(5)
                await channel.purge(limit=1)
                print("And it's gone in", channel)

                channel = discord.utils.get(payload.member.guild.channels, name="general", type=discord.ChannelType.text)
                await channel.send((str ("Hello ")) + (str (person.mention)) + (str (", welcome to **")) + (str (serverName)) + (str ("**! Thank you for joining, have a great time here!")))

@client.event
async def on_message(message):
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

        print(((str ("\n'")) + (str (message)) + (str ("' DMed by ")) + (str (person)) + (str (" at ") + (str (datetime.now())))))
        dmLocation = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\DMs\\")) + (str (personID)) + (str (".txt")))
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
    messageRepeat = message.content

    filedir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\")))
    if not os.path.exists(filedir):
        os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\")))

    with open((str (filedir)) + (str ("MessageLog.txt")), "a", encoding='utf-8') as logAllMessages:
        logAllMessages.write((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (message.author)) + (str (" in [{}".format(serverName) + " - #{}]".format(channelName))) + (str (" at ") + (str (datetime.now())) + (str (" - Server ID is {}".format(serverID)))))
        logAllMessages.close()
        print((str ("\n'")) + (str (messageRepeat)) + (str ("' sent by ")) + (str (message.author)) + (str (" in [{}".format(serverName) + " - #{}]".format(channelName))) + (str (" at ") + (str (datetime.now())) + (str (" - Server ID is {}".format(serverID)))))

# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
        # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS  # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS
# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS# MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS    # MESSAGE LOGS

    if message.content == (".config"):
        global DisabledComponents
        global EnabledComponents

        if os.path.isfile((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Components\\EverythingButCommandsDisabled.info"))):
            DisabledComponents = ("`Blacklist`")
            EnabledComponents = ("`Logging`, `Commands`")

        if os.path.isfile((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Components\\EverythingDisabled.info"))):
            DisabledComponents = ("`Blacklist`, `Commands`")
            EnabledComponents = ("`Logging`")
        else:
            DisabledComponents = ("`Error`")
            EnabledComponents = ("`Error`")
    
        embed=discord.Embed(title="Configuration", color=0x44ff44)
        embed.add_field(name="Enabled components:", value=(EnabledComponents), inline=False)
        embed.add_field(name="Disabled components:", value=(DisabledComponents), inline=False)
        embed.set_footer(text="To modify this, the syntax is .config <[component] | all> <enable | disable | all>")
        await message.channel.send(embed=embed)
        print("Yes")

    if message.content.startswith(".config"):
        txt = message.content
        x = txt.split()
        try:
            component = (x[1])
            newStatus = (x[2])

        except Exception:
            pass

#   Components Directory = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Components\\EverythingDisabled.info"))):

    if os.path.isfile((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Components\\EverythingDisabled.info"))):
        #print("EverythingDisabled.info exists")
        return

    if os.path.isfile((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Components\\EverythingButCommandsDisabled.info"))):
        #print("EverythingButCommandsDisabled.info exists")
        await client.process_commands(message)
        return   

    else:
        blacklistCheck = message.content

    #   Blacklist

        with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\blacklist.json", "r", encoding="utf8") as file:
            data = loads(file.read())
            for word in data:
                if word in blacklistCheck.lower():

                    role = discord.utils.find(lambda r: r.name == 'DraggieBot Whitelisted', person.roles)
                    if role in person.roles:
                        print("Not deleting message")
                        await client.process_commands(message)
                        return

                    await message.delete()

                    randWord = random.randint(1,13)
                    if randWord == 1:
                        await message.channel.send((str ("You just got peace control kyle'd, ") + (str (person.mention))))
                    if randWord == 2:
                        await message.channel.send((str ("You're literally dogwater, ") + (str (person.mention)))) 
                    if randWord == 3:
                        await message.channel.send((str ("200 pumped, ") + (str (person.mention)) + (str ("!"))))
                    if randWord == 4:
                        await message.channel.send((str ("Boxed like a fish, ") + (str (person.mention)) + (str ("!"))))
                    if randWord == 5:
                        await message.channel.send((str (person.mention) + (str (" just got boxed like a fish")) + (str ("!")))) 
                    if randWord == 6:
                        await message.channel.send((str (person.mention) + (str (" was 200 pumped")) + (str ("!"))))
                    if randWord == 7:
                        await message.channel.send((str (person.mention) + (str (" is dogwater")) + (str ("!"))))
                    if randWord == 8:
                        await message.channel.send((str (person.mention) + (str (" got peace control kyle'd")) + (str ("!"))))
                    if randWord == 9:
                        await message.channel.send((str (person.mention) + (str (" is a walking big pot")) + (str ("!!"))))
                    if randWord == 10:
                        await message.channel.send((str (person.mention) + (str (" is so free")) + (str ("!"))))
                    if randWord == 11:
                        await message.channel.send((str (person.mention) + (str (" is freer than the free samples at costco")) + (str ("!"))))
                    if randWord == 12:
                        await message.channel.send((str ("Sorry but you can't say that, ") + (str (person.mention))))
                    if randWord == 13:
                        await message.channel.send((str ("Please refrain from swearing, ") + (str (person.mention))))
                    if randWord == 14:
                        await message.channel.send((str ("Your message contains a blacklisted word or phrase, ") + (str (person.mention)) + (str ("."))))
                    if randWord == 15:
                        await message.channel.send((str ("You can't say that, ") + (str (person.mention)) + (str ("."))))
                    if randWord == 16:
                        await message.channel.send((str ("You're not allowed to say that, ") + (str (person.mention)) + (str ("!"))))
                
                    f = open(GlobalLogDir, "a", encoding="utf8")
                    f.write((str ("\nINFO: ")) + (str ("Message deleted from ")) + (str (message.author)) + (str (" in [{}".format(serverName) + " - #{}]".format(message.channel.name))) + (str (" at ") + (str (datetime.now()))))
                    f.close()
                    print ((str ("\nINFO: ")) + (str ("Message deleted from ")) + (str (message.author)) + (str (" in [{}".format(serverName) + " - #{}]".format(message.channel.name))) + (str (" at ") + (str (datetime.now()))))
                    return
                
        s = (str (message.content))
        if len(s) == 1:
            if message.channel.id == 825470734453047297: 
                return
            if message.channel.id == 837759175786364979: 
                return
            #if channelName == 'join-log':
            #    return

            user = message.author
            role = discord.utils.find(lambda r: r.name == 'DraggieBot Whitelisted', user.roles)
            if role in user.roles:
                print("Not deleting message")
                await client.process_commands(message)
                return
                
            if message.author.id == '382784106984898560':
                return
            if message.content == ('😂'):#              Whitelist 😂
                return
            if message.content == ('😳'):#              Whitelist 😳
                return
            if message.content == ('👀'):#              Whitelist 👀
                return
            if message.content == ('?'): #              Whitelist ?
                return
            if message.content == ('!'):
                return
            if message.content == ('Y'):
                return
            if message.content == ('y'):
                return
            if message.content == ('k'):
                return
            if message.content == ('K'):
                return
            if message.author.bot:
                return
            if message.content == ("⠀"):#space braiile  
                return

            await message.delete()

            person = message.author
            f = open(GlobalLogDir, "a", encoding="utf8")
            f.write((str ("\nINFO: 1 character message! Are they whitelisted? Message: '")) + (str(message.content)) + (str ("' from ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
            print((str ("\nINFO: 1 character message! Are they whitelisted? Message: '")) + (str(message.content)) + (str ("' from ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
            f.close()
            return

    if message.channel.name == 'nolwennium-138':
        emoji = client.get_emoji(786177817993805844)
        await message.add_reaction(emoji)

    authorID = message.author.id
    person = message.author

    boosterRole = discord.utils.find(lambda r: r.name == 'Server Booster', person.roles)
    if boosterRole in person.roles:
        nolwenniumDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")) + (str (authorID)) + (str (".txt"))
        serverNolwenniumDir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")))
    
        if not os.path.exists(serverNolwenniumDir):
            os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium")))

    global currentMinute
    global coinDir
    
    coinDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
    serverdir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")))
    
    if not os.path.exists(serverdir):
        os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins")))

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
        try:
            bbLogChnlId = discord.utils.get(message.guild.channels, name="event-log-baguette", type=discord.ChannelType.text)

            embed = discord.Embed(title="User Joined Server", 
            description=((str (person.mention)) + (str (" has joined the server."))), colour=0x00ff00)
            await bbLogChnlId.send(embed=embed)
        except Exception:
            print((str ("Unable to send that a new user has joined. This server, ")) + (str (serverName)) + (str (", doesn't have a text channel called 'event-log-baguette'.")))

    except ValueError:
        f.write('1')
        f.close()
    
    #print (len(s))

#   Generic commands.

#    if message.content == ("hi"):
#        await message.channel.send('hi')
#        f = open(GlobalLogDir, "a")
#        f.write((str ("\nWORD MENTIONED -> 'hi' ran by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
#        f.close()

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
        f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\\\Logs\\GlobalLog.txt", "a")
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

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\NollyMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:nolly:786177817993805844>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'nolly' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\OliverMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:oliver:790576109795409920>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'oliver' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\JackMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:jacc:786275811405070337>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'jacc' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\JoeMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:joecat:786277202400116770>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'joecat' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()
            
    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\HaydnMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:haydn:786276584671412244>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'haydn' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\MaisyMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:maisy:786276271809101840>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'maisy. emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()        

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\BenMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:bennybooze:788311580768075786>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'bennybooze' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\FloMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:JacksGF:788162163289358367>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'JacksGF' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\IshMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:ish:791381704278540369>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'ish' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\BorisMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:boris:785942478381121556>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'boris' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\MayaMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:maya:785942478448230470>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'maya' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

    #with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\SamMention.json", "r", encoding="utf8") as file:
        data2 = loads(file.read())
        for word in data2:
            if word in message.content:
                person = message.author
                await message.channel.send("<:samf:785942793280815114>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nINFO: 'samf' emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
                f.close()  

#   Nolly = :nolly:786177817993805844
#   Oliver = :oliver:786275811405070337
#   Jack = :jacc:786275811405070337
#   Joe = :joecat:786277202400116770

#   Charlie = 
#    with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\CharlieMention.json", "r", encoding="utf8") as file:
#        data2 = loads(file.read())
#        for word in data2:
#            if word in message.content:
#                person = message.author
#                await message.channel.send("A custom emoji has not bben set up for line 341, 'Charlie', please add one")
#                f = open(GlobalLogDir, "a", encoding="utf8")
#                f.write((str ("\nINFO: Charlie emoji sent, initiated by '")) + (str (message.author)) + (str ("' at ") + (str (datetime.now()))))
#                f.close()

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

    with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\Impact1-Mention.json", "r", encoding="utf8") as file:
        Impact1Mention = loads(file.read())
        for word in Impact1Mention:
            if word in message.content:
                person = message.author
                await message.channel.send("<a:impact1:801435824720969728>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nEMOJI SENT -> Impact1 emoji sent, initiated by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
                f.close()

    with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\JSONs\\Impact2-Mention.json", "r", encoding="utf8") as file:
        Impact2Mention = loads(file.read())
        for word in Impact2Mention:
            if word in message.content:
                person = message.author
                await message.channel.send("<a:impact2:801435824855711804>")
                f = open(GlobalLogDir, "a", encoding="utf8")
                f.write((str ("\nEMOJI SENT -> Impact2 emoji sent, initiated by ")) + (str (message.author)) + (str (" at ") + (str (datetime.now()))))
                f.close()
        
#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

    await client.process_commands(message)

#   essential do not delete     essential do not delete     essential do not delete     essential do not delete     essential do not delete     

#   baguettes
    
@client.command(help="Sends up to 9 random baguette pics", brief="Sends random baguette pics", pass_context=True)
async def baguette(ctx, member: discord.Member = None):
    baguetteRand = (str (random.randint(1,9)))
    await ctx.send(file=discord.File((str ('D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Assets\\Baguettes\\baguette')) + (str (baguetteRand)) + (str (".jpg"))))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.baguette ' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   ping

@client.command(help="Says the ping immediately after user has sent the command. Used for determining latency/ping or downtime.", brief="Shows ping.", pass_context=True)
async def ping(ctx):

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

#   Patchnotes

@client.command(help="Long list of DraggieBot update notes.", brief="(old) Shows what's new in DraggieBot.", pass_context=True)
async def patchnotes(ctx):
    await ctx.send((str ('DRAGGIEBOT is currently on ') + (str (DraggieBot_version))))
    await ctx.send("New in this version:\n\n0.8.0 - Full Audio Support + YouTube Videos")
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.patchnotes' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.patchnotes' ran by ")) + (str (ctx.message.author)))

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
        await ctx.send((str ("Attempting to add `")) + (str (botNum)) + (str ("` bots to game ID `")) + (str (code)) + (str ("`!")))
    else:
        await ctx.send((str ("Attempting to add `")) + (str (botNum)) + (str ("` bot to game ID `")) + (str (code)) + (str ("`!")))

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
                    await ctx.send((str ("Done! `")) + (str (joins)) + (str ("` bot has been added to `")) + (str (code)) + (str ("`.")))

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
    parameters = {}
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e32f979c-fbe7-44f1-8b5b-a0b2c8ff2ea4',
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
    aliases=['shop', 'rank', 'points', 'balance', 'bal', 'coin'])
async def coins(ctx):
    authorID = ctx.message.author.id
    userID = authorID
    user = ctx.message.author
    serverName = ctx.message.guild.name
    serverID = ctx.message.guild.id
    #print (serverID)

    coinDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
    f = open(coinDir, 'r')
    coinBal = f.read()
    f.close()

    nolwenniumUserDir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")) + (str (authorID)) + (str (".txt"))
    nolwenniumDir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")))
    my_file = Path(nolwenniumUserDir)

    if not os.path.exists(nolwenniumDir):
        os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins")))

    if not my_file.is_file():
        with open(nolwenniumUserDir, 'a') as f:
            print ((str ("\n\nset Nolwennium value to 1, new user.")))
            try:
                f.write('0')
                f.close()
            except Exception:
                f.write('0')
                f.close()

    f = open(nolwenniumUserDir, 'r')
    nolwenniumBal = f.read()
    f.close()

#	List of stuff BEFORE showing the user their balance

    try:
        txt = ctx.message.content
        x = txt.split()
        word1 = (str (x[1]))

        usersCoins = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (userID)) + (str (".txt"))

        if word1 == 'set':
            userID = (str (x[2]))
            amount = (str (x[3]))
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

            await ctx.send((str ('<@')) + (str (userID)) + (str (">'s coins have been updated from ")) + (str (oldCoins)) + (str ("<:Coins:852664685270663194> to **")) + (str (newCoins)) + (str ("** <:Coins:852664685270663194>.")))
            return
        
        if word1 == 'add':
            userID = (str (x[2]))
            amountToAdd = (str (x[3]))

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

            await ctx.send((str ('<@')) + (str (userID)) + (str (">'s coins have been updated from ")) + (str (oldCoins)) + (str ("<:Coins:852664685270663194> to **")) + (str (newCoins)) + (str ("** <:Coins:852664685270663194>.")))
            return
        else:
            await ctx.send("I don't know what you mean. The correct syntaxes are:\n.coins\n`.coins set <targetUserID> <newCoins>`\n`.coins add <targetUserID> <addedAmount>`")

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

        embed = discord.Embed(title="User Balance", description=((str ("You have ")) + (str (coinBal)) + (str (" <:Coins:852664685270663194> coins, and ")) + (str (nolwenniumBal)) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium to spend."))), colour=0xFFD700)
        embed.add_field(
        name="Items available to .buy",
        value=(citizenPurchasable) + (knightPurchasable) + (princePurchasable) + (kingPurchasable) + (adminPurchasable),
        inline=False)
        embed.set_footer(text=((str ("User ID: ")) + (str (authorID))))
        await ctx.send(embed=embed)

#   buy

@client.command(help="Shows coin balance. If above a threshold, displays the list of roles the user can buy by typing .buy <role>", brief="Shows your balance, and available to buy items.", pass_context=True)
async def buy(ctx):
    member = ctx.message.author
    authorID = ctx.message.author.id
    text = ctx.message.content
    serverID = ctx.message.guild.id

    x = text.split()
    determiner = (str (x[1]))
    filedir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Coins\\")) + (str (authorID)) + (str (".txt"))
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
    
    else:
        await ctx.send("That's not a valid item to buy!")

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
@commands.has_any_role('Admin', 'Mod', 'Prince')
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
    channel = ctx.author.voice.channel
    serverName = ctx.message.guild.name

    def after_audio():
        voice_client = ctx.guild.voice_client
        randomnumber = random.randint(1,69)
        musicDir = ((str("D:\\App Files\\Brawl Music\\py\\music_")) + (str(randomnumber)) + (str ('.ogg')))
        voice_client.play(discord.FFmpegPCMAudio(source=musicDir), after=lambda e: after_audio())
        print((str ("RADIO: Playing 'music_")) + (str (randomnumber)) + (str ("' in [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in after_audio")))
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
            print((str ("RADIO: Connected and playing 'music_")) + (str (randomnumber)) + (str ("' in channel [")) + (str (serverName)) + (str ("/")) + (str (channel)) + (str ("] Debug data: in playtheaudio()/try:")))
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
    serverID = ctx.message.guild.id

    file=open(((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Logs\\MessageLog.txt"))),encoding="UTF-8").read()
    count=file.count(searchTerm)

    count = count - 1
    
    #await ctx.send((str ("Searched message log file for '**")) + (str (searchTerm)) + (str ("**'. Found `")) + (str (count)) + (str ("` occurences!")))

    embed = discord.Embed()
    embed.add_field(name="Occurences of '**{}**':".format(searchTerm), value="{}".format(count), inline=False)
    embed.set_footer(text=((str ("\nMessageLog.txt"))))
    await ctx.send(embed=embed)

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.log' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   lines

@client.command(help="l i n e s", brief="A whole bunch of useful statistics", pass_context=True)
async def stats(ctx):

    YTAPI_Status = "Enabled"
    SCAPI_Status = "not implemented"

    if round(client.latency * 1000) <= 100:
        pingColour = (0x44ff44)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xffd000)
    elif round(client.latency * 1000) <= 150:
        pingColour = (0xff6600)
    else:
        pingColour = (0x990000)

    fileSizeBytes = os.path.getsize('D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\v1.0.0.py')

    num_lines = sum(1 for line in open ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\v1.0.0.py", encoding='utf-8'))

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

    embed = discord.Embed(title="Bot Stats\n", colour=(pingColour))
    embed.add_field(name="Lines of Code", value="{} lines".format(num_lines), inline=False)    
    embed.add_field(name="File Size", value=((str (fileSizeBytes)) + (str (" bytes"))), inline=False)    
    embed.add_field(name="Uptime", value=((str (real_uptimeInSeconds)) + (str (" ")) + (str (secsOrMins1)) + (str (" (")) + (str (uptimeInSeconds)))  + (str (" ")) + (str (secsOrMins2)) + (str (" since run)")), inline=False)
    embed.add_field(name="Ping", value=((str (ping)) + (str (" ms"))), inline=False)
    embed.add_field(name="Servers Joined", value=(servers), inline=False)
    embed.add_field(name="Members in All Servers", value=(members), inline=False)
    embed.add_field(name="Random Integer", value=(random.randint(0,10000000)), inline=False)

    embed.add_field(name="\nDebug Mode", value="Disabled")
    embed.add_field(name="Command Logging", value="Enabled")
    embed.add_field(name="Message Logging", value="Enabled")
    embed.add_field(name="Voice Channels", value="Enabled")
    embed.add_field(name="YouTube Downloader", value=(YTAPI_Status))
    embed.add_field(name="Supercell API", value=(SCAPI_Status))

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
            os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1")

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
            os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1")
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
async def playdir(ctx):
    channel = ctx.author.voice.channel
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]

    try:
        my_file = Path((str (sp1)))
        if my_file.is_file():
            voice_client = ctx.guild.voice_client
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe", source=(str (sp1)))) 

            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('❌')
            embed=discord.Embed(title="An error occured", description="Manual exception: *File doesn't exist!* Maybe you typed the filename incorrectly?", color=0x990000)
            await ctx.send(embed=embed)
            return
        f = open(GlobalLogDir, "a")
        f.write((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)))

    except:
        channel = ctx.author.voice.channel
        await channel.connect()
        sp1 = text.split(' ', 1)[-1]
        my_file = Path((str (sp1)))
        if my_file.is_file():
            voice_client = ctx.guild.voice_client
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\2\\bin\\ffmpeg.exe", source=(str (sp1)))) 

            await ctx.message.add_reaction('✅')
            await ctx.send(embed=embed)
        else:
            await ctx.message.add_reaction('❌')
            embed=discord.Embed(title="An error occured", description="Manual exception: *File doesn't exist!* Maybe you typed the filename incorrectly?", color=0x990000)
            await ctx.send(embed=embed)
            return
        f = open(GlobalLogDir, "a")
        f.write((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
        f.close()
        print ((str ("\nAUDIO COMMAND RAN -> '.playdir' ran by ")) + (str (ctx.message.author)))

#   oldPlay

@client.command(help="Plays audio at predefined directory.", brief="[Audio] Plays audio using old version", pass_context=True)
async def oldplay(ctx):
    channel = ctx.author.voice.channel
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(executable="D:\\ffmpeg\\bin\\ffmpeg.exe", source=(str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Files\\")) + (str (sp1))))
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

@client.command(help="Streams youtube audio into voice channel.", brief="[Audio] Sets audio volume (WARNING BROKEN)", pass_context=True)
async def volume(ctx):
    try:
        text = ctx.message.content
        sp1 = text.split(' ', 1)[-1]
        newVolume = (float (sp1))
        voiceVolume = newVolume
        await ctx.send((str ("Volume set to ")) + (str (voiceVolume)))
    except:
        await ctx.send('errorrer1?!?!?1!!?1/11!?!!')

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
    os.chdir("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\youtube-dl")
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

#   YouTubeube search, download, convert, play.

@client.command(help="Downloads a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Searches for and plays YouTube video", pass_context=True)
async def yt(ctx, url: str):
    try:
        voice = ctx.guild.voice_client
        os.chdir("Z:\\")
        text = ctx.message.content

        voice.stop()
        await asyncio.sleep(0.5)
        searchTerm = text.split(' ', 1)[-1]

        results = YoutubeSearch(searchTerm, max_results=1).to_dict()

        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print((str ('\n\nresult = ')) + (str (result)))
            url = result

            text = ctx.message.content

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        filename = (str(uuid.uuid4()))

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"File: {file}\n")
                os.rename(file, filename)
                print("Renamed to", (filename))

        voice.play(discord.FFmpegPCMAudio(filename))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.1

        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: **{nname[0]}**")
    except ClientException:
        voice = ctx.guild.voice_client
        os.chdir("Z:\\")
        text = ctx.message.content

        channel = ctx.author.voice.channel
        await channel.connect()
        
        await asyncio.sleep(0.5)
        voice = ctx.guild.voice_client
        voice.stop()
        searchTerm = text.split(' ', 1)[-1]

        results = YoutubeSearch(searchTerm, max_results=1).to_dict()

        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print((str ('\n\nresult = ')) + (str (result)))
            url = result

            text = ctx.message.content

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        filename = ((str(uuid.uuid4())) + (str (".draggiebotAudio")))

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"File: {file}\n")
                os.rename(file, filename)
                print("Renamed to ", (filename))

        voice.play(discord.FFmpegPCMAudio(filename))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.1

        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: **{nname[0]}**")

#   ytstream

@client.command(help="Streams a youtube video using the search term and plays the audio to the voice channel.", brief="[Audio] Streams YT audio. Sligthly buggy, may die randomly.", pass_context=True)
async def yts(ctx):
    try:
        text = ctx.message.content
        searchTerm = text.split(' ', 1)[-1]

        results = YoutubeSearch(searchTerm, max_results=1).to_dict()

        for v in results:
            result = ('https://www.youtube.com/watch?v=' + v['id'])
            print((str ('\n\nresult = ')) + (str (result)))
            url = result
        
            text = ctx.message.content

            ydl_opts = {'format': 'bestaudio'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                
            
            voice_client = ctx.guild.voice_client
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(URL, executable="D:\\Downloads\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\bin\\ffmpeg.exe"))

            await ctx.send((str ("Streaming audio")))
    except:
        print ('\nAn error cccured. Resorting to backup:\n')
        channel = ctx.author.voice.channel
        await channel.connect()
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
            
            voice_client = ctx.guild.voice_client
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(URL, executable="D:\\Downloads\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\ffmpeg-2021-03-14-git-1d61a31497-full_build\\bin\\ffmpeg.exe"))

            await ctx.send((str ("Streaming audio")))
            print((str ("This may be of use: ")) + (str (URL)) + (str ("\n")))

#   Get links

@client.command(help="Gets YouTube video raw links.", brief="Gets YouTube video's and raw audio URL", pass_context=True)
async def links(ctx):
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

@client.command(help="Pauses the current audio.", brief="[Audio] Pauses audio", pass_context=True)
async def pause(ctx):    
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("*✅ Paused audio!*")
    else:
        await ctx.send("Audio is unable to be paused")

#   Resumes audio

@client.command(help="Resumes playing the current audio.", brief="[Audio] Resumes audio", pass_context=True)
async def resume(ctx):    
    voice_client = ctx.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("*✅ Resumed playing audio!*")
    else:
        await ctx.send("Audio is unable to be resumed")

#   Stop audio

@client.command(help="Stops playing the current audio.", brief="[Audio] Stops audio", pass_context=True)
async def stop(ctx):    
    voice_client = ctx.guild.voice_client
    voice_client.stop()
    await ctx.send((str ("Stopped playing audio.")))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nAUDIO COMMAND RAN -> '.stop' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nAUDIO COMMAND RAN -> '.stop' ran by ")) + (str (ctx.message.author)))
    return

#   join/leave voice

@client.command(help="Joins message author's voice channel", brief="[Audio] Joins voice chat", pass_context=True)
async def join(ctx):#    Joins
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send((str ("Joined voice channel *")) + (str (channel)) + (str ("*.")))
    except:
        await ctx.send("You are not in a voice channel, please join one before running the command.")
        return
    f = open(GlobalLogDir, "a")
    f.write((str ("\nAUDIO COMMAND RAN -> '.join' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nAUDIO COMMAND RAN -> '.join' ran by ")) + (str (ctx.message.author)))  

@client.command(help="Leaves message author's voice channel", brief="[Audio] Leaves voice chat", pass_context=True)
async def leave(ctx):#  Leaves
    channel = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
    await ctx.send((str ("Left voice channel ")) + (str (channel)))
    f = open(GlobalLogDir, "a")
    f.write((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nAUDIO COMMAND RAN -> '.leave' ran by ")) + (str (ctx.message.author)))  

#   Purge

@client.command(help="Purges a specified amount of messages", brief="Purges messages", pass_context=True)
@commands.has_any_role('Admin', 'Mod', 'King')
async def purge(ctx):
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

#   i g n o r e

@client.command(help="UwU", brief="UwU", pass_context=True)
@commands.has_any_role('Admin', 'Mod')
async def uwu(ctx):
    uwuwu = random.randint(1,2)
    if uwuwu == 1:
        await ctx.send(file=discord.File(r"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Assets\\Commands\\I_regret_making_this.png", filename="UwU.png"))
    if uwuwu == 2:
        await ctx.send(file=discord.File(r"D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Assets\\Commands\\canvas_1.png", filename="canvas_1.png"))
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
    txt = ctx.message.content
    x = txt.split()
    print(x[1])
    playerTag = (x[1])
    playerTag = playerTag.upper()

    print((str ('playerTag = ') + (str (playerTag))))
    if (x[2]) == 'brawlers':
        url = ((str ('https://api.brawlstars.com/v1/players/%23')) + (str (playerTag)))
        print((str ('url = ') )+ (str (url)))

        headers = {
        'Accept': 'application/json',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhhYzA0YjgxLWZkMzctNDU0My1iNTVlLWJmZjRjOGVhMzJhMiIsImlhdCI6MTYxNTcyMjA0OCwic3ViIjoiZGV2ZWxvcGVyL2EwNzQ5Zjk3LTA5MTYtNDNmZC00NzRkLWQxMWJjOWYwOTZkNCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMzEuMTI1LjE5OS4xMDEiXSwidHlwZSI6ImNsaWVudCJ9XX0.u3RGk5QmvXWz1pfUoDwcc9U-0JUDGaundRqd_bScjFnOdRMfbxfu4T-b_WLQ0DWA5vNdA4L6N0aUXpcCOozt-g',
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
    my_file = Path((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Files\\")) + (str (sp1)))
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
    try:
        text = ctx.message.content
        syntaxErrorChecker = text.split(' ', 1)[-1]
        birthDate = text.split(' ', 2)[-1]
        x = text.split()
        if x[1] == "file":
            with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\logs\\birthdays.txt") as file:
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
            with open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\logs\\birthdays.txt") as file:
                birthdays = file.read()
                embed=discord.Embed(title="All Birthdays", description=(birthdays), colour=0x00acff)
                await ctx.send(embed=embed)
        if (x[1]) == "0":
            await ctx.send("Error! Please ensure your command looks something like this:\n\n**.birthday set 25th June 2006**")

        if x[1] == "set":
            author = (str (ctx.message.author.id))
            file=open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Logs\\birthdays.txt",encoding="UTF-8").read()
            count=file.count(author)
            print (count)
            if count != 0:
                await ctx.send("Error! You have already added your birthday to the file. Please ask an admin to remove it if you believe this is an error.")    
                return

            f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\logs\\birthdays.txt", "a")
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
    arr = os.listdir('D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Files')
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
    my_file = Path((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Files\\")) + (str (x[1])))
    if my_file.is_file():
#           await ctx.send("True")
        await ctx.send(file=discord.File((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Files\\")) + (str (x[1]))))
    else:
        embed=discord.Embed(title="Error: 404", description=((str ("File ")) + (str ((x[1]))) + (str (" not found!"))), colour=0x990000)
        await ctx.send(embed=embed)
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.file' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.file' ran by ")) + (str (ctx.message.author)))    

#   Ship

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

#   Command template

@client.command(help="Lots of help goes here", brief="[template command]", pass_context=True)
async def COMMAND(ctx):
    await ctx.send("Sends a message.")
    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.COMMAND' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()
    print ((str ("\nCOMMAND RAN -> '.COMMAND' ran by ")) + (str (ctx.message.author)))

#   Nolwennium mine

@client.command(help="Mines a random amount of Nolwennium.", brief="Mines Nolwennium for games.", pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def mine(ctx):
    global balance
    global myuuid
    global address

    authorID = ctx.message.author.id
    person = ctx.message.author
    serverID = ctx.message.guild.id
    address = authorID

    filedir = (str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")) + (str (authorID)) + (str (".txt"))
    serverdir = ((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium\\")))
    
    if not os.path.exists(serverdir):
        os.makedirs((str ("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Servers\\")) + (str (serverID)) + (str ("\\Nolwennium")))

    try:
        e = open(filedir, 'r')
        balance = (float (e.read()))
        e.close()
    except:
        e = open(filedir, 'w+')
        e.write(str (0))
        e.close()

        e = open(filedir, 'r')
        balance = (float (e.read()))
        e.close()
        #await ctx.send("Hi! As it's your first time, I'll be gentle. Please run the command again!")
        #return
    
    #await ctx.send((str ("\n\nYour address is: ")) + (str (address)))
    newNumber = random.randint(1,10)
    fee = newNumber/(random.randint(50,200))
    newNumberAfterFee = newNumber - fee
    newNumberAfterFee = round(newNumberAfterFee, 3)
    fee = round(fee, 3)

    minedString = ((str ("\nMined another ")) + (str (newNumber)) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium!")))

    roleBooster = discord.utils.find(lambda r: r.name == 'Server Booster', ctx.message.guild.roles)

    embed=discord.Embed(title="⛏️ Miner ⛏️", description = minedString, colour =0x44ff44)
    embed.add_field(name="Fees Paid", value=fee, inline=False)
    
    balance = balance + newNumberAfterFee

    if roleBooster in person.roles:
        BoosterBonus = random.randint(5,15)
        embed.add_field(name="Server Booster Bonus", value=(str (BoosterBonus)) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium")))
        balance = balance + BoosterBonus

    embed.add_field(name="Total Balance", value=((str (round (balance, 3))) + (str (" <:NolwenniumCoin:846464419503931443> Nolwennium"))), inline=False)
    embed.set_footer(text=((str ("User ID: ")) + (str (authorID))))
    await ctx.send(embed=embed)

    f = open(filedir, 'w+')
    f.write((str (balance)))
    f.close()

    f = open(GlobalLogDir, "a")
    f.write((str ("\nCOMMAND RAN -> '.mine' ran by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))))
    f.close()

#   ON ERROR

@client.event
async def on_command_error(ctx, error):
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
    f = open("D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\errors.txt", "a")
    f.write((str ("\n\nERROR: An error occured! Original command initialised by ")) + (str (ctx.message.author)) + (str (" at ") + (str (datetime.now()))) + (str (".\n          : ")) + (str(error)))
    f.close()

load_dotenv(dotenv_path='D:\\OneDrive - Sapientia Education Trust\\Year 10\\Computer Science\\Python\\draggiebot\\v1\\Tester.env')
client.run(os.getenv('TOKEN'))

#   poggerspogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpogpog