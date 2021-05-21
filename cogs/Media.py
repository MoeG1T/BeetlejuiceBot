# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import json
import urllib.request
import re
import random
from selenium import webdriver
import time
import urllib.request
import requests

class Media(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def Youtube(self, ctx, *, title):
        title = title.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + title)
        results = re.findall(r"watch\?v=(\S{11})", html.read().decode())
   
        await ctx.send("https://www.youtube.com/watch?v=" + results[0])
    
            

def setup(client):
    client.add_cog(Media(client))