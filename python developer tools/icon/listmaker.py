import pandas as pd
import os
import json

if __name__ == "__main__":

    source_path = os.path.join(os.path.dirname(__file__), "list.csv")
    df = pd.read_csv(source_path)
    list = {}

    for i in range(0, len(df)):

        icon = df.iloc[i]["icon"]
        ext = df.iloc[i]["ext."]

        if icon == "/":
            continue
        else:
            svg_content = ""
            with open(
                os.path.join(os.path.dirname(__file__), "icon", icon + ".svg"), "r"
            ) as file:
                svg_content = file.read()
            svg_content = (
                '<svg height="16px" viewBox="0 0 64 64" width="16px">\n'
                + svg_content
                + "</svg>"
            )
            list[ext] = svg_content

    list_json = json.dumps(list, indent=4)

    with open(os.path.join(os.path.dirname(__file__), "icons.json"), "w") as file:
        file.write(list_json)
