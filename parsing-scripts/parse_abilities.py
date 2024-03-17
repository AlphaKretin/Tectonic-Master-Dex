import json
import re


# Index
def parse_internal_name(abil_text):
    id_match = re.search(r"^\[([A-Z]+)\]", abil_text, re.MULTILINE)
    id = id_match.group(1)
    return id


# Name
def parse_ability_name(abil_text):
    name_match = re.search(r"^Name = (.+)", abil_text, re.MULTILINE)
    name = name_match.group(1)
    return name


# Description
def parse_description(abil_text):
    desc_match = re.search(r"^Description = (.+)", abil_text, re.MULTILINE)
    desc = desc_match.group(1)
    return desc


# Flags
def parse_flags(abil_text):
    flags_match = re.search(r"^Flags = (.+)", abil_text, re.MULTILINE)
    if flags_match:
        flags_raw = flags_match.group(1)
        flags = flags_raw.split(",")
        return flags


def parse_ability(abil_text):
    id = parse_internal_name(abil_text)
    data = {
        "Name": parse_ability_name(abil_text),
        "Description": parse_description(abil_text),
    }
    flags = parse_flags(abil_text)
    if flags:
        data["Flags"] = flags
    return (id, data)


with open("../PBS/abilities.txt", "r", encoding="utf8") as infile:
    doc = infile.read()

abils = doc.split("#-------------------------------")
abils = abils[1:]  # first entry is a header, rest fit expected format

abilities = {}

for abil_text in abils:
    (id, data) = parse_ability(abil_text)
    abilities[id] = data

with open("../data/abilities.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(abilities, indent=4))
