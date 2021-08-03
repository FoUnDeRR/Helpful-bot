@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, member : discord.Member, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'{member} was unbanned!', delete_after=5)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Administrator` Permissions!**")
