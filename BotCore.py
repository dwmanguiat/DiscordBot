import discord
import json

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if str(message.channel) == "discord-bot-simulator":
    
        if message.content.startswith('!420'):
            msg = 'blaze it'
            msg = msg.format(message)
            channel = message.channel
            await channel.send(msg)

    else:
        print('message out of channel')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def get_config(path):
    config = {}
    with open(path) as json_file:
        config = json.loads(json_file.read())
    return config


def main():
    config = get_config("config.json")
    client.run(config["Token"])


if __name__ == "__main__":
    main()


