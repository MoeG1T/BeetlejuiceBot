# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
import os
from discord.ext import commands, tasks
import random
import json


BeetStatus = ["Cuppa War", "CUPPA WARZONE", "Howerd Stern Simulator", "Boxing Champs", 
"UFC 4", "Cuppa Killa", "Modern Cuppa Warfare", "Anime Princess Palace 2", "BEET EXILES", "DOD", "Finding Mario Judah"]

Greetings = ["Morning", "Hello", "Hi", "Hola", "hi", "Good Day", "Good Morning", "Hey Sir", "Hey Ma'am", "Ahoy Captain"]

Token = os.environ.get('SECRET_TOKEN')

if __name__ == "__main__":

     def get_prefix(client, message):
          with open("Prefixes.json", "r") as f:
               prefixes = json.load(f)

          if (str(message.guild.id) in prefixes):
               return prefixes[str(message.guild.id)]

          else:
               prefixes[str(message.guild.id)] = '!'

               with open("Prefixes.json", 'w') as w:
                    json.dump(prefixes, w, indent = 4)
               
               return prefixes[str(message.guild.id)]

     client = commands.Bot(command_prefix = get_prefix)

     @client.event
     async def on_guild_join(guild):
          with open("Prefixes.json", "r") as f:
               prefixes = json.load(f)
          
          prefixes[str(guild.id)] = '!'

          with open("Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)

     @client.event
     async def on_guild_remove(guild):
          with open("Prefixes.json", 'r') as f:
               prefixes = json.load(f)
          
          prefixes.pop(str(guild.id))

          with open("Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)
               
     @client.event
     async def on_ready():
          change_game_status.start()
          Beet_Messages.start()
          print("Cuppa Army General At Your Service")

     @tasks.loop(minutes=120)
     async def Beet_Messages():
          try:
               for guild in client.guilds:
                    for channel in guild.channels:
                         if str(channel) == "general":
                              with open("BeetRandomMsgz.txt","r") as f:
                                   await channel.send(random.choice(f.read().splitlines()))
          except (OSError, IOError) as e:
               print(e)

     @client.event
     async def on_messages(message):
          try:
               if message.author == client.user:
                    return
                    
               if any(word in message.content for word in Greetings):
                    await message.channel.send(random.choice(Greetings))

     @tasks.loop(minutes = 400)
     async def change_game_status():
          await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(BeetStatus)))
             
     @client.event
     async def on_command_error(ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.send("More Info Needed")

          elif isinstance(error, commands.MissingPermissions):
               await ctx.send("Only Cuppa Generals Do This")
          
          elif isinstance(error, commands.CommandNotFound):
               await ctx.send("Command Doesn't Exist Pal")


     for filename in os.listdir('./cogs'):
          if filename.endswith('.py'):
               client.load_extension(f'cogs.{filename[:-3]}')
     

     client.run(Token)

