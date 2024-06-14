import pandas as pd
import numpy as np

from sklearn import ensemble, metrics, model_selection

from functools import partial
import optuna



def optimize(trial, x, y):
    criterion = trial.suggest_categorical("criterion", ["gini", "entropy"])
    n_estimators = trial.suggest_int("n_estimators", 100, 1500)
    max_depth = trial.suggest_int("max_depth", 3, 15)
    max_features = trial.suggest_float("max_features", 0.01, 1.0)
    
    model = ensemble.RandomForestClassifier(
        n_estimators = n_estimators,
        max_depth = max_depth,
        max_features = max_features,
        criterion = criterion
    )

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

    optimization_function = partial(optimize, x=X, y=y)

    study = optuna.create_study(direction="minimize")
    study.optimize(optimization_function, n_trials=15)

    print("Best Model accuracy : ", -1.0*study.best_trial.value)
    print("Best Model HyperParameters : ", study.best_params)


# Print Output:

# Best Model accuracy :  0.9109999999999999
# Best Model HyperParameters :  {'criterion': 'entropy', 'n_estimators': 143, 'max_depth': 11, 'max_features': 0.7910254616951846}
