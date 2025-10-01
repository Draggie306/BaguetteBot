import discord
from discord import app_commands
from discord.ext import commands
import os
import time
import psutil


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("COG: Info loaded!")

    @app_commands.command(name="stats", description="[Info] Just a few useful bot statistics.")
    async def stats(self, interaction: discord.Interaction) -> None:
        await self.bot.slash_log(interaction)
        await self.bot.bot_runtime_events(1)
        if round(self.bot.latency * 1000) <= 100:
            pingColour = (0x44ff44)
        elif round(self.bot.latency * 1000) <= 150:
            pingColour = (0xffd000)
        elif round(self.bot.latency * 1000) <= 150:
            pingColour = (0xff6600)
        else:
            pingColour = (0x990000)

        fileSizeBytes = os.path.getsize(f'{self.bot.BASE_DIR}GitHub{self.bot.S_SLASH}BaguetteBot{self.bot.S_SLASH}BaguetteBot.py')

        num_lines = sum(1 for line in open(f"{self.bot.BASE_DIR}GitHub{self.bot.S_SLASH}BaguetteBot{self.bot.S_SLASH}BaguetteBot.py", encoding='utf-8'))
        secsOrMins1 = "seconds"
        current_time = time.time()
        uptimeInSeconds = int(round(current_time - self.bot.start_time))

        cpuPercentage = psutil.cpu_percent()
        memoryUsage = psutil.virtual_memory().percent
        secsOrMins2 = "seconds"
        if uptimeInSeconds > 60:
            uptimeInSeconds = int(round(uptimeInSeconds / 60))
            secsOrMins2 = "minutes"

        real_uptimeInSeconds = int(round(current_time - self.bot.ready_start_time))

        ping = round(self.bot.latency * 1000)

        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            if guild.member_count:
                members += guild.member_count - 1

        DIR = 'D:\\Draggie Programs\\BaguetteBot\\draggiebot\\ExternalAssets\\AudioCache\\'
        cachedVideos = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

        embed = discord.Embed(title="_**Bot Stats**_\n", colour=pingColour)
        embed.add_field(name="CPU Usage", value=f"{cpuPercentage}%")
        embed.add_field(name="RAM Usage", value=f"{memoryUsage}%")
        embed.add_field(name="Lines of Code", value=f"{num_lines} lines")
        embed.add_field(name="File Size", value=(f"{fileSizeBytes} bytes"))
        embed.add_field(name="**Uptime:**", value=(f"{uptimeInSeconds} {secsOrMins2} ({real_uptimeInSeconds}s ago)"))
        embed.add_field(name="**Ping:**", value=(f"{ping} ms"))
        embed.add_field(name="**Videos Loaded:**", value=cachedVideos)
        embed.add_field(name="**Servers :**", value=(servers))
        embed.add_field(name="**Total Members:**", value=members)
        embed.add_field(name="**Bot Events**", value=self.bot.bot_events)
        embed.add_field(name="**Bot Events/sec:**", value=f"{round((self.bot.bot_events / real_uptimeInSeconds), 3)}")
        embed.add_field(name="**Debug Mode:**", value="Disabled")
        embed.add_field(name="**Command Logging:**", value="Enabled")
        embed.add_field(name="**Message Logging:**", value="Enabled")
        embed.add_field(name="**Voice Channels:**", value="Enabled")
        embed.add_field(name="**YouTube Player:**", value=self.bot.YTAPI_STATUS)
        embed.add_field(name="**Audio Subsystem:**", value=self.bot.AUDIO_SUBSYSTEM)
        embed.add_field(name="**Supercell API:**", value=self.bot.SCAPI_STATUS)

        embed.set_footer(text=(f"\nBaguetteBot.py | {self.bot.DRAGGIEBOT_VERSION}/{self.bot.BUILD} | discord.py {discord.__version__} | made by draggie"))
        await interaction.response.send_message(embed=embed)

        with open(self.bot.GlobalLogDir, "a", encoding="UTF-8") as f:
            from datetime import datetime
            f.write(f"\nSLASH COMMAND RAN -> '.stats' ran by {interaction.user.id} in {interaction.guild_id} at {datetime.now()}")


async def setup(bot):
    await bot.add_cog(Info(bot))
