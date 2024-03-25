import json
import re


def parse_basic_string(regex):
    def F(abil_text):
        match = re.search(regex, abil_text, re.MULTILINE)
        if match:
            result = match.group(1)
            return result

    return F


# Index
parse_internal_name = parse_basic_string(r"^\[([A-Z]+)\]")


# Name
parse_ability_name = parse_basic_string(r"^Name = (.+)")


# Description
parse_description = parse_basic_string(r"^Description = (.+)")


parsers = {
    "name": parse_ability_name,
    "description": parse_description,
}


def parse_ability(abil_text):
    id = parse_internal_name(abil_text)
    data = {"key": id}
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

with open("../data/abilities-rr.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(abilities, indent=4))
