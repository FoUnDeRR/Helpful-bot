@client.command(pass_content=True)
async def nick(ctx, member: discord.Member, nick):
    embed = discord.Embed(
        color= discord.Colour.dark_teal()
    )
    embed.add_field(name="Changes", value=f'**Nickname was `changed` for** {member.mention}!')
    await member.edit(nick=nick)
    await ctx.send(embed=embed)
