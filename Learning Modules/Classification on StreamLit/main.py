import streamlit as st
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA



st.title("Classification Models")

st.write('''
         #### Explore various models/data
         Which one is the best?
         ''')

dataset_name = st.sidebar.selectbox("Select Dataset", ("Iris", "Breast Cancer", "Wine Quality"))
classifier_name = st.sidebar.selectbox("Select Classifier", ("KNN", "SVM", "Random Forest"))

st.write(f"User Selection -- Dataset : {dataset_name} | Classifier : {classifier_name}")



def get_dataset(dataset_name):
    if dataset_name == "Iris":
        data = datasets.load_iris()
    elif dataset_name == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    
    X = data.data
    y = data.target

    return X, y



X, y = get_dataset(dataset_name)
st.write("Shape of dataset : ", X.shape)
st.write("Number of classes : ", len(np.unique(y)))



def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["K"] = K
    elif clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = C
    elif clf_name == "Random Forest":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 10, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
    
    st.write("Model Parameters --")
    for k,v in params.items():
        st.write(f"{k} : {v}")

    return params



def get_classifier(clf_name, params):
    if clf_name == "KNN":
        clf = KNeighborsClassifier(n_neighbors=params["K"])
    elif clf_name == "SVM":
        clf = SVC(C=params["C"])
    elif clf_name == "Random Forest":
        clf = RandomForestClassifier(n_estimators=params["n_estimators"],
                                     max_depth=params["max_depth"],
                                     random_state=43)
    
    return clf



params = add_parameter_ui(classifier_name)
clf = get_classifier(classifier_name, params)

# Classification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)
st.write(f"Classifier : {classifier_name} | Accuracy : {acc}")

# Plot the dataset
pca = PCA(2)
X_proj = pca.fit_transform(X)

x1 = X_proj[:, 0]
x2 = X_proj[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

st.pyplot(fig)