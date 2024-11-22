import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("learning_files/asset/FIFA 2018 Statistics.csv")
y = data["Man of the Match"] == "Yes"  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
tree_model = DecisionTreeClassifier(
    random_state=0, max_depth=5, min_samples_split=5
).fit(train_X, train_y)

from sklearn import tree

tree_graph = tree.export_graphviz(
    tree_model, out_file="out.png", feature_names=feature_names
)
# graphviz.Source(tree_graph)


from matplotlib import pyplot as plt
from sklearn.inspection import PartialDependenceDisplay

# Create and plot the data
disp1 = PartialDependenceDisplay.from_estimator(tree_model, val_X, ["Goal Scored"])
# plt.show()

feature_to_plot = "Distance Covered (Kms)"
disp2 = PartialDependenceDisplay.from_estimator(tree_model, val_X, [feature_to_plot])
# plt.show()


# Build Random Forest model
rf_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)

disp3 = PartialDependenceDisplay.from_estimator(rf_model, val_X, [feature_to_plot])
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
f_names = [("Goal Scored", "Distance Covered (Kms)")]
# Similar to previous PDP plot except we use tuple of features instead of single feature
disp4 = PartialDependenceDisplay.from_estimator(tree_model, val_X, f_names, ax=ax)
plt.show()
