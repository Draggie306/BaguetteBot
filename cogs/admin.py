"""
Admin Cog - Administrative commands for BaguetteBot.

This cog contains commands that are restricted to bot administrators
and server moderators, including command syncing, moderation tools,
and utility features.
"""

import discord
from discord import app_commands
from discord.ext import commands
import os
from datetime import datetime
from typing import Optional


class Admin(commands.Cog):
    """Administrative and moderation commands."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the Admin cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="sync-commands", description="[Admin] Sync edited client tree commands to Discord servers")
    async def sync(self, interaction: discord.Interaction):
        """
        Synchronize command tree with Discord.
        
        This command is restricted to the bot owner and is used to sync
        slash commands with Discord's API after making changes.
        Only the bot owner (ID: 382784106984898560) can use this command.
        """
        if interaction.user.id == 382784106984898560:
            await interaction.response.defer()
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands")
            await interaction.followup.send(f"Synced {len(synced)} client tree commands.")
        else:
            await interaction.response.send_message("This is bot admin only.", ephemeral=True)
            
    @app_commands.command(name="slowmode", description="[Utility] Sets the slowmode in a channel.")
    @app_commands.describe(seconds="The slowmode delay in seconds")
    async def setdelay(self, interaction: discord.Interaction, seconds: int):
        """
        Set slowmode delay for the current channel.
        
        Args:
            seconds: Slowmode delay in seconds (0-21600)
            
        Requires: manage_channels permission
        """
        if not interaction.user.guild_permissions.manage_channels:
            return await interaction.response.send_message(
                "You need the `Manage Channels` permission to use this command.",
                ephemeral=True
            )
            
        if seconds < 0 or seconds > 21600:
            return await interaction.response.send_message(
                "Slowmode must be between 0 and 21600 seconds (6 hours).",
                ephemeral=True
            )
            
        await interaction.channel.edit(slowmode_delay=seconds)
        
        embed = discord.Embed(
            title="Slowmode Updated",
            description=f"Slowmode has been set to **{seconds}** seconds in {interaction.channel.mention}.",
            color=0x00ff00
        )
        embed.set_footer(text=f"Changed by {interaction.user.display_name}")
        
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="purge", description="[Moderation] Purge messages from the current channel.")
    @app_commands.describe(amount="Number of messages to delete (1-100)")
    async def purge(self, interaction: discord.Interaction, amount: int):
        """
        Delete multiple messages from the current channel.
        
        Args:
            amount: Number of messages to delete (1-100)
            
        Requires: manage_messages permission
        """
        if not interaction.user.guild_permissions.manage_messages:
            return await interaction.response.send_message(
                "You need the `Manage Messages` permission to use this command.",
                ephemeral=True
            )
            
        if amount < 1 or amount > 100:
            return await interaction.response.send_message(
                "Please specify a number between 1 and 100.",
                ephemeral=True
            )
            
        await interaction.response.defer(ephemeral=True)
        
        deleted = await interaction.channel.purge(limit=amount)
        
        await interaction.followup.send(
            f"Successfully deleted {len(deleted)} messages.",
            ephemeral=True
        )
        
    @app_commands.command(name="nickname", description="Changes nickname for mentioned user")
    @app_commands.describe(member="The member to rename", name="The new nickname")
    async def chnick(self, interaction: discord.Interaction, member: discord.Member, name: str):
        """
        Change a member's nickname.
        
        Args:
            member: The member whose nickname to change
            name: The new nickname to set
            
        Requires: manage_nicknames permission
        """
        if not interaction.user.guild_permissions.manage_nicknames:
            return await interaction.response.send_message(
                "You need the `Manage Nicknames` permission to use this command.",
                ephemeral=True
            )
            
        try:
            await member.edit(nick=name)
            await interaction.response.send_message(
                f"Changed {member.mention}'s nickname to **{name}**."
            )
        except discord.Forbidden:
            await interaction.response.send_message(
                "I don't have permission to change that user's nickname.",
                ephemeral=True
            )
        except discord.HTTPException as e:
            await interaction.response.send_message(
                f"Failed to change nickname: {str(e)}",
                ephemeral=True
            )
            
    @app_commands.command(name="clearroles", description="[Utility] Clears all roles from a user.")
    @app_commands.describe(user="The user whose roles to clear")
    async def clearroles(self, interaction: discord.Interaction, user: discord.Member):
        """
        Remove all roles from a user.
        
        Args:
            user: The member whose roles to remove
            
        Requires: manage_roles permission
        """
        if not interaction.user.guild_permissions.manage_roles:
            return await interaction.response.send_message(
                "You need the `Manage Roles` permission to use this command.",
                ephemeral=True
            )
            
        await interaction.response.defer()
        
        roles_to_remove = [role for role in user.roles if role != interaction.guild.default_role]
        
        try:
            await user.remove_roles(*roles_to_remove, reason=f"Cleared by {interaction.user}")
            await interaction.followup.send(
                f"Removed {len(roles_to_remove)} roles from {user.mention}."
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to modify that user's roles.",
                ephemeral=True
            )
        except discord.HTTPException as e:
            await interaction.followup.send(
                f"Failed to remove roles: {str(e)}",
                ephemeral=True
            )
            
    @app_commands.command(name="copyroles", description="[Utility] Copy roles from one user to another.")
    @app_commands.describe(user1="The user to copy roles from", user2="The user to copy roles to")
    async def copyroles(self, interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):
        """
        Copy roles from one user to another.
        
        Args:
            user1: The member to copy roles from
            user2: The member to copy roles to
            
        Requires: manage_roles permission
        """
        if not interaction.user.guild_permissions.manage_roles:
            return await interaction.response.send_message(
                "You need the `Manage Roles` permission to use this command.",
                ephemeral=True
            )
            
        await interaction.response.defer()
        
        roles_to_add = [role for role in user1.roles if role != interaction.guild.default_role]
        
        try:
            await user2.add_roles(*roles_to_add, reason=f"Copied from {user1} by {interaction.user}")
            await interaction.followup.send(
                f"Copied {len(roles_to_add)} roles from {user1.mention} to {user2.mention}."
            )
        except discord.Forbidden:
            await interaction.followup.send(
                "I don't have permission to modify roles.",
                ephemeral=True
            )
        except discord.HTTPException as e:
            await interaction.followup.send(
                f"Failed to copy roles: {str(e)}",
                ephemeral=True
            )
            
    @app_commands.command(name="roleperms", description="[Utility] Gets all roles with a permission.")
    @app_commands.describe(permission="The permission to search for")
    async def roleperms(self, interaction: discord.Interaction, permission: str):
        """
        List all roles that have a specific permission.
        
        Args:
            permission: The permission name to search for (e.g., 'manage_messages')
        """
        if not interaction.guild:
            return await interaction.response.send_message(
                "This command can only be used in a server.",
                ephemeral=True
            )
            
        # Normalize permission name
        perm_name = permission.lower().replace(" ", "_")
        
        # Find roles with the permission
        roles_with_perm = []
        for role in interaction.guild.roles:
            if hasattr(role.permissions, perm_name):
                if getattr(role.permissions, perm_name):
                    roles_with_perm.append(role)
                    
        if not roles_with_perm:
            await interaction.response.send_message(
                f"No roles found with the permission `{perm_name}`.",
                ephemeral=True
            )
        else:
            role_mentions = [role.mention for role in roles_with_perm]
            embed = discord.Embed(
                title=f"Roles with {perm_name} permission",
                description="\n".join(role_mentions),
                color=0x00acff
            )
            await interaction.response.send_message(embed=embed)


async def setup(bot):
    """Load the Admin cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(Admin(bot, config))
