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
        if after.channel.id == channelID and member =! in client.deniedMembers:
            client.channelowner = member
            client.newChannel = await member.guild.create_voice_channel('Rename Me!', category=client.get_channel(categoryID))
            await member.move_to(client.newChannel)
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            await client.newChannel.set_permissions(client.channelowner, overwrite=overwrite)
        elif before.channel.id == client.newChannel.id and after.channel.id == client.newChannel.id:
            await discord.VoiceChannel.delete(client.newChannel
        elif before.channel.id == client.newChannel.id and after.channel.id =! client.newChannel.id and client.newChannel.members == []:
            await discord.VoiceChannel.delete(client.newChannel)

@client.command()
async def kick(ctx, member: discord.Member):
    if client.channelowner.id == ctx.author.id:
        afkChannel = client.get_channel(437834824393293824)
        await member.move_to(afkChannel)
        channel = client.get_channel(440687280907354113)
        client.channel.send("Kicked " + member.mention + " from " + ctx.author.mention + "'s Channel!")

@client.command()
async def deny(ctx, member: discord.Member):
    client.deniedMembers = []
    if member =! in client.deniedMembers and client.channelowner.id == ctx.author.id:
        client.deniedMembers.append(member)
        afkChannel = client.get_channel(437834824393293824)
        await member.move_to(afkChannel)
        channel = client.get_channel(440687280907354113)
        await channel.send("Denied access to " + member.mention + " from " + ctx.author.mention + "'s channel!")
    elif member == in client.deniedMembers:
        await channel.send(member.mention + " is already denied from " + ctx.author.mention + "'s channel!)
    elif client.channelowner.id =! ctx.author.id:
        await channel.send("You are not the owner of this channel!")

@client.command()
async def undeny(ctx, member: discord.Member):
    if client.deniedMembers is not None and member == in client.deniedMembers and client.channelowner.id == ctx.author.id:
        client.deniedMembers.remove(member)
        channel = client.get_channel(440687280907354113)
        await channel.send("Allowed access to " + member.mention + " to " + ctx.author.mention + "'s channel!")
    elif member != client.deniedMembers:
        await channel.send(member.mention + " was never denied!")
    elif client.channelowner.id =! ctx.author.id:
        await channel.send("You are not the owner of this channel!")
""""""
client.run("NDM3NDgxNzkxMTE3MzI4Mzk1.DcP8TQ.6iCLEPGYYMzt8ZfQxlIBjy-pJ60")
