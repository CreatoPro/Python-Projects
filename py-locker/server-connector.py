import discord
import subprocess

import pyautogui as pg


failsafe = pg.PAUSE = 1 




pg.FAILSAFE = False
# Discord bot token
TOKEN = ''

# Command prefix
COMMAND_PREFIX = '!'

intents = discord.Intents.default()
intents.message_content = True  # Add this line if you want to access message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message author is not a bot and the message starts with the command prefix
    if not message.author.bot and message.content.startswith(COMMAND_PREFIX):
        # Extract the command and arguments from the message content
        command, *args = message.content[len(COMMAND_PREFIX):].split()
        
        # Check if the command is '!lock'
        if command == 'lock':
            # Execute the Python script named 'example.py' located in the same directory as this script
            try:
                result = subprocess.run(['python', 'pc-locker.py'], capture_output=True, text=True)
                print("Locked Your PC is safe")
                pg.click(x=32, y=1054)
                failsafe
                pg.click(x=139, y=988)
                failsafe
                pg.click(x=130, y=914)
                failsafe
                pg.click()
                output = result.stdout.strip() if result.stdout else result.stderr.strip()
                await message.channel.send(f'Locked Your PC My Buddy')
            except FileNotFoundError:
                await message.channel.send('Python interpreter not found.')
            except Exception as e:
                await message.channel.send(f'An error occurred: {e}')

# Run the Discord bot
client.run(TOKEN)
