from discord.ext import commands
from discord import utils, Embed
from time import time
import lavalink

class musicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node('localhost', 7000, 'testing', 'eu', 'music-node')
        self.bot.add_listener(self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.command(name='newplay')
    async def newplay(self, ctx):
        try:
            millisecs = round(time() * 1000)
            text = ctx.message.content
            search_term = text.split(' ', 1)[-1]
            player = self.bot.music.player_manager.get(ctx.guild.id)
            query = f"ytsearch:{search_term}"
            results = await player.node.get_tracks(query)
            track = results['tracks'][0]
            #await ctx.send(track)s
            if not player.is_playing:
                player.add(requester=ctx.author.id, track=track)
                await player.play()
                done_millisecs = round(time() * 1000)
                time_delay = done_millisecs - millisecs
                embed = Embed(title="Playing audio", description=f"**[{player.current.title}]({player.current.uri})**", colour=0x228B22)
                embed.add_field(name="Channel", value=f"{player.current.author}")
                embed.add_field(name="Time taken", value=f"{time_delay}ms")
                await ctx.send(embed=embed)
            else:
                await player.stop()
                await musicCog.newplay(self, ctx)

        except AttributeError:
            member = utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
            if member.voice is not None:
                vc = member.voice.channel
                player = self.bot.music.player_manager.create(ctx.guild.id, endpoint = str(ctx.guild.region))
                if not player.is_connected:
                    player.store('channel', ctx.channel.id)
                    await self.connect_to(ctx.guild.id, str(vc.id))
            
            await musicCog.newplay(self, ctx)

    @commands.command(name='stop')
    async def stop(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        if player.is_playing:
            await player.stop()
            await ctx.send("Stopped playing audio.")
        else:
            await ctx.send("Not playing any audio to stop.")

    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

def setup(bot):
    bot.add_cog(musicCog(bot))
