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
parse_item_name = parse_basic_string(r"^Name = (.+)")

parsers = {"name": parse_item_name}


def parse_move(move_text):
    id = parse_internal_name(move_text)
    data = {"key": id}
    for key, parser in parsers.items():
        result = parser(move_text)
        if result:
            data[key] = result
    return (id, data)


with open("../PBS/items.txt", "r", encoding="utf8") as infile:
    doc = infile.read()

item_texts = doc.split("#-------------------------------")
item_texts = item_texts[1:]  # first entry is a header, rest fit expected format

items = {}

for move_text in item_texts:
    (id, data) = parse_move(move_text)
    items[id] = data

with open("../data/pokemon.json", "r", encoding="utf8") as monfile:
    pokemon = json.loads(monfile.read())


def check_evo(item):
    for _, mon in pokemon.items():
        if "Evolutions" in mon:
            for evo in mon["Evolutions"]:
                if evo["Condition"] == item:
                    return True
    return False


def check_held(item):
    for _, mon in pokemon.items():
        if "WildItemCommon" in mon and mon["WildItemCommon"] == item:
            return True
        if "WildItemUnommon" in mon and mon["WildItemUnommon"] == item:
            return True
        if "WildItemRare" in mon and mon["WildItemRare"] == item:
            return True
    return False


evo_items = {key: item for key, item in items.items() if check_evo(key)}

held_items = {key: item for key, item in items.items() if check_held(key)}

with open("../data/evo-items.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(evo_items, indent=4))

with open("../data/held-items.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(held_items, indent=4))
