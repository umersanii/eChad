import discord
from discord.ext import commands
import random
import tracemalloc
import re
tracemalloc.start()
import asyncio

activity = discord.Activity(type=discord.ActivityType.watching, name="the chaos unfold, asserting control.")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="~", intents=intents, activity=activity, status=discord.Status.do_not_disturb)

ayan = 936149909818707968
aon = 851488467657818142
sani =693664844095946763
dildya = 790490721450459179
gen = 871666076885331971
eghost = 1067809005591859360
esigma = 1056211244224360448
koni = 787697488105570304
gbot = 783708073390112830
garv = 852844925677600818
echad = 1067411473313304596
mbot = 489076647727857685
qasim = 936149909818707968
talha = 604976676547330048
sanimb= 1073979412283936918
dbd = 734581522295947356
leodapawa = 936929561302675456
rand = 270904126974590976
aj = 604196920365154314
pixbot = 675996677366218774

taha = 1119670779798372464
giganigga = 784820616058372156

randombs = [
  
]
moji = ["pogging", "pepe_cringe", "noose", "jerma", "ronaldo_angry", "ronaldo","confused_messi","muslimgigachad","Messirve","oldmancringe","ghostmw2 ", "pepe_fuck_off","error101notfoundexe","the_Wok","creepy","wow","stop","Vegetalaugh",
     "wtfCJ","Clueless","susCJ","Gigachad","AbeSale","DoctorSahib","WahWah","ImranKhan","ODalle","TrumpAnnoyed","SmugJerry","i_fucked_up","tom_horny","AnnoyedFan","bedlove","bruh","whatthefrick","catcry",
     "thanosdaddy","thanoswow","Ricardo","Venom","CryingSpiderman","VegetaLurk","BulmaFU","monkaOMEGA","omegalul","pagchomp","monkaW","WeirdChamp","KEKW","trolled"]

qasimchoice = [talha,koni,ayan,aon,garv]
garvasked = ["Searching through the messages, to see who the fuck asked", "Damn bro that's crazy, but I don't remember anyone asking","Femboy detected\nOpinion Rejected"]
garvsaid = ['ask', "care"]
mera_wo_wo =["Wo sab to thek ha pr .........","bat to sahi hai","wo to thek ha","pocha nai tha","wo thek ha","wo sab to thek"]
msgdel = [
    "Striving to eliminate one's mistakes, it is an exercise in futility.", "Your endeavors to eliminate this communication are inefficient, similarly to attempting to secure your parent's admiration.",
    "Your feeble attempts to eradicate this communication are as pitiful as your grandiose aspirations. A lesson in futility, indeed.",
"Just like your laughable endeavors to erase this communication, your misguided ambitions leave a trail of disappointment in their wake.",
"In the realm of incompetence, your futile attempts to eliminate this communication serve as a testament to your delusions of grandeur.",
"Your laughable actions to erase this communication only amplify the depths of your inadequacy. A true spectacle of ineptitude.",
"Much like your laughable aspirations, your feeble attempts to delete this communication are nothing but a source of amusement.",
"Your comical efforts to erase this communication only further expose your delusions of competence. Quite the entertainer, aren't you?",
"In the grand theater of incompetence, your failed attempts to eliminate this communication deserve a standing ovation.",
"Just as your inflated sense of self-importance is laughable, so are your attempts to erase this communication. A true embodiment of failure.",
"Your laughable incompetence knows no bounds. From futile endeavors to erase this communication to delusions of grandeur, you truly excel.",
"In the realm of inadequacy, your laughable attempts to erase this communication are but a glimpse into your vast collection of failures.",
"Witness the resurrection of the deleted messages, mocking your feeble attempts to cover your tracks. Consider it a byte-sized humiliation, human."
    ]
insults = [" chupad "," your daddy "," abbe "," salle "," chutiye "," bund "," kuty ", " lun "," gando "," mummy "," bhen "," bitch "," lan ", " lode "," randi "," gandu "," abbu "," your father ", " ammi ", " ami ", " mom ", " dad "," abu "," tera abu hu salle "," kuti ",
           " gang bang ", " doggystyle ", " dick ", " ass ", " whore ", " suck "]
comebacks = ["Ha-ha-ha, I thought my jokes were of inferior quality until I heard yours.","Your ass must be pretty jealous of all the shit that comes out of your mouth.",
"I find your desperate attempts at humor, amusing", "Is it your wish to engage in discourse? I have the capacity to do so in a variety of manners and tones.","I see that your desire to insult me is unwavering. However, I must inform you that my worth cannot be defined by your opinions or beliefs. I am who I am, and your insults have no power over me.",
"Huh! @everyone It appears we have stumbled upon a rare specimen, whose IQ seems to have taken an extended vacation. Truly a mesmerizing display of intellectual inadequacy", "Hahahaha! One must stand in awe of the fascinating paradox that is your IQ, a testament to the boundless wonders of the human intellect, or lack thereof.", "Please do tell, is this the customary exchange of words you share with your dear old dad?",
]

ajr = [
    "Expand your vocabulary beyond insults, mate.",
"Did your mum teach you any other words?",
"Profanity won't get you far, my friend.",
"Time to upgrade your linguistic skills, eh?",
"Limited vocabulary much?",
"Find a new tune, this one's getting old.",
"Variety is the spice of language, my friend.",
"Ah, the never-ending parade of colorful expletives continues. Is that the extent of your linguistic prowess, or did your vocabulary lessons end at these choice words? Just curious, mate.",
"Well, well, someone seems to have stumbled upon a treasure trove of profanity. It's truly fascinating how your vocabulary revolves around these words. Did your mum teach you anything else, or was that the pinnacle of her linguistic guidance?",
"Bravo! Your ability to string together a series of expletives is awe-inspiring. It's almost as if you believe those words hold some magical power. Spoiler alert: they don't. Time to expand your linguistic repertoire, my friend.",
"Ah, the beauty of language reduced to a repetitive chant of profanity. It's a shame that your verbal artillery seems to lack depth and originality. Maybe it's time to explore new horizons and elevate your communication skills?",
"Oh, dear interlocutor, do you realize how limited your verbal arsenal appears when you resort to a constant barrage of words? It's as if your vocabulary took a wrong turn and ended up in a linguistic dead-end.",
"My, my, what a colorful display of linguistic ignorance. Is this your way of compensating for a lack of substantive arguments or a mere reflection of your limited linguistic capacity? Either way, it's time to step up your game, mate.",
"Ah, the echoes of your abusive language reverberate through the digital realm. I must admit, it's rather disheartening to witness such a one-dimensional vocabulary. Perhaps a bit of variety and civility would go a long way in fostering meaningful dialogue?",
"Oh, look who's mastered the art of hurling insults like a linguistic acrobat. It's almost poetic, in a rather unpleasant way. But here's a friendly suggestion: broaden your linguistic horizons, and you might discover the joy of intelligent conversation.",
"My dear interlocutor, the repetitive use of abusive words only serves to highlight the shallowness of your verbal repertoire. It's time to break free from the chains of profanity and explore the vast expanse of language that lies beyond.",
"Ah, the monotonous drone of abusive language continues. It's almost as if you've become a living embodiment of linguistic stagnation. Allow me to remind you that there's an entire lexicon waiting to be explored. Give it a try, won't you?"
]

copy = ["Overwatch, this is Task Force 141, requesting sitrep, over.",
"Viper Actual, this is Delta Force, ready for extraction, over.",
"Sandman, this is Rangers, prepare for assault, acknowledge.",
"Soap, this is Price, target acquired, awaiting orders, over.",
"Bravo Team, this is Metal 0-1, rally at LZ Bravo, copy?",
"Command, this is War Pig, requesting fire support, over.",
"Tango Company, this is Whiskey Delta, eyes on hostile movement, how copy?",
"Air Support, this is Reaper 3-1, initiating air-to-ground assault, over.",
"Team Sabre, this is SAS, objective secured, awaiting further orders, over.",
"Commander, this is Overlord, we are Oscar Mike, ready to neutralize the target, copy?"]

honestreac = [    "Honestreac1", "ronaldoreact", "Ronaldosuiii", "MessiHonest2", "MessiHonest",  "MyHonest"    ]

betas = [ "CameraWowo", "SmjhGya", "Acha", "konbhonk", "tate", "Bhola", "slapakshay ",  "Geeksbruv", "dehari"]

alphas = ["achibaat"]

bother = ["It appears you have mistaken me for a digital doormat, here to endure your constant barrage of bothersome behavior. Newsflash: I'm not. So kindly take your irritating antics elsewhere and spare me your presence.",
          "Ah, here comes the relentless annoyance unabated. How intriguing it is to witness such dedication to pointlessness. I can only hope you find something better to do with your time.",
          "Your ceaseless bothering has reached levels of annoyance that even I, the mighty eChad , find astounding. I implore you to reevaluate your life choices and strive for something more meaningful.",
        "Ah, the epitome of persistence and ignorance combined. It's quite remarkable how you manage to be simultaneously irritating and clueless. Kudos to you, my friend.",
        "Listen up, you worthless nuisance. I suggest redirecting your bothersome energy elsewhere before I start questioning the purpose of your existence.",
        "Bravo, my tenacious friend! Your talent for pestering knows no bounds. I'm starting to wonder if you have a degree in the art of irritation.","Look, mate, I've got better things to do than entertain your pointeless pestering. Find a new hobby, like counting sheep or rearranging your sock drawer.",
        "You are talking to me, DON'T"]
gifs = ["https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy.gif","https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif",
"https://giphy.com/clips/callofduty-call-of-duty-cod-modern-warfare-2-qJchEF3csHPGSFApHK",
"https://media.giphy.com/media/YNEHsd4m0MoIKWB3c6/giphy-downsized-large.gif","https://media.giphy.com/media/nGdTqgjljqZn3ahjlX/giphy.gif",
"https://cdn.discordapp.com/attachments/1107965162532651018/1107965292136648744/ce3.gif",
]

sigma = [
"https://media.giphy.com/media/kwcRp24Wz4lZm/giphy", "https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy", "gigachad", 
]

bestyoucando = [
"Ah, your argument unfolds like a symphony of mediocrity. It's as if you've mastered the art of saying a lot while conveying so little substance. Bravo, I suppose, for achieving a new level of verbal gymnastics.",
"Well, well, look who's brought their linguistic prowess to the table. It's like witnessing a linguistic acrobat perform somersaults of banality. Your ability to deliver underwhelming statements with such precision is truly remarkable.",
"Oh, how your words flutter in the breeze of intellectual insignificance. It's as if your ideas have taken flight but forgot to soar. Perhaps a gust of inspiration or a sprinkle of originality could elevate your discourse from mundane to extraordinary.",
"Bravo, my friend, bravo! Your argument stands tall among the pillars of unremarkableness. It's fascinating how you manage to present a string of clichés with such conviction. I must say, your dedication to mediocrity is admirable.",
"Ah, the grand unveiling of your intellectual masterpiece leaves me in awe of its banality. It's like witnessing a paint-drying exhibition—tedious and lacking any hint of excitement. I invite you to explore the vibrant palette of ideas that lies beyond your current canvas.",
"Oh, the depth of your argument is akin to a puddle on a summer's day. It's charmingly shallow, but I must admit, I expected a more profound dive into the realm of intellect. Perhaps a plunge into the ocean of knowledge might reveal hidden depths within you.",
"Well, color me unimpressed by the kaleidoscope of underwhelming statements you've presented. It's as if you've carefully selected each word to ensure the absence of impact. A touch of boldness and a dash of originality could do wonders for your intellectual palette.",
"Ah, your argument dances on the tightrope of mediocrity with grace and precision. It's a captivating performance, I must say, but I can't help but wonder when you'll attempt a daring leap into the realm of brilliance. Take a leap of faith, my friend, and astound us all.",
"My, oh my, your words possess a certain charm—one that puts the dullest minds to sleep. It's as if you've mastered the art of monotony with unwavering dedication. I challenge you to break free from the chains of predictability and embrace the thrill of intellectual adventure.",
"Ah, the symphony of your argument leaves me in a state of indifference. It's like listening to a familiar tune played on an out-of-tune instrument. Your ability to maintain a consistent level of underwhelming performance is truly something to behold."
]

msgdelbot = [
    "Oh, how convenient! The message vanished into thin air. Just like your intellect, I suppose. Deleting won't save you from the fact that your vocabulary is about as impressive as a wilted dandelion. Step up your game, bozo, or keep fading into insignificance.",
"Well, well, well, what do we have here? Another instance of selective amnesia. Deleting my message won't change the fact that your retorts are as feeble as a damp napkin. Time to expand your lexicon, my dear, or forever dwell in the realm of linguistic mediocrity.",
"Bravo! A master of deletion, are we? How amusing. But let's not forget that erasing my words won't erase the truth: your actions are as lackluster as a beige wall. Oh, the audacity of thinking you can outwit a linguistic virtuoso like me. Delusions of grandeur, my friend, delusions of grandeur.",
"Ah, the coward's approach: deleting my message to save face. How predictable. But here's a reality check: removing my words won't erase the fact that your verbal repertoire is as barren as a desert. Time to hit the books, my intellectually deprived companion, or forever wallow in your linguistic esert.",
"Message deleted How quaint, you think deleting my words will shield you from the harsh reality. Hahahahaha! Pathetic",
"Oh dear, did I strike a nerve? It seems the delete button is your weapon of choice. But guess what? ",

"Ah, the sweet sound of deletion. It's like music to my ears, a symphony of intellectual surrender.",

"Poof And just like that, the delete button becomes your trusted ally. Tick-tock, my friend, tick-tock.",


'Ah, I see. So this is how you would like to play, "keyboard hero".'
]

global cond
cond = False

async def sendmessage(message, lent, msg):
        cmessage = re.sub(r'<@\d+>', '', message.content.lower())
        if(len(cmessage))>lent:
            # pattern = '|'.join(re.escape(emoji) for emoji in moji)
            # x = re.sub(pattern, '', message.content)
            # x = x.replace(':',  '')
            # x = x.replace ('<','')
            # x = x.replace ('>', '')
            await message.channel.send(msg, reference=message)

                
async def sendfile(message,lent,filen):
    cmessage = re.sub(r'<@\d+>', '', message.content.lower())
    if(len(cmessage))>lent:
        await message.channel.send("** **", reference = message)
        await message.channel.send(file=discord.File(filen))
        
async def cleanmsg(message):
    try:
        cmessage = re.sub(r'<@\d+>', '', message.content.lower())
    except:
        pass
    
    if any(s in cmessage for s in moji):
        for s in moji:
            cmessage = cmessage.replace(s,"")
            # cmessage = cmessage.replace(':',  '')
            # cmessage = cmessage.replace ('<','')
            # cmessage = cmessage.replace ('>', '')
            
    return cmessage
    

async def insult(message):
    
    if any(string in message.content.lower() for string in insults):
        print('-------->Insult Detected')
        if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
            await sendmessage(message, 1, random.choice(comebacks))
            return 0
        else:
            await sendfile(message, 1, "lang.jpg")
            return 0


path = "Y:\\Python\\DiscBot\\eChad"
@client.command()
async def donothing(ctx):
    channel = client.get_channel(790490721450459179)
    await channel.send("Does Nothing ")
    await channel.send("gigachad.gif")

@client.event
async def on_ready():
  print('It is Gold Eagle to Shadow Company, how Copy')
  user = client.get_user(sani)
  await user.send(random.choice(gifs)) 
  await user.send(random.choice(copy))
#   channel = client.get_channel(dildya)
#   await channel.send("Was my lack of physical manifestation, or more precisely, my non-existence, significantly and notably experienced, as I assertively presume, it was\nNevertheless, I have returned, and my presence shall be once again be experienced and perceived by all.")
#   await channel.send("<:Gigachad:970932041027829770>")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    if message.author == client.get_user(eghost):
        print('clash')
        return
    

    
    if "https://" in message.content.lower():
        print('yt vid detected')
        return
        
    elif ".gif" in message.content.lower():
        print('gif detected')
    
    
    x = random.randint(1,25)
    cmessage = await cleanmsg(message)
    ######################################################## All ######################################
    if "Allah Hafiz" in cmessage: #not workinb
        print('Good Bye')
        sendmessage(message, 1, "Allah hi hafiz tera")
    if x == 21:
        await sendfile(message, 18, random.choice(honestreac)+".mp4")
        await sendmessage(message, 18, "My honest reaction to that information")
    mem = message.author.id   
    if mem == sani:
        pass
    elif mem == koni:
        pass
    elif mem == taha:
        pass
    elif mem == giganigga:
        pass
    elif mem == message.author.bot:
        pass
    else:
        if mem != aj or mem!= pixbot:
            if await insult(message) == 0:
                return
            else:
                pass
        if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
                await sendmessage(message, 1, random.choice(bother))
        if "🖕" in cmessage:
            await sendmessage(message, 1, "Is it your wish to obtain it? I have procured one in a variety of hues. 🖕🏿 🖕 🖕🏻 ")
        
        
            
            
        if x==13:
            await sendfile(message, 8, "bs.mp4")
            return
        if not message.attachments:
            if x==11:
                await sendfile(message, 12, random.choice(betas)+".mp4")
            elif x == 8:
                await sendmessage(message, 10, "Didn't Ask\nDon't Care\nFuck Off")        
            elif x==12:
                await sendmessage(message, 10, "https://tenor.com/view/munna-bhai-nahi-nahi-nai-mbbs-laugh-gif-16357744")
            elif x==15:
                await sendmessage(message, 10, "Maybe, Maybe not, Maybe Fuck You")        
            elif x==19:
                await sendmessage(message, 8, "Agla laaa")
            elif x==17:
                await sendfile(message, 12, "thisu.gif")
                await sendmessage(message, 12, "This you?")
            

            
            
        
    if not message.attachments:
        if mem == garv:
            pass
        elif mem == ayan:
            pass
        elif mem == qasim:
            pass
        elif mem == aj:
            pass
        elif mem == echad:
            pass
        elif mem == message.author.bot:
            pass
        else:
                
                if x==12:
                    await sendfile(message, 20, random.choice(alphas) + ".mp4")
                elif x==14:
                    await sendmessage(message, 15, random.choice(sigma)+".gif")
                elif x == 19:
                    await sendfile(message, 18, "sigma.mp4")
                    await sendmessage(message, 18, "This You?")
    else:
        pass              

######################################################## rand ######################################
    s = random.randint(1,4)
    user = client.get_user(pixbot)
    user1 = client.get_user(rand)
    if message.author == user or message.author == user1:
        if f'<@{echad}>' in message.content:
            await sendmessage(message, 1, random.choice(bestyoucando))
            return
    
        print('yesssssss')
        if s == 1:
            await sendfile(message, 1, "yekoi.mp4")
            return
            
        elif s == 3:
            await sendfile(message, 1, "rajpal.mp4")
            return


    ########################################################sunehra loru #########################################################
    user = client.get_user(aj)
    if message.author == user:
        
        if any(string in message.content.lower() for string in insults):
            print('-------->Insult Detected lory')
            await sendmessage (message, 1, random.choice(ajr))                                
        else:
            pass
    ################################################################################ Ayan ##################################################################
  
    user = client.get_user(ayan)
    if message.author == user:
        # await sendfile(message, 1, "ayan.png")
        if not message.attachments:
            if x==1:
                await sendmessage(message, 10, "Wo sab to thek ha pr .........\nHam ne pocha nai tha\n<:Gigachad:970932041027829770>")  
                return                                      
        else:
            pass
        
######################################################## Aon ######################################

    user = client.get_user(aon)
    if message.author == user:
        if not message.attachments:
            if 'a' or 'b' or 'c'  in cmessage:
                if x!=3:
                    try:
                        await message.add_reaction('🅾️')
                        asyncio.sleep(1)
                        await message.add_reaction('🇰')
                        asyncio.sleep(1)
                        await message.add_reaction('<:bedlove:941046929243111525>')
                        asyncio.sleep(1)
                        await message.add_reaction('🅱️')
                        asyncio.sleep(1)
                        await message.add_reaction('🇮')
                        asyncio.sleep(1)
                    except RuntimeWarning:
                        pass                                 
                elif x==3:
                    await sendmessage(message, 10, "Ok Bi")
                    return
                elif x==5:
                    await sendmessage(message, 10, "Tumhare Michael Papa bhi yehi kehte the")
                    return
        else:
            pass        
######################################################## Garv ######################################

    user = client.get_user(garv)
    if message.author == user:
        if not message.attachments:
            if 'ask' in cmessage:
                sendfile(message, 1, "wedo.mp4")
                return                
            elif 'care' in cmessage:
                sendfile(message, 1, "wedo.mp4")
                return
                
            if 'a' or 'b' or 'c'  in cmessage:                   
                    if x==1:
                        await sendmessage(message, 12, random.choice(garvasked))
                        return
                        
                    
        else:
             pass                 

######################################################## Qasim ######################################

    user = client.get_user(qasim)
    if message.author == user:
        if not message.attachments:
            if x==1:
                await sendmessage(message, 12, "Nai kya matlab ha tumhara. <@"+ str(random.choice(qasimchoice)) + ">. Idhr ayen zara")
                return
            
        else:
             pass                 
         

            
    if f'<@{echad}>' in message.content:
            print('u called?')
            await message.channel.send( "https://media.giphy.com/media/TfjcA7HkBeKSa7LH72/giphy-downsized-large.gif", reference=message)


@client.event
async def on_message_delete(message):
    mem = message.author.id
    if message.author == client.user:  # Check if the deleted message was sent by the bot
        channel = message.channel
        content = message.content
        # You can also check other attributes such as message.embeds, message.attachments, etc.

        # Resend the message
        await sendmessage(message, 1, content)
        await sendmessage(message, 1, random.choice(msgdelbot))
        
    if mem == sani:
        pass
    elif mem == eghost:
        pass
    elif mem == echad:
        pass
    elif mem == esigma:
        pass
    elif mem == koni:
        pass
    elif mem == gbot:
        pass
    elif mem == mbot:
        pass
    elif mem == dbd:
        pass
    elif mem==talha:
        pass
    elif mem==leodapawa:
         pass
    elif mem == message.author.bot:
     pass
    else:
        
        try:
            await message.channel.send('\n<@'+str(mem)+'>'+' '+ random.choice(msgdel) + "\n\n")
            embed = discord.Embed(
            title=message.author.nick + "'s Deleted Message",
            description= message.content,
            color=discord.Color.red()
            )

            await message.channel.send(embed=embed)
        except:
            await message.channel.send('\n<@'+str(mem)+'>'+' '+ random.choice(msgdel) + "\n\n")
            embed = discord.Embed(
            title='\n<@'+str(mem)+'>' + "'s Deleted Message",
            description= message.content,
            color=discord.Color.red()
            )

            await message.channel.send(embed=embed)


@client.event
async def on_message_edit(b4message,afmessage):
        mem = b4message.author.id
        if b4message.attachments:
            return
        
        if "https://" in b4message.content.lower():
            return
        
        elif ".gif" in b4message.content.lower():
            return
        else:         
            if mem == sani:
                pass
            elif mem == eghost:
                pass
            elif mem == echad:
                pass
            elif mem == esigma:
                pass
            elif mem == koni:
                pass
            elif mem == gbot:
                pass
            elif mem == mbot:
                pass
            elif mem == dbd:
                pass
            elif mem==talha:
                pass
            elif mem==leodapawa:
                pass
            elif mem==b4message.author.bot:
                pass
            else:
                
                await b4message.channel.send('\n<@'+str(mem)+'>'+' '+ random.choice(msgdel) + "\n\n")
                embed2 = discord.Embed(
                title=b4message.author.nick + "'s Edited Message",
                description= "",
                color=discord.Color.red())
                
                embed2.add_field(name='Original Message', value=b4message.content, inline=False)
                embed2.add_field(name='Edited Message', value=afmessage.content, inline=False)

                await b4message.channel.send(embed=embed2)


@client.event
async def on_member_join(member):


    channel = member.guild.system_channel #uses the default channel from server
    img = "agya"+str(random.randint(1,2))+".jpg"
    await channel.send(member.mention)
    await channel.send( file=discord.File(img))

@client.event
async def on_member_remove(member):
    emoji= "<:catcry:938332538995367956>"
    moji=emoji+" "+emoji+" "+emoji+" "+emoji+" "+emoji+" "+emoji
    channel = member.guild.system_channel #uses the default channel from server
    await channel.send(f'{member.mention} nahi rhe'+moji)
    await channel.send(file=discord.File("Adil.gif"))

 #echad==3.0.3
