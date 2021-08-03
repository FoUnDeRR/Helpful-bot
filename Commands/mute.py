@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason='No reason provided'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    embed = discord.Embed(

    )
    embed.add_field(name=' :mute: | MUTED', value=f'**{member.mention} You were muted in** **`{ctx.guild.name}`**. **Reason:** `{reason}`'
   
    )
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(embed=embed)
