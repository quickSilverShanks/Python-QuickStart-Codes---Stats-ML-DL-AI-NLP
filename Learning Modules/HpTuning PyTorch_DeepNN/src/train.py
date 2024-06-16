import pandas as pd
import numpy as np
import torch
import optuna

import utils

# low value of below constants are to facilitate quick running of the code, check the comments
DEVICE = "cuda"
EPOCHS = 200  # keep this 1000 or even higher for better results
OPTUNA_TRIALS = 4 # keep this 20 or even higher for better results
BATCH_SIZE = 8192 # adjust this as per available cuda cores or ram size. Also, experiments indicated quicker progress at 8192 as compared to 16384.
EPOCH_LOG_INTERVAL = 25 # higher value for less frequent log prints


def prep_data():
    df = pd.read_csv("../input/train_features.csv")
    df = df.drop(["cp_type", "cp_time", "cp_dose"], axis=1)
    
    targets_df = pd.read_csv("../output/train_targets_folds.csv")
    
    global feature_columns
    global target_columns

    feature_columns = df.drop("sig_id", axis=1).columns
    target_columns = targets_df.drop(["sig_id", "kfold"], axis=1).columns

    df = df.merge(targets_df, on="sig_id", how="left")

    return df



def run_training(fold, params, save_model=False):
    train_df = df[df.kfold != fold].reset_index(drop=True)
    valid_df = df[df.kfold == fold].reset_index(drop=True)

    xtrain = train_df[feature_columns].to_numpy()
    ytrain = train_df[target_columns].to_numpy()

    xvalid =valid_df[feature_columns].to_numpy()
    yvalid =valid_df[target_columns].to_numpy()

    # use MoaDataset below to train on cpu. MoaDatasetGPU on cpu is untested.
    train_dataset = utils.MoaDatasetGPU(features=xtrain, targets=ytrain, device=DEVICE)
    valid_dataset = utils.MoaDatasetGPU(features=xvalid, targets=yvalid, device=DEVICE)

    # num_workers=8 (or anything >0 perhaps) gave some cuda warnings so removed it from both the data loaders below.
    # details on this warning can be found here : https://discuss.pytorch.org/t/w-cudaipctypes-cpp-22-producer-process-has-been-terminated-before-all-shared-cuda-tensors-released-see-note-sharing-cuda-tensors/124445
    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True
    )

    valid_loader = torch.utils.data.DataLoader(
        valid_dataset, batch_size=BATCH_SIZE
    )

    model = utils.Model(
        nfeatures = xtrain.shape[1],
        ntargets = ytrain.shape[1],
        nlayers = params["num_layer"],
        hidden_size = params["hidden_size"],
        dropout = params["dropout"]
    )
    model.to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=params["learning_rate"])
    eng = utils.Engine(model, optimizer, DEVICE)

    best_loss = np.inf
    early_stopping_iter = 10
    early_stopping_counter = 0

    for epoch in range(EPOCHS):
        train_loss = eng.train(train_loader)
        valid_loss = eng.evaluate(valid_loader)
        if (epoch+1)%EPOCH_LOG_INTERVAL == 0:
            print(f"[Fold:{fold+1}, Epoch:{epoch+1}/{EPOCHS}] : Train Loss:{train_loss}, Val Loss:{valid_loss}")
        if valid_loss < best_loss:
            best_loss = valid_loss
            early_stopping_counter = 0
            if save_model:
                torch.save(model.state_dict(), f"../output/model_{fold}.bin")
        else:
            early_stopping_counter += 1
        
        if early_stopping_counter > early_stopping_iter:
            break
    
    return best_loss



def objective(trial):
    params = {
        "num_layer": trial.suggest_int("num_layer", 1,4),
        "hidden_size": trial.suggest_int("hidden_size", 16, 128),
        "dropout": trial.suggest_float("dropout", 0.1, 0.7),
        "learning_rate": trial.suggest_float("learning_rate", 1e-6, 1e-3, log=True)
    }
    all_losses = []
    for f_ in range(5):
        temp_loss = run_training(f_, params, save_model=False)
        all_losses.append(temp_loss)
    
    return np.mean(all_losses)



if __name__ == "__main__":
    df = prep_data()
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=OPTUNA_TRIALS)

    print("Best Trial:")
    trial_ = study.best_trial

    print(trial_.values)
    print(trial_.params)

    scores = 0
    for j in range(5):
        scr = run_training(j, trial_.params, save_model=True)
        scores += scr
    
    print("Avg. Score for 5 folds:", scores / 5)

# Print Outputs:

# Best Trial:
# [0.21970292031764985]
# {'num_layer': 1, 'hidden_size': 109, 'dropout': 0.1350424938862769, 'learning_rate': 6.0074165060706274e-05}
# Avg. Score for 5 folds: 0.2188609778881073
