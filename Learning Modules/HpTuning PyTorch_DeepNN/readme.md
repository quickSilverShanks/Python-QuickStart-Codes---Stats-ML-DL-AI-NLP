
The dataset used for this work is from a Kaggle competition "Mechanisms of Action (MoA) Prediction". Thus is a multilabel classification task with 876 features and 206 targets.
Data Source : https://www.kaggle.com/c/lish-moa


Terminal Commands to prepare the environment with optuna, pytorch and cuda installed:

01> conda create -n pytorch_gpu
02> conda activate pytorch_gpu
03> conda install pip
04> conda install cuda -c nvidia
05> conda install cudatoolkit -c nvidia/label/cuda-12.1.1
06> nvidia-smi
07> conda install pytorch-cuda=12.1 -c pytorch -c nvidia
>>  To check:
    > python
    > from torch import cuda
    > cuda.is_available()
    True
    > exit()
08> pip install optuna
09> pip install pandas scikit-learn iterative-stratification
10> If using VSCode to work on this project: ctrl+shift+p --> select interpreter --> pytorch_gpu



Terminal commands to train the model after changing directory to 'src' folder:
<ul>
    <li>python create_folds.py</li>
    <li>python train.py</li>
</ul>



Future Improvements:
<ul>
    <li>Add a learning rate scheduler in the model.</li>
    <li>Add an option to choose the best optimizer instead of using only Adam.</li>
    <li>Add a better evaluation metric that can be inferred easily, for instance, accuracy rate, f-scores etc..</li>
</ul>
