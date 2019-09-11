import discord
# import pyodbc
import csv
import datetime
import os
import random

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

def antagonizeUser(message, data_file):
    msg = ""
    if os.path.exists(data_file) is True:
        with open(data_file, "r") as tmp_file:
            reader = csv.DictReader(tmp_file)
            values = reader.

        print(values)
        counter = values[0]
        limit = values[1]
        with open(data_file, "w") as tmp_file:
            cols = ["Counter", "Limit"]
            writer = csv.DictWriter(tmp_file, fieldnames=cols)
            if counter >= limit:
                msg = 'shut up matt'
                msg = msg.format(message)
                channel = message.channel
                return msg
                #await channel.send(msg)
            else:
                values[0] = counter + 1
                writer = csv.DictWriter(tmp_file)
                writer.writerow(values)
                print("counted")

            tmp_file.close()

    else:
        cols = ["Counter", "Limit"]
        values = [1, random.randint(1, 50)]
        with open(data_file, "w", newline='') as tmp_file:
            writer = csv.DictWriter(tmp_file, fieldnames=cols)
            writer.writeheader()
            writer.writerow({"Counter": values[0], "Limit": values[1]})

        tmp_file.close()
        msg = ""
        print("new file created")
        return msg
