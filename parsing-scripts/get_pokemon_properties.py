# Gets a list of all unique properties in the pokemon.txt PBS file so I know what I have to parse

import re

with open("../PBS/pokemon.txt", "r", encoding="utf8") as infile:
    doc = infile.read()

properties_match = re.findall(r"^(.+) =", doc, re.MULTILINE)
properties = set(properties_match)

with open("../intermediary/properties.txt", "w", encoding="utf8") as outfile:
    outfile.write("\n".join(properties))