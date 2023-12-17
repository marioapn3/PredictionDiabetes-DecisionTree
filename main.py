import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualize

Tabs = {
     'Home': home,
     'Predict': predict,
     'Visualize': visualize
}

st.sidebar.title('Navigation')

selection = st.sidebar.radio("Go to", list(Tabs.keys()))

df, x, y = load_data()

if selection in ["Predict", "Visualize"]:
     Tabs[selection].app(df, x, y)
else:
     Tabs[selection].app()
