This folder contains code to perform Hyperparameter Tuning using following techniques/libraries:
<ul>
  <li>Grid Search CV</li>
  <li>Random Search CV</li>
  <li>Gird/Random Search with sklearn Pipelines</li>
  <li>Bayesian Optimization using SkOpt</li>
  <li>HyperOpt</li>
  <li>Optuna</li>
</ul>

<br>Next Steps to implement:
<ul>
  <li>Put the functions in a utils.py code.</li>
  <li>Add logging to external files through decorators.</li>
  <li>Provide option to pass input parameters while calling a main model train function.</li>
  <li>Save models as pickled files. Run inference and explainability analysis on it.</li>
  <li>Log all trial models using MLFlow and register the best ones.</li>
</ul>

<br>The dataset is for Mobile Price Classification and is available on Kaggle: https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification/data
<br>The initial version of code is based on a youtube video live coding: https://www.youtube.com/watch?v=5nYqK-HaoKY
