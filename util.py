import os
import csv
import discord
import random

def antagonizeUser(message, data_file, users):

    if str(message.author) not in users:
        return

    msg = ""
    if os.path.exists(data_file) is True:
        with open(data_file, "r") as tmp_file:
            reader = csv.DictReader(tmp_file)
            values = []
            for row in reader:
                values = row

        if values["Counter"] >= values["Limit"]:
            msg = 'shut up {0.mention}'.format(message.author)
            os.remove(data_file)
            return msg

        else:
            new_count = int(values["Counter"])
            new_count += 1
            values.update({"Counter": new_count})

            with open(data_file, "w") as tmp_file:
                cols = ["Counter", "Limit"]
                writer = csv.DictWriter(tmp_file, fieldnames=cols)
                writer.writeheader()
                writer.writerow(values)

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
        return msg
