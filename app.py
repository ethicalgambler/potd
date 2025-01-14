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



# leguppicks
# url = "https://docs.google.com/spreadsheets/d/1XoVHcy6qqwKKT7HiIb5CKwv32_1Ce1fhl5XoPW-lREI/edit?usp=sharing" 

# POTD original
# url = "https://docs.google.com/spreadsheets/d/1KD-sPzMceSj-rWafb-6FPzhoaAQ48i2r2p9oJDQEoUY/edit?usp=sharing"

# POTD test
url = "https://docs.google.com/spreadsheets/d/1PfOBLuiQcNfOdTgdTAkgw8vqivz7liHQimlzr4AgBHc/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# Display the DataFrame without the index


# Function to process the `=HYPERLINK` formulas
def extract_hyperlink(cell):
    # Check if the cell contains the `=HYPERLINK` function
    if isinstance(cell, str) and cell.startswith('=HYPERLINK('):
        # Parse the URL and display text
        url_start = cell.find('"') + 1
        url_end = cell.find('"', url_start)
        url = cell[url_start:url_end]
        
        display_text_start = cell.find('"', url_end + 1) + 1
        display_text_end = cell.find('"', display_text_start)
        display_text = cell[display_text_start:display_text_end]
        
        # Return the HTML for a clickable link
        return f'<a href="{url}" target="_blank">{display_text}</a>'
    return cell

# Apply the function to the entire DataFrame
df = df.applymap(extract_hyperlink)

# Display the DataFrame with clickable links
st.markdown(
    df.to_html(escape=False, index=False),
    unsafe_allow_html=True
)













st.dataframe(df, hide_index=True)



