@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "**No reason provided**"):
    await ctx.send(member.name + "You have been banned from the Bots Tryout Server, Because:"+reason)
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Ban Members` Permissions!**")
