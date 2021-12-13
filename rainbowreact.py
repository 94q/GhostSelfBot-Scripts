@BetterGhost.command(name="rainbowreact", description="Create a rainbow reaction.", usage="rainbowreact [message id]", aliases=["rainbowreaction"])
async def rainbowreact(ctx, messageid:int):
    message = await get_message(ctx, messageid)
    emojis = ["\U0001F7E5", "\U0001F7E7", "\U0001F7E8", "\U0001F7E9", "\U0001F7E6", "\U0001F7EA"]
    for _ in range(3):
        for emoji in emojis: 
            await message.add_reaction(emoji)
            await asyncio.sleep(1)
            await message.remove_reaction(emoji, ctx.author)
