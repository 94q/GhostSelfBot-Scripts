@BetterGhost.command()
async def discordroulette(ctx):
    await ctx.message.delete()
    roulette = random.randint(0, 6)
    if roulette == 1:
        await ctx.send(f'Hey guys did you know my token is {__token__} (sent by discordroulette)')
    if roulette != 1:
        await ctx.send('You dont get my token today :)')
