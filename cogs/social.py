"""
Social Cog - Social interaction commands for BaguetteBot.

This cog contains commands for social features including coins,
mining, yes/no responses, and other community interaction features.
"""

import discord
from discord import app_commands
from discord.ext import commands
import random
from typing import Optional


class Social(commands.Cog):
    """Social interaction and community commands."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the Social cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="yes-no", description="[Social] Randomly answers yes or no.")
    async def yn(self, interaction: discord.Interaction):
        """
        Randomly respond with yes or no.
        
        A simple command that randomly picks between 'Yes' and 'No' responses,
        useful for making decisions or just having fun.
        """
        responses = [
            "Yes",
            "No",
            "Maybe",
            "Definitely",
            "Absolutely not",
            "I don't think so",
            "Of course!",
            "Never",
            "Ask again later",
            "Without a doubt"
        ]
        
        await interaction.response.send_message(random.choice(responses))
        
    @app_commands.command(name="ship", description="[Social] Ships two things together.")
    @app_commands.describe(
        thing1="First thing to ship",
        thing2="Second thing to ship",
        user1="First user to ship",
        user2="Second user to ship"
    )
    async def ship(
        self,
        interaction: discord.Interaction,
        thing1: Optional[str] = None,
        thing2: Optional[str] = None,
        user1: Optional[discord.Member] = None,
        user2: Optional[discord.Member] = None
    ):
        """
        Create a "ship" between two things or users.
        
        Args:
            thing1: First text/thing to ship
            thing2: Second text/thing to ship
            user1: First user to ship
            user2: Second user to ship
            
        Generates a ship name and compatibility percentage.
        """
        # Determine what to ship
        if user1 and user2:
            name1 = user1.display_name
            name2 = user2.display_name
        elif thing1 and thing2:
            name1 = thing1
            name2 = thing2
        else:
            return await interaction.response.send_message(
                "Please provide either two things or two users to ship!",
                ephemeral=True
            )
            
        # Create ship name (first half of name1 + second half of name2)
        mid1 = len(name1) // 2
        mid2 = len(name2) // 2
        ship_name = name1[:mid1] + name2[mid2:]
        
        # Generate compatibility (seeded for consistency)
        combined = f"{name1}{name2}"
        seed = sum(ord(c) for c in combined)
        random.seed(seed)
        compatibility = random.randint(0, 100)
        random.seed()  # Reset seed
        
        # Determine color based on compatibility
        if compatibility >= 75:
            color = 0x00ff00  # Green
        elif compatibility >= 50:
            color = 0xffff00  # Yellow
        elif compatibility >= 25:
            color = 0xff9900  # Orange
        else:
            color = 0xff0000  # Red
            
        embed = discord.Embed(
            title=f"💘 {name1} x {name2} 💘",
            description=f"Ship name: **{ship_name}**",
            color=color
        )
        embed.add_field(
            name="Compatibility",
            value=f"{'❤️' * (compatibility // 10)}{'🖤' * (10 - compatibility // 10)} {compatibility}%"
        )
        
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    """Load the Social cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(Social(bot, config))
