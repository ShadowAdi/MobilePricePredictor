import streamlit as st
import numpy as np 
import pandas as pd
import pickle

st.header("Smart Phone Price Prediction 📱")

with open("./pklFiles/X_Data", 'rb') as file:
    X_Data_load=pickle.load(file)
with open("./pklFiles/pipeline.pkl", 'rb') as file:
    pipeline=pickle.load(file)

with open("./pklFiles/bestModel.pkl", 'rb') as file:
    bestModel=pickle.load(file)
s1=st.selectbox("Select a Company",X_Data_load["Company"].unique())

s2=st.selectbox("Select a series",X_Data_load["series"].unique())

s3=st.selectbox("Select a color",X_Data_load["color"].unique())

s4=st.checkbox("Full HD")

s6=st.checkbox("FWVGA")

s7=st.select_slider("Select A RAM Value",options=X_Data_load["RAM"].unique())

s8=st.select_slider("Select A ROM Value",options=X_Data_load["ROM"].unique())

s9=st.select_slider("Select A Exapandable Value",options=X_Data_load["Expandable"].unique())

s5=st.number_input("Screen Size (in Cm)",5.0,20.0,5.0,0.1)

s10=st.number_input("Battery(in mAh)",1000.0,6000.0,1000.0,100.0)

s11=st.selectbox("Select a Brand",X_Data_load["Brand"].unique())

s12=st.selectbox("Select a Model",X_Data_load["Model"].unique())

s13=st.select_slider("Select A Main Camera Value",options=X_Data_load["Main_Camera_MP"].unique())

s15=st.select_slider("Select A Main Camera Count",options=X_Data_load["Main_Camera_Count"].unique())

s14=st.select_slider("Select A Front Camera Value",options=X_Data_load["Front_Camera_MP"].unique())

s16=st.select_slider("Select A Front Camera Count",options=X_Data_load["Front_Camera_Count"].unique())


btn=st.button("Predict Price")

if btn:
    if s4==True:
        s4=1
    else:
        s4=0
    if s5==True:
        s5=1
    else:
        s5=0

    predict_df={
        "Company":[s1],
        "series":[s2],
        "color":[s3],
        "Full HD":[s4],
        "ScreenSize(in cm)":[s5],
        "FWVGA":[s6],
        "RAM":[s7],
        "ROM":[s8],
        "Expandable":[s9],
        "Battery(in mAh)":[s10],
        "Brand":[s11],
        "Model":[s12],
        "Main_Camera_MP":[s13],
        "Front_Camera_MP":[s14],
        "Main_Camera_Count":[s15],
        "Front_Camera_Count":[s16],
    }

    query_df = pd.DataFrame(predict_df)


    
    transformed_data=pipeline.transform(query_df)

    # print(transformed_data)
    


    prediction = float(round(np.exp(bestModel.predict(transformed_data)[0]),2))
    st.subheader(f"The Predicted Price For Your Mobile Is: {prediction}")
    






