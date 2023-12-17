import streamlit as st

from web_function import predict

def app(df,x,y):

     st.title('Diabetes Prediction App')

     st.write('Please enter the following data for prediction')
     Glucose = st.slider('Glucose', 0.0, 20.0, 0.0)
     BloodPressure = st.slider('BloodPressure', 0.0, 150.0, 0.0)
     Insulin = st.slider('Insulin', 0.0, 1000.0, 0.0)
     bmi = st.slider('BMI', 0.0, 100.0, 0.0)
     Age = st.slider('Age', 0.0, 81.0, 0.0)
     
     features = [Glucose,BloodPressure,Insulin,bmi,Age]

     if st.button('Predict'):
          prediction , score = predict(x,y,features)
          if prediction == 1:
               st.warning('You have Diabetes')
          else:
               st.success('You do not have Diabetes')
        
          st.write('Accuracy score of this model is : ' , (score*100),"%")