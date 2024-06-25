
The dataset used for this work is from Kaggle "<b>IMDB Dataset of 50K Movie Reviews</b>". Thus is a binary classification task of sentiment analysis on IMDB reviews.
<br>Data Source : https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
<br>BERT model config files are from the location : https://www.kaggle.com/datasets/abhishek/bert-base-uncased?resource=download
<br>BERT model file must be downloaded from above location and put in bert_base_uncased folder as its ~400MB and hence unavailable in this GitHub repo.
<br><br>This learning module is based on the youtube video : https://www.youtube.com/watch?v=hinZO--TEk4

<br><br>The model downloaded from above link can be further trained and served using below commands:
<ul>
    <li>Go to the src folder then run train.py : python train.py</li>
    <li>Launch the flask server : python app.py</li>
    <li>Once its running, go to this link in browser to view the prediction : http://127.0.0.1:9999/predict</li>
    <li>Type any sentence in the url as shown here for its sentiment prediction : http://127.0.0.1:9999/predict?sentence=this repo is amazing</li>
</ul>


<br><br>Future Improvements:
<ul>
    <li>Add Docker model training and serve it using Flask</li>
</ul>
