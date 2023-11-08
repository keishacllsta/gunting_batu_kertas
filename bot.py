import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("bot siap digunakan!")
    print("-------------------")

@client.command()
async def play(ctx, choice):
    choices = ['batu', 'kertas', 'gunting']
    bot_choice = random.choice(choices)

    if choice.lower() in choices:
        if choice.lower() == bot_choice:
            result = f"Permainan seri, bot memilih {bot_choice}."
        elif (
            (choice.lower() == 'batu' and bot_choice == 'gunting')
            or (choice.lower() == 'gunting' and bot_choice == 'kertas')
            or (choice.lower() == 'kertas' and bot_choice == 'batu')
        ):
            result = f"Kamu menang! Bot memilih{bot_choice}."
        else:
            result = f"Bot menang! Bot memilih {bot_choice}."
    else:
        result = "Pilihan tidak diketahui. Silahkan pilih 'batu', 'gunting', atau 'kertas'."

    await ctx.send(result)

client.run('MTE3MTc1MDA5MjE3MzIyNjA2NA.G9yBEz.cM00sjdFCLkeN_0DJCkMIR356p66uDElbYgZX8')
# MTE3MTY5MjAxNzU5Njc4MDYxNQ.GwX0US.tOkvW5iFH1xhhf3PQK3gwsXQvKZj4-UYbfUY2w