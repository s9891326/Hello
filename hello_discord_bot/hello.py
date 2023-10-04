import datetime
import re

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# intents
intents = discord.Intents.default()
# intents.message_content = True  # 新增要求讀取訊息權限
# client
guild_id = [1156125035845656638]
client = commands.Bot(command_prefix="%", intents=intents)
# client = discord.Client(intents=intents)


# event 事件處理
@client.event
async def on_ready():
    print(f"「{client.user}」已登入")


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong')
    elif re.findall(f"<@{client.user.id}>", message.content):
        await message.reply("hello")
    elif message.content == "call":
        await message.author.send("私訊給你~ 123")
    await client.process_commands(message)  # 需要加這個 文檔未填寫


@client.event
async def on_message_edit(before, after):
    # await before.channel.send(f'{before.author.mention}修改了訊息!!!')
    embed = discord.Embed(color=0x34495E, timestamp=datetime.datetime.now())
    embed.description = f"{before.author.mention} 在 {before.channel.mention} 編輯了訊息 "
    embed.add_field(
        name="編輯前", value=f"``{before.clean_content}``", inline=False)
    embed.add_field(name="編輯後", value=f"``{after.clean_content}``")
    embed.set_author(name="訊息編輯紀錄")
    guild = client.get_guild(before.guild.id)
    await guild.system_channel.send(embed=embed)


@client.command()
async def hello(ctx, message=""):
    await ctx.send(f"您好w {'您說了' + message if message else ''}")


if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    client.run(DISCORD_TOKEN)
    print(client.all_commands)
