import glob
import pandas as pd
import numpy as np

from sklearn import metrics



if __name__ == "__main__":
    files = glob.glob("../output/model_preds/*.csv")
    df = None
    for f in files:
        if df is None:
            df = pd.read_csv(f)
        else:
            temp_df = pd.read_csv(f)
            df = df.merge(temp_df, on="id", how="left")
    
    targets = df.sentiment.values

    pred_cols = ["lr_pred", "lr_cnt_pred", "rf_svd_pred"]

    for col in pred_cols:
        auc = metrics.roc_auc_score(targets, df[col].values)
        print(f"{col}, overall_auc={auc}")
    
    print("Simple Average:")
    avg_pred = np.mean(df[pred_cols].values, axis=1)
    print(metrics.roc_auc_score(targets, avg_pred))

    print("Weighted Average:")
    lr_pred = df.lr_pred.values
    lr_cnt_pred = df.lr_cnt_pred.values
    rf_svd_pred = df.rf_svd_pred.values
    avg_pred = (3*lr_pred + lr_cnt_pred + rf_svd_pred) / 5
    print(metrics.roc_auc_score(targets, avg_pred))

    print("Rank Average:")
    lr_pred = df.lr_pred.rank().values
    lr_cnt_pred = df.lr_cnt_pred.rank().values
    rf_svd_pred = df.rf_svd_pred.rank().values
    avg_pred = (lr_pred + lr_cnt_pred + rf_svd_pred) / 3
    print(metrics.roc_auc_score(targets, avg_pred))

    print("Weighted Rank Average:")
    lr_pred = df.lr_pred.rank().values
    lr_cnt_pred = df.lr_cnt_pred.rank().values
    rf_svd_pred = df.rf_svd_pred.rank().values
    avg_pred = (3*lr_pred + lr_cnt_pred + rf_svd_pred) / 5
    print(metrics.roc_auc_score(targets, avg_pred))