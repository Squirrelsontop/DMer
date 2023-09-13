import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()
token = os.getenv("token")

spam_message = ""

activity = discord.CustomActivity(name='bomber')

class Bot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True 
    super().__init__(command_prefix = ".", intents = intents, activity=activity)    
bot = Bot()

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


bot.run(token)
