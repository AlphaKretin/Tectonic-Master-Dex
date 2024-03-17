import json
import re


def parse_basic_string(regex):
    def F(abil_text):
        match = re.search(regex, abil_text, re.MULTILINE)
        result = match.group(1)
        return result

    return F


# Index
parse_internal_name = parse_basic_string(r"^\[([A-Z]+)\]")


# Name
parse_ability_name = parse_basic_string(r"^Name = (.+)")


# Description
parse_description = parse_basic_string(r"^Description = (.+)")


# Flags
def parse_flags(abil_text):
    flags_match = re.search(r"^Flags = (.+)", abil_text, re.MULTILINE)
    if flags_match:
        flags_raw = flags_match.group(1)
        flags = flags_raw.split(",")
        return flags


parsers = {
    "Name": parse_ability_name,
    "Description": parse_description,
    "Flags": parse_flags,
}


def parse_ability(abil_text):
    id = parse_internal_name(abil_text)
    data = {"InternalName": id}
    for key, parser in parsers.items():
        result = parser(abil_text)
        if result:
            data[key] = result
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
