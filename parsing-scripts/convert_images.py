import base64
import json

PIC_PATH = "../../Pokemon-Tectonic/Graphics/Pokemon/Front/"

with open("../data/pokemon.json", "r", encoding="utf8") as monfile:
    pokemon = json.loads(monfile.read())


def convert_image(mon):
    mon_pic_path = PIC_PATH + mon + ".png"
    with open(mon_pic_path, "rb") as picfile:
        image_data = base64.b64encode(picfile.read())
    image_string = image_data.decode("utf-8")
    return "data:image/png;base64," + image_string


pics = {mon: convert_image(mon) for mon in pokemon}

with open("../data/pics.json", "w", encoding="utf8") as outfile:
    outfile.write(json.dumps(pics, indent=4))
