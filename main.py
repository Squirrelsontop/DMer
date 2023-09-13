import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()
token = os.getenv("token")

spam_message = ""

activity = discord.CustomActivity(name='first black president')

class Bot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True 
    super().__init__(command_prefix = ".", intents = intents, activity=activity)    
bot = Bot()

@bot.command()
async def dm(ctx, user: discord.User, *, message):
  await ctx.message.delete()
  while True:
    await user.send(message)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


bot.run(token)
