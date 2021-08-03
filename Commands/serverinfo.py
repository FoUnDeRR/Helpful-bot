@client.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]

    serverinfoEmbed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name='Owner', value=f"{ctx.guild.name}", inline=True)
    serverinfoEmbed.add_field(name='Name', value=f"**{ctx.guild.name}**", inline=True)
    serverinfoEmbed.add_field(name='Member Count', value=ctx.guild.member_count, inline=True)
    serverinfoEmbed.add_field(name='Verification Level', value=str(ctx.guild.verification_level), inline=True)
    serverinfoEmbed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=True)
    serverinfoEmbed.add_field(name='Number of Roles', value=str(role_count), inline=True)
    serverinfoEmbed.add_field(name='Bots', value=', '.join(list_of_bots), inline=True)
    serverinfoEmbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)


    await ctx.send(embed = serverinfoEmbed)
