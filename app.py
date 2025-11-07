import streamlit as st
import numpy as np

# App title and layout
st.set_page_config(page_title="Financial Calculator", page_icon="💰", layout="centered")

st.title("💰 Simple Financial Calculator")
st.write("Use this app to calculate **EMI**, **Simple Interest**, or **Compound Interest**.")

# Sidebar for selecting function
option = st.sidebar.selectbox(
    "Select Calculation Type",
    ("Loan EMI Calculator", "Simple Interest", "Compound Interest")
)

# EMI Calculator
if option == "Loan EMI Calculator":
    st.header("🏦 Loan EMI Calculator")
    principal = st.number_input("Enter Loan Amount (PKR)", min_value=0.0, step=1000.0)
    annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
    years = st.number_input("Loan Tenure (Years)", min_value=0.0, step=1.0)

    if st.button("Calculate EMI"):
        monthly_rate = annual_rate / (12 * 100)
        months = years * 12
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
        st.success(f"📊 Monthly EMI: **PKR {emi:,.2f}**")

# Simple Interest
elif option == "Simple Interest":
    st.header("📈 Simple Interest Calculator")
    principal = st.number_input("Principal Amount (PKR)", min_value=0.0, step=1000.0)
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
    time = st.number_input("Time (Years)", min_value=0.0, step=1.0)

    if st.button("Calculate Interest"):
        si = (principal * rate * time) / 100
        total = principal + si
        st.info(f"Simple Interest: **PKR {si:,.2f}**")
        st.success(f"Total Amount after {time} years: **PKR {total:,.2f}**")

# Compound Interest
elif option == "Compound Interest":
    st.header("💹 Compound Interest Calculator")
    principal = st.number_input("Principal Amount (PKR)", min_value=0.0, step=1000.0)
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1)
    time = st.number_input("Time (Years)", min_value=0.0, step=1.0)
    compounding = st.selectbox("Compounding Frequency", ("Annually", "Semi-Annually", "Quarterly", "Monthly"))

    freq_map = {"Annually": 1, "Semi-Annually": 2, "Quarterly": 4, "Monthly": 12}
    n = freq_map[compounding]

    if st.button("Calculate Compound Interest"):
        amount = principal * (1 + (rate / (100 * n)))**(n * time)
        ci = amount - principal
        st.info(f"Compound Interest: **PKR {ci:,.2f}**")
        st.success(f"Total Amount after {time} years: **PKR {amount:,.2f}**")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
