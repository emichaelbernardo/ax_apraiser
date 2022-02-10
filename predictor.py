import streamlit as st
import pandas as pd

st.title('Used Guitar Appraiser')

df = pd.DataFrame({
    'Brand': ['Fender','Gibson','Epiphone','Jackson'],
    'second column': [10, 20, 30, 40]
    })


#DATE_COLUMN = 'date/time'
DATA_URL = ('https://storage.cloud.google.com/guitars/data/all_used_guitars.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
    



option = st.selectbox(
    'What brand is your guitar?',
     df['Brand'])

'You selected: ', option
