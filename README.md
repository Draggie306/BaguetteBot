# BaguetteBot

  

BaguetteBot/DraggieBot is a Discord bot.

Features:

- Logs member activity, role changes and more
- Moderation commands
- Currency systems
- Music playing
- Slash Commands

Read what else the bot can do [here](https://ibaguette.com/b)

Read v1's patch notes [here](https://www.ibaguette.com/p/baguettebot-v1-patch-notes.html)!

In the future, there will be many more controls on a server-level basis.

If there's an issue with it in Discord or a blindingly obvious issue in the code, please add it as an issue, or ping me on Discord via @Draggie#3060! This will help so much :)

Invite the bot to your server [here](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=8&scope=bot%20applications.commands). Make sure the bot has sufficient permissions!

# How to use: commands, server monitoring and more

### **Slash Commands:**

- **components** - enables or disables specified BaguetteBot components. These include member activity logging*, DMs when a user is given a role, DMs for BaguetteBot events and DMs when a user's message gets deleted. Sends a confirmation message when ran.
 
- **ping** - Gets the bot's ping or latency. Sends an embed with the data

- **test** - Gets data needed which may be useful for reporting bugs. Sends a message with various IDs and values.

> Over time, dot commands will be migrated over to Slash Commands, depending on Discord's requirements. Rewriting code takes a long time, so don't expect this to be a fast process.
  
### **Dot Commands:** (ran by typing command name prefixed with a dot)
  
- **baguette** - Sends a random baguette picture. ***(Will be phased out in the near future)***
- **bot** - Bots a Kahoot lobby. The syntax is `.bot <CODE> <AMOUNT> <NAME/"random">`, where `CODE` is the Game PIN, `AMOUNT` is the number of bots to add, and `NAME` is the name of the bots you'd like. This can be `random` where the bot will generate a random Kahoot safe name. *Requires 10 Nolwennium per bot.*
- **coins** - Displays the user's coins amount for that server, determined by the amount of messages sent. Requires the intent `on_message` - or permission `view_messages` to function correctly. 
>Admins can use `.coins <MODIFY> <USERID>`, where `MODIFY` can be either `set` to set a user's coins, `add` to add to a user's balance, or `lookup` to check a user's balance. Use `/s` to do this silently to avoid pings to a users. 
- **buy** - Displays what the user can buy with their current Coin balance.
>Admins: If you want to allow full functionality for this, add these roles to your server: `Citizen` (free), `Knight` (250 coins), `Prince` (1000 coins) and `King` (2500 coins). Users earn 1 coin per message sent. Assign privileges to these roles with care, and this will be available to be turned off in the components menu.
- **bitrate** - Changes a voice channel's bitrate. Use `.bitrate <CHANNELID/"all">` where `CHANNELID` is the voice channel's ID. This can be replaced with `all` to set the bitrate for all voice channels. *Requires 1 Nolwennium.*



> Member activity logging includes status changes, when a user begins typing, message edits, deletions, profile updates. The full list of what the bot can see depends on the permissions it's given in a server.

# Currency System
The bot keeps a record of hundreds of users and tens of thousands of user events per day, including reactions to messages, sent items and time in voice channels, and adds this to a database of numbers which represent how much currency a user has. There are two types, one server-level (simply called Coins) and one across all servers (Nolwennium). Note that sensitive data, such as what a user is actually sending, is not recorded, just the amount of times this happens, only if specifically enabled by an admin. To see whether this is enabled, run the command .coins.
### List of currency-related dot commands:

- **coins** - Displays the user's coins amount for that server, determined by the amount of messages sent. 
>Admins can use `.coins <MODIFY> <USERID>`, where `MODIFY` can be either `set` to set a user's coins, `add` to add to a user's balance, or `lookup` to check a user's balance. Use `/s` to do this silently to avoid pings to a users. Requires the intent `on_message` - or permission `view_messages` to function correctly. 
- **buy** - Displays what the user can buy with their current Coin balance. Users earn 1 coin per message sent. 
>Admins: If you want to allow full functionality for this, add these roles to your server: `Citizen` (free), `Knight` (250 coins), `Prince` (1000 coins) and `King` (2500 coins). Assign privileges to these roles with care, and this will be available to be turned off in the components menu.
- **gamble** - Rolls two 6 sided die. If you guess correctly, you gain a huge profit. If not, you'll lose some of your balance.



___
Privacy note: The bot actively listens for the following events, or gateway intents. Not all of these will be recorded for every user and every server. This data is only used for debugging processes:

- on_ready
-  on_member_join
- on_member_remove
- on_raw_reaction_add
- on_guild_remove
- on_message_delete
- on_message_edit
- on_typing
- on_member_update
- on_message
- on_slash_command_error
- on_command_error
- on_voice_state_change 

# Note: 'versions' are only major versions, the bot runs on the versions published in main, which include minor/patch versions
