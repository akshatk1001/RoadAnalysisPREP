import pandas as pd
import numpy as np

a1 = np.random.randint(low = 1, high = 50, size = (10, 4))
titles = ["a", "b", "c", "d"]

df1 = pd.DataFrame(data = a1, columns = titles)

print("\n", df1, "\n")

print(df1.head(2), "\n")

print(df1.iloc[2], "\n")

df1["e"] = df1["a"] + df1["b"]


new_row = pd.DataFrame(data = [np.random.randint(low = 1, high = 50, size = len(df1.columns))], columns = df1.columns)
df1 = pd.concat([df1, new_row], ignore_index = True)

print(df1, "\n")
