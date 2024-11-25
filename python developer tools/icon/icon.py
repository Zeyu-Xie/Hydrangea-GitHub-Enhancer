import json
import os
import xml.etree.ElementTree as ET

data = []
with open(os.path.join(os.path.dirname(__file__), "icon_plan.json")) as f:
    data = json.load(f)

def resize_svg(input_string, width="16px", height="16px"):
    tree = ET.ElementTree(ET.fromstring(input_string))
    root = tree.getroot()
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]
    root.set("width", width)
    root.set("height", height)
    return ET.tostring(root, encoding="unicode")

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
        svg_code = resize_svg(svg_code)
        for ext in ext_list:
            output[ext.upper()] = svg_code
    with open(os.path.join(os.path.dirname(__file__), "icon_output.json"), "w") as f:
        f.write(json.dumps(output))


if __name__ == "__main__":

    process_icon(data)
