import pandas as pd
import numpy as np

from sklearn import ensemble, metrics, model_selection
from sklearn import decomposition, preprocessing, pipeline

from functools import partial
from skopt import space, gp_minimize



def optimize(params, param_names, x, y):
    params = dict(zip(param_names, params))
    model = ensemble.RandomForestClassifier(**params)
    kfold = model_selection.StratifiedKFold(n_splits=5)
    
    accuracies = []
    for idx in kfold.split(X=x, y=y):
        train_idx, test_idx = idx[0], idx[1]
        xtrain = x[train_idx]
        ytrain = y[train_idx]
        xtest = x[test_idx]
        ytest = y[test_idx]

        model.fit(xtrain, ytrain)
        preds = model.predict(xtest)
        fold_acc = metrics.accuracy_score(ytest, preds)
        accuracies.append(fold_acc)

    return -1.0*np.mean(accuracies)



if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop("price_range", axis=1).values
    y = df.price_range.values

    param_space = [
        space.Integer(3, 15, name='max_depth'),
        space.Integer(100, 600, name='n_estimators'),
        space.Categorical(['gini', 'entropy'], name='criterion'),
        space.Real(0.01, 1, prior='uniform', name='max_features')
    ]

    param_names = [
        'max_depth',
        'n_estimators',
        'criterion',
        'max_features'
    ]

    optimization_function = partial(optimize, param_names=param_names, x=X, y=y)

    # Bayesian optimization using Gaussian Processes
    result = gp_minimize(
        optimization_function,
        dimensions = param_space,
        n_calls = 15,
        n_random_starts = 10,
        verbose = 10
    )

    print("Best Model HyperParameters : ", dict(zip(param_names, result.x)))


# Print and stdout:

# Current minimum: -0.9060
# Best Model HyperParameters :  {'max_depth': 10, 'n_estimators': 282, 'criterion': 'entropy', 'max_features': 0.8502712179499814}
