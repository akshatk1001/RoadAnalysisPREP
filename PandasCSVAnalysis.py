a2 = pd.read_csv("data.csv")

print(a2, "\n")

print(a2.head(2), "\n")

a2["Cals 2"] = a2["Calories"] * 2

del a2["Date"]


nr = pd.DataFrame(data = [np.array([a2["Duration"].mean(), a2["Pulse"].mean(), a2["Maxpulse"].mean(), a2["Calories"].mean(), a2["Cals 2"].mean()])], columns = a2.columns)


a2 = pd.concat([a2, nr], ignore_index = True)

print(a2, "\n")
