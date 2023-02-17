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
st.image("""https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.startuphero.com.br%2Fwp-content%2Fuploads%2F2020%2F04%2FChurn-rate.jpg&imgrefurl=https%3A%2F%2Fwww.startuphero.com.br%2Fchurn-rate-e-o-valor-de-manter-os-clientes-certos%2F&tbnid=oPrbAHJMrxenoM&vet=12ahUKEwi81v_Hzpv9AhUMh5UCHdRcADoQMygCegUIARDWAQ..i&docid=eCY4Cqdgmep_pM&w=1003&h=601&q=churn&ved=2ahUKEwi81v_Hzpv9AhUMh5UCHdRcADoQMygCegUIARDWAQ""")
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
    
