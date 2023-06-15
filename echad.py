import discord
from discord.ext import commands
import random
import tracemalloc
import re
tracemalloc.start()
import asyncio

activity = discord.Activity(type=discord.ActivityType.watching, name="The Small 3's 🍰🍰")

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
insults = ["chupad ","your daddy","abbe","salle","chutiye","bund","kuty", "lun","gando","mummy","bhen","bitch","lan", "lode","randi","gandu","abbu","your father", "ammi", "ami", "mom", "dad","abu","tera abu hu salle","kuti"]
comebacks = ["Ha-ha-ha, I thought my jokes were of inferior quality until I heard yours.","Your ass must be pretty jealous of all the shit that comes out of your mouth.",
"I find your desperate attempts at humor, amusing", "Is it your wish to engage in discourse? I have the capacity to do so in a variety of manners and tones.","I see that your desire to insult me is unwavering. However, I must inform you that my worth cannot be defined by your opinions or beliefs. I am who I am, and your insults have no power over me.",
"Huh! @everyone It appears we have stumbled upon a rare specimen, whose IQ seems to have taken an extended vacation. Truly a mesmerizing display of intellectual inadequacy", "Hahahaha! One must stand in awe of the fascinating paradox that is your IQ, a testament to the boundless wonders of the human intellect, or lack thereof.", "Please do tell, is this the customary exchange of words you share with your dear old dad?",
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

gifs = ["https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy.gif","https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif",
"https://giphy.com/clips/callofduty-call-of-duty-cod-modern-warfare-2-qJchEF3csHPGSFApHK",
"https://media.giphy.com/media/YNEHsd4m0MoIKWB3c6/giphy-downsized-large.gif","https://media.giphy.com/media/nGdTqgjljqZn3ahjlX/giphy.gif",
"https://cdn.discordapp.com/attachments/1107965162532651018/1107965292136648744/ce3.gif",
]

randombs = [
    "Geeksbruv", "dehari"
]

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
    

    
    if "https://" in message.content.lower():
        print('yt vid detected')
        return
        
    elif ".gif" in message.content.lower():
        print('gif detected')
    
    
    x = random.randint(1,30)
    cmessage = await cleanmsg(message)
    ######################################################## All ######################################
    if "Allah Hafiz" in cmessage: #not workinb
        print('Good Bye')
        sendmessage(message, 1, "Allah hi hafiz tera")
    if x == 21:
        await sendfile(message, 20, "Honestreac1.mp4")
        await sendmessage(message, 20, "My honest reaction to that information")
    elif x == 23:
        await sendfile(message, 19, "ronaldoreact.mp4")
        await sendmessage(message, 19, "My honest reaction to that information")
    mem = message.author.id   
    if mem == sani:
        pass
    elif mem == koni:
        pass
    elif mem == message.author.bot:
        pass
    else:
        if await insult(message) == 0:
            return
        else:
            pass
        if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
                await sendmessage(message, 1, "You are  talking to me? DON'T")
                return
        if "🖕" in cmessage:
            await sendmessage(message, 1, "Is it your wish to obtain it? I have procured one in a variety of hues. 🖕🏿 🖕 🖕🏻 ")
            return
        
        if f'<@{echad}>' in message.content:
            print('u called?')
            await message.channel.send( "https://media.giphy.com/media/TfjcA7HkBeKSa7LH72/giphy-downsized-large.gif", reference=message)
            

        if x==13:
            await sendfile(message, 8, "bs.mp4")
            return

        if not message.attachments:
            if x==11:
                await sendfile(message, 25, "konbhonk.mp4")
                return
            elif x == 8:
                await sendmessage(message, 10, "Didn't Ask\nDon't Care\nFuck Off")        
                return
            elif x==12:
                await sendmessage(message, 10, "https://tenor.com/view/munna-bhai-nahi-nahi-nai-mbbs-laugh-gif-16357744")
                return
            elif x==15:
                await sendmessage(message, 10, "Maybe, Maybe not, Maybe Fuck You")        
                return
            elif x==19:
                await sendmessage(message, 8, "Agla laaa")
                return
            elif x==20:
                await sendfile(message, 8, random.choice(randombs))
                return
            elif x==18:
                await sendfile(message, 8, "tate.mp4")
                return
            elif x==17:
                await sendfile(message, 12, "thisu.gif")
                await sendmessage(message, 12, "This you?")
                return
            
        
            

            
            
        
    if not message.attachments:
        if mem == garv:
            pass
        elif mem == ayan:
            pass
        elif mem == qasim:
            pass
        elif mem == echad:
            pass
        elif mem == message.author.bot:
            pass
        else:
                
                if x==12:
                    await sendfile(message, 20, "achibaat.mp4")
                elif x==14:
                    await sendmessage(message, 15, "https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif")
                elif x ==13:
                    await sendmessage(message, 15, "https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy.gif")
                elif x == 19:
                    await sendfile(message, 18, "sigma.mp4")
                    await sendmessage(message, 18, "This You?")
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
         
######################################################## rand ######################################
    user = client.get_user(270904126974590976)
    if message.author == user:
        if x == 1:
            await sendfile(message, 1, "yekoi.mp4")
        elif x==3:
            await sendfile(message, 1, "rajpal.mp4")
            

@client.event
async def on_message_delete(message):
    mem = message.author.id
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
            await message.channel.send('\n<@'+str(mem)+'>'+ random.choice(msgdel) + "\n\n")
            embed = discord.Embed(
            title=message.author.nick + "'s Deleted Message",
            description= message.content,
            color=discord.Color.red()
            )

            await message.channel.send(embed=embed)
        except:
            await message.channel.send('\n<@'+str(mem)+'>'+ random.choice(msgdel) + "\n\n")
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
                
                await b4message.channel.send('\n<@'+str(mem)+'>'+ random.choice(msgdel) + "\n\n")
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
 
 
 
