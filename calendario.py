import discord

client = discord.Client()

# Define a lista de animes e dias da semana
anime_schedule = {
    "Boku no Pico": "Domingo",
    "One Punch Man": "Terça-feira",
    "Death Note": "Quinta-feira"
}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "Quando sair o anime" in message.content:
        anime = message.content.split("Quando sair o anime")[1].strip()
        if anime in anime_schedule:
            response = f"@{message.author.mention} Novo episódio de {anime} sairá {anime_schedule[anime]}."
        else:
            response = "Desculpe @{message.author.mention}, não tenho informações sobre esse anime."
        await message.channel.send(response)

    if "Que horas sair" in message.content:
        anime = message.content.split("Que horas sair")[1].strip()
        if anime in anime_schedule:
            response = f"@{message.author.mention} Novo episódio de {anime} sairá {anime_schedule[anime]}."
        else:
            response = "Desculpe @{message.author.mention}, não tenho informações sobre esse anime."
        await message.channel.send(response)

client.run('YOUR TOKEN')
