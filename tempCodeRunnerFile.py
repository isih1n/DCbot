
if TOKEN is None:
    raise ValueError("❌ API_TOKEN is not set! Check your .env file.")

print(f"✅ Loaded Token: {TOKEN[:5]}********")  # Print only the first few characters for security

# Discord bot setup
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Replace with your actual channel ID