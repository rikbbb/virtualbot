import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
        print("Logged in as:")
        print(client.user.name)
        print("ID:")
        print(client.user.id)
        print("Ready to use!")
    
@client.event
async def on_message(message):
    if  message.author == client.user:
        return
    elif message.content.startswith("!test"):
        await client.send_message(message.channel, "bliep bloep bliep, test test test... IK WERK")
    elif message.content.startswith("!ping"):
        await client.send_message(message.channel, "Pong!")
    elif message.content.startswith("!design"):
        await client.send_message(message.channel, "Het beste programma om te designen is natuurlijk photoshop!")
    elif message.content.startswith("!edit"):
        await client.send_message(message.channel, "Het beste edit programma is natuurlijk première pro! (sony vegas is slecht)")
    elif message.content.startswith("!creators"):
        await client.send_message(message.channel, "De makers van deze server zijn @Fervawi en @rikkert. Ze zijn familie en natuurlijk ook goede vrienden. Ze hopen dat jullie op deze server veel plezier gaan hebben en antwoord kunnen krijgen op jullie vragen.")
    elif message.content.startswith("!info fervawi"):
        await client.send_message(message.channel, "Fervawi is een meisje. Ze is 11 jaar en verjaard op 24 november. Haar hobby's zijn ping pongen en designen met photoshop.")
    elif message.content.startswith("!info rikkert"):
        await client.send_message(message.channel, "Rikkert is een jongen. Hij is 14 jaar en verjaard op 29 november. Zijn hobby's zijn scouts, drummen, editen en programmeren.")
    elif message.content.startswith("!photoshop tutorial"):
        await client.send_message(message.channel, "https://www.youtube.com/playlist?list=PLdKPAoA0w8ZTJydkjZZYMWVNjghtaV0d6")
    elif message.content.startswith("!première pro tutorial"):
        await client.send_message(message.channel, "https://www.youtube.com/playlist?list=PLdKPAoA0w8ZSTj1gUAC49Pn540-V6oOcO")
    elif message.content.startswith("!help"):
        await client.send_message(message.channel, "Vraag dit aan me en ik zal antwoorden: !help, !ping, !test, !design, !edit, !creators, !info fervawi, !info rikkert, !photoshop tutorial, !première pro tutorial")
  
client.run("NDkwODQyMzk5MzU5MzY5MjE3.Dn_uWQ.9bftnSw-55WOjFAZC3PTqqeVa2A")
