import discord
import responses
import asyncio


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
        if len(user_message) != 0 and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

# //////////

async def run():
    intents = discord.Intents(members=True)
    client=discord.Client(intents=intents)
    welcomechannel = await client.fetch_channel(1069011685869895730) 

    @client.event
    async def on_ready():
        print('logged in as')
        print(client.user.name)
        print(client.user.id)
        print('-----')
        # Customise the message below to what you want to send new users!
        newUserMessage = """
        You
        can
        put
        your
        multiline
        message
        here!
        """

    @client.event
    async def on_member_join(member):
        print("Recognised that a member called " + member.name + " joined")
        try: 
            await client.send_message(member, newUserMessage)
            print("Sent message to " + member.name)
        except:
            print("Couldn't message " + member.name)
            embed=discord.Embed(
            title="Welcome "+ member.name + "!",
            description="We're so glad you're here!",
            color=discord.Color.green()
        )
            
        role = discord.utils.get(member.server.roles, name="name-of-your-role") #  Gets the member role as a `role` object
        await client.add_roles(member, role) # Gives the role to the user
        print("Added role '" + role.name + "' to " + member.name)

    TOKEN = 'MTA2ODk5NTY4MDc0OTc2ODc2Nw.GFEp_L.qAdGeG8pRBKJMbhoyQxk0Axe8TZGWJlOyVRXBM'



    client.run(TOKEN)

    @client.event
    async def on_member_leave(member):
        print("Recognised that a member called " + member.name + " left")
        embed=discord.Embed(
            title="😢 Goodbye "+member.name+"!",
            description="Until we meet again old friend.", # A description isn't necessary, you can delete this line if you don't want a description.
            color=discord.Color.red() # There are lots of colors, you can check them here: https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
        )


    TOKEN = 'MTA2ODk5NTY4MDc0OTc2ODc2Nw.GFEp_L.qAdGeG8pRBKJMbhoyQxk0Axe8TZGWJlOyVRXBM'



    client.run(TOKEN)


