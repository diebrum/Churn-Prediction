from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pandas as pd
import joblib

#Loading up the Regression model we created
model = joblib.load('joblib_model.pkl')


#Caching the model for faster loading
@st.cache
def predict(Age,Total_Purchase,Account_Manager,Years,Num_Sites): 
    churn_pred = model.predict(pd.DataFrame([[Age,Total_Purchase,Account_Manager,Years,Num_Sites]], columns=['Age','Total_Purchase','Account_Manager','Years','Num_Sites']))
    return churn_pred

st.title('Churn Detector')
st.image("""https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.lumis.com.br%2Fdata%2Ffiles%2FA0%2F86%2F3B%2F8D%2F1059B61043F8EBA68E0BF9C2%2Fartigo__churn-rate__interna-03.png&imgrefurl=https%3A%2F%2Fwww.lumis.com.br%2Fa-lumis%2Fblog%2Fchurn-rate-saiba-o-que-e-e-como-diminuir-essa-taxa.htm&tbnid=cVwQ1R6DPBBCGM&vet=12ahUKEwjfj6nCz5v9AhVTTLgEHe9XDbwQMygEegUIARCSAQ..i&docid=1mfR2RfneDlpYM&w=334&h=259&q=churn.png""")
st.header('Enter the characteristics of the Client:')

Age = st.number_input('Client Age:', min_value=0.1, max_value=100.0, value=1.0)
Total_Purchase = st.number_input('Total_Purchase:', min_value=0.1, max_value=100000.0, value=1.0)
Account_Manager = st.number_input('Account_Manager:', min_value=0.0, max_value=1.0, value=1.0)
Years = st.number_input('Years:', min_value=0.1, max_value=1000.0, value=1.0)
Num_Sites = st.number_input('Num_Sites:', min_value=0.1, max_value=10000.0, value=1.0)

if st.button('Predict Price'):
    churn = predict(Age,Total_Purchase,Account_Manager,Years,Num_Sites)
    if churn==0:
        st.success("No Churn!")
    else:
        st.success("Churn!")
    
