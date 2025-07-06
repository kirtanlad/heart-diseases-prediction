

import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe1.pkl','rb'))
df = pickle.load(open('data.pkl','rb'))
 
st.title("Heart Predictor")
# brand
# User input fields
age = st.number_input("Age", min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type', ['Typical angina', 'Atypical Angina', 'Non-Anginal pain', 'Asymptomatic'])
trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=0, value=120)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, value=200)
fbs = st.selectbox('Fasting Blood Sugar (>120 mg/dl)', ['True', 'False'])
restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality', 'Showing probable'])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, value=150)
exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, value=0.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
ca = st.number_input('Number of Major Vessels (0-3)', min_value=0, max_value=3, value=0)
thal = st.selectbox('Thalassemia', ['None', 'Normal', 'Fixed defect', 'Reversible defect'])

def prd(p):
    if p==0:
        return "Congratulation you are safe"
    else:
        return "Please concernt to you doctor"
    
if st.button('Predict heart'):
    # query
    ppi = None
    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    if cp == 'Typical angina':
        cp = 0
    elif cp=="Atypical angina":
        cp = 1
    elif cp=="Non-anginal pain":
        cp=2
    else:
        cp=3

    if fbs == 'True':
        fbs = 1
    else:
        fbs = 0

    if restecg == 'Normal':
        restecg = 0
    elif restecg=="Having ST-T wave abnormality":
        restecg = 1
    else:
        restecg=3

    if exang == 'Yes':
        exang = 1
    else:
        exang = 0

    if slope == 'Upsloping':
        slope = 0
    elif slope=="Flat":
        slope = 1
    else:
        slope=3

    if thal == 'None':
        thal = 0
    elif thal=="Normal":
        thal = 1
    elif thal=="Fixed defect":
        thal = 2
    elif thal=="Reversable defect":
        thal=3

    query = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal],dtype=object).reshape(1,13)
    
    p=pipe.predict(query)

    st.write(prd(p))
# fnsafn