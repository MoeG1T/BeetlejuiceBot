# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
import os
from discord.ext import commands, tasks
import random
import json


BeetStatus = ["Cuppa War", "KFC WARZONE", "Howerd Stern Simulator", "Boxing Champs", 
"UFC 4", "Cuppa Killa", "Modern Cuppa Warfare", "Anime Princess Palace 2", "BEET EXILES", "DOD", "Finding Mario Judah"]

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
          print("Cuppa Army General At Your Service")

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

