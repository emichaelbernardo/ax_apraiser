import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Brand': ['Fender','Gibson','Epiphone','Jackson'],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'What brand is your guitar?',
     df['Brand'])

'You selected: ', option
