import discord
import asyncio
import string

email = ('') #your discord account email id
password = ('') #your discord account passwd
channel = discord.Object(id='') #your user id

prefix = '^' #prefix of the bot in the server

# Don't touch these variables
inputString = ''
scratching = False

print('\nIntializing . . .')
client = discord.Client()

async def commandHandler():
        scratching = False
        while not client.is_closed:
            inputString = input('> ')
            if inputString == 'scratch' and scratching == False:
                print('Starting scratch card loop')
                scratching = True
                await scratch()
            elif inputString == 'scratch' and scratching == True:
                print('Stopping scratch card loop')
                scratching = False

#can be customised according to different bots
async def run():
        await client.wait_until_ready()
        print('\nLOGGED IN SUCCESSFULLY')
        while not client.is_closed:
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                botMessage = await client.send_message(channel, prefix + 'work')
                print('Sent: ' + prefix + 'work')
                await asyncio.sleep(300)
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                await asyncio.sleep(300)
                botMessage = await client.send_message(channel, prefix + 'tip')
                print('Sent: ' + prefix + 'tip')
                botMessage = await client.send_message(channel, prefix + 'work')
                print('Sent: ' + prefix + 'work')

async def scratch():
        while not client.is_closed:
            if (scratching == False):
                return
            else:
                botMessage = await client.send_message(channel, prefix + 'scratch')
                print('Sent: ' + prefix + 'scratch')
                await asyncio.sleep(8)

client.loop.create_task(run())
client.run(email,password) #2fa should be disabled!

