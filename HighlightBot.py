import discord
# import pyodbc


def hasEmbeds(message):
    if len(message.embeds) > 0:
        return True
    else:
        return False


def logEmbeds(message):

    if hasEmbeds(message) is False:
        return

    for link in message.embeds:
        print(link.url) # placeholder for logging to db


