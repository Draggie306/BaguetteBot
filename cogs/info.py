"""
Info Cog - Information and help commands for BaguetteBot.

This cog contains commands that provide information about the bot,
including help documentation, statistics, invite links, and utility tools.
"""

import discord
from discord import app_commands
from discord.ext import commands
import os
import time
import psutil
from datetime import datetime
from typing import Optional


class Info(commands.Cog):
    """Commands for bot information and help."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the Info cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="help", description="Everything you need to know about BaguetteBot")
    async def help(self, interaction: discord.Interaction):
        """
        Display help information and useful links.
        
        Shows an embed with links to command documentation, support server,
        bot invite link, and source code repository.
        """
        embed = discord.Embed(
            title="BaguetteBot Help", 
            description="Everything you need to know about BaguetteBot", 
            color=0x00acff
        )
        embed.add_field(
            name="Commands", 
            value="Preview my commands by typing in `/` and clicking the BaguetteBot icon", 
            inline=False
        )
        embed.add_field(
            name="Support", 
            value="Join the support server [here](https://discord.gg/GfetCXH)", 
            inline=False
        )
        embed.add_field(
            name="Invite", 
            value="Invite BaguetteBot to your server [here](https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands). Feel free to select the permissions you want BaguetteBot to have.", 
            inline=False
        )
        embed.add_field(
            name="Source Code", 
            value="BaguetteBot is open source! You can find the source code [here](https://github.com/Draggie306/BaguetteBot/blob/main/BaguetteBot.py)", 
            inline=False
        )
        
        view = discord.ui.View()
        view.add_item(discord.ui.Button(
            label="Commands List", 
            url="https://github.com/Draggie306/BaguetteBot/blob/main/README.md", 
            style=discord.ButtonStyle.link
        ))
        view.add_item(discord.ui.Button(
            label="Support", 
            url="https://discord.gg/GfetCXH", 
            style=discord.ButtonStyle.link
        ))
        view.add_item(discord.ui.Button(
            label="Invite", 
            url="https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands", 
            style=discord.ButtonStyle.link
        ))
        view.add_item(discord.ui.Button(
            label="Source Code", 
            url="https://github.com/Draggie306/BaguetteBot/blob/main/BaguetteBot.py", 
            style=discord.ButtonStyle.link
        ))
        
        await interaction.response.send_message(embed=embed, view=view)
        
    @app_commands.command(name="stats", description="[Info] Just a few useful bot statistics.")
    async def stats(self, interaction: discord.Interaction):
        """
        Display detailed bot statistics.
        
        Shows CPU and RAM usage, uptime, ping, server count, member count,
        and various bot configuration statuses.
        """
        # Determine ping color based on latency
        ping_ms = round(self.bot.latency * 1000)
        if ping_ms <= 100:
            ping_colour = 0x44ff44
        elif ping_ms <= 150:
            ping_colour = 0xffd000
        else:
            ping_colour = 0x990000
            
        # Get file statistics
        bot_file_path = f"{self.config['BASE_DIR']}GitHub{self.config['S_SLASH']}BaguetteBot{self.config['S_SLASH']}BaguetteBot.py"
        try:
            file_size_bytes = os.path.getsize(bot_file_path)
            num_lines = sum(1 for line in open(bot_file_path, encoding='utf-8'))
        except:
            file_size_bytes = 0
            num_lines = 0
            
        # Calculate uptime
        current_time = time.time()
        uptime_seconds = int(round(current_time - self.config['start_time']))
        if uptime_seconds > 60:
            uptime_display = f"{int(round(uptime_seconds / 60))} minutes"
        else:
            uptime_display = f"{uptime_seconds} seconds"
            
        real_uptime_seconds = int(round(current_time - self.config.get('ready_start_time', self.config['start_time'])))
        
        # Get system stats
        cpu_percentage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        
        # Count servers and members
        servers = len(self.bot.guilds)
        members = sum(guild.member_count - 1 for guild in self.bot.guilds if guild.member_count)
        
        # Count cached videos if directory exists
        cache_dir = f"{self.config['BASE_DIR']}ExternalAssets{self.config['S_SLASH']}AudioCache{self.config['S_SLASH']}"
        try:
            cached_videos = len([name for name in os.listdir(cache_dir) if os.path.isfile(os.path.join(cache_dir, name))])
        except:
            cached_videos = 0
            
        # Build embed
        embed = discord.Embed(title="**Bot Stats**", colour=ping_colour)
        embed.add_field(name="CPU Usage", value=f"{cpu_percentage}%")
        embed.add_field(name="RAM Usage", value=f"{memory_usage}%")
        embed.add_field(name="Lines of Code", value=f"{num_lines:,} lines")
        embed.add_field(name="File Size", value=f"{file_size_bytes:,} bytes")
        embed.add_field(name="Uptime", value=f"{uptime_display} ({real_uptime_seconds}s)")
        embed.add_field(name="Ping", value=f"{ping_ms} ms")
        embed.add_field(name="Videos Cached", value=cached_videos)
        embed.add_field(name="Servers", value=servers)
        embed.add_field(name="Total Members", value=f"{members:,}")
        
        bot_events = self.config.get('bot_events', 0)
        embed.add_field(name="Bot Events", value=bot_events)
        if real_uptime_seconds > 0:
            embed.add_field(name="Bot Events/sec", value=f"{round(bot_events / real_uptime_seconds, 3)}")
            
        embed.add_field(name="Command Logging", value="Enabled")
        embed.add_field(name="Message Logging", value="Enabled")
        embed.add_field(name="Voice Channels", value="Enabled")
        embed.add_field(name="YouTube Player", value=self.config.get('YTAPI_STATUS', 'Unknown'))
        embed.add_field(name="Audio Subsystem", value=self.config.get('AUDIO_SUBSYSTEM', 'Unknown'))
        
        embed.set_footer(
            text=f"BaguetteBot.py | {self.config.get('DRAGGIEBOT_VERSION', 'Unknown')}/{self.config.get('BUILD', 'Unknown')} | discord.py {discord.__version__} | made by draggie"
        )
        
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="invite", description="[Info] Get the invite link for the bot.")
    async def invite(self, interaction: discord.Interaction):
        """
        Provide bot invite link and support server.
        
        Sends a message with the bot's invite link and support server information.
        """
        invite_link = "https://discord.com/api/oauth2/authorize?client_id=792850689533542420&permissions=1477895842903&scope=bot%20applications.commands"
        support_server = "https://discord.gg/GfetCXH"
        
        await interaction.response.send_message(
            f"You can invite me to your server with this link: {invite_link}. "
            f"Enjoy all the features of BaguetteBot!\n\n"
            f"If you need help, join the support server: {support_server}"
        )
        
    @app_commands.command(name="snowflake", description="[Utility] Convert a Discord snowflake into a DateTime object, accurate to the second.")
    @app_commands.describe(flake="The Discord snowflake ID to convert")
    async def snowflake(self, interaction: discord.Interaction, flake: str):
        """
        Convert a Discord snowflake ID to a timestamp.
        
        Args:
            flake: Discord snowflake ID as a string
            
        Discord snowflakes encode the timestamp when they were created.
        This command extracts and displays that timestamp.
        """
        try:
            snowflake_int = int(flake)
            discord_epoch = 1420070400000
            timestamp = ((snowflake_int >> 22) + discord_epoch) / 1000
            dt_object = datetime.fromtimestamp(timestamp)
            
            await interaction.response.send_message(
                f"Snowflake `{flake}` was created at: **{dt_object.strftime('%Y-%m-%d %H:%M:%S')} UTC**"
            )
        except ValueError:
            await interaction.response.send_message(
                "Invalid snowflake! Please provide a valid Discord snowflake ID.",
                ephemeral=True
            )
            
    @app_commands.command(name="terms", description="[Info] Views the iBaguette Terms of Service which governs this bot.")
    async def terms(self, interaction: discord.Interaction):
        """
        Display link to Terms of Service.
        
        Provides a link to the iBaguette Terms of Service that govern bot usage.
        """
        await interaction.response.send_message(
            "You can view the iBaguette Terms of Service here: https://terms.ibaguette.com/#discord-bots",
            ephemeral=True
        )


async def setup(bot):
    """Load the Info cog."""
    # Get configuration from bot
    config = getattr(bot, 'config', {})
    await bot.add_cog(Info(bot, config))
