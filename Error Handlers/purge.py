@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Manage Messages` Permissions!**")
