@client.command()
async def emojify(ctx,*,text):
    emojis = []
    for s in text.lower():
        if s.isdecimal():
            num2emo = {'0':'zero','1':'one','2':'two',
                       '3':'three','4':'four','5':'five',
                       '6':'six','7':'seven','8':'eight','9':'nine'}
            emojis.append(f':{num2emo.get(s)}:')
        elif s.isalpha():
            emojis.append(f':regional_indicator_{s}:')
        else:
            emojis.append(s)
    await ctx.send(' '.join(emojis))
