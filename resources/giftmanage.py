from random import choice, randint
from config import data as config
from resources.verify_cooldown import verify_cooldown


def generate_gift():
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    key = ['AySeHlLhEsYa', 'aYsEhLlHeSyA']
    lgt = list()
    gift = str()
    fgift = str()
    for L in key[choice([0, 1])]:
        lgt.append(L.upper())
        lgt.append(ord(L))
    for c in range(len(lgt)):
        if c % 2 == 0:
            gift += str(lgt[c])
        else:
            gift += str(choice(gentype))
    for L in range(len(gift)):
        if L % 5 == 0 and L != 0:
            fgift += '-'
        fgift += gift[L]
    fgift += str(choice(gentype))
    gift += fgift[-1]
    return fgift, gift


async def register_gift(bot, time):
    while True:
        gift_t, _id = generate_gift()
        data = await bot.db.get_data("_id", _id, "gift")
        if data is None:
            data = {"_id": _id, "gift_t": gift_t, "validity": time}
            await bot.db.push_data(data, "gift")
            if not await verify_cooldown(bot, _id, time):
                return gift_t


async def open_gift(bot, gift):
    if "-" in gift:
        key = "gift_t"
    else:
        key = "_id"

    data = await bot.db.get_data(key, gift, "gift")

    if data is not None:

        _id = data['_id']
        time = data['validity']

        if await verify_cooldown(bot, _id, time, True):
            validity = True
        else:
            validity = False

        ethernyas = randint(250, 300)
        coins = randint(50, 100)
        items = ['crystal_fragment_light', 'crystal_fragment_energy', 'crystal_fragment_dark', 'Energy']

        rare = None
        chance = randint(1, 100)
        if chance <= 50:
            item_1 = choice(['Unearthly', 'Surpassing', 'Hurricane', 'Heavenly', 'Blazing', 'Augur'])
            item_2 = choice(['Crystal_of_Energy', 'Discharge_Crystal', 'Acquittal_Crystal'])
            item_3 = choice(['SoulStoneYellow', 'SoulStoneRed', 'SoulStonePurple', 'SoulStoneGreen',
                             'SoulStoneDarkGreen', 'SoulStoneBlue'])
            rare = [item_1, item_2, item_3]

            if chance < 15:
                item_plus = choice(["soul_crystal_of_love", "soul_crystal_of_love", "soul_crystal_of_love",
                                    "soul_crystal_of_hope", "soul_crystal_of_hope", "soul_crystal_of_hope",
                                    "soul_crystal_of_hate", "soul_crystal_of_hate", "soul_crystal_of_hate",
                                    "fused_diamond", "fused_diamond", "fused_ruby", "fused_ruby",
                                    "fused_sapphire", "fused_sapphire", "fused_emerald", "fused_emerald",
                                    "unsealed_stone", "melted_artifact"])
                rare.append(item_plus)

        return {"money": ethernyas, "coins": coins, "items": items, "rare": rare, "validity": validity}

    else:
        return None


def open_chest(chest):

    if chest == "Baú de Evento - Incomum":
        chance_relic = 30
        max_money = 250
        max_coin = 100
        max_energy = 75
        bonus = choice(['Unearthly', 'Surpassing', 'Hurricane', 'Heavenly', 'Blazing', 'Augur'])
        items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus]

        relics = {
            "WrathofNatureCapsule": 1,
            "UltimateSpiritCapsule": 1,
            "SuddenDeathCapsule": 1,
            "InnerPeacesCapsule": 1,
            "EternalWinterCapsule": 1,
            "EssenceofAsuraCapsule": 1,
            "DivineCalderaCapsule": 1,
            "DemoniacEssenceCapsule": 1,
            "unsealed_stone": 3,
            "melted_artifact": 3,
            "boss_key": 3,
            "angel_stone": 3,
            "angel_wing": 3
        }

    elif chest == "Baú de Evento - Raro":
        chance_relic = 60
        max_money = 300
        max_coin = 150
        max_energy = 100
        bonus = choice(["soul_crystal_of_love", "soul_crystal_of_hope", "soul_crystal_of_hate"])
        items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus]

        relics = {
            "WrathofNatureCapsule": 3,
            "UltimateSpiritCapsule": 3,
            "SuddenDeathCapsule": 3,
            "InnerPeacesCapsule": 3,
            "EternalWinterCapsule": 3,
            "EssenceofAsuraCapsule": 3,
            "DivineCalderaCapsule": 3,
            "DemoniacEssenceCapsule": 3,
            "unsealed_stone": 3,
            "melted_artifact": 3,
            "boss_key": 3,
            "angel_stone": 3,
            "angel_wing": 3
        }

    elif chest == "Baú de Evento - Super Raro":
        chance_relic = 90
        max_money = 350
        max_coin = 200
        max_energy = 125
        bonus = choice(["solution_agent_green", "solution_agent_blue", "nucleo_z", "nucleo_y", "nucleo_x"])

        if randint(1, 100) < 60:
            bb = choice(['crystal_of_death', 'enchanted_stone', '?-Bollash', 'nucleo_z', 'nucleo_y', 'nucleo_x'])
            items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus, bb]
        else:
            items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus]

        relics = {
            "WrathofNatureCapsule": 5,
            "UltimateSpiritCapsule": 5,
            "SuddenDeathCapsule": 5,
            "InnerPeacesCapsule": 5,
            "EternalWinterCapsule": 5,
            "EssenceofAsuraCapsule": 5,
            "DivineCalderaCapsule": 5,
            "DemoniacEssenceCapsule": 5,
            "unsealed_stone": 1,
            "melted_artifact": 1,
            "boss_key": 1,
            "angel_stone": 1,
            "angel_wing": 1
        }

    else:
        chance_relic = 100
        max_money = 400
        max_coin = 250
        max_energy = 150
        bonus = choice(["fused_diamond", "fused_ruby", "fused_sapphire", "fused_emerald"])

        if randint(1, 100) < 80:
            bb = choice(['unsealed_stone', 'melted_artifact', 'boss_key', 'angel_stone', 'angel_wing'])
            items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus, bb]
        else:
            items = ['Discharge_Crystal', 'Crystal_of_Energy', 'Acquittal_Crystal', bonus]

        relics = {
            "WrathofNatureCapsule": 1,
            "UltimateSpiritCapsule": 1,
            "SuddenDeathCapsule": 1,
            "InnerPeacesCapsule": 1,
            "EternalWinterCapsule": 1,
            "EssenceofAsuraCapsule": 1,
            "DivineCalderaCapsule": 1,
            "DemoniacEssenceCapsule": 1
        }

    ethernyas = randint(200, max_money)
    coins = randint(50, max_coin)
    Energy = randint(50, max_energy)

    relic = None
    if randint(1, 100) <= chance_relic:
        list_relic = []
        for k, v in relics.items():
            list_relic += [k] * v
        relic = choice(list_relic)

    return {"money": ethernyas, "coins": coins, "Energy": Energy, "items": items, "relic": [relic]}
