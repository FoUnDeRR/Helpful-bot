@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, member : discord.Member, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'{member} was unbanned!', delete_after=5)
