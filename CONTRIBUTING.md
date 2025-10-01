# Contributing to BaguetteBot

Thank you for your interest in contributing to BaguetteBot! This guide will help you understand the codebase and make meaningful contributions.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Creating a New Cog](#creating-a-new-cog)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- discord.py 2.0+
- Git for version control

### Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/BaguetteBot.git
   cd BaguetteBot
   ```
3. Install dependencies (when requirements.txt is available)
4. Create a `.env` file with your bot token

## 📁 Project Structure

```
BaguetteBot/
├── BaguetteBot.py          # Main bot file
├── cogs/                   # Modular command files
│   ├── __init__.py
│   ├── README.md          # Cog documentation
│   ├── utils.py           # Shared utilities
│   ├── info.py            # Info commands
│   ├── admin.py           # Admin commands
│   ├── social.py          # Social commands
│   ├── utility.py         # Utility commands
│   └── events.py          # Event handlers
├── README.md              # Main documentation
├── ARCHITECTURE.md        # Architecture overview
└── CONTRIBUTING.md        # This file
```

## 🔄 Development Workflow

### 1. Choose an Issue
- Check the [Issues](https://github.com/Draggie306/BaguetteBot/issues) page
- Comment on the issue you want to work on
- Wait for approval if it's a major change

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
- Follow the code style guidelines
- Test your changes thoroughly
- Update documentation if needed

### 4. Commit Changes
```bash
git add .
git commit -m "Add: Brief description of changes"
```

Use commit prefixes:
- `Add:` New features
- `Fix:` Bug fixes
- `Update:` Updates to existing features
- `Docs:` Documentation changes
- `Refactor:` Code refactoring

## 🎯 Creating a New Cog

### Step 1: Create the Cog File

Create a new file in the `cogs/` directory:

```python
"""
YourCog - Brief description.

Detailed explanation of what this cog does and its purpose.
"""

import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional


class YourCog(commands.Cog):
    """One-line description for help text."""
    
    def __init__(self, bot, config: dict):
        """
        Initialize the cog.
        
        Args:
            bot: The Discord bot instance
            config: Configuration dictionary with bot settings
        """
        self.bot = bot
        self.config = config
        
    @app_commands.command(name="yourcommand", description="Command description")
    @app_commands.describe(param="Parameter description")
    async def yourcommand(self, interaction: discord.Interaction, param: Optional[str]):
        """
        Detailed command documentation.
        
        Args:
            param: Explain what this parameter does
            
        Provide examples and additional information here.
        """
        # Check permissions if needed
        if not interaction.user.guild_permissions.some_permission:
            return await interaction.response.send_message(
                "You need specific permissions.",
                ephemeral=True
            )
            
        # Your command logic here
        await interaction.response.send_message(f"Hello! You provided: {param}")


async def setup(bot):
    """Load the cog."""
    config = getattr(bot, 'config', {})
    await bot.add_cog(YourCog(bot, config))
```

### Step 2: Register the Cog

Add your cog to the loader in `BaguetteBot.py`:

```python
cogs_to_load = [
    'cogs.info',
    'cogs.admin',
    'cogs.social',
    'cogs.events',
    'cogs.utility',
    'cogs.yourcog',  # Add your cog here
]
```

### Step 3: Document Your Cog

Add documentation to `cogs/README.md`:

```markdown
### `yourcog.py` - Your Cog Name
**Purpose:** Brief description of the cog's purpose.

**Commands:**
- `/yourcommand <param>` - Command description

**Features:**
- Feature 1
- Feature 2

**Permissions Required:**
- Required permission (if any)
```

## 📝 Code Style Guidelines

### General Principles
- Follow [PEP 8](https://pep8.org/) style guide
- Use descriptive variable and function names
- Keep functions focused and single-purpose
- Comment complex logic

### Naming Conventions
```python
# Classes: PascalCase
class MyCog(commands.Cog):
    pass

# Functions and variables: snake_case
async def my_function():
    my_variable = 42

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
```

### Docstrings
Use Google-style docstrings:

```python
async def function_name(param1: str, param2: int) -> bool:
    """
    Brief one-line description.
    
    More detailed explanation of what the function does,
    how it works, and any important notes.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    pass
```

### Type Hints
Always use type hints:

```python
from typing import Optional, List, Dict

async def process_data(
    data: str,
    count: int,
    options: Optional[Dict[str, str]] = None
) -> List[str]:
    pass
```

### Error Handling
Always handle potential errors:

```python
try:
    result = await some_operation()
except discord.Forbidden:
    await interaction.response.send_message(
        "I don't have permission to do that.",
        ephemeral=True
    )
except discord.HTTPException as e:
    print(f"HTTP error occurred: {e}")
    await interaction.response.send_message(
        "An error occurred. Please try again later.",
        ephemeral=True
    )
```

### Permission Checks
Always check permissions for privileged operations:

```python
if not interaction.user.guild_permissions.manage_messages:
    return await interaction.response.send_message(
        "You need the `Manage Messages` permission to use this command.",
        ephemeral=True
    )
```

### Long-Running Operations
Use defer for operations that take time:

```python
await interaction.response.defer()  # Shows "Bot is thinking..."
# ... long operation ...
await interaction.followup.send("Done!")
```

### Sensitive Information
Use ephemeral messages for sensitive data:

```python
await interaction.response.send_message(
    "Your secret data here",
    ephemeral=True  # Only visible to command user
)
```

## 🧪 Testing

### Manual Testing Checklist
Before submitting a PR, test:

- [ ] Command executes without errors
- [ ] Permission checks work correctly
- [ ] Error messages are user-friendly
- [ ] Edge cases are handled
- [ ] Help text is accurate
- [ ] Command works in both DMs and servers (if applicable)
- [ ] No unintended side effects

### Test Different Scenarios
```python
# Test with valid input
/yourcommand param="valid"

# Test with missing parameters
/yourcommand

# Test with invalid input
/yourcommand param="invalid@#$"

# Test without permissions
# (Use an account without the required permissions)

# Test in DMs (if applicable)
```

## 📤 Submitting Changes

### Pull Request Process

1. **Ensure your code follows the style guidelines**
2. **Update documentation** if you've added/changed features
3. **Test thoroughly** before submitting
4. **Create a pull request** with a clear description:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
Describe how you tested the changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tested in live environment
```

### Pull Request Template
```markdown
### What does this PR do?
Explain the purpose and scope of your changes

### Related Issues
Fixes #123 (if applicable)

### Screenshots (if applicable)
Add screenshots for UI changes

### Additional Notes
Any additional information reviewers should know
```

## 🤝 Code Review

Your PR will be reviewed for:
- Code quality and style
- Functionality and correctness
- Documentation completeness
- Test coverage
- Security considerations

Be prepared to:
- Answer questions about your code
- Make requested changes
- Discuss alternative approaches

## 💡 Tips for Success

### Good Practices
✅ Keep commits focused and atomic
✅ Write clear commit messages
✅ Update documentation with code changes
✅ Test edge cases thoroughly
✅ Ask questions if something is unclear

### Things to Avoid
❌ Committing API keys or tokens
❌ Making unrelated changes in one PR
❌ Breaking existing functionality
❌ Ignoring code style guidelines
❌ Submitting untested code

## 📞 Getting Help

- **Discord**: Join the [support server](https://discord.gg/GfetCXH)
- **Issues**: Create an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions

## 🎓 Learning Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord API Documentation](https://discord.com/developers/docs)
- [Python Documentation](https://docs.python.org/3/)
- [Git Basics](https://git-scm.com/book/en/v2)

## 📜 License

By contributing to BaguetteBot, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to BaguetteBot! Every contribution, no matter how small, helps improve the bot for everyone. 🎉
