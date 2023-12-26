import streamlit as st
from web_function import load_data
from streamlit_option_menu import option_menu
from Tabs import home, predict, visualize

Tabs = {
     'Home': home,
     'Predict': predict,
     'Visualize': visualize
}
# make this title on center
st.title("Diabetes Prediction App using Decision Tree Algorithm", anchor='center')
selected = option_menu(
    menu_title=None, 
    options=["Home", "Predict", "Visualize"],
    icons=["house", "eye", "list"],
    menu_icon="cast",
    default_index = 0,
    orientation="horizontal",

)


df, x, y = load_data()



if selected == "Home":
     Tabs["Home"].app()
elif selected == "Predict":
     Tabs["Predict"].app(df, x, y)
elif selected == "Visualize":
     Tabs["Visualize"].app(df, x, y)