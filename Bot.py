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
     with open("Data/Prefixes.json", "r") as f:
          prefixes = json.load(f)
     
     if (str(message.guild.id) in prefixes):
          return prefixes[str(message.guild.id)]

     else:
          prefixes[str(message.guild.id)] = '!'

          with open("Data/Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)
               
          return prefixes[str(message.guild.id)]

if __name__ == "__main__":
     
     client = commands.Bot(command_prefix = get_prefix)


     @client.event
     async def on_guild_join(guild):
          with open("Data/Prefixes.json", "r") as f:
               prefixes = json.load(f)
          
          prefixes[str(guild.id)] = '!'

          with open("Data/Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)

     @client.event
     async def on_guild_remove(guild):
          with open("Data/Prefixes.json", 'r') as f:
               prefixes = json.load(f)
          
          prefixes.pop(str(guild.id))

          with open("Data/Prefixes.json", 'w') as w:
               json.dump(prefixes, w, indent = 4)
               
     @client.event
     async def on_ready():
          change_game_status.start()
          Beet_Messages.start()
          print("Cuppa Army General At Your Service")
     
     @tasks.loop(minutes=500)
     async def Beet_Messages():
          try:
               for guild in client.guilds:
                    for channel in guild.channels:
                         if str(channel) == "general":
                              with open("Data/BeetRandomMsgz.txt", "r") as f:
                                   await channel.send(random.choice(f.read().splitlines()))
          
          except (OSError, IOError) as e:
               print(e)

     @client.event
     async def on_message(msg):
          try:
               #dismiss messages with command prefix at the start
               if msg.content.startswith("!"):
                    await client.process_commands(msg)
                    return

               if msg.author == client.user:
                    return

               if msg.author.bot: 
                    return
               
               #detect greeting and reply to them
               if any(word.lower() in msg.content.lower().split() for word in Greetings):
                    time.sleep(1)
                    await msg.channel.send(random.choice(Greetings))
               
               #detects goodbyes
               if any(word.lower() in msg.content.lower().split() for word in GoodByes):
                    time.sleep(1)
                    await msg.channel.send(random.choice(GoodByes))

               swearwords= []
               with open("Data/SwearWords.txt","r") as f:
                    swearwords = f.read().splitlines()
               
               #detect profanity 
               if any(word in msg.content.lower().split() for word in swearwords):
                    with open("Data/Replies.txt","r") as w:
                         time.sleep(1)
                         await msg.channel.send(random.choice(w.read().splitlines()))
          
          except (OSError, IOError) as e:
               print(e)
          
          await client.process_commands(msg)
          
     @tasks.loop(minutes = 400)
     async def change_game_status():
          await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(BeetStatus)))

     #remove default help command
     client.remove_command("help")
     #help command
     @client.group(invoke_without_command = True)
     async def help(ctx):
          embed = discord.Embed(title="Help", description = "Use <command prefix>help <command name> for information on command", color=ctx.author.color)
          embed.add_field(name = "Moderation", value="ChangePrefix"+"\n"+"ban"+"\n"+"unban")
          embed.add_field(name = "Crypto", value="Coin" +"\n"+ "Top10")
          embed.add_field(name = "Football", value="Table" +"\n"+ "TopScorer")
          embed.add_field(name = "Media", value="Youtube" +"\n"+ "Pic")
          embed.add_field(name = "Translate", value="translate" +"\n"+ "MorseToEnglish" +"\n"+ "EnglishToMorse")
          embed.add_field(name = "Wikipedia", value="description" +"\n"+ "infobox")

          await ctx.send(embed=embed)

     @help.command(aliases= ['unban', 'ChangePrefix'])
     async def ban(ctx):
          embed = discord.Embed(title="Ban, Unban, ChangePrefix", description = "Moderation Commands", color=ctx.author.color)
          embed.add_field(name = "ban", value="<prefix>ban <member> [reason]", inline=False)
          embed.add_field(name = "unban", value="<prefix>unban <member>", inline=False)
          embed.add_field(name = "ChangePrefix", value="<prefix>ChangePrefix <new prefix>", inline=False)

          await ctx.send(embed=embed)
     
     @help.command(aliases = ['Top10'])
     async def Coin(ctx):
          embed = discord.Embed(title=" Coin, Top10", description = "Crypto Commands", color=ctx.author.color)
          embed.add_field(name = "Coin", value="<prefix>Coin <coin symbol>", inline=False)
          embed.add_field(name = "Top10", value="<prefix>Top10 ", inline=False)

          await ctx.send(embed=embed)
     
     @help.command(aliases = ['TopScorer'])
     async def Table(ctx):
          embed = discord.Embed(title="Table, TopScorer", description = "Football Commands", color=ctx.author.color)
          embed.add_field(name = "Table", value="<prefix>Table <league>", inline=False)
          embed.add_field(name = "TopScorer", value="<prefix>TopScorer <league>", inline=False)

          await ctx.send(embed=embed)
     
     @help.command(aliases = ['Pic'])
     async def Youtube(ctx):
          embed = discord.Embed(title="Pic, Youtube", description = "Media Commands", color=ctx.author.color)
          embed.add_field(name = "Pic", value="<prefix>Pic <member>", inline=False)
          embed.add_field(name = "Youtube", value="<prefix>Youtube <title>", inline=False)

          await ctx.send(embed=embed)
     
     @help.command(aliases = ['MorseToEnglish', 'EnglishToMorse'])
     async def translate(ctx):
          embed = discord.Embed(title="MorseToEnglish, EnglishToMorse and translate", description = "Translation Commands", color=ctx.author.color)
          embed.add_field(name = "MorseToEnglish", value="<prefix>MorseToEnglish <text>", inline=False)
          embed.add_field(name = "EnglishToMorse", value="<prefix>EnglishToMorse <text>", inline=False)
          embed.add_field(name = "translate", value="<prefix>translate <language abbreviation> <text>", inline=False)

          await ctx.send(embed=embed)
     
     @help.command(aliases = ['infobox'])
     async def description(ctx):
          embed = discord.Embed(title="description and infobox", description = "Wikipedia Commands", color=ctx.author.color)
          embed.add_field(name = "description", value="<prefix>description <title>", inline=False)
          embed.add_field(name = "infobox", value="<prefix>infobox <title>", inline=False)

          await ctx.send(embed=embed)

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

