import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = "&")

@client.event
async def on_ready():
    print ("Bot Loaded...")

"""Custom Voice Channels"""
@client.event
async def on_voice_state_update(member, before, after):
    channelID = 440255311949987849
    categoryID = 440255201828536320
    if after.channel is not None:
        if after.channel.id == channelID:
            client.channelowner = member
            client.newChannel = await member.guild.create_voice_channel('Rename Me!', category=client.get_channel(categoryID))
            await member.move_to(client.newChannel)
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            await client.newChannel.set_permissions(client.channelowner, overwrite=overwrite)
        elif before.channel.id == client.newChannel.id and after.channel.id ==
        elif before.channel.id == client.newChannel.id and after.channel.id != client.newChannel.id and client.newChannel.members == []:
            await discord.VoiceChannel.delete(client.newChannel)

@client.command()
async def kick(ctx, member: discord.Member):
    if client.channelowner.id == ctx.author.id:
        afkChannel = client.get_channel(437834824393293824)
        client.commandChannel = client.get_channel(440687280907354113)
        await member.move_to(afkChannel)
        client.commandChannel.send("Kicked " + member.mention + " from" + client.channelowner.mention + "'s Channel!")
""""""
client.run("NDM3NDgxNzkxMTE3MzI4Mzk1.DcP8TQ.6iCLEPGYYMzt8ZfQxlIBjy-pJ60")
