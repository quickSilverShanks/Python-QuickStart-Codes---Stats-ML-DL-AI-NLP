
The dataset used for this work is from a Kaggle competition "<b>Bag of Words Meets Bags of Popcorn</b>". Thus is a binary classification task of sentiment analysis on IMDB reviews.
<br>Data Source : https://www.kaggle.com/c/word2vec-nlp-tutorial/data
<br><br>This learning module is based on the youtube video : https://www.youtube.com/watch?v=TuIgtitqJho


<br><br>Code Description:
<ul>
    <li>create_folds.py : creates train data with a fold variable</li>
    <li>lreg.py : trains logistic regression model with TfidfVectorizer based text feature extraction</li>
    <li>lreg_cnt.py : trains logistic regression model with CountVectorizer based text feature extraction</li>
    <li>rf_svd.py : trains random forest classifier with TruncatedSVD on TfidfVectorizer based features</li>
    <li>blending.py : code blending predictions of above models' predictions</li>
    <li>optimal_weights.py : find optimal weights using scipy to blend the 3 contributing models trained above</li>
    <li>lr_blend.py : find optimal weights using logistic regression to blend the 3 predictions</li>
    <li>xgb_model.py : stacking with 3 models' predictions used as features along with rest of the input</li>
</ul>

<br><br>Future Improvements:
<ul>
    <li>Add a text preprocessor for text cleaning.</li>
    <li>Add hyperparameter optimization before stacking/blending.</li>
</ul>
