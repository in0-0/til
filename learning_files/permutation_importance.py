import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("learning_files/asset/FIFA 2018 Statistics.csv")
y = data["Man of the Match"] == "Yes"  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=100, random_state=0).fit(
    train_X, train_y
)


import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state=1).fit(val_X, val_y)
print(perm.feature_importances_)
# eli5.show_weights(perm, feature_names=val_X.columns.tolist()) # Only for Ipython
print(
    eli5.format_as_text(
        eli5.explain_weights(perm, feature_names=val_X.columns.tolist())
    )
)
