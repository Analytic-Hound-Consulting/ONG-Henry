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
    page_title='Migration Indicators',
    layout='wide'
)


image = Image.open('./Stream_finalisimo_kpi_last3/images/migrantesIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTAN VARIABLES ON THIS CATEGORY OF INDICATORS.]")

st.markdown("-----------")

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")
#------------------------------------------------
#ACA ARRANCA Indicadores sobre Migración
#Grafico 27

st.write(":blue[_NET NUMBER OF MIGRANTS: Net total of migrants during the period, that is, the number of immigrants minus the number of emigrants, including both citizens and noncitizens.(thousands)_]")

df_gup = df.groupby(['Year'])['Net Number of Migrants (thousands)'].sum().reset_index()

fig_ntm = px.line(df_gup, x=df_gup["Year"], y=df_gup['Net Number of Migrants (thousands)'], title='Net Number of Migrants (thousands)')
fig_ntm.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Net Number of Migrants (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

selected_pais = st.sidebar.selectbox("Select a country :", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_ntm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Net Number of Migrants (thousands)'],  title=f'Net Number of Migrants (thousands): {selected_pais}')
fig_ntm_fil.update_traces(line_color='#ED80DD', line_width=3)

col55,col56 = st.columns(2)

with col55:
    st.plotly_chart(fig_ntm,use_container_width=True )

with col56:
    st.plotly_chart(fig_ntm_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------------

st.write(":blue[_NET MIGRATION RATE: Difference between the number of immigrants and the number of emigrants (people leaving an area) throughout the year (per 1,000 population)_]")

#Grafico 28

df_gup = df.groupby(['Year'])['Net Migration Rate (per 1,000 population)'].sum().reset_index()

fig_ntmh = px.line(df_gup, x=df_gup["Year"], y=df_gup['Net Migration Rate (per 1,000 population)'], title='Net Migration Rate (per 1,000 population)')
fig_ntmh.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Net Migration Rate (per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_ntmh_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Net Migration Rate (per 1,000 population)'],  title=f'Net Migration Rate (per 1,000 population): {selected_pais}')
fig_ntmh_fil.update_traces(line_color='#ED80DD', line_width=3)

col57,col58 = st.columns(2)

with col57:
    st.plotly_chart(fig_ntmh,use_container_width=True )

with col58:
    st.plotly_chart(fig_ntmh_fil,use_container_width=True )
    
st.markdown("-----------")    
#------------------------------------------------

st.write(":blue[ REFUGEE POPULATION BY COUNTRY OR TERRITORY OF ORIGIN: Country of origin generally refers to the nationality or country of citizenship of a claimant.]")

#Grafico 29

df_gup = df.groupby(['Year'])['Refugee population by country or territory of origin'].sum().reset_index()

fig_rp = px.line(df_gup, x=df_gup["Year"], y=df_gup['Refugee population by country or territory of origin'], title='Refugee population by country or territory of origin')
fig_rp.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Refugee population by country or territory of origin'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_rp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Refugee population by country or territory of origin'],  title=f'Refugee population by country or territory of origin: {selected_pais}')
fig_rp_fil.update_traces(line_color='#ED80DD', line_width=3)

col59,col60 = st.columns(2)

with col59:
    st.plotly_chart(fig_rp,use_container_width=True )

with col60:
    st.plotly_chart(fig_rp_fil,use_container_width=True )


st.markdown("-----------")
    


#------------------------------------------------


st.write(":blue[REFUGEE POPULATION BY COUNTRY OR TERRITORY OF ASYLUM: Country of asylum is the country where an asylum claim was filled and granted.]")


#Grafico 30

df_gup = df.groupby(['Year'])['Refugee population by country or territory of asylum'].sum().reset_index()

fig_rpp= px.line(df_gup, x=df_gup["Year"], y=df_gup['Refugee population by country or territory of asylum'], title='Refugee population by country or territory of asylum')
fig_rpp.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------


# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Refugee population by country or territory of asylum'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_rpp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Refugee population by country or territory of asylum'],  title=f'Refugee population by country or territory of asylum: {selected_pais}')
fig_rpp_fil.update_traces(line_color='#ED80DD', line_width=3)

col61,col62 = st.columns(2)

with col61:
    st.plotly_chart(fig_rpp,use_container_width=True )

with col62:
    st.plotly_chart(fig_rpp_fil,use_container_width=True )
