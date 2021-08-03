@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
