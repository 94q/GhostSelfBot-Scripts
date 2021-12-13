@BetterGhost.command()
async def dmall(ctx, *, message):
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"Sending '{message}' to {user} people")
        except:
            pass