@BetterGhost.command(name="floppa", description="Random floppa images.", usage="floppa")
async def floppa(BetterGhost):
    request = requests.get(f"https://www.reddit.com/r/bigfloppa/random.json", headers={'User-agent': get_random_user_agent()}).json()
    url = request[0]["data"]["children"][0]["data"]["url"]

    if not url.startswith("https://v.redd"):
        embed = discord.Embed(title="floppa", color=__embedcolour__)
        embed.set_image(url=url)
        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
        embed.timestamp = datetime.now()

        await BetterGhost.send(embed=embed)

    else:
        await BetterGhost.send(url)