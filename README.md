

# Spend Analyser using Python

This is a Spend Analyser app built with Python using the Streamlit library. It allows users to input their spending data, which is then stored in a CSV file. The app then reads the CSV file and displays the spending data as a table and a chart.

## Installation

To run this app on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the repository directory in your terminal.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the app by running `streamlit run app.py`.

## Usage

Once you have the app running, you can start inputting your spending data by filling in the form on the left-hand side of the app. You can input the item and amount spent, and then click the "Submit" button to save the data to the CSV file.

The spending data is then displayed as a table and a chart on the right-hand side of the app. The chart displays the total amount spent on each item.

If you want to clear all the spending data, you can click the "Clear All" button at the bottom of the app.

## Code Overview

The code defines a Spend Analyser app using Streamlit library. It consists of three major parts:

1. CSV file handling - The app reads and writes spending data to a CSV file, and checks if the file exists before writing data to it.

2. User input form - The app creates a form for users to input their spending data, including the item and amount spent.

3. Data visualization - The app displays the spending data as a table and a bar chart, showing the total amount spent on each item.

The app allows users to input their spending data, which is then stored in the CSV file. The spending data is then displayed in a table and a chart, which helps users visualize their spending patterns.

Additionally, the app includes a "Clear All" button that allows users to clear all the spending data from the CSV file.

## Streamlit Link

You can also view this app on Streamlit Sharing by clicking [here](https://deepankarvarma-spend-analyser-using-python-app-co2dtv.streamlit.app/).
