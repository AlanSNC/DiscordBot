# Dépendances nécessaires : discord.py et python-dotenv
# Installe-les avec :
# python -m pip install -U discord.py python-dotenv

import discord
from discord.ext import commands
from dotenv import load_dotenv


import asyncio
import random
import os

intents = discord.Intents.default()
intents.voice_states = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} est prêt et connecté !")

@bot.event
async def on_voice_state_update(member, before, after):
    
    if before.channel is None and after.channel is not None:
        voice_channel = after.channel
        

        intro_files = {
            464088992586137620: ["media/BattyRETURN.mp3"],
            421190412900892672: ["media/Skyjinx.mp3"],
            322059268641521664: ["media/willlutaIntro.mp3"],
            451802068852670464: ["media/OuranosIntro.mp3"],
            638353037936820225: ["media/Ralph2.mp3", "media/ToYourEterntity.mp3","media/RalphDADADAN.mp3"],
            1004126098654760991:["media/Ralph.mp3"],
            586148316799303681: ["media/Nico2.mp3","media/Nico4Real.mp3"],
            656642201337593857: ["media/Hedinhozzz.mp3"],
            244456370953256961: ["media/Momo.mp3", "media/Momo3.mp3"],
            358680058010796032: ["media/Tony.mp3"],
            497558179333275658: ["media/Drako.mp3"],
            715278953614409739: ["media/Aimerde.mp3"]
        }

        if member.id in intro_files:
            print(f"{member.display_name} joined {voice_channel.name}")
            audio_file = random.choice(intro_files[member.id])
            print(audio_file)

            if member.guild.voice_client is None or not member.guild.voice_client.is_connected():
                voice_client = await voice_channel.connect()
            else:
                voice_client = member.guild.voice_client

            voice_client.play(discord.FFmpegPCMAudio(audio_file))

            while voice_client.is_playing():
                await asyncio.sleep(1)

            await voice_client.disconnect()

 
    elif before.channel is not None and after.channel is None:
        voice_channel = before.channel

        outro_files = {
            638353037936820225: ["media/Prout.mp3"],
        }

        if member.id in outro_files:
            print(f"{member.display_name} left {voice_channel.name}")
            audio_file = random.choice(outro_files[member.id])

            if member.guild.voice_client is None or not member.guild.voice_client.is_connected():
                voice_client = await voice_channel.connect()
            else:
                voice_client = member.guild.voice_client

            voice_client.play(discord.FFmpegPCMAudio(audio_file))

            while voice_client.is_playing():
                await asyncio.sleep(1)

            await voice_client.disconnect()

@bot.command()
async def join(ctx):
    """Command to make the bot join a voice channel."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel.")

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
bot.run(os.getenv('DISCORD_TOKEN'))
