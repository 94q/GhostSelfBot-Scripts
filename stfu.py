stfuPeople = [] # Put your user id here.
stfuMessages = ["taci", "taci in mortii mei de caine"] # You can change these to what ever u want.


@BetterGhost.command(name="addstfu", description="Add a user to the auto stfu list.", usage="addstfu (@user/id)")
async def addstfu(ctx, user: discord.User):
    global sftuPeople
    stfuPeople.append(user.id)
    print_info(f"Added {user} to the auto stfu list.")
    await ctx.send(f"Added `{user}` to the auto stfu list.")


@BetterGhost.command(name="removestfu", description="Remove a user from the auto stfu list.", usage="removestfu (@user/id)",
               aliases=["remstfu", "delstfu", "deletstfu"])
async def removestfu(ctx, user: discord.User):
    global stfuPeople
    stfuPeople.remove(user.id)
    print_info(f"Removed {user} from the auto stfu list.")
    await ctx.send(f"Removed `{user}` from the auto stfu list.")


@BetterGhost.listen()
async def on_message(message):
    global stfuPeople, stfuMessages
    if message.author.id in stfuPeople:
        try:
            await message.reply(random.choice(stfuMessages))
        except:
            pass
        try:
            print_info(f"Replied to {message.author} in {message.guild} because theyre annoying.")
        except:
            print_info(f"Replied to {message.author} because theyre annoying.")
