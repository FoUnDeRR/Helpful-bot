@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "**No reason provided**"):
    await member.send("You have been kicked from the Bots Tryout Server, Because:"+reason)
    await member.kick(reason=reason)
