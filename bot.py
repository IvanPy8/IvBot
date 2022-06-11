import discord
import random

TOKEN = "OTc3NTk3OTM4ODQ5MTg1ODQy.GQvfdr.LuYcZVw42jUQ9OlViaHhiQfbSn2xDTmCztXBLg"

intents = discord.Intents.all()
perm = discord.Permissions.all()
perm.ban_members = True
perm.kick_members = True
intents.members = True
client = discord.Client(intents=intents, permissions=perm)
COMMANDS = {"/прив": ["Привет", "Приветствую", "Кого я вижу!"], "/как дела": ["\U0001F916Хорошо, я же **робот**",
                                                                              "Все отлично!", "ЗаБИПчательно\U0001F916!"],
            "/чем занимаешься": ["\u2709Сижу тут, сообщения читаю, отвечаю...", "Тебе пишу\U0001F600!"],
            "/чем ты питаешься": ["Бип-буп. Бап. \U0001F50B_**Электричеством**_", "Памятью компьютера :D"],
            "/хелп": ["Меня зовут @Ivan_bot#7309 \U0001F916\nМой создатель: @Иван ИС8#9319\nКоманды:\n  /прив:"
                      " отправляет случайное приветствие. Работает с любыми командами, начинающимися на \"/прив\".\n  "
                      "/как дела: отправит случайный ответ. Работает с любыми командами, начинающимися на \"/как "
                      "дела\".\n  /чем занимаешься: отправит случайный ответ."
                      " Работает с любыми командами, начинающимися на \"/чем занимаешься\".\n  /чем ты питаешься:"
                      " отправит случайный ответ. Работает с любыми командами, начинающимися на \"/чем ты питаешься\"."
                      "\n  /забанить: блокирует участника.\n  Использование:\n    /забанить @Пример#0102\n"
                      "    /забанить @Другой_Пример#0897 Плохое поведение\n  /кикнуть: выгоняет участника."
                      "\n  Использование:\n    /кикнуть @Пример#9999\n"
                      "    /кикнуть @Другой_Пример#3456 Оскорбления в чате"]
            }


@client.event
async def on_ready():
    print(f"logged in as {client.user.name} with id {client.user.id}")


@client.event
async def on_message(message):
    channel = message.channel
    for key in COMMANDS.keys():
        if message.content.lower().startswith(key):
            await channel.send(random.choice(COMMANDS[key]))
    if message.content.lower().startswith("/забанить"):
        args = message.content.split(" ")[1:]
        banned = False
        try:
            for member in client.get_all_members():
                if str(member) == args[0]:
                    try:
                        await channel.send(f"{str(member)} был забанен. Причина: {args[1]}.")
                        await member.ban(reason=args[1])
                        banned = True
                    except IndexError:
                        await channel.send(f"{str(member)} был забанен. Причина не указана.")
                        await member.ban(reason="Причина не указана.")
                        banned = True
            if not banned:
                await channel.send(f"\u274C_Ошибка: **отсутствует участник с именем {args[0]}**_.")
        except IndexError:
            pass
    if message.content.lower().startswith("/кикнуть"):
        args = message.content.split(" ")[1:]
        kicked = False
        try:
            for member in client.get_all_members():
                if str(member) == args[0]:
                    try:
                        await channel.send(f"{str(member)} был кикнут. Причина: {args[1]}.")
                        await member.kick(reason=args[1])
                    except IndexError:
                        await channel.send(f"{str(member)} был кикнут. Причина не указана.")
                        await member.kick(reason="Причина не указана.")
                    kicked = True
                    break
            if not kicked:
                await channel.send(f"\u274C_Ошибка: **отсутствует участник с именем {args[0]}**_.")
        except IndexError:
            pass


client.run(TOKEN)
