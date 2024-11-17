import json
import os

data = []
with open(os.path.join(os.path.dirname(__file__), "icon.json")) as f:
    data = json.load(f)


def process_icon(icon_data):
    output = {}
    l = len(icon_data)
    for i in range(l):
        ext_list = icon_data[i]['ext']
        path = os.path.join(os.path.dirname(__file__),
                            "icon", icon_data[i]['path'])
        svg_code = ""
        with open(path) as f:
            svg_code = f.read()
        for ext in ext_list:
            output[ext] = svg_code
    with open(os.path.join(os.path.dirname(__file__), "output.json"), "w") as f:
        f.write(json.dumps(output, indent=4))


if __name__ == "__main__":

    process_icon(data)
