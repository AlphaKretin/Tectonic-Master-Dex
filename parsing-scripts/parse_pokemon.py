import json
import re


def parse_basic_string(regex):
    def F(mon_text):
        match = re.search(regex, mon_text, re.MULTILINE)
        if match:
            result = match.group(1)
            return result

    return F


def parse_mapped_string(regex, map):
    def F(mon_text):
        match = re.search(regex, mon_text, re.MULTILINE)
        if match:
            result = match.group(1)
            mapped_result = map[result]
            return mapped_result

    return F


def parse_integer(regex):
    def F(mon_text):
        num_match = re.search(regex, mon_text, re.MULTILINE)
        if num_match:
            num_raw = num_match.group(1)
            num = int(num_raw)
            return num

    return F


def parse_float(regex):
    def F(mon_text):
        num_match = re.search(regex, mon_text, re.MULTILINE)
        if num_match:
            num_raw = num_match.group(1)
            num = float(num_raw)
            return num

    return F


# Index
parse_pokedex_number = parse_integer(r"^\[(\d+)\]")


# Name
parse_pokemon_name = parse_basic_string(r"^Name = (.+)")


# InternalName
parse_internal_name = parse_basic_string(r"^InternalName = (.+)")


# Type1
# Type2
def parse_types(mon_text):
    types = []
    type1_match = re.search(r"^Type1 = (.+)", mon_text, re.MULTILINE)
    if type1_match:
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
    if stats_match:
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

parse_gender_rate = parse_mapped_string(r"^GenderRate = (.+)", gender_rate_map)

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

parse_growth_rate = parse_mapped_string(r"^GrowthRate = (.+)", growth_rate_map)

# BaseEXP
parse_base_exp = parse_integer(r"^BaseEXP = (.+)")


# Rareness
parse_catch_rate = parse_integer(r"^Rareness = (.+)")


# Happiness
parse_base_happiness = parse_integer(r"^Happiness = (.+)")


# Abilities
with open("../data/abilities.json", "r", encoding="utf8") as infile:
    abilities = json.loads(infile.read())


def parse_abilities(mon_text):
    abils_match = re.search(r"^Abilities = (.+)", mon_text, re.MULTILINE)
    if abils_match:
        abils_raw = abils_match.group(1)
        abils_list = abils_raw.split(",")
        abils = [abilities[abil] for abil in abils_list]
        # TODO: Determine if ability is signature
        return abils


# from https://stackoverflow.com/a/312464
def chunks(lst, n):
    a = []
    for i in range(0, len(lst), n):
        a.append(lst[i : i + n])
    return a


def parse_level_moves(mon_text):
    moves_match = re.search(r"^Moves = (.+)", mon_text, re.MULTILINE)
    if moves_match:
        moves_raw = moves_match.group(1)
        moves_list = moves_raw.split(",")
        move_pairs = chunks(moves_list, 2)
        # use the moves' internal names so full data can be fetched later in the pipeline
        move_tuples = [(int(level), move) for [level, move] in move_pairs]
        return move_tuples


# LineMoves
def parse_moves_list(regex):
    def F(mon_text):
        moves_match = re.search(regex, mon_text, re.MULTILINE)
        if moves_match:
            moves_raw = moves_match.group(1)
            moves_list = moves_raw.split(",")
            return moves_list

    return F


# TODO: proliferate across evolution lines
parse_line_moves = parse_moves_list(r"^LineMoves = (.+)")

# TutorMoves
parse_tutor_moves = parse_moves_list(r"^TutorMoves = (.+)")


# Tribes
def parse_tribes(mon_text):
    tribes_match = re.search(r"^Tribes = (.+)", mon_text, re.MULTILINE)
    if tribes_match:
        tribes_raw = tribes_match.group(1)
        tribes_list = tribes_raw.split(",")
        tribes = [tribe.title() for tribe in tribes_list]
        return tribes


# Height
parse_height = parse_float(r"^Height = (.+)")

# Weight
parse_weight = parse_float(r"^Weight = (.+)")

# Color
parse_colour = parse_basic_string(r"^Color = (.+)")

# Shape
parse_shape = parse_basic_string(r"^Shape = (.+)")

# Kind
parse_kind = parse_basic_string(r"^Kind = (.+)")

# Pokedex
parse_pokedex = parse_basic_string(r"^Pokedex = (.+)")

# WildItemCommon
parse_wild_item_common = parse_basic_string(r"^WildItemCommon = (.+)")

# WildItemUncommon
parse_wild_item_uncommon = parse_basic_string(r"^WildItemUncommon = (.+)")

# WildItemRare
parse_wild_item_rare = parse_basic_string(r"^WildItemRare = (.+)")

# FormName
parse_form = parse_basic_string(r"^FormName = (.+)")


# Evolutions
def parse_evolutions(mon_text):
    evos_match = re.search(r"^Evolutions = (.+)", mon_text, re.MULTILINE)
    if evos_match:
        evos_raw = evos_match.group(1)
        evos_list = evos_raw.split(",")
        evos_trios = chunks(evos_list, 3)
        evos = [
            {"Pokemon": trio[0], "Method": trio[1], "Condition": trio[2]}
            for trio in evos_trios
        ]
        return evos


parsers = {
    "Number": parse_pokedex_number,
    "Name": parse_pokemon_name,
    "Types": parse_types,
    "BaseStats": parse_base_stats,
    "GenderRate": parse_gender_rate,
    "GrowthRate": parse_growth_rate,
    "BaseEXP": parse_base_exp,
    "CatchRate": parse_catch_rate,
    "Happiness": parse_base_happiness,
    "Abilities": parse_abilities,
    "Moves": parse_level_moves,
    "LineMoves": parse_line_moves,
    "TutorMoves": parse_tutor_moves,
    "Tribes": parse_tribes,
    "Height": parse_height,
    "Weight": parse_weight,
    "Color": parse_colour,
    "Shape": parse_shape,
    "Kind": parse_kind,
    "Pokedex": parse_pokedex,
    "WildItemCommon": parse_wild_item_common,
    "WildItemUnommon": parse_wild_item_uncommon,
    "WildItemRare": parse_wild_item_rare,
    "FormName": parse_form,
    "Evolutions": parse_evolutions,
}


def parse_mon(mon_text):
    id = parse_internal_name(mon_text)
    data = {"InternalName": id}
    for key, parser in parsers.items():
        result = parser(mon_text)
        if result:
            data[key] = result
    return (id, data)


with open("../PBS/pokemon.txt", "r", encoding="utf8") as infile:
    doc = infile.read()

mons = doc.split("#-------------------------------")
mons = mons[1:]  # first entry is a header, rest fit expected format

pokemon = {}

for mon_text in mons:
    (id, data) = parse_mon(mon_text)
    pokemon[id] = data

# TODO: Proliferate necessary cross-line changes
# Fill in pre-evolution data for two-way links
for mon, data in pokemon.items():
    if "Evolutions" in data:
        for evo in data["Evolutions"]:
            # assuming a pokemon only has one prevo so we don't need to handle multiple
            pokemon[evo["Pokemon"]]["Prevolutions"] = [
                {
                    "Pokemon": mon,
                    "Method": evo["Method"],
                    "Condition": evo["Condition"],
                }
            ]


def proliferate(mon):
    data = pokemon[mon]
    if not "Evolutions" in data:
        return
    for evo in data["Evolutions"]:
        name = evo["Pokemon"]
        if "Tribes" in data and not "Tribes" in pokemon[name]:
            pokemon[name]["Tribes"] = data["Tribes"]
        proliferate(name)


for mon, _ in pokemon.items():
    proliferate(mon)

# TODO: Read in encounter data

with open("../data/pokemon.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(pokemon, indent=4))
