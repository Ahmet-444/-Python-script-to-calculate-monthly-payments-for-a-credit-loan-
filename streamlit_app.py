import streamlit as st
st.title("Credit Monthly Payment Calculator")
P = st.number_input("Enter the principal amount (P):",
min_value=0.0, format="%.2f")
r = st.number_input("Enter the monthly interest rate (r) as a percentage:",
min_value=0.0, format="%.4f")
n = st.number_input("Enter the number of months to repay the credit (n):",
min_value=1, format="%d")
A = 0.0
r = r/1200
if r > 0:
 A = P * r * (1+r)**n / ((1+r)**n - 1)
else:
    A = P / n

st.header(f"The monthly payment is: ${A:,.2f}")