import pandas as pd
import numpy as np
import os
import sys
import subprocess

path_file = os.path.join(os.path.dirname(__file__), "formatted_result.csv")

df = pd.read_csv(path_file)
l = df.shape[0]

while True:
    rnd = np.random.randint(0, l)
    subprocess.run(["clear"])
    print("=====================================")
    print("Random row:", rnd)
    print(df.iloc[rnd])
    
    if not pd.isna(df.iloc[rnd]["icon"]):
        print("Icon:", df.iloc[rnd]["icon"])
    else:
        print("No icon")
        icon = input("Please input icon:")
        df.loc[rnd, "icon"] = icon
        df.to_csv(path_file, index=False)
        df = pd.read_csv(path_file)
        print("Icon saved")