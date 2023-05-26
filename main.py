import numpy as np
import pandas as pd
import streamlit as st 
import joblib

classifier=joblib.load('creditScore.pkl')


def welcome():
    return "Welcome All"


def predict_CreditScore(Age,Occupation,Annual_Income,Monthly_Inhand_Salary,Num_Bank_Accounts,Num_Credit_Card,Interest_Rate,Num_of_Loan,Delay_from_due_date,Num_of_Delayed_Payment,Changed_Credit_Limit,Num_Credit_Inquiries,Credit_Mix,Outstanding_Debt,Credit_Utilization_Ratio,Payment_of_Min_Amount,Total_EMI_per_month,Amount_invested_monthly,Payment_Behaviour,Monthly_Balance ):

    prediction=classifier.predict(pd.DataFrame({'Age':[Age],'Occupation':[Occupation],"Annual_Income":[Annual_Income],"Monthly_Inhand_Salary":[Monthly_Inhand_Salary],'Num_Bank_Accounts':[Num_Bank_Accounts],'Num_Credit_Card':[Num_Credit_Card],'Interest_Rate':[Interest_Rate],"Num_of_Loan":[Num_of_Loan],"Delay_from_due_date":[Delay_from_due_date],"Num_of_Delayed_Payment":[Num_of_Delayed_Payment],"Changed_Credit_Limit":[Changed_Credit_Limit],"Num_Credit_Inquiries":[Num_Credit_Inquiries],"Credit_Mix":[Credit_Mix],"Outstanding_Debt":[Outstanding_Debt],"Credit_Utilization_Ratio":[Credit_Utilization_Ratio],"Payment_of_Min_Amount":[Payment_of_Min_Amount],"Total_EMI_per_month":[Total_EMI_per_month],"Amount_invested_monthly":[Amount_invested_monthly],"Payment_Behaviour":[Payment_Behaviour],"Monthly_Balance":[Monthly_Balance]}))

    return prediction
  
      
def main():
    st.title("Credit Score Classification")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit Score Classification ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age= st.text_input("Age","30")
    Occupation= st.text_input("Occupation","Developer")
    Annual_Income= st.text_input("Annual_Income","50000")
    Monthly_Inhand_Salary = st.text_input("Monthly_Inhand_Salary","5000")
    Num_Bank_Accounts= st.text_input("Num_Bank_Accounts","5")
    Num_Credit_Card= st.text_input("Num_Credit_Card","9")
    Interest_Rate= st.text_input("Interest_Rate","12")
    Num_of_Loan= st.text_input("Num_of_Loan","50")
    Delay_from_due_date = st.text_input("Delay_from_due_date","50")
    Num_of_Delayed_Payment= st.text_input("Num_of_Delayed_Payment","5")
    Changed_Credit_Limit = st.text_input("Changed_Credit_Limit","50")
    Num_Credit_Inquiries = st.text_input("Num_Credit_Inquiries","20")
    Credit_Mix = st.text_input("Credit_Mix","Good")
    Outstanding_Debt= st.text_input("Outstanding_Debt","809.98")
    Credit_Utilization_Ratio= st.text_input("Credit_Utilization_Ratio","31.944960")
    Payment_of_Min_Amount= st.text_input("Payment_of_Min_Amount","No")
    Total_EMI_per_month= st.text_input("Total_EMI_per_month","49.574949")
    Amount_invested_monthly= st.text_input("Amount_invested_monthly","80.41529543900253")
    Payment_Behaviour= st.text_input("Payment_Behaviour","High_spent_Small_value_payments")
    Monthly_Balance= st.text_input("Monthly_Balance","312.49408867943663")
    
    result=""
    if st.button("Predict"):
        result=predict_CreditScore(Age,Occupation,Annual_Income,Monthly_Inhand_Salary,Num_Bank_Accounts,Num_Credit_Card,Interest_Rate,Num_of_Loan,Delay_from_due_date,Num_of_Delayed_Payment,Changed_Credit_Limit,Num_Credit_Inquiries,Credit_Mix,Outstanding_Debt,Credit_Utilization_Ratio,Payment_of_Min_Amount,Total_EMI_per_month,Amount_invested_monthly,Payment_Behaviour,Monthly_Balance)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main() 
