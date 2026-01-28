import discord
from discord import app_commands
from discord.ext import commands
import random
import asyncio
import os
import json
import logging
from logging.handlers import RotatingFileHandler
import re
from firebase_admin import credentials, firestore, initialize_app
from data import *
from disc_token import *
from functools import partial
from google.api_core import retry

# Custom filter to exclude redundant messages
class RedundantFilter(logging.Filter):
    def filter(self, record):
        if "Heartbeat" in record.msg and "error" not in record.msg.lower():
            return False
        return True

# Setup logging
logger = logging.getLogger('bot')
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler('bot.log', maxBytes=5*1024*1024, backupCount=0)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
handler.setFormatter(formatter)
handler.addFilter(RedundantFilter())
logger.addHandler(handler)

# Firebase setup
cred = credentials.Certificate("/home/umersani/serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

# Bot configuration
activity = discord.Activity(type=discord.ActivityType.watching, name="the chaos unfold, asserting control.")
PHRASE_RESPONSES = {
    "aglaa laa": "Putha hoo",
    "agla la 把": "Putha hoo",
    "kdhr ha": "Pakistan me",
    "kahan ha": "Pakistan me",
    "khan ha": "Pakistan me",
    "kidhr ha": "Pakistan me",
    "kidr ha": "Pakistan me",
}
RESPONSE_PROBABILITIES = {
    "animated_emoji": {"weight": 0.2, "action": lambda bot, msg: msg.add_reaction(random.choice(bot.animated_emojis))},
    "honest_reaction": {"weight": 0.1, "action": lambda bot, msg: bot.send_response(msg, 1, content="My honest reaction to that information", files=f"data/vids/{random.choice(honestreac)}.mp4")},
    "beta_video": {"weight": 0.05, "action": lambda bot, msg: bot.send_response(msg, 12, files=f"data/vids/{random.choice(betas)}.mp4")},
    "thisu_gif": {"weight": 0.05, "action": lambda bot, msg: bot.send_response(msg, 25, content="This you?", files="data/gifs/thisu.gif")},
    "text_response": {"weight": 0.1, "action": lambda bot, msg: bot.send_response(msg, 10, random.choice(responses_text))},
    "talha_quote": {
        "weight": 0.1,
        "action": lambda bot, msg: bot.send_response(
            msg, 10,
            embed=discord.Embed(title="Naughty Seal says:", description=random.choice(talhaquotes), color=discord.Color.pink()).set_image(url="attachment://HornyTalha.png"),
            files="data/pics/taruha4.png"
        )
    },
    "response_video": {"weight": 0.1, "action": lambda bot, msg: bot.send_response(msg, 8, files=f"data/vids/{random.choice(response_file)}.mp4")},
    "alpha_video": {"weight": 0.05, "action": lambda bot, msg: bot.send_response(msg, 15, files=f"data/vids/{random.choice(alphas)}.mp4")},
    "sigma_text": {"weight": 0.05, "action": lambda bot, msg: bot.send_response(msg, 12, random.choice(sigma))},
    "gigachad_reaction": {"weight": 0.05, "action": lambda bot, msg: msg.add_reaction('<:Gigachad:970932041027829770>')},
}

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.all(), activity=activity, status=discord.Status.do_not_disturb)
        self.tracked_messages = {}
        self.animated_emojis = []
        self.regular_emojis = []

    async def setup_hook(self):
        self.loop.create_task(self.heartbeat())

    async def heartbeat(self):
        retry_predicate = retry.if_exception_type(TimeoutError, ConnectionError)
        retry_policy = retry.Retry(
            predicate=retry_predicate,
            initial=1.0,
            maximum=10.0,
            multiplier=2.0
        )

        def set_status():
            db.collection("status").document("alive").set(
                {"echad_last_seen": firestore.SERVER_TIMESTAMP}, merge=True
            )

        while True:
            try:
                loop = asyncio.get_event_loop()
                logger.info("Sending heartbeat to Firestore")
                await loop.run_in_executor(None, retry_policy(set_status))
                logger.info("Heartbeat successful")
            except Exception as e:
                logger.error(f"Heartbeat error: {e}")
            await asyncio.sleep(50)
        
    async def cleanmsg(self, message):
        try:
            return re.sub(r'<([^<>]+)>', '', message.content.lower())
        except re.error as e:
            logger.error(f"Regex error in cleanmsg: {e}")
            return message.content.lower()

    async def handle_spam(self, message):
        if ("Gift 50$" in message.content):
            logger.info('Spam Detected')
            if (message.channel.id == dildya):
                await message.channel.send(message.author.mention + " " + "Allah ni marzi")
            else:
                try:
                    if message.channel.permissions_for(message.guild.me).manage_messages:
                        await message.delete()
                    else:
                        logger.warning("Missing permissions to delete messages in this channel.")
                except Exception as e:
                    logger.error(f"Failed to delete spam message: {e}")

    async def send_response(self, message, min_length, content=None, files=None, embed=None, reference=True):
        cleaned = await self.cleanmsg(message)
        if len(cleaned) > min_length:
            kwargs = {"content": content} if content else {}
            if files:
                # Handle both local files and URLs
                file_list = files if isinstance(files, list) else [files]
                discord_files = []
                for f in file_list:
                    # If it's a URL, add it to content instead of trying to open as file
                    if isinstance(f, str) and (f.startswith('http://') or f.startswith('https://')):
                        if kwargs.get("content"):
                            kwargs["content"] += f"\n{f}"
                        else:
                            kwargs["content"] = f
                    else:
                        # It's a local file path
                        discord_files.append(discord.File(f))
                
                if discord_files:
                    kwargs["files"] = discord_files
            if embed:
                kwargs["embed"] = embed
            if reference:
                kwargs["reference"] = message
            await message.channel.send(**kwargs)

    async def read_ngrok_url(self):
        if os.path.exists(NGROK_URL_FILE):
            try:
                with open(NGROK_URL_FILE, "r") as f:
                    data = json.load(f)
                    return data.get("ngrok_url", "⚠️ Ngrok URL not available!")
            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"Error reading ngrok URL file: {e}")
                return "⚠️ Error reading ngrok URL file!"
        return "⚠️ Ngrok URL file not found!"

    async def rizz_fun(self, id, val):
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
            with open("unspoken.txt", "w") as file:
                file.writelines(lines)
        return value

    async def out_of_context(self, message):
        if message.channel.id == outofcontext_c:
            if message.attachments:
                for attachment in message.attachments:
                    target_extensions = (".jpeg", ".jpg", ".png")
                    if attachment.filename.lower().endswith(target_extensions):
                        await message.add_reaction("👀")
                        break
            else:
                if message.author.id not in alpha_ids:
                    await message.delete()
                    await message.author.send(random.choice(out_of_context_responses))

    async def check_context(self, message):
        user_message_counts = {}
        count = 0
        if not isinstance(message.channel, discord.DMChannel):
            async for msg in message.channel.history(limit=10):
                author = msg.author.id
                if author in user_message_counts:
                    user_message_counts[author] += 1
                    count += 1
                else:
                    user_message_counts[author] = 1
                    count += 1
            if len(user_message_counts.items()) == 2 and count == 10:
                return user_message_counts.keys()
            return None

    async def unspokenrizz(self, message, odds):
        mem = message.author.id
        if message.channel.id == unspoken_rizz:
            if mem in rizzelers:
                if message.attachments:
                    for attachment in message.attachments:
                        target_extensions = (".jpeg", ".jpg", ".png")
                        if attachment.filename.lower().endswith(target_extensions):
                            if mem != cb:
                                rizz_level = await self.rizz_fun(mem, 1)
                                await self.send_response(message, -1, random.choice(rizzplus) + "\nRizz Level = " + str(rizz_level))
                                await message.channel.send(file=discord.File("data/vids/RizzUp.mp4"))
                                break
                            else:
                                odds_rizz = random.choice(["1","-1","-1","-1","1"])
                                odds_rizz = int(odds_rizz)
                                rizz_level = await self.rizz_fun(mem, odds_rizz)
                                if odds_rizz == 1:
                                    await self.send_response(message, -1, random.choice(rizzplus) + "\nRizz Level = " + str(rizz_level))
                                    await message.channel.send(file=discord.File("data/vids/RizzUp.mp4"))
                                    break
                                else:
                                    await self.send_response(message, -1, random.choice(rizzminus) + "\nRizz Level = " + str(rizz_level))
                                    await message.channel.send(file=discord.File("data/vids/RizzDown.mp4"))
                                    break
                if odds == 3:
                    rizzres = ["https://cdn.discordapp.com/emojis/1118471926860496938.gif?size=128&quality=lossless", "<:Gigachad:970932041027829770>"]
                    await self.send_response(message, 8, random.choice(rizzres))
                    return
                else:
                    return

    async def handle_specific_texts(self, message):
        content = message.content.lower()
        for phrase, response in PHRASE_RESPONSES.items():
            if phrase in content:
                await self.send_response(message, 1, response)
                return True
        return False

    async def insult(self, message):
        if any(string in message.content.lower() for string in insults):
            logger.info('Insult Detected')
            return True

    # Command Definitions
    # Slash commands disabled - using text-based commands instead
    # @app_commands.command(name="do_nothing", description="Do nothing")
    # async def do_nothing(self, interaction: discord.Interaction):
    #     await interaction.response.send_message("*Does Nothing*")

    # @app_commands.command(name="getapi", description="Get the current ngrok API URL")
    # async def get_api(self, interaction: discord.Interaction):
    #     try:
    #         if interaction.user.id != sani:
    #             return await interaction.response.send_message("❌ Agla laa", ephemeral=True)
    #         ngrok_url = await self.read_ngrok_url()
    #         if not ngrok_url:
    #             return await interaction.response.send_message(
    #                 "❌ API not currently available. Please check if the monitoring service is running.",
    #                 ephemeral=True
    #             )
    #         message_content = f"• [Direct Access Link]({ngrok_url})\n"
    #         await interaction.response.send_message(message_content, ephemeral=True)
    #     except Exception as e:
    #         await interaction.response.send_message(f"⚠️ An error occurred: {str(e)}", ephemeral=True)

    # @app_commands.command(name="getip", description="Get the current host IP")
    # async def get_ip(self, interaction: discord.Interaction):
    #     try:
    #         if interaction.user.id != sani:
    #             return await interaction.response.send_message("❌ Agla laa", ephemeral=True)
    #         ip = os.popen("hostname -I").read().strip()
    #         if not ip:
    #             return await interaction.response.send_message(
    #                 "❌ IP not currently available. Please check if the monitoring service is running.",
    #                 ephemeral=True
    #             )
    #         message_content = f"• IP: {ip}\n"
    #         await interaction.response.send_message(message_content, ephemeral=True)
    #     except Exception as e:
    #         await interaction.response.send_message(f"⚠️ An error occurred: {str(e)}", ephemeral=True)

    # @app_commands.command(name="sync_commands", description="Force sync bot commands")
    # async def sync_commands(self, interaction: discord.Interaction):
    #     if interaction.user.id != sani:
    #         return await interaction.response.send_message("❌ Agla laa", ephemeral=True)
    #     try:
    #         # Clear guild commands first
    #         self.tree.clear_commands(guild=discord.Object(id=GUILD_ID))
    #         # Clear global commands
    #         self.tree.clear_commands(guild=None)
    #         
    #         # Copy all commands to global
    #         self.tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
    #         
    #         # Sync globally (for DMs)
    #         await self.tree.sync()
    #         # Sync to guild (faster updates in server)
    #         await self.tree.sync(guild=discord.Object(id=GUILD_ID))
    #         
    #         await interaction.response.send_message("✅ Commands cleared and synced successfully (global + guild)", ephemeral=True)
    #     except Exception as e:
    #         await interaction.response.send_message(f"⚠️ Error syncing commands: {str(e)}", ephemeral=True)

    # @app_commands.command(name="getlogs", description="Retrieve the last set of bot logs")
    # @app_commands.describe(lines="Number of log lines to retrieve", to_dm="Send logs to DMs")
    # async def get_logs(self, interaction: discord.Interaction, lines: int = 50, to_dm: bool = False):
    #     if interaction.user.id != sani:
    #         return await interaction.response.send_message("❌ Agla laa", ephemeral=True)
    #     try:
    #         if not interaction.channel.permissions_for(interaction.guild.me).send_messages:
    #             return await interaction.response.send_message(
    #                 "⚠️ I don't have permission to send messages in this channel!", ephemeral=True
    #             )
    #         if not os.path.exists("bot.log"):
    #             return await interaction.response.send_message("⚠️ Log file not found!", ephemeral=True)
    #         with open("bot.log", "r") as f:
    #             log_lines = f.readlines()[-lines:]
    #             log_content = "".join(log_lines).strip()
    #         if not log_content:
    #             return await interaction.response.send_message("⚠️ Log file is empty!", ephemeral=True)
    #         if to_dm:
    #             try:
    #                 user = interaction.user
    #                 if len(log_content) > 2000:
    #                     with open("temp_logs.txt", "w") as temp_file:
    #                         temp_file.write(log_content)
    #                     await user.send(
    #                         content=f"📜 Last {lines} lines of bot logs (sent to DMs):",
    #                         file=discord.File("temp_logs.txt")
    #                     )
    #                     os.remove("temp_logs.txt")
    #                     await interaction.response.send_message(
    #                         "✅ Logs sent to your DMs as a file!", ephemeral=True
    #                     )
    #                 else:
    #                     await user.send(
    #                         content=f"📜 Last {lines} lines of bot logs (sent to DMs):\n```\n{log_content}\n```"
    #                     )
    #                     await interaction.response.send_message(
    #                         "✅ Logs sent to your DMs!", ephemeral=True
    #                     )
    #             except discord.Forbidden:
    #                 await interaction.response.send_message(
    #                     "⚠️ I couldn't send you a DM. Please enable DMs from server members or unblock me!", ephemeral=True
    #                 )
    #             except Exception as e:
    #                 logger.error(f"Error sending logs to DM: {e}")
    #                 await interaction.response.send_message(
    #                     f"⚠️ Error sending logs to DM: {str(e)}", ephemeral=True
    #                 )
    #         else:
    #             if len(log_content) > 2000:
    #                 with open("temp_logs.txt", "w") as temp_file:
    #                     temp_file.write(log_content)
    #                 await interaction.response.send_message(
    #                     content=f"📜 Last {lines} lines of bot logs (too long, sending as file):",
    #                     file=discord.File("temp_logs.txt"),
    #                     ephemeral=True
    #                 )
    #                 os.remove("temp_logs.txt")
    #             else:
    #                 await interaction.response.send_message(
    #                     content=f"📜 Last {lines} lines of bot logs:\n```\n{log_content}\n```",
    #                     ephemeral=True
    #                 )
    #     except Exception as e:
    #         logger.error(f"Error retrieving logs: {e}")
    #         await interaction.response.send_message(
    #             f"⚠️ Error retrieving logs: {str(e)}", ephemeral=True
    #         )


    async def on_ready(self):
        # Slash commands disabled - using text-based commands instead
        # try:
        #     # Sync commands globally for DM support
        #     await self.tree.sync()
        #     logger.info(f"Successfully synced commands globally")
        #     # Also sync to guild for faster availability in server
        #     await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        #     logger.info(f"Successfully synced commands for guild {GUILD_ID}")
        # except Exception as e:
        #     logger.error(f"Failed to sync commands: {e}")
        logger.info('It is Gold Eagle to Shadow Company, how Copy')
        logger.info(f"Bot is in {len(self.guilds)} guilds: {[f'{g.name} ({g.id})' for g in self.guilds]}")
        
        guild = self.get_guild(GUILD_ID)
        if guild is None:
            logger.error(f"Guild {GUILD_ID} not found. Ensure the bot is in the guild and GUILD_ID is correct.")
            return
        for emoji in guild.emojis:
            (self.animated_emojis if emoji.animated else self.regular_emojis).append(emoji)
        logger.info(f"Loaded {len(self.animated_emojis)} animated and {len(self.regular_emojis)} regular emojis from guild {GUILD_ID}")
        
        user = self.get_user(sani)
        try:
            # Send a random GIF URL (gifs list contains URLs, not file paths)
            await user.send(random.choice(gifs))
        except Exception as e:
            logger.error(f"Failed to send startup message to user: {e}")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            self.tracked_messages[message.id] = {
                'content': message.content,
                'username': message.author.name,
            }
            return
        if message.author.id == eghost:
            logger.info('Clash Detected')
            return
        if message.author.bot:
            if message.author.id not in bot_ids:
                logger.info('Bot Detected')
                return
        if "https://" in message.content.lower():
            logger.info('External link Detected')
            return

        await self.process_commands(message)
        mem = message.author.id
        x = random.randint(0, 26)
        odds = random.randint(1, 6)

        # Text-based admin commands for user sani
        if mem == sani:
            content_lower = message.content.lower().strip()
            
            if content_lower == "getapi":
                try:
                    ngrok_url = await self.read_ngrok_url()
                    if ngrok_url and not ngrok_url.startswith("⚠️"):
                        await message.channel.send(f"• [Direct Access Link]({ngrok_url})")
                    else:
                        await message.channel.send(ngrok_url)
                    return
                except Exception as e:
                    await message.channel.send(f"⚠️ An error occurred: {str(e)}")
                    return
            
            elif content_lower == "getip":
                try:
                    ip = os.popen("hostname -I").read().strip()
                    if ip:
                        await message.channel.send(f"• IP: {ip}")
                    else:
                        await message.channel.send("⚠️ IP not currently available.")
                    return
                except Exception as e:
                    await message.channel.send(f"⚠️ An error occurred: {str(e)}")
                    return
            
            elif content_lower == "getlogs":
                try:
                    if not os.path.exists("bot.log"):
                        await message.channel.send("⚠️ Log file not found!")
                        return
                    
                    with open("bot.log", "r") as f:
                        log_lines = f.readlines()[-50:]
                        log_content = "".join(log_lines).strip()
                    
                    if not log_content:
                        await message.channel.send("⚠️ Log file is empty!")
                        return
                    
                    if len(log_content) > 2000:
                        with open("temp_logs.txt", "w") as temp_file:
                            temp_file.write(log_content)
                        await message.channel.send(
                            content=f"📜 Last 50 lines of bot logs:",
                            file=discord.File("temp_logs.txt")
                        )
                        os.remove("temp_logs.txt")
                    else:
                        await message.channel.send(f"📜 Last 50 lines of bot logs:\n```\n{log_content}\n```")
                    return
                except Exception as e:
                    logger.error(f"Error retrieving logs: {e}")
                    await message.channel.send(f"⚠️ Error retrieving logs: {str(e)}")
                    return

        await self.out_of_context(message)
        await self.unspokenrizz(message, odds)
        await self.handle_spam(message)

        if mem not in alpha_ids and await self.insult(message):
            if odds > 1 and x < 6:
                await self.send_response(message, 1, files="data/vids/galinai.mp4")

        if message.channel.id not in prohibited_channels:
            if any(string in message.content for string in bye):
                logger.info('Good Bye')
                await self.send_response(message, 1, "Allah hi Hafiz ha tumhara")
                return
            if any(string in message.content for string in sensitive_words):
                logger.info('O Allah the Almighty')
                return

        if await self.handle_specific_texts(message):
            return

        if 10 <= x <= 12 and message.channel.id not in (unspoken_rizz, randi_rano, outofcontext_c):
            try:
                await RESPONSE_PROBABILITIES["animated_emoji"]["action"](self, message)
            except Exception as e:
                logger.error(f"Emoji reaction error: {e}")

            if not message.attachments or message.channel.id not in prohibited_channels:
                if mem not in alpha_ids:
                    choice = random.choices(
                        list(RESPONSE_PROBABILITIES.keys()),
                        weights=[r["weight"] for r in RESPONSE_PROBABILITIES.values()],
                        k=1
                    )[0]
                    if choice in ("beta_video", "thisu_gif", "text_response", "talha_quote", "response_video"):
                        await RESPONSE_PROBABILITIES[choice]["action"](self, message)
                else:
                    if mem in alpha_ids or mem == talha:
                        choice = random.choices(
                            ["alpha_video", "sigma_text", "gigachad_reaction"],
                            weights=[0.33, 0.33, 0.34],
                            k=1
                        )[0]
                        await RESPONSE_PROBABILITIES[choice]["action"](self, message)

        # if mem == qasim:
        #     files = [discord.File(f"data/pics/qasim{i}.png") for i in ("", "1")]
        #     await message.channel.send(files=files, reference=message)

        if mem in (rand, pixbot):
            s = random.randint(1, 8)
            logger.info(f'Random bot response: {s}')
            if f'<@{echad}>' in message.content:
                await self.send_response(message, 1, random.choice(bestyoucando))
                return
            logger.info('Bot has entered the chat')
            if s == 1:
                await self.send_response(message, -1, files="data/vids/yekoi.mp4")
            elif s == 3:
                await self.send_response(message, -1, files="data/vids/rajpal.mp4")
            elif (s == 5 or s == 6) and mem == rand:
                await self.send_response(message, -1, files=f"data/vids/Majboor{random.randint(1,3)}.mp4")
            elif s == 7:
                await self.send_response(message, -1, files=f"data/gifs/{random.choice(bot_gifs)}")

        if mem == cb:
            if x in (2, 3):
                await self.send_response(message, 8, "Ok Owo Shit")
            elif x in (7, 8):
                await self.send_response(message, 8, "Okie Donkie")

        if mem == koni:
            if x == 2 and len(message.content) > 7:
                files = [discord.File(f"data/pics/konain{i}.png") for i in ("2", "3")]
                await message.channel.send(files=files)
            elif x == 3 and len(message.content) > 7:
                files = [discord.File(f"data/pics/koni{i}.jpg") for i in ("", "2")]
                await message.channel.send(files=files)

        fasiilist = ["Ok Gay", "Ok Khassi"]
        if mem == aj:
            if not message.attachments:
                if x in (2, 3, 7):
                    await self.send_response(message, 8, random.choice(fasiilist))
                elif x in (4, 5):
                    await message.channel.send(files=[discord.File("data/pics/fasi.jpg")])

        if mem == talha:
            if not message.attachments:
                if x in (2, 3):
                    await self.send_response(message, 6, "Ok  :flag_pk:i")
                elif x in (9, 4):
                    await message.add_reaction(':flag_pk:')
                elif x in (5, 6) and len(message.content) > 7:
                    files = [discord.File(f"data/pics/talha{i}.png") for i in ("", "1", "2")]
                    await message.channel.send(files=files)
                elif x == 7:
                    files = [discord.File(f"data/pics/taruha{i}.png") for i in ("", "1")]
                    await message.channel.send(files=files)
                elif x == 8:
                    files = [discord.File(f"data/pics/taruha{i}.png") for i in ("2", "3")]
                    await message.channel.send(files=files)
                elif x == 9:
                    await self.send_response(message, -1, files="data/pics/taruha5.png")
                elif x == 10:
                    await self.send_response(message, -1, files="data/gifs/taruha.gif")

        user = self.get_user(qasim)
        if message.author == user:
            if not message.attachments:
                if x in (2, 3):
                    await self.send_response(message, 12, f"Nai kya matlab ha tumhara. <@{random.choice(qasimchoice)}>. Idhr ayen zara")
                elif x in (7, 9) and len(message.content) > 7:
                    files = [discord.File(f"data/pics/qasim{i}.png") for i in ("1", "")]
                    await message.channel.send(files=files)

        if "<@&1067810754088153094>" in message.content:
            logger.info('You called?')
            await self.send_response(message, 1, random.choice(u_called))

    async def on_message_delete(self, message):
        mem = message.author.id
        if message.attachments and message.channel.id == unspoken_rizz:
            return
        if message.id in self.tracked_messages:
            deleted_message = self.tracked_messages[message.id]
            logger.info(f"Message deleted by: {deleted_message['username']}")
            logger.info(f"Deleted message: {deleted_message['content']}")
            await message.channel.send(message.content)
            await message.channel.send(random.choice(msgdelbot))
        if mem != sani and not message.author.bot and message.content:
            try:
                embed = discord.Embed(
                    title=(message.author.nick or f'<@{mem}>') + "'s Deleted Message",
                    description=message.content,
                    color=discord.Color.red()
                )
                await message.channel.send(content=f'\n<@{mem}> {random.choice(msgdel)}\n\n', embed=embed)
            except Exception as e:
                logger.error(f"Error sending deleted message embed: {e}")
                embed = discord.Embed(
                    title=f'<@{mem}>' + "'s Deleted Message",
                    description=message.content,
                    color=discord.Color.red()
                )
                await message.channel.send(content=f'\n<@{mem}> {random.choice(msgdel)}\n\n', embed=embed)

    async def on_message_edit(self, b4message, afmessage):
        mem = b4message.author.id
        if b4message.attachments or "https://" in b4message.content.lower() or ".gif" in b4message.content.lower():
            return
        if mem not in alpha_ids and not b4message.author.bot and b4message.content:
            try:
                embed = discord.Embed(
                    title=(b4message.author.nick or f'<@{mem}>') + "'s Edited Message",
                    description="",
                    color=discord.Color.red()
                )
                embed.add_field(name='Original Message', value=b4message.content, inline=False)
                embed.add_field(name='Edited Message', value=afmessage.content, inline=False)
                await b4message.channel.send(content=f'\n<@{mem}> {random.choice(msgdel)}\n\n', embed=embed)
            except Exception as e:
                logger.error(f"Error sending edited message embed: {e}")

    async def on_member_join(self, member):
        if member.guild.id == 790490721450459177:
            return
        channel = member.guild.system_channel
        img = f"data/pics/agya{random.randint(1,2)}.jpg"
        await channel.send(member.mention)
        await channel.send(file=discord.File(img))

    async def on_member_remove(self, member):
        emoji = "<:catcry:938332538995367956>"
        moji = f"{emoji}  {emoji}  {emoji}  {emoji}  {emoji}  {emoji}"
        channel = member.guild.system_channel
        await channel.send(f'{member.mention} nahi rhe {moji}')
        await channel.send(file=discord.File("data/gifs/Adil.gif"))

# Run the bot
bot = MyBot()
bot.run(TOKEN)