@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Arguement Has been Detected:** **Missing `Administrator` Permissions!**")
