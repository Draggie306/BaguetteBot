from discord.ext import commands
from discord import utils, Embed
from time import time, sleep
import lavalink, random, os, math, discord
from discord_slash import SlashCommand

emoji_Nolwennium = "<:NolwenniumCoin:846464419503931443>"
name_Nolwennium = "Nolwennium"
Croissants = [796777705520758795, 821405856285196350, 588081261537394730]

async def getServerVoiceVolume(ctx):
    try:
        f = open(
            f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences\\Voice_Chat_Volume.txt", "r")
        volume = f.read()
        f.close()
        return int(volume)
    except Exception as e:
        print(f"Exception {e} in getServerVoiceVolume")
        with open(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences\\Voice_Chat_Volume.txt", "w+") as f:
            print(f"w+")
            f.close()

        f = open(f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences\\Voice_Chat_Volume.txt", "w")
        f.write("50")
        print("wrote 50")
        f.close()
        
        await ctx.send("<a:AnimatedTick:956621591108804652> Server volume set to 50% (first run)")
        return(50)
        #await ctx.send(f"Error occured while getting server voice chat volume! This may be because it was not set or was not stopped corerctly. Try setting the volume by typing .volume [percentage].\n\n`{e}`")


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.music = lavalink.Client(self.bot.user.id)
        self.bot.music.add_node(
            "localhost", 2332, "sussyamogus", "na", None, 600, None, 10
        )
        self.bot.add_listener(
            self.bot.music.voice_update_handler, 'on_socket_response')
        self.bot.music.add_event_hook(self.track_hook)

    @commands.command(name='newplay', help="BaguetteBot's new audio playing feature. Type '.newplay' followed by your YouTube search term while in a voice chat to start playing audio!", brief="Joins and plays auido in a Voice Channel.")
    async def newplay(self, ctx):
        try:
            volume = await getServerVoiceVolume(ctx)
            millisecs = round(time() * 1000)
            text = ctx.message.content
            test1 = text.split()
            try:
                tester = test1[1]
            except IndexError as e:
                await ctx.send("No search term specified.")
                return
            search_term = text.split(' ', 1)[-1]
            print(f"Search term in {ctx.guild.name}: {search_term}")
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

    @commands.command(name='stop', help="Stops the bot playing audio in Voice Chat.", brief="Stops playing audio.")
    async def stop(self, ctx):
        player = self.bot.music.player_manager.get(ctx.guild.id)
        if player.is_playing:
            await player.stop()
            await ctx.send("Stopped playing audio.")
        else:
            await ctx.send("Not playing any audio to stop.")
        
    @commands.command(name='queue')
    async def queue(self, ctx, page: int = 1):
        player = self.bot.music.player_manager.get(ctx.guild.id)

        items_per_page = 10
        pages = math.ceil(len(player.queue) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue_list = ''
        for index, track in enumerate(player.queue[start:end], start=start):
            queue_list += f'`{index + 1}.` [**{track.title}**]({track.uri})\n'

            embed = discord.Embed(colour=discord.Color.blurple(), description=f'**{len(player.queue)} tracks**\n\n{queue_list}')
            embed.set_footer(text=f'Viewing page {page}/{pages}')
            await ctx.send(embed=embed)

    @commands.command(name='lock', aliases=["lockvolume", "unlock"], help="Locks a Voice Chat's volume from being changed. Admin permissions required.",  brief="Locks server voice volume.")
    async def lockvolume(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            server_preference_directory = f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences"
            check_lock = f"{server_preference_directory}\\volume.locked"
            if not os.path.isfile(check_lock):
                sp1 = (ctx.message.content).split(' ', 1)[-1]
                await ctx.send(f"Locking volume to {sp1}%...")
                try:
                    sp1=int(sp1)
                except Exception:
                    await ctx.send(f"<a:AnimatedCross:956621593113665536> No volume specified to lock at!")
                    return
                
                server_preference_file = f"{server_preference_directory}\\Voice_Chat_Volume.txt"
                with open(server_preference_file, "w+") as e:
                    e.write("")
                    e.close()
                    print("Wrote 0 in w+ during locking")
                f = open(server_preference_file, "a")
                f.write(str (sp1))

                with open(check_lock, "w+") as e:
                    e.close()
                    await ctx.send("Locked successfully.")
                
                player = self.bot.music.player_manager.get(ctx.guild.id)
                if player is not None:
                    if player.is_connected:
                        if player.is_playing:
                            await player.set_volume(sp1)
            else:
                os.remove(check_lock)
                await ctx.send("Removed lock.")
        else:
            await ctx.send("You cannot lock the volume as you are missing the Administrator permission.")
                

    @commands.command(name='volume', aliases=["setvolume"])
    async def volume(self, ctx):
        server_preference_directory = f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Servers\\{ctx.guild.id}\\Preferences"
        server_preference_file = f"{server_preference_directory}\\Voice_Chat_Volume.txt"
        check_lock = f"{server_preference_directory}\\volume.locked"
        text = ctx.message.content
        sp1 = text.split(' ', 1)[-1]
        volume = sp1

        filedir = (f"D:\\Draggie Programs\\BaguetteBot\\draggiebot\\Nolwennium\\{ctx.message.author.id}.txt")
        try:
            with open(filedir, 'r') as f:
                balance = f.read()
                f.close()
        except FileNotFoundError:
            e = open(filedir, 'w+')
            e.write("0")
            e.close()
        new_balance = float(balance) - 1
        if new_balance <= 0:
            await ctx.send(f"You do not have enough {name_Nolwennium} {emoji_Nolwennium} to change the volume. It will cost 1 and you have {balance}. You can type `.mine` to get some.")
            return
        else:
            f = open(filedir, 'w+')
            f.write(str (new_balance))
            f.close()

        if os.path.exists(server_preference_directory):
            if not os.path.isfile(check_lock):
                with open(server_preference_file, "w+") as e:
                    e.close()
                f = open(server_preference_file, "a")
                f.write(str (volume))
                await ctx.send(f"<a:AnimatedTick:956621591108804652> Server volume set to {volume}%.")
                f.close()
            else:
                f = open(server_preference_file, 'r')
                set_volume = f.read()
                f.close()
                await ctx.send(f"<a:AnimatedCross:956621593113665536> Server volume could not be set. It has been locked to {set_volume}% by an admin and must be unlocked first.")
        else:
            os.mkdir(server_preference_directory)
            with open(server_preference_file, "w+") as e:
                e.close()
            f = open(server_preference_file, "a")
            f.write("100")
            f.close()
            await ctx.send("<a:AnimatedTick:956621591108804652> Volume is now being controlled by the command `.volume`.")

        player = self.bot.music.player_manager.get(ctx.guild.id)
        if player is not None:
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
