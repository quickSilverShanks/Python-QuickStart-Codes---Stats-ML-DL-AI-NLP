import pandas as pd
import numpy as np

from sklearn import ensemble, metrics, model_selection

if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop("price_range", axis=1).values
    y = df.price_range.values

    classifier = ensemble.RandomForestClassifier(n_jobs=-1)
    param_grid = {
        "n_estimators" : [100, 200, 300, 400],
        "max_depth" : [1, 3, 5, 7],
        "criterion" : ["gini", "entropy"]
    }
    
    model = model_selection.GridSearchCV(
        estimator = classifier,
        param_grid = param_grid,
        scoring = "accuracy",
        verbose = 10,
        n_jobs = 1,
        cv = 5
    )

    model.fit(X,y)
    print("Best Score : ", model.best_score_)
    print("Best Model HyperParameters : ", model.best_estimator_.get_params())


# Print Outputs:

# Best Score :  0.8664999999999999
# Best Model HyperParameters :  {'bootstrap': True, 'ccp_alpha': 0.0, 'class_weight': None, 'criterion': 'gini', 'max_depth': 7, 
#                                'max_features': 'sqrt', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 
#                                'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'monotonic_cst': None, 
#                                'n_estimators': 300, 'n_jobs': -1, 'oob_score': False, 'random_state': None, 'verbose': 0, 'warm_start': False}
