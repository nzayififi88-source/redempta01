import pickle
import numpy as np
import streamlit as st

#with open ('saving.pkl','rb') as file :
      #  model=pickle .load(file)

with open('C:/Users/user/Desktop/my work in machine learning/saving.pkl', 'rb') as file:
    model = pickle.load(file)

    
st.title ("loan prediction ")
st.write ("fill the following information")
income = st.number_input("income")
credit_score = st.number_input("credit_score")
loan_amount = st.number_input("loan_amount")
year_employed = st.number_input("years_employed")
#points = st.number_input("points")
if st.button ("predict"):
    arr= np.array([[income,credit_score,loan_amount,year_employed]])
    y_pred=model.predict(arr)
    st.success(y_pred[0])
    
                     