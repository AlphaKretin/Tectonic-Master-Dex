import json
import re


def parse_basic_string(regex):
    def F(move_text):
        match = re.search(regex, move_text, re.MULTILINE)
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


def parse_number(regex):
    def F(mon_text):
        num_match = re.search(regex, mon_text, re.MULTILINE)
        if num_match:
            num_raw = num_match.group(1)
            num = int(num_raw)
            return num

    return F


# Index
parse_internal_name = parse_basic_string(r"^\[([A-Z0-9]+)\]")


# Name
parse_move_name = parse_basic_string(r"^Name = (.+)")


# Type
def parse_type(move_text):
    type_match = re.search(r"^Type = (.+)", move_text, re.MULTILINE)
    if type_match:
        type = type_match.group(1).title()
        return type


# Category
parse_category = parse_basic_string(r"^Category = (.+)")


# Power
parse_power = parse_number(r"^Power = (.+)")


# Accuracy
parse_accuracy = parse_number(r"^Accuracy = (.+)")


# TotalPP
parse_pp = parse_number(r"^TotalPP = (.+)")


# Target
target_map = {
    "None": "None",
    "User": "User",
    "NearAlly": "Near Ally",
    "UserOrNearAlly": "User or Near Ally",
    "UserAndAllies": "User and Allies",
    "NearFoe": "Near Foe",
    "RandomNearFoe": "Random Near Foe",
    "AllNearFoes": "All Near Foes",
    "Foe": "Foe",
    "AllFoes": "All Foes",
    "NearOther": "Near Other",
    "AllNearOthers": "All Near Others",
    "Other": "Other",
    "AllBattlers": "All Battlers",
    "UserSide": "User Side",
    "FoeSide": "Foe Side",
    "BothSides": "Both Sides",
    "UserOrNearOther": "User or Near Other",
    "UserOrOther": "User or Other",
}

parse_target = parse_mapped_string(r"^Target = (.+)", target_map)

# Priority
parse_priority = parse_number(r"^Priority = (.+)")

# Description
parse_description = parse_basic_string(r"^Description = (.+)")

parsers = {
    "Name": parse_move_name,
    "Type": parse_type,
    "Category": parse_category,
    "Power": parse_power,
    "Accuracy": parse_accuracy,
    "TotalPP": parse_pp,
    "Target": parse_target,
    "Priority": parse_priority,
    "Description": parse_description,
}


def parse_move(move_text):
    id = parse_internal_name(move_text)
    data = {"InternalName": id}
    for key, parser in parsers.items():
        result = parser(move_text)
        if result:
            data[key] = result
    return (id, data)


with open("../PBS/moves.txt", "r", encoding="utf8") as infile:
    doc = infile.read()

move_texts = doc.split("#-------------------------------")
move_texts = move_texts[1:]  # first entry is a header, rest fit expected format

moves = {}

for move_text in move_texts:
    (id, data) = parse_move(move_text)
    moves[id] = data

with open("../data/moves.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(moves, indent=4))
