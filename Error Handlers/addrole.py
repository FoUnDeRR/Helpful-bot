@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Administrator` Permissions!**")
