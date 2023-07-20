import streamlit as st
import pickle
import numpy as np
#from PIL import Image
from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#image = Image.open('FuelPredx_logo.jpg')

def load_model():
    with open('Draft_gbr_saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor = data["model"]

def show_predict_page():

    st.markdown("<h1 style='text-align: center; color: DarkGoldenRod;'>TracDraft</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: DarkGreen;'> Cloud-centric Serverless Package for Transient Draft prediction of Tractor</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: DarkRed;'>Input the following tractor  parameters for real-time draft prediction of tractor : </h3>", unsafe_allow_html=True)

    #st.sidebar.image(image, use_column_width=True)
    TractorPTOPower = st.number_input('Tractor maximum PTO power (hp)')
    Tractor_PTO2 = TractorPTOPower / 1.36
    Tirewidth = st.number_input('Tire Sectional width (m)')
    Tiredia = st.number_input('Tire overall diameter (m)')
    Drawbarheight = st.number_input('Drawbar height (m)')
    Wheelbase = st.number_input('Wheel base (m)')
    Totalmass = st.number_input('Total mass (kN)')
    Velocity = st.number_input('Forward Velocity (km/h)')
    #Engine_Speed = st.number_input('Engine operating speed (rpm)')
    #Speed_Depression = st.number_input('Engine speed depression (rpm)')

    #Tractor_PTO = st.number_input('Tractor maximum PTO power (hp)')
    #Tractor_PTO2 = Tractor_PTO/1.36
    #Engine_Speed = st.number_input('Engine operating speed (rpm)')
    #Speed_Depression = st.number_input('Engine speed depression (rpm)')

    ok = st.button("Predict Maximum Drawbar Pull")
    if ok:
        X = np.array([[Tractor_PTO2, Tirewidth, Tiredia, Drawbarheight, Wheelbase, Totalmass, Velocity]])
        #Y = sc.transform(X)
        #Y = Y.astype(float)
        X = X.astype(float)
        salary = regressor.predict(X)
        st.subheader(f"The maximum drawbar pull at 15% wheel slip (kN) is {salary[0]:.2f}")



