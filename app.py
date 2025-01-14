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
# st.set_page_config(base="light")



url = "https://docs.google.com/spreadsheets/d/1XoVHcy6qqwKKT7HiIb5CKwv32_1Ce1fhl5XoPW-lREI/edit?usp=sharing" 
# url = "https://docs.google.com/spreadsheets/d/1KD-sPzMceSj-rWafb-6FPzhoaAQ48i2r2p9oJDQEoUY/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
df['Date'] = pd.to_datetime(df['Date'])



df_filtered = df
st.dataframe(df_filtered)


# git add . && git commit -m "Deploy test commits" && git push -u origin main