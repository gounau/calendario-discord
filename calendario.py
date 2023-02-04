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

    message_lower = message.content.lower()
    if not any(keyword in message_lower for keyword in ["quando sair o anime", "que horas sair"]):
        return

    anime = message.content.split("quando sair o anime")[1].strip() if "quando sair o anime" in message_lower else message.content.split("que horas sair")[1].strip()
    anime = anime.strip()
    response = f"Desculpe @{message.author.mention}, não tenho informações sobre o anime '{anime}'"
    if anime in anime_schedule:
        response = f"@{message.author.mention} Novo episódio de {anime} sairá {anime_schedule[anime]}."
    await message.channel.send(response)

client.run('YOUR TOKEN')
