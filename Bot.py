# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
import os
from discord.ext import commands, tasks
import random
import json
import time


BeetStatus = ["Cuppa War", "CUPPA WARZONE", "Howerd Stern Simulator", "Boxing Champs", 
"UFC 4", "Cuppa Killa", "Modern Cuppa Warfare", "Anime Princess Palace 2", "BEET EXILES", "DOD", "Finding Mario Judah"]

Greetings = ["Morning", "Hello", "Hi", "Hola", "Good Day", "Good Morning", "Hey Sir", "Hey Ma'am", "Ahoy Captain", "Hey Champ", "Hey", "What's Gucci"]

GoodByes = ["Ciao", "Adios", "Goodbye", "Bye", "See ya", "cya", "Take Care"]

Token = os.environ.get('SECRET_TOKEN')

def get_prefix(client, message):
     with open("Data\Prefixes.json", "r") as f:
          prefixes = json.load(f)
     
     if (str(message.guild.id) in prefixes):
          return prefixes[str(message.guild.id)]

     else:
          prefixes[str(message.guild.id)] = '!'

          with open("Data\Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)
               
          return prefixes[str(message.guild.id)]

if __name__ == "__main__":
     

     client = commands.Bot(command_prefix = get_prefix)

     @client.event
     async def on_guild_join(guild):
          with open("Data\Prefixes.json", "r") as f:
               prefixes = json.load(f)
          
          prefixes[str(guild.id)] = '!'

          with open("Data\Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)

     @client.event
     async def on_guild_remove(guild):
          with open("Data\Prefixes.json", 'r') as f:
               prefixes = json.load(f)
          
          prefixes.pop(str(guild.id))

          with open("Data\Prefixes.json", 'w') as w:
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
                              with open("Data\BeetRandomMsgz.txt","r") as f:
                                   await channel.send(random.choice(f.read().splitlines()))
          except (OSError, IOError) as e:
               print(e)

     @client.event
     async def on_message(msg):
          try:
               if msg.content.startswith("!"):
                    await client.process_commands(msg)
                    return

               if msg.author == client.user:
                    return

               if msg.author.bot: 
                    return
                    
               if any(word.lower() in msg.content.lower() for word in Greetings):
                    time.sleep(1)
                    await msg.channel.send(random.choice(Greetings))

               if any(word.lower() in msg.content.lower() for word in GoodByes):
                    time.sleep(1)
                    await msg.channel.send(random.choice(GoodByes))

               swearwords= []
               with open("Data\SwearWords.txt","r") as f:
                    swearwords = f.read().splitlines()

               if any(word in msg.content.lower() for word in swearwords):
                    with open("Data\Replies.txt","r") as w:
                         time.sleep(1)
                         await msg.channel.send(random.choice(w.read().splitlines()))
          
          except (OSError, IOError) as e:
               print(e)
          
          await client.process_commands(msg)
          
     @tasks.loop(minutes = 400)
     async def change_game_status():
          await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(BeetStatus)))
             
     @client.event
     async def on_command_error(ctx, error):
          if isinstance(error, commands.MissingRequiredArgument):
               await ctx.send("More Info Needed")

          elif isinstance(error, commands.MissingPermissions):
               await ctx.send("Only Cuppa Generals Do This Command")
          
          elif isinstance(error, commands.CommandNotFound):
               await ctx.send("Command Doesn't Exist Pal")

          elif isinstance(error, commands.BadArgument):
               await ctx.send("Invalid info provided")

     for filename in os.listdir('./cogs'):
          if filename.endswith('.py'):
               client.load_extension(f'cogs.{filename[:-3]}')
     

     client.run(Token)

