@client.command()
async def ping(ctx) :
        embed = discord.Embed(
            color= discord.Colour.dark_teal() # or any color you want
        )
        embed.add_field(name= 'Ping', value= f' :ping_pong:  Pong!! {round (client.latency * 1000)}  ms'),
        await ctx.send(embed=embed)
