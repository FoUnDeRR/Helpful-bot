@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f'{member} Avatar')
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
