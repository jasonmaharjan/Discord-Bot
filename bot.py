import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DISCORD_BOT_TOKEN"))


async def send_message(message, user_sent_message, is_private):
    try:
        response = responses.handle_responses(user_sent_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print("Exception occured:", e)


def run_discord_bot():
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")

    if TOKEN is not None:

        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():  # Bot is started
            print(f'{client.user} is now running!!!')

        @client.event
        async def on_message(message):  # Bot accepting messages sent from users
            # Avoid infinite loop (bots may rise)
            if message.author == client.user:
                return

            username = str(message.author)

            user_sent_message = str(message.content)

            print(f'\n{username} is sending a request >> {user_sent_message}\n')

            await send_message(message, user_sent_message, is_private=False)

        client.run(TOKEN)

    else:
        print("DISCORD TOKEN NOT FOUND!")
