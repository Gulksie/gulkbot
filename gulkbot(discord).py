'''Just a simple bot i coded for my friend's discord. See helptext for commands and creds for credits.
Feel free to modfy this if you want, but please give give me some credit. See contact in helptext for contact info'''


import re, discord, random, asyncio, logging
from time import sleep

logging.basicConfig(level=logging.INFO) #sets up logging

client = discord.Client() #does stuff idrk what

scramble = False #so only one scramble can happen at a time

na = '''Hey, you can't do that!
Do %help to see everything you can do.'''

helptext = '''Gulkbot Help

Currently, the commands for Gulkbot are:

%ping - Sends you a "Pong!" back
%scramble - A simple word scrambler. Scrambles one of 50 messages and tells you it.
%unscramble - Guess what the scrambled word was from %scramble. Only usable if there is an ongoing scramble.
%nickberghasalargewilly - Does he?
%spam - Spams a message. Format is:
%spam [amount to spam(Min 1 Max 20)] [message(Up to 50 charicters)]
%google - Googles whatever is after %google.
%say - Says whatever you tell it to
%help - I think you know what this is...''' #gets pmed upon request with %help

creds = '''Gulkbot Credits

Made by Gulk in Python 3.6.0 (python.org) and discord.py(github.com/Rapptz/discord.py).
I had nothing to do with the making of discord.py, and discord.py is Copyright (c) 2015-2016 Rapptz.
Discord.py docs - discordpy.readthedocs.io/en/latest/api.html

CONTACT:
Gulk - gulkyt@outlook.com
Rapptz - github.com/Rapptz or stackoverflow.com/users/1381108/rapptz
Python - python.org/about/help/''' #gets pmed upon request with %credits

googlelink = 'http://www.google.com/search?q=' #basis for google search link in %google
counter = 0 #counter for counter things


#words for scrambler
words = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day', 'eye', 'fact', 'family', 'government', 'group', 'hand', 'home', 'job', 'life', 'lot', 'man', 'money', 'month', 'mother', 'Mr', 'night', 'number', 'part', 'people', 'place', 'point', 'problem', 'program', 'question', 'right', 'room', 'school', 'state', 'story', 'student', 'study', 'system', 'thing', 'time', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']

@client.event
async def on_ready(): #logs in client
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        
                

@client.event
async def on_message(message):
        global counter
        #fun counter
        counter += 1
        if counter ==250:
                client.send_message(message.channel, 'I have a rather large penis.')
        #%scramble
        #scrambles word and outputs to chat if %scramble is sent
        if not scramble and message.content.startswith('%scramble'):
                while True:
                        word = words[random.randint(1, 50)]
                        word_s = ''.join(random.sample(word, len(word)))
                        if word == word_s:
                                continue
                        else:
                                break
                await client.send_message(message.channel, 'Unscramble the word ' + word_s + ' with %unscramble [word], or %giveup to give up.')
                while True: #waits for a %unscramble with the right peramiters then checks if it is the same as word above and outputs if it is or not
                        unscr = await client.wait_for_message(author=message.author, channel=message.channel)
                        if unscr.content.startswith('%unscramble'):
                                unscr = unscr.content.split()
                                if len(unscr) != 2:
                                        await client.send_message(message.channel, na + '\n You are still going. Type %giveup to give up.')
                                else:
                                        unscr = unscr[1]
                                        break
                        elif unscr.content.startswith('%giveup'):
                                await client.send_message(message.channel, 'You gave up. RIP.\nThe word was ' + word +', by the way.')
                                return
                if unscr == word:
                        await client.send_message(message.channel, 'You got the word! Type %scramble to go again.')
                else:
                        await client.send_message(message.channel, 'Aww, that guess was wrong. The word was ' + word + '. Type %scramble to go again.')


        #%ping
        #returns pong if %ping is sent in chat
        elif message.content.startswith('%ping'):
                await client.send_message(message.channel, 'Pong!')


        #%lucahasasmallwilly
        #sends luca has a small willy if %lucahasasmallwilly is sent
        elif message.content.startswith('%nickberghasalargewilly'):
                await client.send_message(message.channel, 'I agree.')
                sleep(3)
                for i in range(5):
                        await client.send_message(message.channel, '<@!280810526366498816> has a large willy')


        #%spam
        #Outputs a spam of what is sent in chat if message starts with %scramble and message only contains 3 peramiters and peramiters are correct
        elif message.content.startswith('%spam'):
                message_ = message.content.split()
                if len(message_) != 3 or not message_[1].isdigit() or not len(message_[2]) in range(20) or not int(message_[1]) in range(1, 21):
                        await client.send_message(message.channel, na)
                else:
                        for i in range(int(message_[1])):
                                await client.send_message(message.channel, message_[2])


        #%google
        #googles message when requested with %google
        elif message.content.startswith('%google'):
                message_ = message.content.split()
                googlelink_ = googlelink + message_[1]
                message_ = message_[2:]
                for word in message_:
                        googlelink_ = googlelink_ + '+' + word
                await client.send_message(message.channel, googlelink_)


        #%help
        #Sends help (helptext) to user when requested with %help
        elif message.content.startswith('%help'):
                await client.send_message(message.author, helptext)
                await client.send_message(message.channel, message.author.mention + ', check your PMs.')


        #%credits
        #sends credits to user when requested with %credits
        elif message.content.startswith('%credits'):
                await client.send_message(message.author, creds)
                await client.send_message(message.channel, message.author.mention + ', check your PMs.')


        #%say
        #says in chat whatever it is told to with %say
        elif message.content.startswith('%say'):
                await client.send_message(message.channel, ''.join(list(message.content)[5:]))
                await client.delete_message(message)


        #%die
        #closes program if I (and only i, you can edit this by changing the id to your id) tell it to
        elif message.content.startswith('%die') and message.author.id == '232230909363879939':  #replace the two 232230909363879939s with whoever you want to be able to kill the bot. get this number by doing \@[username]
                await client.send_message(message.channel, '<@!232230909363879939> killed me. Ow')
                await client.logout()
                print('Logged out.')


client.run('YOUR BOT TOKEN HERE') 
