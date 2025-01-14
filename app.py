import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import calendar
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout="wide")

# st.set_page_config(layout="centered", initial_sidebar_state="expanded", theme={"base": "light"})


st.title("Light Mode Only App")

# leguppicks
# url = "https://docs.google.com/spreadsheets/d/1XoVHcy6qqwKKT7HiIb5CKwv32_1Ce1fhl5XoPW-lREI/edit?usp=sharing" 

# POTD original
# url = "https://docs.google.com/spreadsheets/d/1KD-sPzMceSj-rWafb-6FPzhoaAQ48i2r2p9oJDQEoUY/edit?usp=sharing"

# POTD test
url = "https://docs.google.com/spreadsheets/d/1PfOBLuiQcNfOdTgdTAkgw8vqivz7liHQimlzr4AgBHc/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# Display the DataFrame without the index


# Define a list of new, readable column names
new_column_names = [
    'Column_1', 'Column_2', 'Column_3', 'Column_4', 'Column_5', 'Column_6', 
    'Column_7', 'Column_8', 'Column_9', 'Column_10', 'Column_11', 'Column_12', 
    'Column_13', 'Column_14', 'Column_15', 'Column_16', 'Column_17'
]

# Rename the columns
df.columns = new_column_names

# Now you can reference the columns by their new names

#
###



st.dataframe(df, hide_index=True)



