import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load existing data or create new DataFrame
if st.checkbox("Do you have existing spend data?"):
    file = st.file_uploader("Upload a CSV file")
    if file is not None:
        data = pd.read_csv(file)
    else:
        data = pd.DataFrame(columns=["Date", "Category", "Amount"])
else:
    data = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Get user input
st.write("## Add New Spend Data")
amount = st.number_input("Amount", min_value=0.01, step=0.01)
category = st.selectbox("Category", ["Groceries", "Entertainment", "Travel", "Utilities", "Other"])
date = st.date_input("Date", pd.Timestamp.today().date())

# Add new spend data to DataFrame
if st.button("Add"):
    new_row = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    data = data.append(new_row, ignore_index=True)

# Display data
st.write("## Spend Data")
st.dataframe(data)

# Total Spend
st.write("## Total Spend")
total_spend = data["Amount"].sum()
st.write(f"Total Spend: ${total_spend:.2f}")

# Monthly Spend
st.write("## Monthly Spend")
monthly_spend = data.groupby(pd.Grouper(key="Date", freq="M"))["Amount"].sum().reset_index()
monthly_spend["Month"] = monthly_spend["Date"].dt.strftime("%b %Y")
st.bar_chart(monthly_spend.set_index("Month"))

# Category Spend
st.write("## Category Spend")
category_spend = data.groupby(["Category"])["Amount"].sum().reset_index()
st.bar_chart(category_spend.set_index("Category"))

# Date Range Filter
st.write("## Filter Data by Date Range")
min_date = data["Date"].min().date() if not data.empty else pd.Timestamp.today().date()
max_date = data["Date"].max().date() if not data.empty else pd.Timestamp.today().date()
start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

filtered_data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]
st.dataframe(filtered_data)

# Filtered Monthly Spend
st.write("## Filtered Monthly Spend")
filtered_monthly_spend = filtered_data.groupby(pd.Grouper(key="Date", freq="M"))["Amount"].sum().reset_index()
filtered_monthly_spend["Month"] = filtered_monthly_spend["Date"].dt.strftime("%b %Y")
st.bar_chart(filtered_monthly_spend.set_index("Month"))

# Filtered Category Spend
st.write("## Filtered Category Spend")
filtered_category_spend = filtered_data.groupby(["Category"])["Amount"].sum().reset_index()
st.bar_chart(filtered_category_spend.set_index("Category"))