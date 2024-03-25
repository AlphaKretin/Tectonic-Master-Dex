import json


def convert(mon):
    pokemon = {}
    pokemon["ID"] = mon["Number"]
    pokemon["key"] = mon["InternalName"]
    pokemon["dexID"] = mon["Number"]
    pokemon["stats"] = {}
    pokemon["stats"]["HP"] = mon["BaseStats"]["hp"]
    pokemon["stats"]["attack"] = mon["BaseStats"]["attack"]
    pokemon["stats"]["defense"] = mon["BaseStats"]["defense"]
    pokemon["stats"]["spAttack"] = mon["BaseStats"]["sp_atk"]
    pokemon["stats"]["spDefense"] = mon["BaseStats"]["sp_def"]
    pokemon["stats"]["speed"] = mon["BaseStats"]["speed"]
    pokemon["stats"]["total"] = (
        mon["BaseStats"]["hp"]
        + mon["BaseStats"]["attack"]
        + mon["BaseStats"]["defense"]
        + mon["BaseStats"]["sp_atk"]
        + mon["BaseStats"]["sp_def"]
        + mon["BaseStats"]["speed"]
    )
    pokemon["abilities"] = {}
    pokemon["abilities"]["primary"] = mon["Abilities"][0]["InternalName"]
    if len(mon["Abilities"]) > 1:
        pokemon["abilities"]["secondary"] = mon["Abilities"][1]["InternalName"]
    pokemon["type"] = {}
    pokemon["type"]["primary"] = mon["Types"][0].upper()
    if len(mon["Types"]) > 1:
        pokemon["type"]["secondary"] = mon["Types"][1].upper()
    pokemon["family"] = {}
    if "Evolutions" in mon:
        pokemon["family"]["evolutions"] = [
            [evo["Method"].upper(), evo["Condition"], evo["Pokemon"], 0]
            for evo in mon["Evolutions"]
        ]
    if "Prevolutions" in mon:
        pokemon["family"]["ancestor"] = mon["Prevolutions"][0]["Pokemon"]
    else:
        pokemon["family"]["ancestor"] = mon["InternalName"]
    pokemon["learnset"] = {}
    pokemon["learnset"]["levelup"] = [[mov[1], mov[0]] for mov in mon["Moves"]]
    if "TutorMoves" in mon:
        pokemon["learnset"]["tutor"] = mon["TutorMoves"]
    pokemon["name"] = mon["Name"]
    return pokemon


# convert pokemon to RR dex format
with open("../data/pokemon.json", "r", encoding="utf8") as infile:
    pokemon = json.loads(infile.read())

rr_pokemon = {id: convert(mon) for id, mon in pokemon.items()}

with open("../data/pokmon-rr.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(rr_pokemon, indent=4))
