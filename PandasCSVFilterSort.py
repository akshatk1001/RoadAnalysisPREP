'''
Data Filtering and Sorting: 
Given a DataFrame, filter out rows based on certain conditions (e.g., all rows where a column's value is greater than a specific threshold).
Then, sort the remaining data based on a specific column.
'''

import numpy as np
import pandas as pd

a2 = pd.read_csv("data.csv")

del a2["Date"]

print(a2, "\n")

for col in a2:
    for num in a2[str(col)]:
        if float(num) > 300:
            a2 = a2.drop(a2[a2[str(col)] == num].index)

a2 = a2.dropna()

print(a2, "\n")

a2 = a2.sort_values(by = "Calories", ascending = True, na_position= "first")

a2 = a2.reset_index()

print(a2, "\n")
