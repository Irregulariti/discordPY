import discord
from discord.ext import commands, tasks
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])
import time
from threading import Thread

global v
v = ""
a = ["древнийлучник", "", "слизень", "", "стальнойстраж", "", "кошмар", "", "близнецы", "", "повелительогня", "",
     "паучиха", "", "утопленник", "", "колдун", "", "смерть", "", "наездник", "", "разбойник", "", "лавовыйкуб", "",
     "призрачныйохотник", "", "чёрныйдракон", "", "гигант", "", "снежныймонстр", "", "проклятыйлегион", "", "монстр",
     "", "некромант", "", "пожирательтьмы", "", "чудовище", "", "кузнец", "", "могущественныйшалкер", "", "заклинатель",
     "", "мёртвыйвсадник", ""]  # основной
e = ["Древний лучник", "", "Слизень", "", "Стальной страж", "", "Кошмар", "", "Близнецы", "", "Повелитель огня", "",
     "Паучиха", "", "Утопленник", "", "Колдун", "", "Смерть", "", "Наездник", "", "Разбойник", "", "Лавовый Куб", "",
     "Призрачный охотник", "", "Чёрный дракон", "", "Гигант", "", "Снежный монстр", "", "Проклятый легион", "",
     "Монстр",
     "", "Некромант", "", "Пожиратель тьмы", "", "Чудовище", "", "Кузнец", "", "Могущественный Шалкер", "",
     "Заклинатель",
     "", "Мёртвый всадник", ""]  # для вывода
t = ["древнийлучник", 1200, "слизень", 1800, "стальнойстраж", 2100, "кошмар", 1, "близнецы", 1, "повелитель огня", 3600,
     "паучиха", 10800, "утопленник", 1, "колдун", 14400, "смерть", 1, "наездник", 1, "разбойник", 9000, "лавовыйкуб",
     21600,
     "призрачныйохотник", 10800, "чёрныйдракон", 1, "гигант", 12600, "снежныймонстр", 3600, "проклятыйлегион", 25200,
     "монстр",
     1, "некромант", 1, "пожирательтьмы", 16200, "чудовище", 27000, "кузнец", 18000, "могущественныйшалкер", 19800,
     "заклинатель",
     1, "мёртвыйвсадник", 21600]  # фикс список


def timer():
    while True:
        for i in range(1, len(a) + 1, 2):
            if a[i] != "":
                a[i] = a[i] - 1
                h = int((a[i] / 60) // 60)
                m = int((a[i] // 60) - (h * 60))
                if m != 0:
                    e[i] = str(m) + "мин."
                    if h != 0:
                        e[i] = str(h) + "ч." + e[i]
        time.sleep(1)


def restart():
    while True:
        for i in range(1, len(a) + 1, 2):
            try:
                if a[i] <= 0:
                    e[i] = "Босс запущен"
            except TypeError:
                continue


@bot.command()
async def ввод(ctx, v, b, c):
    v = str(v)
    v = v.lower()
    v = v.replace(" ", "")
    for i in range(0, len(a), 2):
        if a[i].find(v) >= 0:
            v = a[i]
            break
    b, c = int(b), int(c)
    d = (b * 60 + c) * 60
    a[a.index(v) + 1] = d  # замена времени в основном списке боссов
    await ctx.send('{новый таймер на босса' + " " + str(e[a.index(v)]) + " " + "запущен}", delete_after=2)


@bot.command()
async def рестарт(ctx, v):
    v = v.lower()
    v = v.replace(" ", "")
    for i in range(0, len(a), 2):
        if a[i].find(v) >= 0:
            v = a[i]
            break
    a[t.index(v) + 1] = t[t.index(v) + 1]  # реплэйс основного списка статичным временем
    await ctx.send('{Босс' + " " + str(e[a.index(v)]) + " " + "рестартнут}", delete_after=2)


@bot.command()
async def чпб(ctx):
    q = 15
    st = "| "
    for i in range(0, len(e)):
        if i % 2 == 0:
            st = st + e[i] + "[" + str(q) + "]" + " - "
            if i != 30 and i < 48:
                q += 5
            elif i >= 48:
                q += 10
        else:
            st = st + e[i] + " " + "|" + " "
    await ctx.send(st)


@bot.command()
async def хелп(ctx):
    await ctx.send("-ввод [Название Босса(слитно)] [часы] [минуты]" + " - ввод времени вручную\n-рестарт [Название Босса(слитно)] " + " - рестарт времени на стандартное\n-чпб - выводит расписание боссов\n-clear - очищает все сообщения канала\n-near - выводит боссов до которых осталось менее 10 минут\n(Также вы можете вводить название боссов не полностью, а лишь частично. Например: Могущественный Шалкер - шалкер, Слизень - слиз и т.д)")

@bot.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send('{Сообщения успешно удалены}', delete_after=2)


@bot.command()
async def near(ctx):
    q = 15
    c = []
    ct = ""
    for i in range(1, len(a) + 1, 2):
        if a[i] != "":
            if a[i] <= 600:
                c.append(e[i - 1])
                c.append(e[i])
    for i in range(0, len(c)):
        if i % 2 == 0:
            ct = ct + str(c[i]) + " " + "-"
            if i != 30 and i < 48:
                q += 5
            elif i >= 48:
                q += 10
        else:
            ct = ct + " " + str(c[i]) + " " + "|" + " "
    try:
        await ctx.send(ct)
    except discord.errors.HTTPException:
        None
@bot.command()
async def заменастандартноговремени(ctx,v,vr):
    vr=int(vr)
    v=str(v)
    v = v.lower()
    v = v.replace(" ", "")
    for i in range(0, len(a), 2):
        if a[i].find(v) >= 0:
            v = a[i]
            break
    t[a.index(v)+1]=vr
Thread(target=timer).start()
Thread(target=restart).start()
bot.run(settings['token'])
