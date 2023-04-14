Invite the bot to your server! 
- [admin link](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=8&scope=bot%20applications.commands)
- [choose permissions](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=1618585447491&scope=bot%20applications.commands)

# BaguetteBot

BaguetteBot/DraggieBot is a Discord.py bot, specialising in audio playing, fast & custom utilities, as well as enhanced logging and intelligent spam prevention.
The bot's support server along with all my other projects is [Baguette Brigaders](https://discord.gg/F5Vu9PhXMr). Join to get notified of updates, capabilities and chat with a ton of cool people in our community.

## Details

Check out how to use the bot, video instructions and some explanations [on my website](https://ibaguette.com/b).
You can also check out [my large blog](https://discord.gg/F5Vu9PhXMr) for technical developments and a live feed for any major updates.

If there's an issue with it in Discord or a blindingly obvious issue/error/typo in the code, please add it as an issue, create a merge request, or ping me on Discord - I'm [Draggie#3060](discord:///users/382784106984898560)! This will help so much :)


## Features

- Logs
  - Member activities checker (auto roles)
  - Role modifications
  - Server events, e.g channel changes and deletions
- Moderation commands
	- intelligent spam and raid prevention
	- enforces rules, reducing bypass rates
- Utilities
	- backup emojis
	- backup layout
	- role permission checking
	- 
- Social activities
	- auto reactions
	- voice chat activities
- Audio playing
  - YouTube videos & playlists
  - Spotify tracks & playlists
  - automatic seeking, queuing, volume changes and locks
  - **releasing soon:** audio filters and effects
  - custom URLs
- Currency systems, both in a server and globally
	- use Coins to buy roles within servers
	- use the global currency to play a minigame and brag to others!
- Fully supported, easy-to-use Slash Commands

# How to use

Read below for commands, server monitoring, griefing prevention and more

## **Slash Commands:**

### sync-commands
Used to synchronize edited client tree commands to Discord servers. The command is only accessible to bot administrators.

To use this command, the bot administrator must run the command in Discord, and it will sync the client tree commands to the server. This command is asynchronous and returns nothing.

The command also includes an interaction parameter that represents the interaction between the user and the bot. The slash_log function is called to log the interaction, and the defer function is called to delay the bot's response to the interaction due to rate limiting.

If the user who initiated the interaction is not a bot administrator, the bot will send a message saying that the command is bot admin only. Otherwise, the bot will respond with a message indicating that the client tree commands have been synced.

### stats
Provides useful statistics about the bot. It displays information such as CPU and RAM usage, number of lines of code, file size, uptime, ping, servers and members, and of various statuses such as whether Debug Mode is enabled and what YouTube Player system is being used

### snowflake
Converts a Discord snowflake obtained by using developer mode into an easy to read string with the snowflake's date and time, accurate to the second.
The command outputs the corresponding date and time in both exact and relative formats.

### coins
Shows the coin balance of a user. If the coin balance is above a threshold, it also displays items to buy.
> The code fetches the user's balance, creates a new user if the user is new, and shows the user their balance. The command has three options: set, add, and lookup. **set** and **add** are admin-only operations and require the **user id** to target and **mod_value** to use as a value for the operation. 
> If the user is not an admin and runs this command with set or add options, they will receive a message informing them that they do not have full administrator privileges to run this command. The **lookup** option is available to all users and requires the **user id** to look up the coin balance.

### buy
Shows your balance and items that can be purchased, based on checks the user's balance, whether the user already has the item, and whether the user has the required role for a higher-level item

> The bot provides messages to the user to indicate if the purchase was successful or if the user does not have enough currency.
> When you enter an item name as an argument, the bot deducts the cost of that item from your balance and assigns the corresponding role. Roles are used to provide users with additional permissions or features within the server. 
### slowmode

**Admin:** Sets slowmode in the current channel in seconds.

> It takes an input of seconds and checks if the user has the **manage_channels** permission. If the input is valid and the permission is granted, the command sets the slowmode delay in the channel and logs the command usage. If the input is invalid or the permission is not granted, an error message is displayed.
> Response type: embed

### emoji-backup

Retrieves emojis from a server ID and saves them to a local directory, allowing users to retrieve the emojis at a later date, automates the process of backing up server emojis in lossless resolution.

>  The code uses requests to download and save the emoji images to a specified directory. The command also includes error handling and permissions checks to ensure that only users with the necessary permissions can access and backup the server emojis.
>  Response type: message
  
### get-messages

**Global Admin:** Gets the bot's latest 30 direct messages to a specific user.


### logsearch

**Admin:** Allows users to search the message history of a server for a specific term and shows how many times it was sent. The command is not case-sensitive and does not account for bot messages.

> The function first checks if the user has the **view_audit_log** permission and if the command is used in a server. It then opens the message log file for the server and counts the occurrences of the given term.
> Response type: message

### volume
This command allows users who are currently in a Voice Chat to change the audio player's volume, or lock it with admin priviliges. The limit is 1,000% loudness.

> The volume command takes two arguments - percentage and lock (optional). The percentage argument specifies the volume in percentage to play, while the lock argument allows users to lock the volume. If lock is set to True, only guild managers will be able to modify the volume again.
> The command first checks if the inputted percentage is a valid integer. If not, an error message is returned. If the input is valid, the command proceeds to set the volume to the inputted percentage. The command also checks if the volume is locked - if it is, only guild managers can modify the volume.





Privacy note: The bot actively listens for the following Discord.py events, or gateway intents. **You can choose the permissions that the bot is granted at all times in your server.** Not all of these will be recorded for every user and every server. This data is only used for debugging processes:

- on_ready
- on_member_join
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

# Footnotes
- Releases published are only major versions, the bot runs on the versions published in `main`, which include minor/patch versions.
- Changes to the code are often made in BaguetteBot Beta. This uses the `dev` branch and has a lot more patch versions.
