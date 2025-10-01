"""
Events Cog - Event handlers for BaguetteBot.

This cog contains all event listeners that respond to various Discord events
such as member joins, message edits, reactions, and other server activities.
"""

import discord
from discord.ext import commands
import random
from datetime import datetime


class Events(commands.Cog):
    """Discord event handlers for bot functionality."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the Events cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Handle command errors.
        
        Args:
            ctx: Command context
            error: The error that occurred
            
        Logs errors and sends user-friendly error messages.
        """
        print("error!")
        
        # Ignore certain errors
        if "is not found" in str(error):
            print(f"Command returned an error but will be ignored. Server: {ctx.guild.name}, error message = {error}")
            return
            
        if "on cooldown" in str(error):
            await ctx.send(f"{error}.")
            return
            
        if ctx.message.content.startswith(".."):
            return
            
        # Send error embed
        random_cry_list = [
            '<:AmberCry:828577834146594856>',
            '<:BibiByeBye:828683852939395072>',
            '<:ColetteCry:828683829631516732>',
            '<:JessieCry:828683805861740654>',
            '<:SpikeCry:828683779206807622>',
            '<:SurgeCry:828683755694063667>',
            '<:TaraCry:828683724286853151>'
        ]
        
        embed = discord.Embed(
            title=f"{random.choice(random_cry_list)} An error occured",
            description=f"**{str(error)}**\n\n*If this keeps occuring, please raise an issue [here](https://github.com/Draggie306/BaguetteBot/issues)*.",
            color=0x990000
        )
        await ctx.send(embed=embed)
        print(str(error))
        
        # Log error to file
        try:
            global_log_dir = self.config.get('GlobalLogDir', 'GlobalLog.txt')
            with open(global_log_dir, "a") as f:
                f.write(f"\nERROR: An error occured! Original command initialised by {ctx.author} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
                
            base_dir = self.config.get('BASE_DIR', '')
            with open(f"{base_dir}errors.txt", "a") as f:
                f.write(f"\nERROR: An error occured! Original command initialised by {ctx.author} at {datetime.now()}. ERROR MESSAGE: {str(error)}")
        except Exception as e:
            print(f"Failed to log error: {e}")
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Handle member join events.
        
        Args:
            member: The member who joined
            
        Sends a welcome message and logs the join.
        """
        print(f"[MemberJoin]    {member.name} joined {member.guild.name}")
        
        # You can add welcome message logic here
        # For example:
        # welcome_channel = member.guild.system_channel
        # if welcome_channel:
        #     await welcome_channel.send(f"Welcome {member.mention} to {member.guild.name}!")
            
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """
        Handle member leave events.
        
        Args:
            member: The member who left
            
        Logs the member departure.
        """
        print(f"[MemberLeave]   {member.name} left {member.guild.name}")
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """
        Handle bot joining a new guild.
        
        Args:
            guild: The guild the bot joined
            
        Logs the guild join and can send setup information.
        """
        print(f"[GuildJoin]     Joined guild: {guild.name} (ID: {guild.id})")
        
        # You can add setup logic here
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        """
        Handle bot being removed from a guild.
        
        Args:
            guild: The guild the bot was removed from
            
        Logs the guild removal.
        """
        print(f"[GuildRemove]   Removed from guild: {guild.name} (ID: {guild.id})")
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Handle message deletion events.
        
        Args:
            message: The deleted message
            
        Logs message deletions for moderation purposes.
        """
        if message.author.bot:
            return
            
        print(f"[MessageDelete] Message deleted in {message.guild.name if message.guild else 'DM'}: {message.content[:50]}")
        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        """
        Handle message edit events.
        
        Args:
            before: The message before editing
            after: The message after editing
            
        Logs message edits for moderation purposes.
        """
        if before.author.bot or before.content == after.content:
            return
            
        print(f"[MessageEdit]   Message edited in {before.guild.name if before.guild else 'DM'}")
        

async def setup(bot):
    """Load the Events cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(Events(bot, config))
