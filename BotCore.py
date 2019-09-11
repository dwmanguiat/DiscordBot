import discord
import json
import HighlightBot as hb
import util


client = discord.Client()

@client.event
async def on_message(message):

    # stops bot from replying to self
    if message.author == client.user:
        return

    msg = util.antagonizeUser(message, config["Message Counter"], ["mschlehr#5056", "RottenAirplane#5943"])
    if msg:
        channel = message.channel
        msg.format(message)
        await channel.send(str(msg))
    else:
        return

    if str(message.channel) in config["Channels"]:
    
        hb.logEmbeds(message, config["Embed Logging csv"])

    else:
        return



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print("Config file loaded")
    print('------')


def get_config(path):
    config_dict = {}
    with open(path) as json_file:
        config_dict = json.loads(json_file.read())
    return config_dict


def main():
    global config
    config = get_config("config.json")
    client.run(config["Token"])


if __name__ == "__main__":
    main()


