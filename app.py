import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the pre-trained machine learning model
model = pickle.load(open('credit_2.pkl', 'rb'))

# Create the input fields for the user to input values
gender = st.selectbox('Gender', ['Male', 'Female'])
education_level = st.selectbox('Education Level', ['High School', 'Graduate', 'Uneducated', 'College', 'Post-Graduate', 'Doctorate'])
marital_status = st.selectbox('Marital Status', ['Divorced', 'Married', 'Single'])
Income_Category = st.selectbox('Income Category', ['$120K+', '$40k-$60k', '$60K-$80K', '$80K-$120K', 'Less than $40K'])
Card_Category = st.selectbox('Card Category', ['Blue', 'Gold', 'Platinum'])

dependent_count = st.text_input('Dependent Count', '0')
total_relationship_count = st.text_input('Total Relationship Count', '0')
months_inactive_12_mon = st.text_input('Months Inactive 12 Months', '0')
contacts_count_12_mon = st.text_input('Contacts Count 12 Months', '0')
total_amt_chng_q4_q1 = st.text_input('Total Amount Change Q4 Q1', '0')
total_trans_ct = st.text_input('Total Transaction Count', '0')
total_ct = st.text_input('Total Transaction Change','0')

gender_val = 1 if gender == 'Male' else 0
edu_val = 0 if education_level == 'High School' else 1 if education_level == 'Graduate' else 2 if education_level == 'Uneducated' else 3 if education_level == 'College' else 4 if Education_Level == 'Post-Graduate' else 5 if Education_Level == 'Doctorate' else 6
mrg_val = 0 if marital_status == 'Divorced' else 1 if marital_status == 'Married' else 2 if marital_status == 'Single' else 3 
inc_val = 0 if Income_Category == '$120K+' else 1 if Income_Category == '$40k-$60k' else 2 if Income_Category == '$60K-$80K' else 3 if Income_Category == '$80K-$120K' else 4 if Income_Category == 'Less than $40K' else 5 
ctg_val = 0 if Card_Category == 'Blue' else 1 if Card_Category == 'Gold' else 2 if Card_Category == 'Platinum' else 3

input_df = pd.DataFrame({
'Gender': [int(gender_val)],
'Education_Level': [int(edu_val)],
'Marital_Status': [int(mrg_val)],
'Income_Category': [int(inc_val)],
'Card_Category': [int(ctg_val)],
'Dependent_count': [int(dependent_count)],
'Total_Relationship_Count': [int(total_relationship_count)],
'Months_Inactive_12_mon': [int(months_inactive_12_mon)],
'Contacts_Count_12_mon': [int(contacts_count_12_mon)],
'Total_Amt_Chng_Q4_Q1': [int(total_amt_chng_q4_q1)],
'Total_Trans_Ct': [int(total_trans_ct)]
})
prediction = model.predict(input_df)
st.write('The predicted category of this customer is:', prediction[0])