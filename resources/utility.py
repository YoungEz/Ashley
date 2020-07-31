import discord
import operator
from pytz import timezone

from config import data as config
from random import choice
from asyncio import TimeoutError

responses = config['answers']
questions = config['questions']
color_embed = None
legend = {"-": -1, "Comum": 0, "Incomum": 1, "Raro": 2, "Super Raro": 3, "Ultra Raro": 4, "Secret": 5,
          "Legendary": 6, "Heroic": 7, "Divine": 8, "Sealed": 9, "For Pet": 10}


def include(string_, list_):
    for i in list_:
        if i.lower() in string_.lower():
            return True
    return False


def get_content(content):
    answer = content.replace("`", "[censored]").replace("*", "[censored]").replace("_", "[censored]") \
        .replace("~", "[censored]").replace("@", "[censored]").replace("here", "[censored]") \
        .replace("everyone", "[censored]").replace("ash ", "[censored]").replace("ash.", "[censored]")
    return answer


def choice_etherny():
    list_amount = {"yellow": 75, "purple": 20, "black": 5}
    list_items = []
    for i_, amount in list_amount.items():
        list_items += [i_] * amount
    answer = choice(list_items)
    return answer


def quant_etherny(amount):
    answer = {"amount": 0, "list": [0, 0, 0]}
    for _ in range(amount):
        etherny = choice_etherny()
        if etherny == "yellow":
            answer['amount'] += 1
            answer['list'][0] += 1
        elif etherny == "purple":
            answer['amount'] += 10
            answer['list'][1] += 1
        else:
            answer['amount'] += 100
            answer['list'][2] += 1
    return answer


def embed_creator(description, img_url, monster, hp_max, hp, monster_img, lower_net):
    global color_embed
    color = [0xff0000, 0xffcc00, 0x00cc00]
    if monster:
        color_embed = 0xf15a02
    else:
        color_value = (hp / (hp_max / 100))
        checkpoints = [1, 31, 71]
        for c in range(0, 3):
            if color_value > checkpoints[c]:
                color_embed = color[c]
    embed = discord.Embed(
        description=description,
        color=color_embed
    )
    if lower_net == 'disable':
        embed.set_image(url=img_url)
    embed.set_thumbnail(url=f"{monster_img}")
    return embed


def patent_calculator(rank_point, medal):
    amount_rp = 200
    amount_medal = 0
    count_medal = 0
    count_patent = 1
    patent = 0
    if 100 < rank_point < 200:
        patent += 1
    elif rank_point >= 200:
        while True:
            if rank_point >= amount_rp and medal >= amount_medal:
                amount_medal += count_medal
                amount_rp += 100
                count_medal += 1
                count_patent += 1
            else:
                patent = count_patent
                if patent >= 30:
                    patent = 30
                break
    return patent


def convert_item_name(item, db_items):
    for key in db_items.keys():
        if item.lower() in ['ficha', 'medalha', 'rank point']:
            item += "s"
        if item.lower() == db_items[key][1].lower():
            return key
    return None


async def paginator(bot, items, inventory, embed, ctx):
    descriptions = []
    cont = 0
    cont_i = 0
    description = ''

    if str(ctx.command) == "inventory":
        dict_ = dict()
        for _ in inventory.keys():
            dict_[_] = items[_][3]
        sorted_x = sorted(dict_.items(), key=operator.itemgetter(1), reverse=False)
        list_i = [sorted_x[x][0] for x in range(len(inventory.keys()))]
    else:
        list_i = inventory.keys()

    for key in list_i:
        if cont == 0:
            description = embed[2]
        if str(ctx.command) == "inventory":
            try:
                rarity = list(legend.keys())[list(legend.values()).index(items[key][3])]
                string = f'{items[key][0]} ``{inventory[key]}{("⠀" * (5 - len(str(inventory[key]))))}`` ' \
                         f'``{items[key][1]}{("-" * (30 - len(items[key][1])))}>`` **{rarity.lower()}**\n'
            except KeyError:
                string = f"<:negate:520418505993093130> ``{key.upper()}: ITEM NÃO ENCONTRADO!``"
        else:
            cost = "".join(f"{items[i[0]][0]} {i[0]}: **{i[1]}** **│** " for i in inventory[key]['cost'])
            reward = "".join(f"{items[i[0]][0]} {i[0]}: **{i[1]}** **│** " for i in inventory[key]['reward'])
            icon = inventory[key]['reward'][0][0]
            string = f"{items[icon][0]} ``{key.upper()}``\n**Custo:** {cost[:-7]} \n **Recompença:** {reward[:-7]}\n\n"
        cont += len(string)
        if cont <= 1500 and cont_i < 20:
            description += string
            cont_i += 1
        else:
            descriptions.append(description)
            description = f'{embed[2]}{string}'
            cont = len(description)
            cont_i = 0
    descriptions.append(description)
    cont = 0
    emojis = ['⬅', '➡', '✖']
    msg = await ctx.send('<:alert_status:519896811192844288>│``Aguarde...``')
    for c in emojis:
        await msg.add_reaction(c)
    while True:
        Embed = discord.Embed(
            title=embed[0],
            color=embed[1],
            description=descriptions[cont]
        )
        Embed.set_author(name=bot.user, icon_url=bot.user.avatar_url)
        Embed.set_thumbnail(url="{}".format(ctx.author.avatar_url))
        Embed.set_footer(text="Ashley ® Todos os direitos reservados.  [Pag {}/{}]".format(cont + 1, len(descriptions)))
        await msg.edit(embed=Embed, content='')
        try:
            reaction = await bot.wait_for('reaction_add', timeout=30.0)
        except TimeoutError:
            break
        while reaction[1].id != ctx.author.id:
            try:
                reaction = await bot.wait_for('reaction_add', timeout=30.0)
            except TimeoutError:
                break
        if reaction[0].emoji == '⬅' and cont > 0:
            cont -= 1
        if reaction[0].emoji == '➡' and cont < len(descriptions) - 1:
            cont += 1
        if reaction[0].emoji == '✖':
            break
    await msg.delete()


async def get_response(message):
    if len(message.content) > 10:
        if include(message.content, ['denky', 'pai', 'criador']):
            if message.author.id != 300592580381376513:
                response = choice(responses['denky_f'])
                return response
            else:
                return "Eu não consigo falar nada contra o senhor!"
        if include(message.content, questions['denky_r']) and include(message.content, ['ashley', 'ash']):
            response = choice(responses['resposta_ashley'])
            return response
        for c in range(0, len(questions['perg_pq'])):
            if questions['perg_pq'][c] in message.content.lower():
                response = choice(responses['resposta_pq'])
                return response
        for c in range(0, len(questions['perg_qual'])):
            if questions['perg_qual'][c] in message.content.lower():
                if questions['perg_qual'][c] == "quando":
                    response = choice(responses['resposta_quando'])
                    return response
                elif questions['perg_qual'][c] == "como":
                    response = choice(responses['resposta_como'])
                    return response
                elif questions['perg_qual'][c] == "onde":
                    response = choice(responses['resposta_onde'])
                    return response
                elif questions['perg_qual'][c] == "vamos":
                    response = choice(responses['resposta_vamos'])
                    return response
                elif questions['perg_qual'][c] == "qual":
                    response = choice(responses['resposta_qual'])
                    return response
                elif questions['perg_qual'][c] == "quanto":
                    response = choice(responses['resposta_quanto'])
                    return response
                elif questions['perg_qual'][c] == "quem":
                    response = choice(responses['resposta_quem'])
                    return response
                elif questions['perg_qual'][c] == "quer":
                    response = choice(responses['resposta_quer'])
                    return response
                elif questions['perg_qual'][c] == "o que" or questions['perg_qual'][c] == "oq":
                    response = choice(responses['resposta_o_que'])
                    return response
                else:
                    response = choice(responses['resposta_outras'])
                    return response
        if ' ou ' in message.content.lower():
            response = choice(responses['resposta_ou'])
            return response
    response = choice(responses['resposta_comum'])
    return response


def parse_duration(duration: int):
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    duration = []
    if days > 0:
        if days > 1:
            duration.append(f'{days} dias')
        else:
            duration.append(f'{days} dia')
    if hours > 0:
        if hours > 1:
            duration.append(f'{hours} horas')
        else:
            duration.append(f'{hours} hora')
    if minutes > 0:
        if minutes > 1:
            duration.append(f'{minutes} minutos')
        else:
            duration.append(f'{minutes} minuto')
    if seconds > 0:
        if seconds > 1:
            duration.append(f'{seconds} segundos')
        else:
            duration.append(f'{seconds} segundo')
    return ', '.join(duration)


def date_format(date):
    date_timezone = timezone("America/Recife")
    date_ = date.astimezone(date_timezone)
    return date_.strftime("%d/%m/%Y %H:%M")


PROVINCES = [542406551923720202,
             542406630218661929,
             542406759017611275,
             542406909278420992,
             542406979151462430,
             542407056339238922,
             542407122558779404,
             542407283750076514,
             542407345750278164,
             542407416768233530]

ERRORS = ['The check functions for command staff ban failed.',
          'The check functions for command staff kick failed.',
          'The check functions for command staff language failed.',
          'The check functions for command staff limpar failed.',
          'Command raised an exception: IndexError: list index out of range',
          'Command raised an exception: TimeoutError: ',
          'The check functions for command config guild failed.',
          'The check functions for command config report failed.',
          'The check functions for command staff slowmode failed.',
          'The check functions for command staff delete failed.',
          'The check functions for command logger failed.']

enforcado = ['''
```
X==:== 
X  :   
X   
X  
X  
X  
===========
```''', '''
```
X==:== 
X  :   
X  O   
X  
X  
X  
===========
```''', '''
```
X==:== 
X  :   
X  O   
X  | 
X  
X  
===========
```''', '''
```
X==:== 
X  :   
X  O   
X \| 
X 
X 
===========
```''', '''
```
X==:== 
X  :   
X  O   
X \|/ 
X  
X  
===========
```''', '''
```
X==:== 
X  :   
X  O   
X \|/ 
X /  
X  
===========
```
''', '''
```
X==:== 
X  :   
X  O   
X \|/ 
X / \ 
X 
===========
```''']
