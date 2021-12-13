@BetterGhost.command()
async def proxyscrape(ctx):
    embed = discord.Embed(title="All Proxies Available")
    embed.add_field(name=f"{__prefix__}help", value="Displays all available commands", inline=False)
    embed.add_field(name=f"{__prefix__}http", value="Sends fresh http proxy list", inline=False)
    embed.add_field(name=f"{__prefix__}https", value="Sends fresh https proxy list", inline=False)
    embed.add_field(name=f"{__prefix__}socks4", value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name=f"{__prefix__}socks5", value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name=f"{__prefix__}all", value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    await ctx.send(embed=embed)

@BetterGhost.command()
async def http(ctx):
    f = open("data/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=discord.File("data/http-proxies.txt"))

@BetterGhost.command()
async def https(ctx):
    f = open("data/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=discord.File("data/https-proxies.txt"))

@BetterGhost.command()
async def socks4(ctx):
    f = open("data/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=discord.File("data/socks4-proxies.txt"))

@BetterGhost.command()
async def socks5(ctx):
    f = open("data/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=discord.File("data/socks5-proxies.txt"))

@BetterGhost.command()
async def all(ctx):
    f = open("data/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=discord.File("data/all-proxies.txt"))