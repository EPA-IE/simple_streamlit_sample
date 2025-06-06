import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd


st.title('Simple test app')

# generate data
df = pd.DataFrame(np.random.randint(0,500,size=(50, 3)), columns=list('ABC')) 
st.write(df)


# df.plot(x='A', y='B', kind='scatter', s='C')

fig = px.scatter(df, x='A', y='B', size='C')
st.plotly_chart(fig)