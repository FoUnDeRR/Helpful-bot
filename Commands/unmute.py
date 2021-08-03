@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    embed = discord.Embed(
        
    )
    embed.add_field(name=' :speaker: | UNMUTE', value=f'**{member.mention} You were unmuted in the server.** **`{ctx.guild.name}`**')

    await member.remove_roles(mutedRole)
    await ctx.send(embed=embed)
