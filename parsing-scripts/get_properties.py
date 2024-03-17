# Gets a list of all unique properties in the requested PBS file so I know what I have to parse

import os
import re
import sys

if len(sys.argv) < 2:
    print("Please provide the name of the PBS file to parse!")
    sys.exit()

pbs = sys.argv[1]

file_path = f"../PBS/{pbs}.txt"

if not os.path.isfile(file_path):
    print(f"Cannot find a {pbs}.txt file in the PBS folder!")
    sys.exit()

with open(file_path, "r", encoding="utf8") as infile:
    doc = infile.read()

properties_match = re.findall(r"^(.+) =", doc, re.MULTILINE)
properties = set(properties_match)

with open(f"../intermediary/{pbs}_properties.txt", "w", encoding="utf8") as outfile:
    outfile.write("\n".join(properties))
