import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = "&")

@client.event
async def on_ready():
    print ("Bot Loaded...")

class CustomVC:
    @client.event
    async def on_voice_state_update(member, before, after):
        channelID = 440255311949987849
        categoryID = 440255201828536320
        if after.channel.id == channelID:
            global newChannel
            newChannel = await member.guild.create_voice_channel('Rename Me!', category=client.get_channel(categoryID))
            await member.move_to(newChannel)
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            await newChannel.set_permissions(member, overwrite=overwrite)
        elif before.channel.id == newChannel.id and after.channel.id != newChannel.id and newChannel.members == []:
            await discord.VoiceChannel.delete(newChannel)
    @client.event
    async def on_message(message):
        if message.content.upper().startswith
        
client.run("NDM3NDgxNzkxMTE3MzI4Mzk1.DcP8TQ.6iCLEPGYYMzt8ZfQxlIBjy-pJ60")
