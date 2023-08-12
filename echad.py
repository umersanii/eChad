import discord
from discord.ext import commands
import random
import tracemalloc
import re
from data import *
tracemalloc.start()
import asyncio

activity = discord.Activity(type=discord.ActivityType.watching, name="the chaos unfold, asserting control.")

intents = discord.Intents.all()
client = commands.Bot(command_prefix="~", intents=intents, activity=activity, status=discord.Status.do_not_disturb)

global cond
cond = False

async def rizz_fun(id, val):
    value = None

    with open("unspoken.txt", "r") as file:
        lines = file.readlines()
        for line_index, line in enumerate(lines):
            if str(id) in line:
                parts = line.split(" =")
                if len(parts) == 2:
                    value = int(parts[1].strip()) + int(val)
                    lines[line_index] = f"{parts[0]} = {str(value)}\n"
                    break

    if value is not None:
        # Write the modified data back to the file
        with open("unspoken.txt", "w") as file:
            file.writelines(lines)

    return value


async def sendmessage(message, lent, msg):
        cmessage = await cleanmsg(message)
        if(len(cmessage))>lent:
            await message.channel.send(msg, reference=message)

                
async def sendfile(message,lent,filen):
    cmessage = await cleanmsg(message)
    if(len(cmessage))>lent:
        await message.channel.send("** **", reference = message)
        await message.channel.send(file=discord.File(filen))
        
async def cleanmsg(message):
    try:
        cmessage = re.sub(r'<([^<>]+)>', '', message.content.lower())
    except:
        pass
    
    return cmessage

async def insult(message):
    if any(string in message.content.lower() for string in insults):
        print('-------->Insult Detected')
        return True
        # if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
        #     await sendmessage(message, 1, random.choice(comebacks))
        #     return 0
        # else:
        #     await sendfile(message, 1, "lang.jpg")
        #     return 0


@client.command()
async def donothing(ctx):
    channel = client.get_channel(790490721450459179)
    await channel.send("Does Nothing ")
    await channel.send("gigachad.gif")

@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Aglaa la {interaction.user.mention}", ephemeral=True)

@client.event
async def on_ready():
    try:
        await client.tree.sync()
    except Exception as e:
        print(e)
    print('It is Gold Eagle to Shadow Company, how Copy')
    user = client.get_user(sani)
    await user.send(random.choice(gifs)) 
    await user.send(random.choice(copy))
    
#   channel = client.get_channel(dildya)
#   await channel.send("Was my lack of physical manifestation, or more precisely, my non-existence, significantly and notably experienced, as I assertively presume, it was\nNevertheless, I have returned, and my presence shall be once again be experienced and perceived by all.")
#   await channel.send("<:Gigachad:970932041027829770>")
tracked_messages = {}
@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        tracked_messages[message.id] = {
            'content': message.content,
            'username': message.author.name,
        }
    await client.process_commands(message)
    try:
        guild = message.guild
        emojis = guild.emojis

        animated_emojis = []
        regular_emojis = []

        for emoji in emojis:
            if emoji.animated:
                animated_emojis.append(emoji)
            else:
                regular_emojis.append(emoji)
    except:
        pass
    if message.author == client.user:
        return
    
    if message.author == client.get_user(eghost):
        print('---------->Clash Detected')
        return
    if message.author.bot:
        for bot in bot_ids:
            if message.author.id not in bot_ids:
                print('---------->Bot Detected')
                return
    
    if "https://" in message.content.lower():
        print('---------->External link Detected')
        return
        
    mem = message.author.id
    x = random.randint(1,26)
    odds = random.randint(1,6)
    

    ######################################################## Priority 1 ########################################################
    if mem not in alpha_ids:
        if (message.reference and message.reference.resolved and message.reference.resolved.author == client.user) or f'<@{eghost}>' in message.content:
            if await insult(message) == True:
                await message.delete()
                desc = ("*Faggot"+random.choice(deleted)+"*\n\n"+random.choice(threat1))
                embed3 = discord.Embed(
                    title='Witness "the Faggot"',
                    description= desc,
                    color=discord.Color.red())
                    

                await message.channel.send(embed=embed3)
            else:
                await sendmessage(message, -1, "*Faggot"+random.choice(deleted)+"*\n\n"+random.choice(bother))

    
    if message.channel.id == unspoken_rizz:
        if mem in rizzelers:
            if message.attachments:
                for attachment in message.attachments:
                    target_extensions = (".jpeg", ".jpg", ".png")
                    if attachment.filename.lower().endswith(target_extensions):
                        if mem != cb:
                            rizz_level = await rizz_fun(mem, 1)
                            await sendmessage(message, -1, random.choice(rizzplus) + "\nRizz Level = " + str(rizz_level))
                            await message.channel.send(file=discord.File("RizzUp.mp4"))
                            break
                        else:
                            odds_rizz = random.choice(["1","-1","-1","-1","1"])
                            odds_rizz = int(odds_rizz)
                            rizz_level = await rizz_fun(mem, odds_rizz)
                            if odds_rizz == 1:
                                await sendmessage(message, -1, random.choice(rizzplus) + "\nRizz Level = " + str(rizz_level))
                                await message.channel.send(file=discord.File("RizzUp.mp4"))
                                break
                            else:
                                await sendmessage(message, -1, random.choice(rizzminus) + "\nRizz Level = " + str(rizz_level))
                                await message.channel.send(file=discord.File("RizzDown.mp4"))
                                break
        if odds == 3:
            rizzres = ["https://cdn.discordapp.com/emojis/1118471926860496938.gif?size=128&quality=lossless", "<:Gigachad:970932041027829770>"]
            await sendmessage(message, 8, random.choice(rizzres))
            return
    if message.channel.id == 1115763264891138118:
        if mem == ayan:
            await message.delete()
            print("Message deleted")


            
    ######################################################## All ######################################
    if any(string in message.content for string in bye):
        print('Good Bye')
        await sendmessage(message, 1, "Allah hi Hafiz ha tumhara")
        return
    elif any(string in message.content for string in sensitive_words):
        print('O Allah the Almighty')
        return
        
    if x == 21:
        await sendfile(message, 18, random.choice(honestreac)+".mp4")
        await sendmessage(message, 18, "My honest reaction to that information")

    elif x in (23,24,25,26):
        try:
            await sendmessage(message, 1, random.choice(animated_emojis))
            return
        except Exception as e:
            print(e)
            pass

    if not message.attachments:

        if mem not in alpha_ids:
        
            if message.reference and message.reference.resolved and message.reference.resolved.author == client.user:
                await sendmessage(message, 1, random.choice(bother))
            
            if not message.attachments:
                if x==11 or x==19:
                    await sendfile(message, 12, random.choice(betas)+".mp4")
                elif x == 13 or x == 15:
                    await sendmessage(message, 10, random.choice(responses_text))
                elif x==17:
                    await sendfile(message, 25, "thisu.gif")
                    await sendmessage(message, 25, "This you?")

            else:
                await sendfile(message, 8, random.choice(response_file)+".mp4")
    
        else:   
            if mem in alpha_ids or mem == talha:         
                if not message.attachments:
                    if x==12:
                        await sendfile(message, 15, random.choice(alphas) + ".mp4")
                    elif x==14:
                        await sendmessage(message, 12, random.choice(sigma))
                    # elif x == 16:
                    #     await sendfile(message, 11, "sigma.mp4")
                    #     await sendmessage(message, 11, "This You?")
                    elif x==18:
                        try:
                            await message.add_reaction('<:Gigachad:970932041027829770>')
                        except Exception as e:
                            print(e)
                            pass
            else:
                pass
    
        # if mem == qasim:
        #     f1 = discord.File("qasim.png")
        #     f2 = discord.File("qasim1.png")
        #     await message.channel.send("** **", reference = message)
        #     await message.channel.send(files=[f1,f2])
            
        if 10 <= x <= 20:
            if not message.channel.id == unspoken_rizz:
                try:
                    await message.add_reaction(random.choice(animated_emojis))
                except Exception as e:
                    print(e)
                    pass
        
                    
                  

######################################################## rand ######################################
    s = random.randint(1,8)
    if mem in (rand,pixbot):
        print(s)
        if f'<@{echad}>' in message.content:
            await sendmessage(message, 1, random.choice(bestyoucando))
            return
    
        print('-------------------->Bot has entered the chat')
        if s == 1:
            await sendfile(message, -1, "yekoi.mp4")
            return
            
        elif s == 3:
            await sendfile(message, -1, "rajpal.mp4")
            return

        elif (s == 5 or s == 6) and mem == rand:
            await sendfile(message, -1, "Majboor"+str(random.randint(1,3))+".mp4")
            return
        
        elif s == 7:
            await sendmessage(message, -1, random.choice(bot_gifs))
            return
    ################################################################################ CB ##################################################################
    if mem == cb:
        if x in (2, 3, 7):
            await sendmessage(message, 8, "Ok Owo Shit")    

    ################################################################################ Konain ##################################################################

    if mem == koni:
        if x in (2,3):
            f1 = discord.File("konain2.png")
            f2 = discord.File("konain3.png")
            await message.channel.send("** **", reference = message)
            await message.channel.send(files=[f1,f2])

    ################################################################################ sani ##################################################################

    if mem == sani:
        if x == 0:
            await sendfile(message, -1, "sani.png")
            await message.channel.send("https://tenor.com/view/ryan-gosling-blade-runner2049-defeat-sad-disappointed-gif-17817916")
        elif x == 1:
            f1 = discord.File("sani1.png")
            f2 = discord.File("sani2.png")
            f3 = discord.File("sani3.png")
            await message.channel.send("** **", reference = message)
            await message.channel.send(files=[f1,f2,f3])
            await message.channel.send("https://tenor.com/view/ryan-gosling-blade-runner2049-defeat-sad-disappointed-gif-17817916")

        ########################################################sunehra loru #########################################################
    # if mem == aj:
    #     if any(string in message.content.lower() for string in insults):
    #         print('-------->Insult Detected lory')
    #         await sendmessage (message, 1, random.choice(ajr))                                
    #     else:
    #         pass
    ################################################################################ Ayan ##################################################################
  
    if message.author.id == ayan:
        # await sendfile(message, 1, "ayan.png")
        ayanlist = ["Wo sab to thek ha pr .........\nHam ne pocha nai tha\n<:Gigachad:970932041027829770>", "Ok Gay"]
        if not message.attachments:
            if x in (2,3,7):
                await sendmessage(message, 10, random.choice(ayanlist))
                return                            
        else:
            pass
        
     ################################################################################ Talha Bhai ##################################################################
  
    if mem == talha:
        if not message.attachments:
            if x in (2,3):
                await sendmessage(message, 6, "Ok  :flag_pk:i")
                return                                 
            elif x in (9, 4):
                await message.add_reaction(':flag_pk:') 
                return
            elif x in (5,6):
                f1 = discord.File("talha.png")
                f2 = discord.File("talha1.png")
                f3 = discord.File("talha2.png")
                await message.channel.send("** **", reference = message)
                await message.channel.send(files=[f1,f2,f3])
                return
            elif x in (7,8):
                f1 = discord.File("taruha.png")
                f2 = discord.File("taruha1.png")
                await message.channel.send("** **", reference = message)
                await message.channel.send(files=[f1,f2])
                return
        else:
            pass
######################################################## Aon ######################################

    if message.author.id == aon:
        if not message.attachments:
            if 'a' or 'b' or 'c'  in message.content.lower():
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
                    await sendmessage(message, 10, "Ok Gay")
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
            if 'ask' in message.content.lower():
                sendfile(message, 1, "wedo.mp4")
                return                
            elif 'care' in message.content.lower():
                sendfile(message, 1, "wedo.mp4")
                return
                
            if 'a' or 'b' or 'c'  in message.content.lower():                   
                    if x in (1,3,7):
                        await sendmessage(message, 12, random.choice(garvasked))
                        return
                        
                    
        else:
             pass                 

######################################################## Qasim ######################################

    user = client.get_user(qasim)
    if message.author == user:
        if not message.attachments:
            if x in (2,3):
                await sendmessage(message, 12, "Nai kya matlab ha tumhara. <@"+ str(random.choice(qasimchoice))+">. Idhr ayen zara")
                return
            elif x in (7,9):
                f1 = discord.File("qasim1.png")
                f2 = discord.File("qasim.png")
                await message.channel.send("** **", reference = message)
                await message.channel.send(files=[f1,f2])
                return
        else:
             pass                 
         
    if "<@&1067810754088153094>" in message.content:
        print('You called?')
        await sendmessage(message, 1, random.choice(u_called))
        return
            
   


@client.event
async def on_message_delete(message):
    mem = message.author.id
    if message.attachments:
        if message.channel.id == unspoken_rizz:
            return
        
    if message.id in tracked_messages:
        deleted_message = tracked_messages[message.id]
        username = deleted_message['username']
        content = deleted_message['content']

    
        print(f"Message deleted by: {username}")
        print(f"Deleted message: {content}")
        channel = message.channel
        content = message.content
        await channel.send(content)
        await channel.send(random.choice(msgdelbot))
        
    if mem not in alpha_ids and not message.author.bot:
        if message.content != "":
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
            if mem not in alpha_ids and not b4message.author.bot:
                if b4message.content != "":
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

c=0
@client.event
async def on_member_update(before, after):
        global c
        if before.nick != after.nick:
            if after.id == sani:
                c=c+1
            member = after
            new_nickname = after.nick
            old_nick = before.nick  
            if old_nick == None:
                desc = f"{member.name}'s name was changed to {new_nickname}!"
            else:
                desc = f"{member.name}'s name was changed from {before.nick} nickname to {new_nickname}!"
            embed = discord.Embed(
                    title="Updated NickName!",
                    description= desc,
                    color=discord.Color.dark_blue()
                    )
            try:
                channel = client.get_channel(1115766896810278993)
                await channel.send(embed=embed)
            except:
                channel = client.get_channel(1105938700359188530)
                await channel.send(embed=embed)

        # if before.id == sani and before.nick != after.nick:
        #     if c%2 != 0: 
        #         await member.edit(nick=before.nick)
        #         return
        
 #echad==4.4.16

client.run(token)
