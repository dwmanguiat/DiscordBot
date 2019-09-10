from discord import message
# import pyodbc


def has_embeds(embedsList):
    if len(embedsList) > 0:
        # add shit to db
        print("this message contains embedded links")
        for link in embedsList:
            print(link.url)

    return True
