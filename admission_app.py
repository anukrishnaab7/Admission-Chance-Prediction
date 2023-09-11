import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import joblib

# Load the pickled model
classifier = joblib.load('classifier.pkl')

def welcome():
    return 'welcome all'

def prediction(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research):
    prediction = classifier.predict([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])
    print(prediction)
    return prediction
# this is the main function in which we define our webpage 
def main():
    st.title("Chance of Admission for Higher Studies")
      
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Admission Prediction </h1>
    </div>
    """
      
    st.markdown(html_temp, unsafe_allow_html=True)
      
    GRE_Score = st.text_input("GRE_Score", "Type Here")
    TOEFL_Score = st.text_input("TOEFL_Score", "Type Here")
    University_Rating = st.text_input("University_Rating", "Type Here")
    SOP = st.text_input("SOP", "Type Here")
    LOR = st.text_input("LOR", "Type Here")
    CGPA = st.text_input("CGPA", "Type Here")
    Research = st.text_input("Research", "Type Here")

    result = ""
      
    if st.button("Predict"):
        # Convert input values to numeric
        GRE_Score = float(GRE_Score)
        TOEFL_Score = float(TOEFL_Score)
        University_Rating = float(University_Rating)
        SOP = float(SOP)
        LOR = float(LOR)
        CGPA = float(CGPA)
        Research = float(Research)
        
        prediction_result = prediction(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research)
        
        if len(prediction_result) > 0:
            prediction_percentage = prediction_result[0] * 100
            st.success('Your chance of admission is {:.2f}%'.format(prediction_percentage))
        else:
            st.error('Error in prediction')
     
if __name__=='__main__':
    main()

# streamlit run admission_app.py
