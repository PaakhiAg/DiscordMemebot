import discord
import requests
import json
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()


# Function to get a random meme
def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data["url"]


# Discord bot client
class MyClient(discord.Client):

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):

        # Prevent the bot from replying to itself
        if message.author == self.user:
            return

        # Hello command
        if message.content.startswith("$hello"):
            await message.channel.send("Hello World!")

        # Meme command
        if message.content.startswith("$meme"):
            meme_url = get_meme()
            print("Sending meme:", meme_url)
            await message.channel.send(meme_url)


# Discord intents
intents = discord.Intents.default()
intents.message_content = True


# Start the bot
client = MyClient(intents=intents)

client.run(os.getenv("DISCORD_TOKEN"))