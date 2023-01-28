import discord
import responses

# async is going to send a message to the current channel or the user
async def send_message(message, user_message, is_private):
    try:
        # Here we are going to insert the user message to the responses.py and get a 
        # BotResponse and save it in response.
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA2ODk5NTY4MDc0OTc2ODc2Nw.GFEp_L.qAdGeG8pRBKJMbhoyQxk0Axe8TZGWJlOyVRXBM'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        #this ensures that the bot doesn't read it own message and respond to it 
        #causing an infinite loop
        if message.author == client.user:
            return 
        
        #get the information from the user 
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #this is for debugging purposes
        print(f"{username} said: '{user_message}' ({channel})")

        #this checks whether the use typed a message with question mark 
        # this means that you want to have the response sent in private.
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)


