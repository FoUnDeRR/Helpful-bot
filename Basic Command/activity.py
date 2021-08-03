async def ch_pr():
    await client.wait_until_ready()


    statuses = ["Nothing :D", f" {len(client.guilds)} servers | #help", "discord.py"]

    while not client.is_closed():

        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name="Discord"))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=("Discord Wumpus")))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers | >help"))
        
        await asyncio.sleep(10)
        
client.loop.create_task(ch_pr())
