import wavelink
import discord
from discord.ext import commands
from wavelink.ext import spotify

class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(
            bot=self.bot,
            host="localhost",
            port=2333,
            password="youshallnotpass",
            spotify_client=spotify.SpotifyClient(
                client_id="",
                client_secret="",
            ),
        )

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f"Node: <{node.identifier}> is ready!")

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track, reason):
        if not player.queue.is_empty:
            new = await player.queue.get_wait()
            await player.play(new)
        else:
            await player.stop()

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        """Play a song with the given search query.

        If not connected, connect to our voice channel.
        """
        if ctx.author.voice is None:
            return await ctx.send("Not in voice channel")
        vc: wavelink.Player = ctx.voice_client or await ctx.author.voice.channel.connect(cls=wavelink.Player)
        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(search)
            await ctx.send(f'Playing `{search.title}` in the voice channel...')
        else:
            await vc.queue.put_wait(search)
            await ctx.send(f'Added `{search.title}` to the queue...')

    @commands.command()
    async def queue(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client
        if not vc.queue.is_empty:
            print(f"Here is the current queue: {vc.queue}")
            await ctx.send(f"Here is the current queue: {vc.queue}")
    
    @commands.command()
    async def skip(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client
        if not vc.queue.is_empty:
            await vc.stop()
            await ctx.send(f"Now playing: {vc.queue[0]}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))