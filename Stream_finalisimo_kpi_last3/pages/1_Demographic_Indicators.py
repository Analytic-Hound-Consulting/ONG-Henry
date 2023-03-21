import pandas as pd
import streamlit as st
import plotly.express as px
import base64
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import plotly.graph_objs as go
from PIL import Image


st.set_page_config(
    page_title='Demographic Indicators',
    layout='wide'
)

image = Image.open('./Stream_finalisimo_kpi_last3/images/demograficosIng.jpg')

st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTANT VARIABLES ON THIS CATEGORY OF INDICATORS.]")

st.markdown("-----------")


df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")


#Grafico Population Total

st.write (':blue[_POPULATION TOTAL: Bases on the facto definition of population, which counts all residents regardless of legal status or citizenship. (Total)._]')
    
df_gup = df.groupby(['Year'])['Population Total'].sum().reset_index()

fig_pb = px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Total'], title="Total Population")

fig_pb.update_traces(line_color='#728C9F', line_width=3)

#-----------------------------------------------

# Gráfico Population Total FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Total'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()
selected_pais = st.sidebar.selectbox("Select a country:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_pb_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Total'],  title=f'Total Population: {selected_pais}')
fig_pb_fil.update_traces(line_color='#ED80DD', line_width=3)

col35,col36 = st.columns(2)

with col35:
    st.plotly_chart(fig_pb,use_container_width=True )

with col36:
    st.plotly_chart(fig_pb_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------------

st.write (':blue[_POPULATION DENSITY : Amount of people per square meter of land area (people per sq. hm of land area)._]')

#Grafico 19

df_gup = df.groupby(['Year'])['Population Density'].sum().reset_index()

fig_dp = px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Density'], title="Population Density")
fig_dp.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Density'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_dp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Density'],  title=f'Population Density: {selected_pais}')
fig_dp_fil.update_traces(line_color='#ED80DD', line_width=3)

col37,col38 = st.columns(2)

with col37:
    st.plotly_chart(fig_dp,use_container_width=True )

with col38:
    st.plotly_chart(fig_dp_fil,use_container_width=True )
    
st.markdown("-----------")
#------------------------------------------------
#Grafico 20

st.write (':blue[_NATURAL CHANGE: Births minus Deaths (thousands)._]')

df_gup = df.groupby(['Year'])['Natural Change, Births minus Deaths (thousands)'].sum().reset_index()

fig_nm= px.line(df_gup, x=df_gup["Year"], y=df_gup['Natural Change, Births minus Deaths (thousands)'], title='Natural change, births minus deaths (thousands)')
fig_nm.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Natural Change, Births minus Deaths (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_nm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Natural Change, Births minus Deaths (thousands)'],  title=f'Natural change, births minus deaths (thousands): {selected_pais}')
fig_nm_fil.update_traces(line_color='#ED80DD', line_width=3)

col39,col40 = st.columns(2)

with col39:
    st.plotly_chart(fig_nm,use_container_width=True )

with col40:
    st.plotly_chart(fig_nm_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------------
#Grafico 21

st.write (':blue[_RATE OF NATURAL CHANGE: Birth rate minus the death rate of a particular population, over a particular time period (per 1,000 population)_]')


df_gup = df.groupby(['Year'])['Rate of Natural Change (per 1,000 population)'].sum().reset_index()

fig_nm= px.line(df_gup, x=df_gup["Year"], y=df_gup['Rate of Natural Change (per 1,000 population)'], title='Rate of Natural Change (per 1,000 population)')
fig_nm.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Rate of Natural Change (per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_nm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Rate of Natural Change (per 1,000 population)'],  title=f'Rate of Natural Change (per 1,000 population): {selected_pais}')
fig_nm_fil.update_traces(line_color='#ED80DD', line_width=3)


col41,col42 = st.columns(2)

with col41:
    st.plotly_chart(fig_nm,use_container_width=True )

with col42:
    st.plotly_chart(fig_nm_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------------
#Grafico 22

st.write (':blue[_POPULATION GROWTH RATE: Exponential rate of growth of midyear population from year t-1 to t. (see “population total” definition)(Annual percentage)_]')


df_gup = df.groupby(['Year'])['Population Growth Rate (percentage)'].sum().reset_index()

fig_tp= px.line(df_gup, x=df_gup["Year"], y=df_gup['Population Growth Rate (percentage)'], title='Population Growth Rate (percentage)')
fig_tp.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Population Growth Rate (percentage)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Population Growth Rate (percentage)'],  title=f'Population Growth Rate (percentage): {selected_pais}')
fig_tp_fil.update_traces(line_color='#ED80DD', line_width=3)


col43,col44 = st.columns(2)

with col43:
    st.plotly_chart(fig_tp,use_container_width=True )

with col44:
    st.plotly_chart(fig_tp_fil,use_container_width=True )

#

