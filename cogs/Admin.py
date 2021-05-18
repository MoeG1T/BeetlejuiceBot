# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import json

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True, manage_roles=True)  
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(administrator=True, manage_roles=True)  
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        memberName, memberDisc = member.split("#")

        for banned in banned_users:
            user = banned.user
            
            if(user.name, user.discriminator) == (memberName, memberDisc):
                await ctx.guild.unban(user)
                await ctx.send(f'Allowed Back to Cuppa Army {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ChangePrefix(self, ctx, prefix):
        with open("Data\Prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("Data\Prefixes.json", 'w') as w:
            json.dump(prefixes, w, indent = 4)
        
        await ctx.send("Prefix Changed")

def setup(client):
    client.add_cog(Admin(client))
