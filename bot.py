import discord
import requests
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get bot token
TOKEN = os.getenv("DC_TOKEN")

# Check if the token is loaded correctly
if TOKEN is None:
    raise ValueError("❌ API_TOKEN is not set! Check your .env file.")

print(f"✅ Loaded Token: {TOKEN[:5]}********")  # Print only the first few characters for security

# Discord bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Replace with your actual channel ID
CHANNEL_ID = 1351770980384636928  
COIN_ID = "bitcoin"  # Change to another coin like "ethereum" if needed
CURRENCY = "usd"

async def update_channel_name():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            # Fetch price from CoinGecko API
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies={CURRENCY}"
            response = requests.get(url)
            data = response.json()
            price = data[COIN_ID][CURRENCY]

            # Get the channel and update its name
            channel = client.get_channel(CHANNEL_ID)
            if channel:
                new_name = f"BTC: ${price}"  # Example format
                await channel.edit(name=new_name)
                print(f"✅ Updated channel name to: {new_name}")
            else:
                print("❌ Channel not found!")

        except Exception as e:
            print(f"⚠️ Error: {e}")

        await asyncio.sleep(300)  # Update every 5 minutes

@client.event
async def on_ready():
    print(f"🚀 Logged in as {client.user}")
    client.loop.create_task(update_channel_name())

# Run the bot
client.run(TOKEN)
