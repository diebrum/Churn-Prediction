!pip install sklearn
import xgboost as xgb
import streamlit as st
import pandas as pd

#Loading up the Regression model we created
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

#Caching the model for faster loading
@st.cache
def predict(Age,Total_Purchase,Account_Manager,Years,Num_Sites):   

    churn_pred = model.predict(pd.DataFrame([[Age,Total_Purchase,Account_Manager,Years,Num_Sites]], columns=['Age','Total_Purchase','Account_Manager','Years,Num_Sites']))
    return churn_pred
st.title('Churn Detector')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the characteristics of the Client:')

Age = st.number_input('Client Age:', min_value=0.1, max_value=100.0, value=1.0)
Total_Purchase = st.number_input('Total_Purchase:', min_value=0.1, max_value=100000.0, value=1.0)
Account_Manager = st.number_input('Account_Manager:', min_value=0, max_value=1, value=1.0)
Years = st.number_input('Years:', min_value=0.1, max_value=1000.0, value=1.0)
Num_Sites = st.number_input('Num_Sites:', min_value=0.1, max_value=10000.0, value=1.0)

if st.button('Predict Price'):
    churn = predict(Age,Total_Purchase,Account_Manager,Years,Num_Sites)
    st.success(f'The client churn probability is  ${churn[0]:.2f} ')
