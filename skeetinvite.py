@BetterGhost.command(name="skeetinvite", description="Generates a fake skeet invite", usage="skeetinvite")
async def fakeskeet(ctx, url: str):
        
        if url is not None:
            letters_and_digits = string.ascii_letters + string.digits
            fake_skeet_code = ''.join((random.choice(letters_and_digits) for i in range(32)))

            embed= discord.Embed(color=0x5FC312, title=f'Successfully Generated Skeet Invite', description=
            f'''
            Successfully generated Skeet Invite...
            To redeem click the link.
            **Invite URL:** [https://gamesense.pub/forums/register.php?invite={fake_skeet_code}]({url})
            ''', 
            )
            await ctx.send(embed=embed)