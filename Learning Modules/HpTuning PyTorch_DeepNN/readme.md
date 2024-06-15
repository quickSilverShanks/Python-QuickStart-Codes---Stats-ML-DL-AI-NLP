
The dataset used for this work is from a Kaggle competition "<b>Mechanisms of Action (MoA) Prediction</b>". Thus is a multilabel classification task with 876 features and 206 targets.
<br>Data Source : https://www.kaggle.com/c/lish-moa


<br>Terminal Commands to prepare the environment with optuna, pytorch and cuda installed:

01> conda create -n pytorch_gpu
<br>02> conda activate pytorch_gpu
<br>03> conda install pip
<br>04> conda install cuda -c nvidia
<br>05> conda install cudatoolkit -c nvidia/label/cuda-12.1.1
<br>06> nvidia-smi
<br>07> conda install pytorch-cuda=12.1 -c pytorch -c nvidia
<br>&nbsp;&nbsp;&nbsp;&nbsp;To check:
<br>&nbsp;&nbsp;&nbsp;&nbsp;> python
<br>&nbsp;&nbsp;&nbsp;&nbsp;> from torch import cuda
<br>&nbsp;&nbsp;&nbsp;&nbsp;> cuda.is_available()
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True
<br>&nbsp;&nbsp;&nbsp;&nbsp;> exit()
<br>08> pip install optuna
<br>09> pip install pandas scikit-learn iterative-stratification
<br>10> If using VSCode to work on this project: ctrl+shift+p --> select interpreter --> pytorch_gpu



<br>Note : Unzip input/train_features.zip before starting the code runs.
<br><br>Terminal commands to train the model after changing directory to 'src' folder:
<ul>
    <li>python create_folds.py</li>
    <li>python train.py</li>
</ul>

<br><br>Future Improvements:
<ul>
    <li>Add a learning rate scheduler in the model.</li>
    <li>Add an option to choose the best optimizer instead of using only Adam.</li>
    <li>Add a better evaluation metric that can be inferred easily, for instance, accuracy rate, f-scores etc..</li>
</ul>
