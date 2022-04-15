from discord.ext import commands
from discord import utils, Embed
from time import time
import lavalink
import os


async def setVolume(ctx):
    server_preference_directory = f"D:\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences"
    server_preference_file = f"{server_preference_directory}\\Voice_Chat_Volume.txt"
    text = ctx.message.content
    sp1 = text.split(' ', 1)[-1]
    volume = sp1
    if os.path.exists(server_preference_directory):
        with open(server_preference_file, "w+") as e:
            e.close()
        f = open(server_preference_file, "a")
        f.write(str(volume))
        await ctx.send(f"<a:AnimatedTick:956621591108804652> Volume set to {volume}%.\n*This will take effect next time an audio command is run.*")
        f.close()
    else:
        os.mkdir(server_preference_directory)
        with open(server_preference_file, "w+") as e:
            e.close()
        f = open(server_preference_file, "a")
        f.write(str(100))
        f.close()
        await ctx.send("<a:AnimatedTick:956621591108804652> Volume is now being controlled by the command `.volume`.")


async def getServerVoiceVolume(ctx):
    try:
        f = open(
            f"D:\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences\\Voice_Chat_Volume.txt", "r")
        volume = f.read()
        f.close()
        return int(volume)
    except FileNotFoundError:
        await setVolume(ctx)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node(
            'localhost', 7193, 'testing', 'eu', 'music-node')
        self.bot.add_listener(
            self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.command(name='newplay')
    async def newplay(self, ctx):
        try:
            volume = await getServerVoiceVolume(ctx)
            millisecs = round(time() * 1000)
            text = ctx.message.content
            search_term = text.split(' ', 1)[-1]
            player = self.bot.music.player_manager.get(ctx.guild.id)
            if "http" not in search_term:
                query = f"ytsearch:{search_term}"
            else:
                query = search_term
            results = await player.node.get_tracks(query)
            track = results['tracks'][0]
            # await ctx.send(track)
            if player.is_connected:
                if not player.is_playing:
                    player.add(requester=ctx.author.id, track=track)
                    await player.play()
                    await player.set_volume(volume)
                    done_millisecs = round(time() * 1000)
                    time_delay = done_millisecs - millisecs
                    embed = Embed(
                        title="Playing audio", description=f"**[{player.current.title}]({player.current.uri})**", colour=0x228B22)
                    embed.add_field(
                        name="Channel", value=f"{player.current.author}")
                    embed.add_field(name="Time taken", value=f"{time_delay}ms")
                    await ctx.send(embed=embed)
                else:
                    print("Stopping player.")
                    await player.stop()
                    await Music.newplay(self, ctx)
            else:
                raise AttributeError

        except AttributeError:
            member = utils.find(
                lambda m: m.id == ctx.author.id, ctx.guild.members)
            if member.voice is not None:
                vc = member.voice.channel
                player = self.bot.music.player_manager.create(
                    ctx.guild.id, endpoint=str(ctx.guild.region))
                if not player.is_connected:
                    player.store('channel', ctx.channel.id)
                    await self.connect_to(ctx.guild.id, str(vc.id))
                    await ctx.send(f"Joined Voice Channel <#{vc.id}>")
            await Music.newplay(self, ctx)

    @commands.command(name='stop')
    async def stop(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        if player.is_playing:
            await player.stop()
            await ctx.send("Stopped playing audio.")
        else:
            await ctx.send("Not playing any audio to stop.")

    async def change_volume_instantly(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        if player.is_connected:
            if player.is_playing:
                volume = await getServerVoiceVolume(ctx)
                await player.set_volume(volume)

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)


def setup(bot):
    bot.add_cog(Music(bot))
