# BaguetteBot Cogs Documentation

This directory contains the modular command structure (cogs) for BaguetteBot. Each cog groups related commands together for better organization and maintainability.

## 📁 Cog Structure

### `info.py` - Information Commands
**Purpose:** Provides information about the bot and helpful resources.

**Commands:**
- `/help` - Display help information and useful links
- `/stats` - Show detailed bot statistics (CPU, RAM, uptime, servers, etc.)
- `/invite` - Get the bot invite link and support server
- `/snowflake <flake>` - Convert Discord snowflake ID to timestamp
- `/terms` - View Terms of Service

**Features:**
- Comprehensive bot statistics with color-coded ping display
- Interactive help menu with button links
- Snowflake timestamp conversion utility

---

### `admin.py` - Administrative Commands
**Purpose:** Commands for bot administration and server moderation.

**Commands:**
- `/sync-commands` - Sync slash commands with Discord (bot owner only)
- `/slowmode <seconds>` - Set channel slowmode delay
- `/purge <amount>` - Delete multiple messages (1-100)
- `/nickname <member> <name>` - Change a member's nickname
- `/clearroles <user>` - Remove all roles from a user
- `/copyroles <user1> <user2>` - Copy roles from one user to another
- `/roleperms <permission>` - List roles with a specific permission

**Permissions Required:**
- Most commands require appropriate guild permissions
- `/sync-commands` restricted to bot owner (ID: 382784106984898560)

---

### `social.py` - Social Commands
**Purpose:** Fun social interaction and community engagement commands.

**Commands:**
- `/yes-no` - Random yes/no decision maker
- `/ship <thing1> <thing2>` OR `<user1> <user2>` - Ship two things/users together

**Features:**
- Ship name generator with compatibility percentage
- Multiple random response options for yes-no
- Seeded random for consistent ship compatibility

---

### `utility.py` - Utility Commands
**Purpose:** Server management and utility helper functions.

**Commands:**
- `/emoji-backup <guild_id>` - Backup all server emojis to disk
- `/logsearch <term>` - Search message logs for a term
- `/bitrates [bitrate]` - Set bitrate for all voice channels

**Features:**
- Downloads emojis in original quality (PNG/GIF)
- Case-insensitive log searching
- Bulk voice channel management

**Permissions Required:**
- `/emoji-backup` - manage_emojis
- `/logsearch` - view_audit_log
- `/bitrates` - manage_channels

---

### `events.py` - Event Handlers
**Purpose:** Handles Discord events for logging and bot functionality.

**Event Listeners:**
- `on_command_error` - Handle and log command errors
- `on_member_join` - Log member joins
- `on_member_remove` - Log member leaves
- `on_guild_join` - Log bot joining new servers
- `on_guild_remove` - Log bot being removed from servers
- `on_message_delete` - Log message deletions
- `on_message_edit` - Log message edits

**Features:**
- Comprehensive error logging
- User-friendly error messages with issue tracker link
- Automatic error file logging

---

### `utils.py` - Utility Functions
**Purpose:** Shared helper functions and utilities used across cogs.

**Key Functions:**
- `slash_log()` - Log slash command usage and check ToS acceptance
- `get_coins()` - Retrieve user coin balance
- `update_coins()` - Update user coin balance with boost support
- `duration_to_time()` - Convert milliseconds to formatted time string
- `error_code()` - Send formatted error messages
- `bot_runtime_events()` - Track bot runtime events

**Classes:**
- `AcceptToSButtons` - Terms of Service acceptance button handler

---

## 🔧 Configuration

Each cog receives a `config` dictionary from the bot containing:

```python
{
    'DRAGGIEBOT_VERSION': str,  # Bot version
    'BUILD': str,                # Build identifier
    'BASE_DIR': str,             # Base directory path
    'S_SLASH': str,              # System slash character
    'GlobalLogDir': str,         # Global log file path
    'start_time': float,         # Bot start timestamp
    'ready_start_time': float,   # Bot ready timestamp
    'bot_events': int,           # Event counter
    'YTAPI_STATUS': str,         # YouTube API status
    'AUDIO_SUBSYSTEM': str,      # Audio system name
    'SCAPI_STATUS': str,         # Supercell API status
}
```

## 📝 Adding New Cogs

To create a new cog:

1. **Create the cog file** in the `cogs/` directory:
```python
"""
YourCog - Brief description.

Detailed description of what this cog does.
"""

import discord
from discord import app_commands
from discord.ext import commands

class YourCog(commands.Cog):
    """One-line description."""
    
    def __init__(self, bot, config: dict):
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="yourcommand", description="Command description")
    async def yourcommand(self, interaction: discord.Interaction):
        """
        Detailed docstring.
        
        Explain what the command does, its parameters, and behavior.
        """
        await interaction.response.send_message("Hello!")

async def setup(bot):
    """Load the cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(YourCog(bot, config))
```

2. **Add to cog loader** in `BaguetteBot.py`:
```python
cogs_to_load = ['cogs.info', 'cogs.admin', ..., 'cogs.yourcog']
```

3. **Test thoroughly** before deploying.

## 🎯 Best Practices

### Documentation
- Include comprehensive docstrings for all commands
- Use Google-style docstring format
- Document parameters and return values

### Error Handling
- Always validate user input
- Use try-except blocks for external API calls
- Send ephemeral error messages when appropriate

### Permissions
- Check permissions before executing privileged commands
- Provide clear error messages for permission issues
- Use appropriate permission checks (guild_permissions, etc.)

### Code Style
- Follow PEP 8 style guidelines
- Use type hints for function parameters
- Keep functions focused and single-purpose
- Use descriptive variable names

### Async Best Practices
- Always use `await` for async operations
- Defer responses for long-running commands
- Use `ephemeral=True` for sensitive/private responses

## 🔄 Migration Status

Commands are being gradually migrated from the main `BaguetteBot.py` file to cogs:

✅ **Migrated:**
- Info commands (help, stats, invite, snowflake, terms)
- Admin commands (sync, slowmode, purge, nickname, role management)
- Social commands (yes-no, ship)
- Utility commands (emoji-backup, logsearch, bitrates)
- Event handlers (error handling, member events, guild events)

⏳ **To Be Migrated:**
- Voice/Audio commands (play, skip, pause, volume, queue, etc.)
- Currency system (coins, buy, mine)
- Specialized commands (GPT, leschoristes, brawlstars)
- Remaining social features

## 📚 Additional Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord API Documentation](https://discord.com/developers/docs)
- [BaguetteBot Repository](https://github.com/Draggie306/BaguetteBot)
- [Support Server](https://discord.gg/GfetCXH)

## 🤝 Contributing

When contributing new cogs:
1. Follow the existing structure and patterns
2. Include comprehensive documentation
3. Test all commands thoroughly
4. Update this README with new cog information
5. Submit a pull request with a clear description

---

**Last Updated:** 2024
**Bot Version:** v1.3.9
