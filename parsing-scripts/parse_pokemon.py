import json
import re


def parse_basic_string(regex):
    def F(mon_text):
        match = re.search(regex, mon_text, re.MULTILINE)
        if match:
            result = match.group(1)
            return result

    return F


def parse_number(regex):
    def F(mon_text):
        num_match = re.search(regex, mon_text, re.MULTILINE)
        if num_match:
            num_raw = num_match.group(1)
            num = int(num_raw)
            return num


# Index
parse_pokedex_number = parse_number(r"^\[(\d+)\]")


# Name
parse_pokemon_name = parse_basic_string(r"^Name = (.+)")


# InternalName
parse_internal_name = parse_basic_string(r"^InternalName = (.+)")


# Type1
# Type2
def parse_types(mon_text):
    types = []
    type1_match = re.search(r"^Type1 = (.+)", mon_text, re.MULTILINE)
    type1 = type1_match.group(1).title()

    types.append(type1)

    type2_match = re.search(r"^Type2 = (.+)", mon_text, re.MULTILINE)
    if type2_match:
        type2 = type2_match.group(1).title()
        types.append(type2)

    return types


# BaseStats
def parse_base_stats(mon_text):
    stats_match = re.search(r"^BaseStats = (.+)", mon_text, re.MULTILINE)
    stats_row = stats_match.group(1)
    stats_nums = [int(stat) for stat in stats_row.split(",")]
    # HP, Attack, Defense, Speed, Sp. Atk, Sp. Def
    stats = {
        "hp": stats_nums[0],
        "attack": stats_nums[1],
        "defense": stats_nums[2],
        "speed": stats_nums[3],
        "sp_atk": stats_nums[4],
        "sp_def": stats_nums[5],
    }
    return stats


# GenderRate
# Adapted from Plugins/Tectonic Master Dex/PokeDex Entry/PokemonPokedexInfo_Scene.rb
gender_rate_map = {
    "AlwaysMale": "Male",
    "FemaleOneEighth": "7/8 Male",
    "Female25Percent": "3/4 Male",
    "Female50Percent": "50/50",
    "Female75Percent": "3/4 Fem.",
    "FemaleSevenEighths": "7/8 Fem.",
    "AlwaysFemale": "Female",
    "Genderless": "None",
}


def parse_gender_rate(mon_text):
    rate_match = re.search(r"^GenderRate = (.+)", mon_text, re.MULTILINE)
    rate_raw = rate_match.group(1)
    rate = gender_rate_map[rate_raw]
    return rate


# GrowthRate
# Some names are abbreviated in-game, their full canon names are used here
growth_rate_map = {
    "Medium": "Medium Fast",
    "Erratic": "Erratic",
    "Fluctuating": "Fluctuating",
    "Parabolic": "Medium Slow",
    "Fast": "Fast",
    "Slow": "Slow",
}


def parse_growth_rate(mon_text):
    rate_match = re.search(r"^GrowthRate = (.+)", mon_text, re.MULTILINE)
    rate_raw = rate_match.group(1)
    rate = growth_rate_map[rate_raw]
    return rate


# BaseEXP
parse_base_exp = parse_number(r"^BaseEXP = (.+)")


# Rareness
parse_catch_rate = parse_number(r"^Rareness = (.+)")


# Happiness
parse_base_happiness = parse_number(r"^Happiness = (.+)")


# Abilities
with open("../data/abilities.json", "r", encoding="utf8") as infile:
    abilities = json.loads(infile.read())


def parse_abilities(mon_text):
    abils_match = re.search(r"^Abilities = (.+)", mon_text, re.MULTILINE)
    abils_raw = abils_match.group(1)
    abils_list = abils_raw.split(",")
    abils = [abilities[abil] for abil in abils_list]
    # TODO: Determine if ability is signature
    return abils


# Moves
# LineMoves
# TutorMoves
# Tribes
# Height
# Weight
# Color
# Shape
# Kind
# Pokedex
# WildItemCommon
# WildItemUncommon
# WildItemRare
# FormName
# Evolutions
