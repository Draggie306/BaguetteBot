# BaguetteBot Architecture Documentation

## Overview

BaguetteBot has been refactored to use a modular, cog-based architecture following modern discord.py best practices. This document outlines the architectural design and organization.

## Project Structure

```
BaguetteBot/
├── BaguetteBot.py          # Main bot file (entry point)
├── cogs/                   # Command modules (cogs)
│   ├── __init__.py        # Package initialization
│   ├── README.md          # Cog documentation
│   ├── utils.py           # Shared utility functions
│   ├── info.py            # Information commands
│   ├── admin.py           # Administrative commands
│   ├── social.py          # Social interaction commands
│   ├── utility.py         # Utility commands
│   ├── events.py          # Event handlers
│   └── music.py           # Audio/voice commands (legacy)
├── README.md              # Main documentation
└── ARCHITECTURE.md        # This file
```

## Design Principles

### 1. Separation of Concerns
Each cog handles a specific domain:
- **Info**: Bot information and help
- **Admin**: Administrative tasks and moderation
- **Social**: Community interaction features
- **Utility**: Server management tools
- **Events**: Discord event handling

### 2. Modularity
- Commands are grouped by functionality
- Each cog is self-contained and can be loaded/unloaded independently
- Shared functionality is extracted to `utils.py`

### 3. Documentation
- Every command has comprehensive docstrings
- Google-style docstring format
- Parameter descriptions using `@app_commands.describe`
- README.md in cogs directory explains each module

### 4. Configuration Management
The bot uses a centralized configuration dictionary:

```python
client.config = {
    'DRAGGIEBOT_VERSION': str,    # Bot version
    'BUILD': str,                  # Build identifier
    'BASE_DIR': str,               # Base directory path
    'S_SLASH': str,                # System-specific path separator
    'GlobalLogDir': str,           # Global log file path
    'start_time': float,           # Bot start timestamp
    'ready_start_time': float,     # Ready event timestamp
    'bot_events': int,             # Event counter
    'YTAPI_STATUS': str,           # API status indicators
    'AUDIO_SUBSYSTEM': str,
    'SCAPI_STATUS': str,
}
```

This configuration is passed to all cogs during initialization, ensuring consistent access to bot settings.

## Command Organization

### Slash Commands (Modern)
All new commands use discord.py's `app_commands` system:
```python
@app_commands.command(name="command", description="Description")
async def command(self, interaction: discord.Interaction):
    """Docstring explaining the command."""
    await interaction.response.send_message("Response")
```

### Legacy Commands (Prefix-based)
Older prefix commands (`.command`) remain in the main file for backwards compatibility but will gradually be migrated or deprecated.

## Cog Loading

Cogs are loaded dynamically during the `on_ready` event:

```python
@client.event
async def on_ready():
    # ... initialization code ...
    
    cogs_to_load = ['cogs.info', 'cogs.admin', 'cogs.social', 'cogs.events', 'cogs.utility']
    for cog in cogs_to_load:
        try:
            await client.load_extension(cog)
            print(f"[CogLoader] Loaded {cog}")
        except Exception as e:
            print(f"[CogLoader] Failed to load {cog}: {e}")
```

## Error Handling

### Command Errors
Handled in the Events cog via `on_command_error`:
- Logs errors to file and console
- Sends user-friendly error messages
- Includes link to GitHub issues for persistent problems

### Error Utility
The `utils.py` module provides an `error_code()` function for consistent error messaging across cogs.

## Permission System

Commands check permissions before execution:
```python
if not interaction.user.guild_permissions.manage_channels:
    return await interaction.response.send_message(
        "You need the `Manage Channels` permission.",
        ephemeral=True
    )
```

## Logging

### Command Logging
- All slash commands logged via `slash_log()` utility
- Logs include user ID, command name, and timestamp
- Writes to both console and `GlobalLogDir`

### Event Logging
- Major events logged in Events cog
- Member joins/leaves, guild joins/leaves, message modifications
- Consistent logging format across all events

## Data Persistence

### File-based Storage
- Coins: `Servers/{guild_id}/Coins/{user_id}.txt`
- User settings: `Users/JSONSettings/{user_id}.json`
- Emoji backups: `emoji_backups/{guild_id}/`
- Message logs: `Servers/{guild_id}/Logs/MessageLog.txt`

### Database Considerations
Current implementation uses file-based storage. For scalability, consider migrating to:
- SQLite for local deployment
- PostgreSQL for cloud deployment
- Redis for caching and session management

## Best Practices

### Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters
- Descriptive variable and function names
- Consistent formatting across all files

### Async Programming
- Always `await` async operations
- Use `defer()` for long-running commands
- Proper exception handling in async contexts

### Security
- Never commit API keys or tokens
- Validate all user input
- Use ephemeral messages for sensitive data
- Check permissions before privileged operations

## Migration Guide

### Migrating Commands to Cogs

1. **Identify the command's category** (Info, Admin, Social, Utility, etc.)

2. **Create or modify the appropriate cog**:
```python
@app_commands.command(name="mycommand", description="Description")
@app_commands.describe(param="Parameter description")
async def mycommand(self, interaction: discord.Interaction, param: str):
    """
    Detailed docstring.
    
    Args:
        param: Parameter explanation
    """
    # Implementation
```

3. **Move utility functions** to `utils.py` if they're reusable

4. **Update configuration access**:
   - Old: Direct global variable access
   - New: `self.config['VARIABLE_NAME']`

5. **Test thoroughly** before removing from main file

6. **Update documentation** in `cogs/README.md`

## Future Improvements

### Short Term
- [ ] Migrate remaining voice/audio commands
- [ ] Migrate currency system (coins, buy, mine)
- [ ] Migrate specialized commands (GPT, brawlstars, etc.)
- [ ] Create dedicated Currency cog
- [ ] Update music.py to modern Wavelink

### Long Term
- [ ] Database migration (SQLite/PostgreSQL)
- [ ] Implement caching layer
- [ ] Add unit tests for each cog
- [ ] Create admin dashboard
- [ ] Implement plugin system for custom servers
- [ ] Add internationalization (i18n) support
- [ ] Performance monitoring and analytics

## Testing

### Manual Testing
Each command should be tested for:
- Correct functionality
- Permission checks
- Error handling
- User feedback quality

### Automated Testing (Future)
```python
# Example test structure
import pytest
from cogs.info import Info

@pytest.mark.asyncio
async def test_help_command():
    # Test help command functionality
    pass
```

## Contributing

When adding new features:
1. Determine appropriate cog or create a new one
2. Follow existing code patterns
3. Add comprehensive documentation
4. Update relevant README files
5. Test all edge cases
6. Submit PR with clear description

## Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord API Documentation](https://discord.com/developers/docs)
- [Python Best Practices (PEP 8)](https://pep8.org/)
- [Async Programming in Python](https://docs.python.org/3/library/asyncio.html)

---

**Last Updated:** 2024  
**Bot Version:** v1.3.9  
**Architecture Version:** 2.0 (Cog-based)
