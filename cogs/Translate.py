# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import googletrans
from googletrans import Translator
import json


class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def translate(self, ctx, lang, *, args):
        if lang not in googletrans.LANGUAGES and lang not in googletrans.LANGCODES:
            await ctx.send("Make sure it is something like [!translate fr hello]")
        
        translator = Translator()
        translated = translator.translate(args, dest = lang)

        await ctx.send(translated.text)


    def encrypt(self, message):
        
        with open("Data/Morse.json", "r") as f:
            MORSE_CODE = json.load(f)
        
        Morse = ''
        for letter in message:
            if letter != ' ':
                Morse += MORSE_CODE[letter] + ' '
            else:
                #space between morse letters
                Morse += ' / '
  
        return Morse

    @commands.command()
    async def EnglishToMorse(self, ctx, *, english):
        invalid = False
        english = english.upper()
        for letter in english:
            if letter.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ()?/,.1234567890- ":
                invalid = True
        if(invalid):
            raise commands.BadArgument
        else:
            await ctx.send(self.encrypt(english))
           

def setup(client):
    client.add_cog(Translate(client))