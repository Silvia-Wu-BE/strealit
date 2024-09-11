import streamlit as st
import pandas as pd

# Function to read the CSV file
def get_data_from_csv(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df

# Streamlit UI
st.title("Select Variables for Calculation")

# Read data from the CSV file
csv_file_path = 'data.csv'  # Update with the path to your CSV file
data_df = get_data_from_csv(csv_file_path)

# Display the data in the app
st.write("Data from CSV:")
st.write(data_df)

# Dropdown for user to select a variable (column)
variable = st.selectbox("Select a variable (name)", data_df['name'])

# Input for the user to enter another value to multiply
multiplier = st.number_input("Enter a value to multiply with", min_value=1, max_value=100, value=1)

# Perform the calculation
if st.button("Calculate"):
    selected_value = data_df.loc[data_df['name'] == variable, 'value'].values[0]
    result = selected_value * multiplier
    st.write(f"Calculation result: {selected_value} * {multiplier} = {result}")
