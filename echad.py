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
msgdel = ["*Striving to eliminate one's mistakes, it is an exercise in futility.*", "*Your endeavors to eliminate this communication are inefficient, similarly to attempting to secure your parent's admiration.*"]
insults = ["chupad ","your daddy","abbe","salle","chutiye","bund","kuty", "lun","gando","mummy","bhen","bitch","lan", "lode","randi","gandu","abbu","your father", "ammi", "ami", "mom", "dad","abu","tera abu hu salle","kuti"]
comebacks = ["Ha-ha-ha, I thought my jokes were of inferior quality until I heard yours.","Your ass must be pretty jealous of all the shit that comes out of your mouth.",
"I find your desperate attempts at humor, amusing", "Is it your wish to engage in discourse? I have the capacity to do so in a variety of manners and tones.","I see that your desire to insult me is unwavering. However, I must inform you that my worth cannot be defined by your opinions or beliefs. I am who I am, and your insults have no power over me."
]
gifs = ["https://media.giphy.com/media/YlRpYzrkHbtSYDAlaE/giphy.gif","https://media.giphy.com/media/kwcRp24Wz4lZm/giphy.gif",
"https://giphy.com/clips/callofduty-call-of-duty-cod-modern-warfare-2-qJchEF3csHPGSFApHK",
"https://media.giphy.com/media/YNEHsd4m0MoIKWB3c6/giphy-downsized-large.gif","https://media.giphy.com/media/nGdTqgjljqZn3ahjlX/giphy.gif"]


async def sendmessage(message, lent, msg):
        cmessage = re.sub(r'<@\d+>', '', message.content.lower())
        if(len(cmessage))>lent:
            # for emoji in moji:
            #     if f'<:{emoji}:' in message.content:
            #         print("moji detected")
            # else:
            #     await message.channel.send(msg, reference=message)
            pattern = '|'.join(re.escape(emoji) for emoji in moji)
            x = re.sub(pattern, '', message.content)
            x = x.replace(':',  '')
            x = x.replace ('<','')
            x = x.replace ('>', '')
            await message.channel.send(x, reference=message)

                
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
            
    return cmessage
    

async def insult(message):
    if any(string in message.content.lower() for string in insults):
        print('1')
        if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
            print('12')
            await sendmessage(message, 1, random.choice(comebacks))
        else:
            await sendfile(message, 1, "lang.jpg")


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
#   channel = client.get_channel(dildya)
#   await channel.send("Was my lack of physical manifestation, or more precisely, my non-existence, significantly and notably experienced, as I assertively presume, it was\nNevertheless, I have returned, and my presence shall be once again be experienced and perceived by all.")
#   await channel.send("<:Gigachad:970932041027829770>")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    if message.author.id == 693664844095946763:
        print("author yes")
        await sendmessage(message, 1, "yes")
        print("message yes")
        return


    
    if "https://" in message.content.lower():
        print('yt vid detected')
        return
        
    elif ".gif" in message.content.lower():
        print('gif detected')
    
    
    x = random.randint(10,30)
    cmessage = await cleanmsg(message)
    


    if f'<@{echad}>' in message.content:
        print('u called?')
        await message.channel.send( "https://media.giphy.com/media/TfjcA7HkBeKSa7LH72/giphy-downsized-large.gif", reference=message)
    else:
        pass
    
    ################################################################################ Ayan ##################################################################
  
    user = client.get_user(ayan)
    if message.author == user:
        # await sendfile(message, 1, "ayan.png")
        if not message.attachments:
            s = random.randint(1, 4)
            if s==1:
                await sendmessage(message, 10, "Wo sab to thek ha pr .........\nHam ne pocha nai tha\n<:Gigachad:970932041027829770>")  
                return                                      
        else:
            pass
        
######################################################## Aon ######################################

    user = client.get_user(aon)
    if message.author == user:
        if not message.attachments:
            s = random.randint(1, 6)
            if 'a' or 'b' or 'c'  in cmessage:
                if s!=3:
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
                elif s==3:
                    await sendmessage(message, 10, "Ok Bi")
                    return
                elif s==5:
                    await sendmessage(message, 10, "Tumhare Michael Papa bhi yehi kehte the")
                    return
        else:
            pass        
######################################################## Garv ######################################

    user = client.get_user(garv)
    if message.author == user:
        if not message.attachments:
            s = random.randint(1, 4)
            # if 'ask' in cmessage:
                # sendfile(meesage, 1, "wedo.mp4")
                
            # elif 'care' in cmessage:
                # sendfile(meesage, 1, "wedo.mp4")
                
            if 'a' or 'b' or 'c'  in cmessage:                   
                    if s==1:
                        await sendmessage(message, 12, random.choice(garvasked))
                        return
                        
                    
        else:
             pass                 

######################################################## Qasim ######################################

    user = client.get_user(qasim)
    if message.author == user:
        s = random.randint(1, 4)
        if not message.attachments:
            if s==1:
                await sendmessage(message, 15, "Nai kya matlab ha tumhara. <@"+ str(random.choice(qasimchoice)) + ">. Idhr ayen zara")
            
            # elif x==15:
            #     await sendmessage(message, 15, "Maybe, Maybe not, Maybe Fuck You")   
        else:
             pass                 
         
######################################################## rand ######################################
    user = client.get_user(270904126974590976)
    if message.author == user:
        s = random.randint(1, 4)
        if s == 1:
            await sendfile(message, 1, "yekoi.mp4")
        elif s==3:
            await sendfile(message, 1, "rajpal.mp4")
            

######################################################## All ######################################
    mem = message.author.id
    if mem == message.author.bot:
        pass
    else:
        if "Allah Hafiz" in message.content.lower():
            sendmessage(message, 1, "Allah hi hafiz tumhara")
        if x == 21:
            await sendfile(message, 25, "Honestreac1.mp4")
            await sendmessage(message, 25, "My honest reaction to that information")
        if x== 23:
            await sendfile(message, 23, "ronaldoreact.mp4")
            await sendmessage(message, 23, "My honest reaction to that information")
            
    
    if mem == sani:
        pass
    elif mem == koni:
        pass
    elif mem == message.author.bot:
        pass
    else:
        await insult(message)
        if "🖕" in cmessage:
            await sendmessage(message, 1, "Is it your wish to obtain it? I have procured one in a variety of hues. 🖕🏿 🖕 🖕🏻 ")
        if not message.attachments:
            if x==11:
                await sendfile(message, 25, "konbhonk.mp4")
            elif x==12:
                await sendmessage(message, 10, "https://tenor.com/view/munna-bhai-nahi-nahi-nai-mbbs-laugh-gif-16357744")
            elif x==15:
                await sendmessage(message, 10, "Maybe, Maybe not, Maybe Fuck You")        
            elif x==19:
                await sendmessage(message, 8, "Agla laaa")
            elif x==18:
                await sendfile(message, 8, "tate.mp4")
            elif x==17:
                await sendfile(message, 12, "thisu.gif")
                await sendmessage(message, 12, "This you?")
            if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
                await sendmessage(message, 1, "You are  talking to me? DON'T")
            
            
        
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
        print('yes')               



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
        await message.channel.send('\n<@'+str(mem)+'>' + "\n"+ random.choice(msgdel) + "\n\n")
        await message.channel.send(message.author.name + " was saying : " + "*"+message.content+"*")

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
                
                await b4message.channel.send('\n<@'+str(mem)+'>' + "\n"+ random.choice(msgdel) + "\n\n" + afmessage.author.name + 
                " edited his message from : " + "*" +b4message.content + "*\n" + " to " + "\n**"+afmessage.content+"**")

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
 
 
 
client.run()
