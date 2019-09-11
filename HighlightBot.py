import discord
# import pyodbc
import csv
import datetime
import os

def hasEmbeds(message):
    if len(message.embeds) > 0:
        return True
    else:
        return False


def logEmbeds(message, data_file):

    path = os.path.normpath(data_file)
    columns = ["embedURL", "author", "UTC", "channel"]

    if hasEmbeds(message) is False:
        return

    if os.path.exists(path) is False:
        with open(os.path.normpath(data_file), "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, columns)
            writer.writeheader()

        csv_file.close()

    for link in message.embeds:
        with open(os.path.normpath(data_file), "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, columns)
            writer.writerow({'embedURL': link.url, 'author': message.author, 'UTC': datetime.datetime.utcnow(),
                            'channel': message.channel})

        csv_file.close()
