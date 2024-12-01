import pandas as pd
import os
import json
from lxml import etree


def resize_svg(input_file, output_file, size=16):
    tree = etree.parse(input_file)
    root = tree.getroot()
    namespace = {"svg": "http://www.w3.org/2000/svg"}
    root.set("width", f"{size}px")
    root.set("height", f"{size}px")
    viewBox = root.get("viewBox")
    if viewBox:
        values = list(map(float, viewBox.split()))
        if values[2] != values[3]:
            raise ValueError(f" {input_file} SVG is not square!")
    root.set("namespace", namespace["svg"])
    tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="utf-8")


def process_source_icon():
    """
    Transform the source icon in `source_icon` folder to 16x16 icon in `icon` folder
    """

    source_path = os.path.join(os.path.dirname(__file__), "list", "is.csv")
    special_source_path = os.path.join(os.path.dirname(__file__), "list", "sis.csv")
    df = pd.read_csv(source_path)
    special_df = pd.read_csv(special_source_path)
    icon_dict = {}

    for i in range(0, len(df)):
        icon = df.iloc[i]["icon"]
        ext = df.iloc[i]["ext."]
        if icon == "/":
            continue
        else:
            resize_svg(
                os.path.join(os.path.dirname(__file__), "source_icon", icon + ".svg"),
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"),
                16,
            )
            svg_content = ""
            with open(
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"), "r"
            ) as file:
                svg_content = file.read()
            icon_dict[ext] = svg_content

    for i in range(0, len(special_df)):
        icon = special_df.iloc[i]["icon"]
        ext = special_df.iloc[i]["name"]
        if icon == "/":
            continue
        else:
            resize_svg(
                os.path.join(os.path.dirname(__file__), "source_icon", icon + ".svg"),
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"),
                16,
            )
            svg_content = ""
            with open(
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"), "r"
            ) as file:
                svg_content = file.read()
            icon_dict[ext] = svg_content


def load_icon_dict():
    """
    Load the icon dictionary from `list/is.csv` and `list/sis.csv` to `list/icons.json`
    """

    source_path = os.path.join(os.path.dirname(__file__), "list", "is.csv")
    special_source_path = os.path.join(os.path.dirname(__file__), "list", "sis.csv")
    df = pd.read_csv(source_path)
    special_df = pd.read_csv(special_source_path)
    icon_dict = {}
    for i in range(0, len(df)):
        icon = df.iloc[i]["icon"]
        ext = df.iloc[i]["ext."]
        if icon == "/":
            continue
        else:
            with open(
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"), "r"
            ) as file:
                svg_content = file.read()
            icon_dict[ext] = svg_content
    for i in range(0, len(special_df)):
        icon = special_df.iloc[i]["icon"]
        ext = special_df.iloc[i]["name"]
        if icon == "/":
            continue
        else:
            with open(
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"), "r"
            ) as file:
                svg_content = file.read()
            icon_dict[ext] = svg_content

    with open(
        os.path.join(os.path.dirname(__file__), "list", "icons.json"), "w"
    ) as file:
        file.write(json.dumps(icon_dict, indent=4))


if __name__ == "__main__":

    process_source_icon()
    load_icon_dict()
