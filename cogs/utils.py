"""
Utility functions and helpers for BaguetteBot.

This module contains shared utility functions used across different cogs.
"""

import os
import json
import discord
from datetime import datetime
from typing import Optional


async def slash_log(interaction: discord.Interaction, base_dir: str, s_slash: str, global_log_dir: str):
    """
    Log slash command usage to file and check ToS acceptance.
    
    Args:
        interaction: The Discord interaction object
        base_dir: Base directory path
        s_slash: System-specific slash character
        global_log_dir: Global log file directory
    """
    print(f"/ [SlashCommand]   {interaction.data['name']} ran by {interaction.user.id} ({interaction.user.name} at {datetime.now()})")
    
    if not os.path.isfile(f"{base_dir}Users\\JSONSettings{s_slash}{interaction.user.id}.json"):
        view = discord.ui.View()
        view.add_item(AcceptToSButtons(label="Accept ToS", style=discord.ButtonStyle.success))
        view.add_item(discord.ui.Button(label="View ToS", style=discord.ButtonStyle.link, url="https://terms.ibaguette.com/#discord-bots"))
        return await interaction.response.send_message(
            "You must accept the iBaguette Terms of Service and BaguetteBot supplemental Terms of Service once before using a Slash Command.", 
            view=view, 
            ephemeral=True
        )
    else:
        with open(f"{base_dir}Users\\JSONSettings{s_slash}{interaction.user.id}.json", 'r') as json_file:
            json_data = json.load(json_file)
            if not json_data['accepted_tos'] == 'true':
                view = discord.ui.View()
                view.add_item(AcceptToSButtons(label="Accept ToS", style=discord.ButtonStyle.success))
                view.add_item(discord.ui.Button(label="View ToS", style=discord.ButtonStyle.link, url="https://terms.ibaguette.com/#discord-bots"))
                return await interaction.response.send_message(
                    "You must accept the iBaguette Terms of Service and BaguetteBot supplemental Terms of Service once before using a Slash Command.", 
                    view=view, 
                    ephemeral=True
                )
                
    with open(global_log_dir, 'a', encoding="utf-8") as file:
        file.write(f"/ [SlashCommand]      {interaction.data['name']} ran by {interaction.user.id} ({interaction.user.name} at {datetime.now()})\n")


async def get_coins(server_id: int, user_id: int, base_dir: str, s_slash: str) -> Optional[int]:
    """
    Get a user's coin balance.
    
    Args:
        server_id: Discord server ID
        user_id: Discord user ID
        base_dir: Base directory path
        s_slash: System-specific slash character
        
    Returns:
        User's coin balance or None if not found
    """
    coin_dir = f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}.txt"
    if not os.path.exists(coin_dir):
        return None
    with open(coin_dir, 'r') as f:
        balance = int(f.read())
    print(f"[CoinsQuery]    Balance called for {user_id} in {server_id}. (Balance: {balance})")
    return balance


def update_coins(server_id: int, user_id: int, coins_calc: int, base_dir: str, s_slash: str) -> int:
    """
    Update a user's coin balance.
    
    Args:
        server_id: Discord server ID
        user_id: Discord user ID
        coins_calc: Amount to add/subtract
        base_dir: Base directory path
        s_slash: System-specific slash character
        
    Returns:
        New coin balance
    """
    coin_dir = f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}.txt"
    if not os.path.exists(f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins"):
        os.makedirs(f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins")
        
    multiplication_amount = 1
    if os.path.isfile(f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}_boosted.json"):
        with open(f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}_boosted.json", 'r') as f:
            info = json.load(f)
            expiration_time = info['currentBoosts'][0]['expirationTime']
            expiration_datetime = datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f')
            if expiration_datetime > datetime.now():
                multiplication_amount = info['currentBoosts'][0]['multiplier']
            else:
                os.remove(f"{base_dir}Servers{s_slash}{server_id}{s_slash}Coins{s_slash}{user_id}_boosted.json")
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


async def bot_runtime_events(event_int: int, bot_events: int) -> int:
    """
    Track bot runtime events.
    
    Args:
        event_int: Number of events to add
        bot_events: Current bot events count
        
    Returns:
        Updated bot events count
    """
    return bot_events + event_int


async def duration_to_time(duration: int, format: Optional[int] = None) -> str:
    """
    Convert duration in milliseconds to formatted time string.
    
    Args:
        duration: Duration in milliseconds
        format: Optional format specifier
        
    Returns:
        Formatted time string
    """
    seconds = int((duration / 1000) % 60)
    minutes = int((duration / (1000 * 60)) % 60)
    hours = int((duration / (1000 * 60 * 60)) % 24)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"


async def error_code(interaction: discord.Interaction, code: int, error_messages_codes: list, base_dir: str, *note: str, **raw_error: Exception):
    """
    Send formatted error message to user.
    
    Args:
        interaction: Discord interaction object
        code: Error code to display
        error_messages_codes: List of error message codes
        base_dir: Base directory path
        note: Optional error note
        raw_error: Optional raw exception
    """
    if note:
        print(f"A manual error was encountered and here is the information: {note}")
        
    random_cry = [
        '<:AmberCry:828577834146594856>', 
        '<:BibiByeBye:828683852939395072>', 
        '<:ColetteCry:828683829631516732>', 
        '<:JessieCry:828683805861740654>', 
        '<:SpikeCry:828683779206807622>', 
        '<:SurgeCry:828683755694063667>', 
        '<:TaraCry:828683724286853151>'
    ]
    
    import random
    embed = discord.Embed(
        title=f"{random.choice(random_cry)} An error occured",
        description=f"**{str(random.choice(error_messages_codes[code]))}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.",
        color=0x990000
    )
    
    try:
        await interaction.response.send_message(embed=embed)
    except discord.app_commands.errors.CommandInvokeError:
        await interaction.followup.send(embed=embed)
    
    if raw_error:
        with open(f"{base_dir}errors.txt", "a") as f:
            f.write(f"\nERROR: An error occured! Original command initialised by {interaction.user} at {datetime.now()}. ERROR MESSAGE: {str(raw_error)}")


class AcceptToSButtons(discord.ui.Button):
    """Button for accepting Terms of Service."""
    
    def __init__(self, label: str, style: discord.ButtonStyle, base_dir: str, s_slash: str):
        super().__init__(label=label, style=style)
        self.base_dir = base_dir
        self.s_slash = s_slash
        
    async def callback(self, interaction: discord.Interaction):
        """Handle ToS acceptance button click."""
        user_id = interaction.user.id
        filepath = f"{self.base_dir}Users{self.s_slash}JSONSettings{self.s_slash}{user_id}.json"
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
            data['accepted_tos'] = 'true'
            with open(filepath, 'w') as f:
                json.dump(data, f)
        
        await interaction.response.send_message("Thank you for accepting the Terms of Service!", ephemeral=True)
