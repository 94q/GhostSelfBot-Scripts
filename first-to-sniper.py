#Version 1.5

# +---------------------------------------------------------------------------------------+
# | Script made by 5mf, if you want more blacklisted servers, add more IDs to the list |
# +---------------------------------------------------------------------------------------+

@BetterGhost.listen()
async def on_message(message):
    # +---------------------------------------------------------------------------------------+
    BlacklistedServers = [123,456,789] #Here add or change the blacklisted server ids
    FirstMlist = ['hi.','Hello.','Hi.']
    SecondTList = ['Am i the first one?','Am i the first to dm you?','Did i dm you first?',"Can you tell me if i am the first one please?","Am i the first one sir?","Did i win?","Who won?","Did i won?","Can you tell me who won?","Who dm'ed you first?","Did i win this?"] #add more if you want
    secondT = True #set this to True/False if you want to ask him after a few seconds a random message from the list
    PingHost = False # set this to True/False if you want to ping the message author in dm
    # +---------------------------------------------------------------------------------------+
    if message.guild.id not in BlacklistedServers:
        if 'first to dm' in message.content.lower() or 'dm me first' in message.content.lower() or 'first one to dm' in message.content.lower() or 'first to msg' in message.content.lower() or 'first one to msg' in message.content.lower() or 'first to message' in message.content.lower() or 'first one to message' in message.content.lower() or 'msg me first' in message.content.lower() or 'message me first' in message.content.lower():
            if 'ban' in message.content.lower() or 'kick' in message.content.lower() or 'selfbot' in message.content.lower() or 'warn' in message.content.lower():
                print_info(f"[First To Sniper] Avoided getting banned. (the message had the banished words in it). Original message: {message.content}")
                pass
            else:
                host = message.author
                dm = await host.create_dm()

                if PingHost == True:
                    if secondT == True:
                        await dm.send(f'{host.mention} {random.choice(FirstMlist)} {random.choice(SecondTList)}')
                    else:
                        await dm.send(f'{host.mention} {random.choice(FirstMlist)}')
                else:
                    if secondT == True:
                        await dm.send(f'{random.choice(FirstMlist)} {random.choice(SecondTList)}')
                    else:
                        await dm.send(f'{random.choice(FirstMlist)}')

                print_info(f"[First To Sniper] Sniped a first to giveaway. Original message was sent by {host.name} with the text : {message.content}")