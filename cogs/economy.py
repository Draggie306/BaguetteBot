import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
import os
import json
from datetime import datetime, timedelta
from pathlib import Path

# These will be imported from the main bot file
# We'll access them through the bot instance


class CoinsButtons2(discord.ui.Button):
    def __init__(self, label: str, style: discord.ButtonStyle, bot):
        super().__init__(label=label, style=style)
        self.bot = bot

    async def callback(self, interaction):
        view = discord.ui.View()
        view.timeout = None

        # Coin balance
        coinBal = await self.bot.get_cog('Economy').get_coins(interaction.guild_id, interaction.user.id)
        nolwennium_bal = await self.bot.get_cog('Economy').get_nolwennium(interaction)
        view = discord.ui.View()

        if self.label == "View Page 2":
            BASE_DIR = self.bot.BASE_DIR
            S_SLASH = self.bot.S_SLASH
            EMOJI_COINS = self.bot.EMOJI_COINS
            EMOJI_NOLWENNIUM = self.bot.EMOJI_NOLWENNIUM
            
            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {EMOJI_COINS} coins and {nolwennium_bal} {EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)

            base_json = {
                'currentBoosts': [],
                'used_boosts': 0,
            }

            current_boosts_path = f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Coins{S_SLASH}{interaction.user.id}_boosted.json"
            if os.path.isfile(current_boosts_path):
                with open(current_boosts_path, 'r') as boosts_file:
                    boosts_json = json.load(boosts_file)
                    boosts_file.close()

                    # Remove expired boosts
                    current_time = datetime.now()
                    current_boosts = []
                    for boost in boosts_json['currentBoosts']:
                        expiration_time = datetime.strptime(boost['expirationTime'], '%Y-%m-%d %H:%M:%S.%f')
                        if expiration_time > current_time:
                            current_boosts.append(boost)
                    boosts_json['currentBoosts'] = current_boosts

                    # Display currently active boosts
                    if len(current_boosts) > 0:
                        active_boosts_string = '\n'.join([f"{boost['name']} ({boost['multiplier']}x) until {boost['expirationTime']}" for boost in current_boosts])
                        embed.add_field(
                            name="Currently active Boosts",
                            value=active_boosts_string,
                            inline=False
                        )

            # Define the available boosts
            boosts = [
                {
                    'name': '2x Coins for 1 hour',
                    'multiplier': 3,
                    'duration': 1,
                    'unit': 'hours',
                    'price': 50
                },
                {
                    'name': '2x Coins for 1 day',
                    'multiplier': 2,
                    'duration': 1,
                    'unit': 'days',
                    'price': 100
                },
                {
                    'name': '3x Coins for 7 days',
                    'multiplier': 5,
                    'duration': 7,
                    'unit': 'days',
                    'price': 1500
                },
                # Add more boosts here
            ]

            # Display available boosts
            for i in boosts:
                embed.add_field(
                    name=i["name"],
                    value=f"Multiplier: {i['multiplier']}x\nDuration: {i['duration']} {i['unit']}\n**Price: {i['price']} Coins**",
                    inline=False
                )

            # Add buttons for each available boost
            for boost in boosts:
                button_label = f"{boost['name']}"
                view.add_item(CoinsButtons2(style=discord.ButtonStyle.blurple, label=button_label, bot=self.bot))

            embed.set_footer(text=('Use the buttons below to buy what you want.'))

            await interaction.response.edit_message(embed=embed, view=view)

        if self.label == "2x Coins for 1 day":
            BASE_DIR = self.bot.BASE_DIR
            S_SLASH = self.bot.S_SLASH
            
            data = {
                'name': '2x Coins for 1 day',
                'multiplier': 2,
                'duration': 1,
                'unit': 'days',
                'price': 100
            }

            # Load the current boosts from the JSON file
            current_boosts_path = f"{BASE_DIR}Servers{S_SLASH}{interaction.guild_id}{S_SLASH}Coins{S_SLASH}{interaction.user.id}_boosted.json"
            boosts_json = {'currentBoosts': []}
            if os.path.isfile(current_boosts_path):
                with open(current_boosts_path, 'r') as boosts_file:
                    boosts_json = json.load(boosts_file)
                    boosts_file.close()

            # Check if the user has enough coins to purchase the boost
            if coinBal < data['price']:
                await interaction.response.send_message(f"You don't have enough coins to purchase this boost. You need {data['price'] - coinBal} more.", ephemeral=True)
                return

            # Calculate the expiration time for the boost
            current_time = datetime.now()
            if data['unit'] == 'seconds':
                expiration_time = current_time + timedelta(seconds=data['duration'])
            elif data['unit'] == 'minutes':
                expiration_time = current_time + timedelta(minutes=data['duration'])
            elif data['unit'] == 'hours':
                expiration_time = current_time + timedelta(hours=data['duration'])
            elif data['unit'] == 'days':
                expiration_time = current_time + timedelta(days=data['duration'])
            else:
                # Handle unknown boost unit
                expiration_time = current_time

            # Add the boost to the currentBoosts list in the JSON file
            boosts_json['currentBoosts'].append({
                'name': data['name'],
                'multiplier': data['multiplier'],
                'expirationTime': expiration_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            })

            # Deduct the price of the boost from the user's coins
            coinBal -= data['price']

            # Save the updated JSON file and update the embed and view
            with open(current_boosts_path, 'w') as boosts_file:
                json.dump(boosts_json, boosts_file)
                boosts_file.close()

            self.bot.get_cog('Economy').update_coins(interaction.guild_id, interaction.user.id, -data['price'])

            await interaction.response.send_message(f"You have purchased the **{data['name']}** boost! You will now earn {data['multiplier']}x multiplier!")


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_coins(self, server_id: int, user_id: int) -> int:
        """Gets a user's coins. The `server_id` and `user_id` as integers must be provided."""
        coin_dir = f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{user_id}.txt"
        if not os.path.exists(coin_dir):
            return None
        with open(coin_dir, 'r') as f:
            balance = int(f.read())
        print(f"[CoinsQuery]    Balance called for {user_id} in {server_id}. (Balance: {balance})")
        return balance

    def update_coins(self, server_id: int, user_id: int, coins_calc: int) -> int:
        """Gets then updates a user's coins. The `server_id` and `user_id` as integers must be provided.
        The amount of coins to add/subtract as an integer must be added too.
        Returns new amount of Coins."""
        coin_dir = f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{user_id}.txt"
        if not os.path.exists(f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins"):
            os.makedirs(f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins")
        multiplication_amount = 1
        if os.path.isfile(f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{user_id}_boosted.json"):
            with open(f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{user_id}_boosted.json", 'r') as f:
                info = json.load(f)
                expiration_time = info['currentBoosts'][0]['expirationTime']
                expiration_datetime = datetime.strptime(expiration_time, '%Y-%m-%d %H:%M:%S.%f')
                # Compare the expiration time to the current time
                if expiration_datetime > datetime.now():
                    # The boost is still active
                    multiplication_amount = info['currentBoosts'][0]['multiplier']
                else:
                    os.remove(f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{server_id}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{user_id}_boosted.json")
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

    def nolwenniumUserDirectory(self, ctx):
        nolwenniumUserDir = f"{self.bot.BASE_DIR}Nolwennium{self.bot.S_SLASH}{ctx.user.id}.txt"
        return nolwenniumUserDir

    async def get_nolwennium(self, ctx):
        nolwenniumUserDir = self.nolwenniumUserDirectory(ctx)
        with open(nolwenniumUserDir, 'r') as f:
            nolwennium_balance = f.read()
            f.close()
        return nolwennium_balance

    async def get_user_settings(self, user_id) -> dict:
        """Returns a JSON dict with the user's settings."""
        if os.path.isfile(f"{self.bot.BASE_DIR}Users{self.bot.S_SLASH}JSONSettings{self.bot.S_SLASH}{user_id}.json"):
            with open(f"{self.bot.BASE_DIR}Users{self.bot.S_SLASH}JSONSettings{self.bot.S_SLASH}{user_id}.json", "r") as file:
                json_data = json.load(file)

            if json_data['accepted_tos'] == 'true':
                settings = json_data['user_settings']
                return settings
            else:
                return None
        else:
            print(f"[GetUserSettings]   No valid user settings file for user id {user_id}")
            self.first_save_user_settings(user_id)
            await self.get_user_settings(user_id)

    def first_save_user_settings(self, user_id):
        # Define the default file layout
        default_configfile = {
            "user_settings": {
                "send_generalised_dms": "false",
                "get_dm_notification_for_role_addition": "false",
                "get_dm_notification_for_role_removal": "false",
                "get_dm_notification_for_coin_threshold": "false",
                "reminders_for_voice_time": "false",
                "participate_in_experiments": "false",
                "can_use_shop_section_2": "false",
                "contribute_to_statistics": "true",
            },
            "accepted_tos": "false",
            "config_version": "1",
        }
        
        # Read the existing JSON file, if it exists
        filepath = f"{self.bot.BASE_DIR}Users{self.bot.S_SLASH}JSONSettings{self.bot.S_SLASH}{user_id}.json"
        # Read the JSON file
        if not os.path.exists(filepath):
            # Create the file with default values
            with open(filepath, 'w') as f:
                json.dump(default_configfile, f)
        else:
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(default_configfile, f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("COG: Economy loaded!")

    @app_commands.command(name="coins", description="[Social] Shows coin balance. If above a threshold, shows items to buy!")
    @app_commands.guild_only()
    @app_commands.describe(operation="[Admin Only] set/add/lookup.", target_user="[Admin Only] Enter the user id for the operation to target", amount="[Admin Only] Use this as the value for the operation")
    @app_commands.choices(operation=[
        app_commands.Choice(name="Set", value="Set"),
        app_commands.Choice(name="Add", value="Add"),
        app_commands.Choice(name="Lookup", value="Lookup")
    ])
    async def coins(self, interaction: discord.Interaction, operation: Optional[app_commands.Choice[str]] = None, target_user: Optional[discord.Member] = None, amount: Optional[int] = None) -> None:
        await self.bot.slash_log(interaction)
        if interaction.guild and interaction.guild_id in self.bot.TESTER_GUILD_IDS:
            print(operation, target_user, amount)
            member_role = discord.utils.get(interaction.guild.roles, id=806481292392267796)
            staff_role = discord.utils.get(interaction.guild.roles, id=963738031863525436)
            owner_role = discord.utils.get(interaction.guild.roles, id=759861763247570946)
            if member_role in interaction.user.roles or staff_role in interaction.user.roles or owner_role in interaction.user.roles:
                print(interaction.user.id)
                authorID = interaction.user.id
                userID = authorID
                user = interaction.user
                serverID = interaction.guild_id

                coinBal = await self.get_coins(serverID, interaction.user.id)

                nolwenniumUserDir = (f"{self.bot.BASE_DIR}Nolwennium{self.bot.S_SLASH}{authorID}.txt")
                my_file = Path(nolwenniumUserDir)

                if not my_file.is_file():
                    with open(nolwenniumUserDir, 'w+') as f:
                        print(f"\nSet {self.bot.NAME_NOLWENNIUM} value to 0, {authorID} is a new user.")
                        try:
                            f.write('0')
                            f.close()
                        except Exception:
                            f.write('0')
                            f.close()

                with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                    nolwennium_bal = round(float(nolwennium_balance_file.read()), 2)
                    nolwennium_balance_file.close()

                if serverID == 384403250172133387 or serverID == 759861456300015657:
                    canRunCommand = member_role
                    canRunCommand2 = discord.utils.find(lambda r: r.id == 759861763247570946, interaction.guild.roles)
                    if canRunCommand or canRunCommand2 in user.roles:
                        if operation:
                            # List of stuff BEFORE showing the user their balance
                            if not operation or not target_user:
                                return await interaction.response.send_message(self.bot.IDK_WHAT_U_MEAN)
                            word1 = operation
                            userID = int(target_user.id)

                            if interaction.user.guild_permissions.administrator is True:
                                if word1.value == 'Set':
                                    if not amount or not userID:
                                        return await interaction.response.send_message(self.bot.IDK_WHAT_U_MEAN)
                                    users_coins = (f"{self.bot.BASE_DIR}Servers{self.bot.S_SLASH}{serverID}{self.bot.S_SLASH}Coins{self.bot.S_SLASH}{userID}.txt")
                                    old_coins = await self.get_coins(interaction.guild_id, userID)
                                    with open(users_coins, 'w+') as f:
                                        f.write(str(amount))
                                    new_coins = await self.get_coins(interaction.guild_id, userID)
                                    return await interaction.response.send_message(f"Successfully set the user's coins from {old_coins} to **{new_coins}**.")
                                elif word1.value == 'Add':
                                    if not amount or not userID:
                                        return await interaction.response.send_message(self.bot.IDK_WHAT_U_MEAN)
                                    added_balance = self.update_coins(interaction.guild_id, userID, amount)
                                    return await interaction.response.send_message(f"Successfully added {amount} Coins to the user. They now have **{added_balance}**!")
                                elif word1.value == 'Lookup':
                                    if not userID:
                                        return await interaction.response.send_message(self.bot.IDK_WHAT_U_MEAN)
                                    users_coins = await self.get_coins(interaction.guild_id, userID)
                                    if users_coins is None:
                                        return await interaction.response.send_message(f"<@{userID}> has not started earning Coins yet.")
                                    return await interaction.response.send_message(f"<@{userID}> has **{users_coins}** Coins.")

                                else:
                                    return await interaction.response.send_message(self.bot.IDK_WHAT_U_MEAN)

                            else:
                                await interaction.response.send_message("You don't have full administrator privileges to run this command. Try `/coins` without any added options?")

                        else: # If no operation is specified, show the user their balance
                            Roles = self.bot.Roles
                            hasCitizen = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[0], interaction.guild.roles)
                            hasKnight = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[1], interaction.guild.roles)
                            hasBaron = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[2], interaction.guild.roles)
                            hasViscount = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[3], interaction.guild.roles)
                            hasEarl = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[4], interaction.guild.roles)
                            hasMarquess = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[5], interaction.guild.roles)
                            hasDuke = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[6], interaction.guild.roles)
                            hasPrince = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[7], interaction.guild.roles)
                            hasKing = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[8], interaction.guild.roles)
                            hasAdmin = discord.utils.find(lambda r: r.id == Roles.ROLES_LIST_ID[9], interaction.guild.roles)

                            import random
                            randomCry = random.randint(1,7)
                            global cry
                            if randomCry == 1:
                                cry = '<:AmberCry:828577834146594856>'
                            if randomCry == 2:
                                cry = '<:BibiByeBye:828683852939395072>'
                            if randomCry == 3:
                                cry = '<:ColetteCry:828683829631516732>'
                            if randomCry == 4:
                                cry = '<:JessieCry:828683805861740654>'
                            if randomCry == 5:
                                cry = '<:SpikeCry:828683779206807622>'
                            if randomCry == 6:
                                cry = '<:SurgeCry:828683755694063667>'
                            if randomCry == 7:
                                cry = '<:TaraCry:828683724286853151>'

                            next_available_role_cost = 0
                            roles_tier = -1

                            if hasCitizen in user.roles:
                                roles_tier = Roles.Citizen_Tier
                            if hasKnight in user.roles:
                                roles_tier = Roles.Knight_Tier
                            if hasBaron in user.roles:
                                roles_tier = Roles.Baron_Tier
                            if hasViscount in user.roles:
                                roles_tier = Roles.Viscount_Tier
                            if hasEarl in user.roles:
                                roles_tier = Roles.Earl_Tier
                            if hasMarquess in user.roles:
                                roles_tier = Roles.Marquess_Tier
                            if hasMarquess in user.roles:
                                roles_tier = Roles.Marquess_Tier
                            if hasDuke in user.roles:
                                roles_tier = Roles.Duke_Tier
                            if hasPrince in user.roles:
                                roles_tier = Roles.Prince_Tier
                            if hasKing in user.roles:
                                roles_tier = Roles.King_Tier

                            nextRole = Roles.ROLES_LIST[(roles_tier + 1)]
                            next_available_role_cost = Roles.ROLES_COSTS[(roles_tier + 1)]

                            if roles_tier != -1:
                                roles_liste = ""

                                for i in range((roles_tier + 1)):
                                    roles_liste = (f"{roles_liste}" + f"{(Roles.ROLES_LIST[i])}: Unlocked! 🔓\n")
                                    i = i + 1

                                with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                                    nolwennium_balance = round(float(nolwennium_balance_file.read()), 2)
                                    nolwennium_balance_file.close()

                                finalSum = f"{roles_liste}" + f"{nextRole}: {Roles.ROLES_COSTS[(roles_tier + 1)]} {self.bot.EMOJI_COINS} 🔒"

                                if "🔓" not in finalSum:
                                    if f"{self.bot.EMOJI_COINS}" not in finalSum:
                                        finalSum = "***You have bought all possible roles! Maybe some more will come out in the future...***"
                            else:
                                embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {self.bot.EMOJI_COINS} coins and {nolwennium_bal} {self.bot.EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)
                                embed.add_field(
                                    name="Items curently available for you to buy:",
                                    value=f"**Citizen**: FREE {self.bot.EMOJI_COINS}\n\nType </buy:1057428586610573359> `item:citizen` to start ascending through purchasable roles!",
                                    inline=False)
                                embed.set_footer(text=(f'Type </buy:1057428586610573359> to buy your selected item! For example, </buy:1057428586610573359> `item:citizen`.\nYou can buy roles for Coins in this server, and use {self.bot.NAME_NOLWENNIUM} to run bot commands (in all servers).'))
                                await interaction.response.send_message(embed=embed)
                                return

                            embed = discord.Embed(title="User Balance", description=(f"You have {coinBal} {self.bot.EMOJI_COINS} coins and {nolwennium_bal} {self.bot.EMOJI_NOLWENNIUM} Nolwennium available to spend."), colour=0xFFD700)
                            embed.add_field(
                                name="Items available to buy:",
                                value=finalSum,
                                inline=False
                            )
                            if next_available_role_cost > 0:
                                embed.add_field(
                                    name="Next item available to buy in:",
                                    value=f"{next_available_role_cost - int(coinBal)} {self.bot.EMOJI_COINS} Coins (**{nextRole}**)",
                                    inline=False
                                )
                            elif next_available_role_cost <= 0:
                                embed.add_field(name="Buy your roles!", value=f":warning: You can afford a new role. Once bought, this will say how\n many more {self.bot.EMOJI_COINS} Coins are needed until the next role.")

                            embed.set_footer(text=(f'Type </buy:1057428586610573359> `item` to buy your selected item! For example, </buy:1057428586610573359> `item:citizen`.\nYou can buy roles for Coins in this server, and use {self.bot.NAME_NOLWENNIUM} to run bot commands (saved across all servers).'))

                            x = await self.get_user_settings(interaction.user.id)

                            view = discord.ui.View()
                            if x['can_use_shop_section_2'] == 'true':
                                view.add_item(CoinsButtons2(label="View Page 2", style=discord.ButtonStyle.blurple, bot=self.bot))

                            await interaction.response.send_message(embed=embed, view=view)
                    else:
                        await interaction.response.send_message("You do not have permission to access the shop interface.")
                else:
                    nolwenniumUserDir = self.nolwenniumUserDirectory(interaction)
                    my_file = Path(nolwenniumUserDir)
                    if not my_file.is_file():
                        nolly = "0"
                    else:
                        with open(nolwenniumUserDir, 'r') as nolwennium_balance_file:
                            nolwennium_balance = nolwennium_balance_file.read()
                            nolwennium_balance_file.close()
                        nolly = f"{nolwennium_balance} {self.bot.EMOJI_NOLWENNIUM}"
                    await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check https://ibaguette.com/discord for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {self.bot.EMOJI_NOLWENNIUM}")
            else:
                await self.bot.error_code(interaction, 1)
        else:
            await self.bot.error_code(interaction, 1)

    @app_commands.command(name="buy", description="[Social] Shows your balance, and available to buy items.")
    @app_commands.guild_only()
    @app_commands.choices(item=[
        app_commands.Choice(name="Citizen", value="Citizen"),
        app_commands.Choice(name="Knight", value="Knight"),
        app_commands.Choice(name="Baron", value="Baron"),
        app_commands.Choice(name="Viscount", value="Viscount"),
        app_commands.Choice(name="Earl", value="Earl"),
        app_commands.Choice(name="Marquess", value="Marquess"),
        app_commands.Choice(name="Duke", value="Duke"),
        app_commands.Choice(name="Prince", value="Prince"),
        app_commands.Choice(name="King", value="King")
    ])
    @app_commands.describe(item="Enter the item to buy here")
    async def buy(self, interaction: discord.Interaction, item: app_commands.Choice[str]) -> None:
        await self.bot.slash_log(interaction)
        if not interaction.guild:
            return await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
        if interaction.guild_id in self.bot.TESTER_GUILD_IDS:
            canRunCommand = self.bot.rolePrivate
            owner = discord.utils.find(lambda r: r.name == 'Owner', interaction.guild.roles)
            staff = discord.utils.find(lambda r: r.name == 'Staff', interaction.guild.roles)
            can_access_shop_ui = False
            if owner in interaction.user.roles:
                print("Owner is in the roles list")
                await interaction.channel.send("> Note: you already have owner permissions, this overrides the shop's items, permissions, and perks")
                can_access_shop_ui = True
            if staff in interaction.user.roles:
                print("Staff is in the roles list")
                await interaction.channel.send("> Note: already have staff permissions, this overrides the shop's items, permissions, and perks")
                can_access_shop_ui = True
            if canRunCommand in interaction.user.roles:
                print("Member is in the list")
                can_access_shop_ui = True
            if can_access_shop_ui:
                member = await interaction.guild.fetch_member(interaction.user.id)
                item_name = item.value.lower()

                coinBal = await self.get_coins(interaction.guild_id, interaction.user.id)
                
                EMOJI_COINS = self.bot.EMOJI_COINS
                NAME_NOLWENNIUM = self.bot.NAME_NOLWENNIUM

                if item_name == 'citizen':
                    cost = 1
                    hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                    if hasCitizen in member.roles:
                        await interaction.response.send_message("You can't buy Citizen, you already have it!")
                        return

                    coinBal = int(coinBal) - cost
                    self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                    role = discord.utils.get(interaction.guild.roles, name="Citizen")
                    await member.add_roles(role)
                    embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought Citizen for free! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                    embed.add_field(name="Perks",
                                    value=f"• Above Member in the Member List\n• Custom nickname\n• Add reactions\n• Bonus {NAME_NOLWENNIUM}",
                                    inline=False
                                    )
                    await interaction.response.send_message(embed=embed)
                    return

    #           KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT KNIGHT

                if item_name == 'knight':
                    cost = 25
                    roleName = "Knight"
                    hasKnight = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasKnight in member.roles:
                        await interaction.response.send_message(f"You can't buy {roleName}, you already have it!")
                        return

                    hasCitizen = discord.utils.find(lambda r: r.name == 'Citizen', interaction.guild.roles)
                    if hasCitizen in member.roles:
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Citizen"))
                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Create private threads",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Citizen before {roleName}.")
                        return
                    return

    #           BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON BARON

                if item_name == 'baron':
                    cost = 50
                    roleName = "Baron"
                    #   Check if the person already has the role.
                    hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasBaron in member.roles:
                        await interaction.response.send_message(f"You can't buy {roleName}, you already have it!")
                        return

                    #   Check if the person has the previous role. If not, can't buy.
                    hasKnight = discord.utils.find(lambda r: r.name == 'Knight', interaction.guild.roles)
                    if hasKnight in member.roles:
                        #   Tests balance if user can afford the new role.
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        #   If the balance is adequate, allow the purchase.
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Knight"))
                        await member.add_roles(role)

                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value=f"Everything in Citizen, and:\n• Use external stickers\n• Increased Coins earning\n• Bonus {NAME_NOLWENNIUM}",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Knight before {roleName}.")
                        return
                    return

    #           VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT VISCOUNT

                if item_name == 'viscount':
                    cost = 100
                    roleName = "Viscount"
                    #   Check if the person already has the role.
                    hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasBaron in member.roles:
                        await interaction.response.send_message("You can't buy Viscount, you already have it!")
                        return

                    #   Check if the person has the previous role. If not, can't buy.
                    hasBaron = discord.utils.find(lambda r: r.name == 'Baron', interaction.guild.roles)
                    if hasBaron in member.roles:
                        #   Tests balance if user can afford the new role.
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        #   If the balance is adequate, allow the purchase.
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Baron"))
                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Everything in Baron, and:\n• Use TTS messages\n• Use server activities",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Baron before {roleName}.")
                        return
                    return

    #           EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL EARL

                if item_name == 'earl':
                    cost = 250
                    roleName = "Earl"
                    #   Check if the person already has the role.
                    hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasBaron in member.roles:
                        await interaction.response.send_message("You can't buy Earl, you already have it!")
                        return

                    #   Check if the person has the previous role. If not, can't buy.
                    hasViscount = discord.utils.find(lambda r: r.name == "Viscount", interaction.guild.roles)
                    if hasViscount in member.roles:
                        #   Tests balance if user can afford the new role.
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        #   If the balance is adequate, allow the purchase.
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        if role is not None:
                            await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Viscount")) # Remove previous role
                            await member.add_roles(role)
                        else:
                            print(f"Role '{roleName}' not found")

                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Everything in Viscount, and:\n• Add and edit server events",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Viscount before {roleName}.")
                        return
                    return

    #           MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS MARQUESS

                if item_name == 'marquess':
                    cost = 500
                    roleName = "Marquess"
                    #   Check if the person already has the role.
                    hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasBaron in member.roles:
                        await interaction.response.send_message("You can't buy Earl, you already have it!")
                        return

                    #   Check if the person has the previous role. If not, can't buy.
                    hasEarl = discord.utils.find(lambda r: r.name == 'Earl', interaction.guild.roles)
                    if hasEarl in member.roles:
                        #   Tests balance if user can afford the new role.
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        #   If the balance is adequate, allow the purchase.
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Earl"))
                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Everything in Earl, and:\n• View detailed server statistics\n• Access to some more stuff, you'll figure it out",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Earl before {roleName}.")
                        return
                    return

    #           DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE DUKE

                if item_name == 'duke':
                    cost = 1000
                    roleName = "Duke"
                    #   Check if the person already has the role.
                    hasBaron = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasBaron in member.roles:
                        await interaction.response.send_message("You can't buy Earl, you already have it!")
                        return
                    #   Check if the person has the previous role. If not, can't buy.
                    hasMarquess = discord.utils.find(lambda r: r.name == 'Marquess', interaction.guild.roles)
                    if hasMarquess in member.roles:
                        #   Tests balance if user can afford the new role.
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        #   If the balance is adequate, allow the purchase.
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Marquess"))

                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Everything in Marquess, and:\n• Mute members\n• Manage threads\n• View private threads\n• Access to history of <#1035684553546809456>",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message(f"You must buy Marquess before {roleName}.")
                        return
                    return

    #           PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINCE PRINC

                if item_name == 'prince':
                    cost = 2500
                    roleName = "Prince"
                    hasPrince = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasPrince in member.roles:
                        await interaction.response.send_message("You can't buy Prince, you already have it!")
                        return

                    hasDuke = discord.utils.find(lambda r: r.name == 'Duke', interaction.guild.roles)
                    if hasDuke in member.roles:
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest <= 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name=roleName)
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Duke"))
                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought {roleName} for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value="Everything in Duke, and:\n• Move members in voice channels\n• Use Priority speaker in voice chat\n• Change others' nicknames\n• Time out members if they are being annoying\n• Add emojis and stickers\n• Add custom channels",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message("You must buy Knight before Prince.")
                    return

    #           KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING KING

                if item_name == 'king':
                    cost = 10000
                    roleName = "King"
                    hasKing = discord.utils.find(lambda r: r.name == roleName, interaction.guild.roles)
                    if hasKing in member.roles:
                        await interaction.response.send_message("You can't buy King, you already have it!")
                        return

                    hasPrince = discord.utils.find(lambda r: r.name == 'Prince', interaction.guild.roles)
                    if hasPrince in member.roles:
                        coinBalTest = int(coinBal) - cost
                        if coinBalTest < 0:
                            requiredAmount = cost - int(coinBal)
                            await interaction.response.send_message(f"You do not have enough Coins to buy {roleName}. You need {requiredAmount} more.")
                            return
                        coinBal = int(coinBal) - cost
                        self.update_coins(interaction.guild_id, interaction.user.id, -cost)

                        role = discord.utils.get(interaction.guild.roles, name="King")
                        await member.add_roles(role)
                        await member.remove_roles(discord.utils.get(interaction.guild.roles, name="Prince"))
                        embed = discord.Embed(title="Baguette Brigaders Shop", description=(f"You've just bought King for {cost} {EMOJI_COINS}! Remaining balance: {coinBal} {EMOJI_COINS}"), colour=0xFFD700)
                        embed.add_field(name="Perks",
                                        value=f"Everything in Prince, and:\n• Deafen members\n• Pin and manage messages\n• Add custom webhooks\n• Add custom bots\n• Add into Other Channels and define permissions",
                                        inline=False)
                        await interaction.response.send_message(embed=embed)
                    else:
                        await interaction.response.send_message("You must buy Prince before King.")
                    return

                if item_name == 'admin':
                    await self.bot.error_code(interaction, 1)
                else:
                    await interaction.response.send_message(f"**{item_name}** isn't a valid item to buy. Try `Citizen/Knight/Baron/Viscount/Earl/Marquess/Duke/Prince/King/Admin`!")
            else:
                await self.bot.error_code(interaction, 1)
        else:
            nolwenniumUserDir = self.nolwenniumUserDirectory(interaction)
            my_file = Path(nolwenniumUserDir)
            if not my_file.is_file():
                nolly = "0"
            else:
                f = open(nolwenniumUserDir, 'r')
                nolwennium_bal = f.read()
                f.close()
                nolly = f"{nolwennium_bal} {self.bot.EMOJI_NOLWENNIUM}"
            await interaction.response.send_message(f"Gear up! This command will be unlocked for this server soon. Check discord.gg/GfetCXH for updates on what this will do, and for the all-new currency system. You are eligible for {nolly} new currency points! {self.bot.EMOJI_NOLWENNIUM}")


async def setup(bot):
    await bot.add_cog(Economy(bot))
