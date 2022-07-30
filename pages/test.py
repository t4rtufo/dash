import pandas as pd

penguins = pd.read_csv("./data/penguins_size.csv")
penguins["sex"] = penguins['sex'].fillna(penguins['sex'].mode()[0])
penguins.iloc[:, 2:6] = penguins.iloc[:, 2:6].fillna(
    penguins.iloc[:, 2:6].mean())

gentoo_ratio = penguins[penguins["species"]
                        == "Gentoo"].size * 100 / penguins.size
print(gentoo_ratio)
