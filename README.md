Invite the bot to your server! 
- [admin link](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=8&scope=bot%20applications.commands)
- [choose permissions](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=1618585447491&scope=bot%20applications.commands)

# BaguetteBot

BaguetteBot/DraggieBot is a Discord.py bot, specialising in audio playing, fast & custom utilities, as well as enhanced logging and intelligent spam prevention.
The bot's support server along with all my other projects is (Baguette Brigaders)[https://discord.gg/F5Vu9PhXMr]. Join to get notified of updates, capabilities and chat with a ton of cool people in our community.

## Details

Check out how to use the bot, video instructions and some explanations [on my website](https://ibaguette.com/b).
You can also check out [my large blog](https://discord.gg/F5Vu9PhXMr) for technical developments and a live feed for any major updates.

If there's an issue with it in Discord or a blindingly obvious issue in the code, please add it as an issue, or ping me on Discord via @Draggie#3060! This will help so much :)

Invite the bot to your server [here](https://discord.com/oauth2/authorize?client_id=792850689533542420&permissions=8&scope=bot%20applications.commands). Make sure the bot has sufficient permissions!

## Features

- Logs
- - Member activities checker (auto roles)
- - Role modifications
- - Server events, e.g channel changes and deletions
- Moderation commands
- Social activities
- Audio playing
- - YouTube videos & playlists
- - Spotify tracks & playlists
- - automatic seeking, queuing, volume changes and locks
- - custom URLs
- Currency systems, both in a server and globally
- Fully supported, easy-to-use Slash Commands

# How to use

Read below for commands, server monitoring, griefing prevention and more

### **Slash Commands:**

- **sync-commands**
Used to synchronize edited client tree commands to Discord servers. The command is only accessible to bot administrators.

To use this command, the bot administrator must run the command in Discord, and it will sync the client tree commands to the server. This command is asynchronous and returns nothing.

The command also includes an interaction parameter that represents the interaction between the user and the bot. The slash_log function is called to log the interaction, and the defer function is called to delay the bot's response to the interaction due to rate limiting.

If the user who initiated the interaction is not a bot administrator, the bot will send a message saying that the command is bot admin only. Otherwise, the bot will respond with a message indicating that the client tree commands have been synced.

- **stats**
Provides useful statistics about the bot. It displays information such as CPU and RAM usage, number of lines of code, file size, uptime, ping, number of videos loaded, servers and members, and various statuses such as Debug Mode and YouTube Player. It also logs the command usage in a global log file.

- **snowflake**
converts a Discord snowflake into a DateTime object with accuracy to the second. Users input the snowflake as a string, and the command will output the corresponding date and time in both exact and relative formats.

The command works by first converting the input snowflake into an integer, then using it to calculate a Unix timestamp. The timestamp is then converted into a string representing the date and time in UTC format. Finally, the string is split into its individual components and formatted into a message that is sent back to the user. If the input is not a valid integer, an error message is sent instead.

- **coins**
Shows the coin balance of a user. If the coin balance is above a threshold, it also displays items to buy. The command uses three role ids: member_role, staff_role, and owner_role. The code fetches the user's balance, creates a new user if the user is new, and shows the user their balance. The command has three options: set, add, and lookup. Set and add are admin-only operations and require the user id to target and mod_value to use as a value for the operation. If the user is not an admin and runs this command with set or add options, they will receive a message informing them that they do not have full administrator privileges to run this command. The lookup option is available to all users and requires the user id to look up the coin balance.

- **buy**
Shows your balance and items that can be purchased. When you enter an item name as an argument, the bot deducts the cost of that item from your balance and assigns the corresponding role. Roles are used to provide users with additional permissions or features within the server. The Python code checks the user's balance, whether the user already has the item, and whether the user has the required role for a higher-level item. The bot provides messages to the user to indicate if the purchase was successful or if the user does not have enough currency.

- slowmode

This command allows Discord server admins to set the slowmode delay in a channel through a slash command. With this command, users can input the number of seconds they want to set for slowmode and it will be applied to the specified channel. If the input is invalid or the user does not have the required permission, an error message will be displayed.

It takes an input of seconds and checks if the user has the manage_channels permission. If the input is valid and the permission is granted, the command sets the slowmode delay in the channel and logs the command usage. If the input is invalid or the permission is not granted, an error message is displayed. Finally, an embed message is sent to confirm the successful execution of the command.

- emoji-backup

Retrieves emojis from a server ID and saves them to a local directory, allowing users to retrieve the emojis at a later date.

Automates the process of backing up server emojis. The code uses requests to download and save the emoji images to a specified directory, while using Discord.py to interact with users and the server. The command also includes error handling and permissions checks to ensure that only users with the necessary permissions can access and backup the server emojis.

> Over time, dot commands will be migrated over to Slash Commands, depending on Discord's requirements. Rewriting code takes a long time, so don't expect this to be a fast process.
  
- get-messages
specific user object. The command is only available to users with admin privileges, and it requires the user ID of the target user. Once executed, the command will display the 30 most recent messages sent to the user, along with the name of the sender and the message content.

Retrieves the direct messages sent to a particular user object. The command can be executed by using the "/get_messages" command, followed by the user ID of the target user. The command uses the "create_dm()" method to create a direct message channel, then iterates through the channel's message history to retrieve the 30 most recent messages. The sender's name and the message content are displayed using the "send_message()" method. The command is only available to users with admin privileges, as specified by the if statement that checks the user ID.


- logsearch
Allows users to search the message history of a server for a specific term and returns how many times it was sent. The command is not case-sensitive and does not account for bot messages.

Developer Notes
The function first checks if the user has the view_audit_log permission and if the command is used in a server. It then opens the message log file for the server and counts the occurrences of the given term. The result is sent in an embed message along with the server name and ID. The command also logs when it was ran and by whom.

- volume
This command allows users to change the audio player's volume or lock it.

Developer Notes
The volume command takes two arguments - percentage and lock (optional). The percentage argument specifies the volume in percentage to play, while the lock argument allows users to lock the volume. If lock is set to True, only guild managers will be able to modify the volume again.

The command first checks if the inputted percentage is a valid integer. If not, an error message is returned. If the input is valid, the command proceeds to set the volume to the inputted percentage. The command also checks if the volume is locked - if it is, only guild managers can modify the volume.

The command also uses an experimental audio player, Wavelink, to handle audio.

Developer Notes:
The code utilizes the @client.tree.command decorator to create the command and the @app_commands.describe decorator to add a description for the term argument. The function first checks if the user has the view_audit_log guild permission and if the command is being used in a guild. It then reads a text file containing the message log for the server and counts how many times the specified term appears. The function creates and sends an embed with the results and logs the command usage to a file.





Privacy note: The bot actively listens for the following events, or gateway intents. Not all of these will be recorded for every user and every server. This data is only used for debugging processes:

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

# Note: 'versions' are only major versions, the bot runs on the versions published in main, which include minor/patch versions
