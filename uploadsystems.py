@BetterGhost.command()
async def generateinviteupload(ctx):
    def id_generator(size=40, chars=string.ascii_lowercase[0:6] + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    await ctx.message.delete()
    avatar_embed = discord.Embed(color = discord.Colour(0xFF0000),title = f'Enjoy Upload.Systems!!', description=f'Here is your invite {ctx.message.author.mention} : {id_generator()}')
    await ctx.send(embed=avatar_embed)