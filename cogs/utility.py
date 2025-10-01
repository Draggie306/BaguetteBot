"""
Utility Cog - Utility and helper commands for BaguetteBot.

This cog contains utility commands for server management, backups,
logging, and other administrative helper functions.
"""

import discord
from discord import app_commands
from discord.ext import commands
import os
import requests
from datetime import datetime
from typing import Optional


class Utility(commands.Cog):
    """Utility and helper commands for server management."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the Utility cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="emoji-backup", description="[Utility] Backs up all your server emojis.")
    @app_commands.describe(guild_id="The server ID to backup emojis from")
    async def emojis(self, interaction: discord.Interaction, guild_id: str):
        """
        Backup all emojis from a server.
        
        Args:
            guild_id: The Discord server ID to backup emojis from
            
        Downloads and saves all custom emojis from the specified server
        to allow for later restoration or transfer.
        
        Requires: manage_emojis permission
        """
        if not interaction.user.guild_permissions.manage_emojis:
            return await interaction.response.send_message(
                "You need the `Manage Emojis` permission to use this command.",
                ephemeral=True
            )
            
        try:
            guild_id_int = int(guild_id)
        except ValueError:
            return await interaction.response.send_message(
                "Invalid server ID. Please provide a valid numeric ID.",
                ephemeral=True
            )
            
        guild = self.bot.get_guild(guild_id_int)
        if not guild:
            return await interaction.response.send_message(
                "Could not find that server. Make sure the bot is in the server.",
                ephemeral=True
            )
            
        await interaction.response.defer()
        
        # Create backup directory
        backup_dir = f"{self.config.get('BASE_DIR', '')}emoji_backups{self.config.get('S_SLASH', '/')}{guild_id}"
        os.makedirs(backup_dir, exist_ok=True)
        
        saved_count = 0
        failed_count = 0
        
        for emoji in guild.emojis:
            try:
                # Download emoji
                emoji_url = str(emoji.url)
                extension = "gif" if emoji.animated else "png"
                filename = f"{emoji.name}.{extension}"
                filepath = os.path.join(backup_dir, filename)
                
                response = requests.get(emoji_url)
                if response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    saved_count += 1
                else:
                    failed_count += 1
            except Exception as e:
                print(f"Failed to backup emoji {emoji.name}: {e}")
                failed_count += 1
                
        embed = discord.Embed(
            title="Emoji Backup Complete",
            description=f"Backed up {saved_count} emojis from {guild.name}",
            color=0x00ff00
        )
        if failed_count > 0:
            embed.add_field(name="Failed", value=f"{failed_count} emojis could not be backed up")
            
        embed.add_field(name="Location", value=backup_dir)
        
        await interaction.followup.send(embed=embed)
        
    @app_commands.command(name="logsearch", description="[Utility] Search the message history for a term.")
    @app_commands.describe(term="The term to search for in message logs")
    async def log(self, interaction: discord.Interaction, term: str):
        """
        Search message logs for a specific term.
        
        Args:
            term: The search term to look for
            
        Searches the server's message logs and returns how many times
        the term was found. Case-insensitive search.
        
        Requires: view_audit_log permission
        """
        if not interaction.user.guild_permissions.view_audit_log:
            return await interaction.response.send_message(
                "You need the `View Audit Log` permission to use this command.",
                ephemeral=True
            )
            
        if not interaction.guild:
            return await interaction.response.send_message(
                "This command can only be used in a server.",
                ephemeral=True
            )
            
        await interaction.response.defer()
        
        # Build log file path
        log_dir = f"{self.config.get('BASE_DIR', '')}Servers{self.config.get('S_SLASH', '/')}{interaction.guild_id}{self.config.get('S_SLASH', '/')}Logs{self.config.get('S_SLASH', '')}MessageLog.txt"
        
        if not os.path.exists(log_dir):
            return await interaction.followup.send(
                "No message logs found for this server.",
                ephemeral=True
            )
            
        try:
            count = 0
            with open(log_dir, 'r', encoding='utf-8') as f:
                for line in f:
                    if term.lower() in line.lower():
                        count += 1
                        
            await interaction.followup.send(
                f"Found **{count}** occurrences of '**{term}**' in the message logs."
            )
        except Exception as e:
            await interaction.followup.send(
                f"Error searching logs: {str(e)}",
                ephemeral=True
            )
            
    @app_commands.command(name="bitrates", description="[Utility] Set all Voice Channel bitrates")
    @app_commands.describe(bitrate="The bitrate to set (in kbps)")
    async def bitrates(self, interaction: discord.Interaction, bitrate: Optional[str]):
        """
        Set bitrate for all voice channels in the server.
        
        Args:
            bitrate: Target bitrate in kbps (optional, defaults to 96)
            
        Updates the bitrate for all voice channels to improve or standardize
        audio quality across the server.
        
        Requires: manage_channels permission
        """
        if not interaction.user.guild_permissions.manage_channels:
            return await interaction.response.send_message(
                "You need the `Manage Channels` permission to use this command.",
                ephemeral=True
            )
            
        # Parse bitrate
        try:
            target_bitrate = int(bitrate) if bitrate else 96
            if target_bitrate < 8 or target_bitrate > 384:
                return await interaction.response.send_message(
                    "Bitrate must be between 8 and 384 kbps.",
                    ephemeral=True
                )
        except ValueError:
            return await interaction.response.send_message(
                "Invalid bitrate. Please provide a number.",
                ephemeral=True
            )
            
        await interaction.response.defer()
        
        # Update all voice channels
        updated = 0
        failed = 0
        
        for channel in interaction.guild.voice_channels:
            try:
                await channel.edit(bitrate=target_bitrate * 1000)  # Convert to bps
                updated += 1
            except Exception as e:
                print(f"Failed to update {channel.name}: {e}")
                failed += 1
                
        embed = discord.Embed(
            title="Voice Channel Bitrates Updated",
            description=f"Updated bitrate to **{target_bitrate} kbps** for {updated} voice channels.",
            color=0x00ff00
        )
        if failed > 0:
            embed.add_field(name="Failed", value=f"{failed} channels could not be updated")
            
        await interaction.followup.send(embed=embed)


async def setup(bot):
    """Load the Utility cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(Utility(bot, config))
