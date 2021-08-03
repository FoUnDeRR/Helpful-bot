@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Ban Members` Permissions!**")
