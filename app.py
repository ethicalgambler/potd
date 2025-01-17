import streamlit as st
from streamlit_theme import st_theme
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import calendar
import time
import pytz
import pathlib
import numpy as np
from streamlit_gsheets import GSheetsConnection


# Load page config start
st.set_page_config(layout="wide")
# Load page config end

# Custom CSS fucntion start
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)
# Custom CSS fucntion end

# Script to identify if light mode is being used
theme = st_theme()
background_color = theme.get("backgroundColor", None)

if background_color != "#ffffff":
    st.warning("This is a warning alert!")
else:
    
    url = "https://docs.google.com/spreadsheets/d/1PfOBLuiQcNfOdTgdTAkgw8vqivz7liHQimlzr4AgBHc/edit?usp=sharing"

    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    column_names = [
        'Capper', 'Tot W/L', 'L10', 'STRK', 'Avg U', 'ROI %', 'Date', 'League / Sport', 'Pick /Prop', 'Units', 'US', 'Dec', 'W', 'L', 'P', 'W/L', 'Notes'
    ]

    df.columns = column_names

    



    # today = datetime.today()
    # formatted_date = today.strftime('%m/%d/%y').lstrip('0').replace('/0', '/')
    # st.success(formatted_date)

    user_timezone = pytz.timezone('America/New_York')  # Example for Eastern Time
    user_time = datetime.now(user_timezone)

    formatted_date = user_time.strftime('%m/%d/%y').lstrip('0').replace('/0', '/')
    st.success(formatted_date)

    

    # Filter the DataFrame to show only rows from today
    df_today = df[df['Date'] == formatted_date]


    st.dataframe(df_today, hide_index=True)
    # st.dataframe(df_today)


