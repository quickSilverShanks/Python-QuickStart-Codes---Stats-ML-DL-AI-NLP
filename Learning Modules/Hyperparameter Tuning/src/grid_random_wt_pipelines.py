import pandas as pd
import numpy as np

from sklearn import ensemble, metrics, model_selection
from sklearn import decomposition, preprocessing, pipeline

if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop("price_range", axis=1).values
    y = df.price_range.values

    scl = preprocessing.StandardScaler()
    pca = decomposition.PCA()
    rf = ensemble.RandomForestClassifier(n_jobs=-1)

    classifier = pipeline.Pipeline(
        [
            ('scaling', scl),
            ('pca', pca),
            ('rf', rf)
        ]
    )

    param_grid = {
        "pca__n_components" : np.arange(4,16),
        "rf__n_estimators" : np.arange(100, 1500, 100),
        "rf__max_depth" : np.arange(1, 20),
        "rf__criterion" : ["gini", "entropy"]
    }
    
    model = model_selection.RandomizedSearchCV(
        estimator = classifier,
        param_distributions = param_grid,
        scoring = "accuracy",
        verbose = 10,
        n_jobs = 1,
        n_iter = 16,
        cv = 5
    )

    model.fit(X,y)
    print("Best Score : ", model.best_score_)
    print("Best Model HyperParameters : ", model.best_estimator_.get_params())


# Print Outputs:

# Best Score :  0.6765
# Best Model HyperParameters :  {'memory': None, 
#                                'steps': [('scaling', StandardScaler()), ('pca', PCA(n_components=15)), 
#                                          ('rf', RandomForestClassifier(criterion='entropy', max_depth=11, n_estimators=1300, n_jobs=-1))], 
#                                 'verbose': False, 'scaling': StandardScaler(), 'pca': PCA(n_components=15), 
#                                 'rf': RandomForestClassifier(criterion='entropy', max_depth=11, n_estimators=1300, n_jobs=-1), 
#                                 'scaling__copy': True, 'scaling__with_mean': True, 'scaling__with_std': True, 'pca__copy': True, 'pca__iterated_power': 'auto', 
#                                 'pca__n_components': 15, 'pca__n_oversamples': 10, 'pca__power_iteration_normalizer': 'auto', 'pca__random_state': None, 
#                                 'pca__svd_solver': 'auto', 'pca__tol': 0.0, 'pca__whiten': False, 'rf__bootstrap': True, 'rf__ccp_alpha': 0.0, 'rf__class_weight': None, 
#                                 'rf__criterion': 'entropy', 'rf__max_depth': 11, 'rf__max_features': 'sqrt', 'rf__max_leaf_nodes': None, 'rf__max_samples': None, 
#                                 'rf__min_impurity_decrease': 0.0, 'rf__min_samples_leaf': 1, 'rf__min_samples_split': 2, 'rf__min_weight_fraction_leaf': 0.0, 
#                                 'rf__monotonic_cst': None, 'rf__n_estimators': 1300, 'rf__n_jobs': -1, 'rf__oob_score': False, 'rf__random_state': None, 'rf__verbose': 0, 
#                                 'rf__warm_start': False}
