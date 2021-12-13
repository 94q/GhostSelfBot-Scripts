embedTalkEnabled = False # Put True if u want to have it enabled

@BetterGhost.command(name="embedtalk", description="Enable or disable embed talk.", usage="embedtalk")
async def embedtalk(BetterGhost):
    global embedTalkEnabled
    
    if (not embedTalkEnabled):
        embedTalkEnabled = True
        await BetterGhost.send("From now on every message you send will be replaced with an embed.")
    else:
        embedTalkEnabled = False
        await BetterGhost.send("From now on every message you send will no longer be replaced with an embed.")
        
@BetterGhost.listen()
async def on_message(message):
    if (message.author == BetterGhost.user):
        if (not message.content.startswith(__prefix__)):
            if (embedTalkEnabled):
                if (uwuifyEnabled):
                    message.content = uwuify.uwu(message.content)
                    
                embed = discord.Embed(description=message.content, color=__embedcolour__)
                await message.edit(content="", embed=embed)