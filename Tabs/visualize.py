import warnings
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns   
from sklearn import tree
from sklearn.metrics import confusion_matrix
import streamlit as st

from web_function import train_model

def app(df, x, y):
    warnings.filterwarnings("ignore")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualize Page Diabetes Prediction App")

    if st.checkbox('Plot Confusion Matrix'):
        model, score = train_model(x, y)
        y_pred = model.predict(x)  # Predictions on the features
        cm = confusion_matrix(y, y_pred)
        plt.figure(figsize=(10, 7))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
        plt.xlabel('Predicted')
        plt.ylabel('True')
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, 
            rounded=True, class_names=['No Diabetes', 'Diabetes'], 
            feature_names=x.columns
        )
        st.graphviz_chart(dot_data)

