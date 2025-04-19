import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and ready to respond to commands!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print("Error: BOT_TOKEN is not set in the .env file.")