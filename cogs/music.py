import wavelink
import discord
from discord import app_commands
from discord.ext import commands
from wavelink.ext import spotify
from os import path

MINIFIED_BASE_DIR = "D:\\Draggie Programs\\BetaBaguetteBot\\"
BASE_DIR = "D:\\Draggie Programs\\BetaBaguetteBot\\draggiebot\\"
BASE_DIR_MINUS_SLASH = "D:\\Draggie Programs\\BetaBaguetteBot\\draggiebot"
S_SLASH = "\\"

async def get_server_voice_volume(guild_id: int) -> int:
    """Returns the volume of a guild chosen by its members.\n
    Must include parameter of the guild id\n
    Returns an percentage as an integer. You can divide this by 100 if you want a float."""
    if not path.isfile(f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt"):
        with open (f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'w') as f:
            f.write(str("30"))
    with open (f"{BASE_DIR}Servers{S_SLASH}{guild_id}{S_SLASH}Preferences{S_SLASH}Voice_Chat_Volume.txt", 'r') as file:
        volume = file.read()
    print(f"[VoiceVolQuery]      Server {guild_id} has a volume of {volume}%")
    return int(volume)

with open(f"{BASE_DIR_MINUS_SLASH}\\spotify_api_key.txt", 'r') as spapi:
    spotify_id = spapi.read()
with open(f"{BASE_DIR_MINUS_SLASH}\\spotify_client_id.txt", 'r') as spcid:
    spotify_client_id = spcid.read()

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
                client_id=spotify_client_id,
                client_secret=spotify_id,
            ),
        )

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f"Node: <{node.identifier}> is ready!")

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track, reason):
        try:
            if not player.queue.is_empty:
                new = await player.queue.get_wait()
                volume = await get_server_voice_volume(player.guild.id)
                print("Playing new song.")
                await player.play(new, volume=int(volume))
            else:
                await player.stop()
        except Exception as e:
            await player.channel.send(e)

    @commands.command()
    async def play(self, ctx: commands.Context, *, search):
        """Play a song with the given search query.

        If not connected, connect to our voice channel.
        """

        if ctx.author.voice is None:
            return await ctx.send("Not in voice channel")
        vc: wavelink.Player = ctx.voice_client or await ctx.author.voice.channel.connect(cls=wavelink.Player)
        tracks = False
        if "open.spotify.com/playlist" in search:
            await ctx.send("Searching spotify playlist...")
            tracks = await spotify.SpotifyTrack.search(query=search)

        elif "open.spotify.com/track" in search:
            await ctx.send("Searching spotify individual track")
            async for track in spotify.SpotifyTrack.iterator(query=search, type=spotify.SpotifySearchType.album):
                await ctx.send(track)

        track = wavelink.YouTubeTrack(search)


        if tracks:
            for track in tracks:
                await vc.queue.put_wait(track)
            await ctx.send(f'Added {len(tracks)} tracks to the queue. There are {len(vc.queue)-1} tracks currently queued.')
            if not vc.is_playing():
                volume = await get_server_voice_volume(ctx.guild.id)
                await vc.set_volume(volume)
                await ctx.send(f"Now playing: **{vc.queue[0]}**.")
                await vc.play(track)

        else:
            if vc.queue.is_empty and not vc.is_playing():
                volume = await get_server_voice_volume(ctx.guild.id)
                await vc.set_volume(volume)
                await vc.play(search)
                await ctx.send(f'Playing `{search.title}` in the voice channel...')
                await ctx.send(f"debug: Queue:```{vc.queue}```")
            else:
                await vc.queue.put_wait(search)
                await ctx.send(f'Added `{search.title}` to the queue...')

    @commands.command()
    async def stop(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client
        if vc.is_playing():
            await vc.stop()
            await ctx.send("I stopped it.")


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
            await ctx.send(f"Now playing: {vc.queue[0]}. There are {len(vc.queue)-1} songs left.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))