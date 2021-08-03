@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Manage Messages` Permissions!**")
