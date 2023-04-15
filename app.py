import streamlit as st
import pandas as pd
import os

# Define the name of the CSV file to store the data
CSV_FILE_NAME = "spend_data.csv"

# Define the columns for the CSV file
CSV_COLUMNS = ["Item", "Amount"]

# Define a function to clear the CSV file
def clear_csv_file():
    if os.path.isfile(CSV_FILE_NAME):
        os.remove(CSV_FILE_NAME)
    with open(CSV_FILE_NAME, "w") as file:
        file.write(",".join(CSV_COLUMNS) + "\n")

# Check if the CSV file exists, if not create it
if not os.path.isfile(CSV_FILE_NAME):
    clear_csv_file()

# Define a function to append data to the CSV file
def append_data_to_csv_file(item, amount):
    with open(CSV_FILE_NAME, "a") as file:
        file.write(item + "," + str(amount) + "\n")

# Define a function to read the CSV file and return a DataFrame
def read_csv_file():
    clear_csv_file()
    return pd.read_csv(CSV_FILE_NAME)

# Define the Streamlit app
def app():
    # Set the title of the app
    st.title("Spend Analyzer")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.pixelstalk.net/wp-content/uploads/images6/Dark-Blue-Background-Desktop.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    # Create a form for user input
    form = st.form(key="spend_form")
    
    # Add form fields for item and amount
    item = form.text_input("Item")
    amount = form.number_input("Amount", min_value=0.01, step=0.01)
    
    # Add a submit button to the form
    submitted = form.form_submit_button("Submit")
    
    # If the form is submitted, append the data to the CSV file
    if submitted:
        append_data_to_csv_file(item, amount)
    
    # Read the CSV file and display the spend data as a table
    spend_data = read_csv_file()
    st.table(spend_data)
    
    # Display a spend chart based on the spend data
    spend_chart_data = spend_data.groupby("Item")["Amount"].sum()
    st.bar_chart(spend_chart_data)

if __name__=="__main__":
    app()
