import pandas as pd

# Data input: List of dictionaries representing the table
data = [
    {"Description": "aaaaaaaaa", "Name": "ASD", "Timing": "anytime"},
    {"Description": "bbbbbbbbb", "Name": "ASD", "Timing": "2"},
    {"Description": "ccccccccc", "Name": "QWE", "Timing": "3"},
    {"Description": "ddddddddd", "Name": "ERT", "Timing": "3"},
    {"Description": "eeeeeeeeee", "Name": "ERT", "Timing": "4"},
    {"Description": "ffffffffffffffff", "Name": "ERT", "Timing": "5"},
    {"Description": "gggggggggg", "Name": "DFG", "Timing": "anytime"},
    {"Description": "hhhhhhhhhh", "Name": "CVB", "Timing": "anytime"},
    {"Description": "iiiiiiiii", "Name": "CVB", "Timing": "3"},
    {"Description": "jjjjjjjjjj", "Name": "VBN", "Timing": "4"},
    {"Description": "kkkkkk", "Name": "VBN", "Timing": "anytime"},
    {"Description": "lllllllll", "Name": "GHJ", "Timing": "2"},
    {"Description": "mmmmmmm", "Name": "YUI", "Timing": "3"},
    {"Description": "nnnnnn", "Name": "GHJ", "Timing": "2"},
    {"Description": "oooooooo", "Name": "UIO", "Timing": "anytime"},
    {"Description": "pppppppppp", "Name": "UIO", "Timing": "2"},
]

df = pd.DataFrame(data)
print(df)

df_234_any = df[df["Timing"].isin(["2", "3", "4", "anytime"])]
print(df_234_any)

df_234_any_dict = df[["Description", "Name"]].apply(
    lambda x: {x["Description"]: x["Name"]}, axis=1
)

print(df_234_any_dict)
