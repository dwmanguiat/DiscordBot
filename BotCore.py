import discord
import json
import HighlightBot as hb


client = discord.Client()


@client.event
async def on_message(message):

    # stops bot from replying to self
    if message.author == client.user:
        return

    if str(message.author) == "dmango#4247":

        msg = hb.antagonizeUser(message, config["Message Counter"])
        if msg != "":
            await message.channel.send(msg)

    if str(message.channel) in config["Channels"]:
    
        hb.logEmbeds(message, config["Embed Logging csv"])

    else:
        print('message out of channel')



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


