import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Mpora Ski Audience Clustering")
st.write("""

The following data has been collected from an onsite competition with the prize being a bundle of ski equipment including a pair of skis, outerwear and other accessories.

This application utilises audience clustering which allows the data to be filtered to show the brands the Mpora audience own based on number of ski trips year and their preferred style of skiing. 

""")

df = pd.read_csv("ski_clean.csv")

st.subheader("Select input data to dynamically change the output data")

def ski_filter(no_times_ski, backcountry, piste, freestyle):
  df_filter = df.loc[((df['no_ski_trips'] == no_times_ski)) & ((df['backcountry'] == backcountry)) & ((df['piste'] == piste)) & ((df['freestyle'] == freestyle))]
  return (df_filter[['armada', 'faction',	'planks',	'tnf',	'arcteryx',	'fjallraven',	'lowe_alpine',	'fw',	'patagonia',	'salomon',	'dakine',	'atomic',	'haglofs',	'rab',	'black_crows',	'black_diamond']].sum()*100/df_filter.piste.count())



no_times_ski = st.selectbox(
    'Ski trips a year',
    (0,1,2,3)
)

backcountry = st.selectbox(
    'Backcountry skier: 1=Yes, 0=No',
    (1,0)
)

piste = st.selectbox(
    'Piste skier: 1=Yes, 0=No',
    (1,0)
)

freestyle = st.selectbox(
    'Freestyle skier: 1=Yes, 0=No',
    (1,0)
)


st.write("""

Brands -- x-axis

Percentage of audience that own product from the brand -- y-axis

""")


st.bar_chart(ski_filter(no_times_ski, backcountry, piste, freestyle))