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
    page_title='Health Indicators',
    layout='wide'
)

image = Image.open('./Stream_finalisimo_kpi_last3/images/saludIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.write(":violet[IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTANT VARIABLES ON THIS CATEGORY OR INDICATORS.]")

st.markdown("-----------")



df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")
#------------------------------------------------
# ACA ARRANCA Indicadores de Salud

#Grafico 22

st.write(":blue[_CRUDE BIRTH RATE : Number of live births occurring during the year (births per 1,000 population)._]")


df_gup = df.groupby(['Year'])[ 'Crude Birth Rate (births per 1,000 population)'].sum().reset_index()

fig_tn = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Crude Birth Rate (births per 1,000 population)'], title='Crude Birth Rate (births per 1,000 population)')
fig_tn.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Crude Birth Rate (births per 1,000 population)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()
selected_pais = st.sidebar.selectbox("Select a country:", paises, key='country_selector7')
# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tn_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Crude Birth Rate (births per 1,000 population)'],  title=f'Crude Birth Rate (births per 1,000 population): {selected_pais}')
fig_tn_fil.update_traces(line_color='#ED80DD', line_width=3)



col45,col46 = st.columns(2)

with col45:
    st.plotly_chart(fig_tn,use_container_width=True )

with col46:
    st.plotly_chart(fig_tn_fil,use_container_width=True )

st.markdown("-----------")
#------------------------------------------------

st.write(":blue[_MEDIAN AGE , as of 1 July Age that divides the population in two parts of equal size, that is, there are as many persons with ages above the median as there are with ages below the median. (years)_]")

#Grafico 23

df_gup = df.groupby(['Year'])[ 'Median Age, as of 1 July (years)' ].sum().reset_index()

fig_em = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Median Age, as of 1 July (years)'], title='Median Age, as of 1 July (years)')
fig_em.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Median Age, as of 1 July (years)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_em_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Median Age, as of 1 July (years)'],  title=f'Median Age, as of 1 July (years): {selected_pais}')
fig_em_fil.update_traces(line_color='#ED80DD', line_width=3)



col45,col46 = st.columns(2)

with col45:
    st.plotly_chart(fig_em,use_container_width=True )

with col46:
    st.plotly_chart(fig_em_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------------

st.write(":blue[ _LIFE EXPECTANCY AT BIRTH , BOTH SEXES: Number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life (years)_]")

#Grafico 24

df_gup = df.groupby(['Year'])[ 'Life Expectancy at Birth, both sexes (years)'].sum().reset_index()

fig_es = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Life Expectancy at Birth, both sexes (years)'], title='Life Expectancy at Birth, both sexes (years)')
fig_es.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Life Expectancy at Birth, both sexes (years)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_es_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Life Expectancy at Birth, both sexes (years)'],  title=f'Life Expectancy at Birth, both sexes (years): {selected_pais}')
fig_es_fil.update_traces(line_color='#ED80DD', line_width=3)



col47,col48 = st.columns(2)

with col47:
    st.plotly_chart(fig_es,use_container_width=True )

with col48:
    st.plotly_chart(fig_es_fil,use_container_width=True )
    
st.markdown("-----------")    
#------------------------------------------------

st.write(":blue[_INFANT MORTALITY RATE: Number of infant deaths for every 1,000 live births. (infant deaths per 1,000 live births)_]")

#Grafico 25

df_gup = df.groupby(['Year'])['Infant Mortality Rate (infant deaths per 1,000 live births)'].sum().reset_index()

fig_im = px.line(df_gup, x=df_gup["Year"], y=df_gup['Infant Mortality Rate (infant deaths per 1,000 live births)'], title='Infant Mortality Rate (infant deaths per 1,000 live births)')
fig_im.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Infant Mortality Rate (infant deaths per 1,000 live births)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_im_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Infant Mortality Rate (infant deaths per 1,000 live births)'],  title=f'Infant Mortality Rate (infant deaths per 1,000 live births): {selected_pais}')
fig_im_fil.update_traces(line_color='#ED80DD', line_width=3)



col49,col50 = st.columns(2)

with col49:
    st.plotly_chart(fig_im,use_container_width=True )

with col50:
    st.plotly_chart(fig_im_fil,use_container_width=True )
    
st.markdown("-----------")    

#------------------------------------------------

st.write(":blue[_INFANT DEATHS UNDER AGE 1: Death of an infant before his or her first birthday. (thousands)_]")

#Grafico 26

df_gup = df.groupby(['Year'])['Infant Deaths, under age 1 (thousands)'].sum().reset_index()

fig_id = px.line(df_gup, x=df_gup["Year"], y=df_gup['Infant Deaths, under age 1 (thousands)'], title='Infant Deaths, under age 1 (thousands)')
fig_id.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Infant Deaths, under age 1 (thousands)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_id_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Infant Deaths, under age 1 (thousands)'],  title=f'Infant Deaths, under age 1 (thousands): {selected_pais}')
fig_id_fil.update_traces(line_color='#ED80DD', line_width=3)



col51,col52 = st.columns(2)

with col51:
    st.plotly_chart(fig_id,use_container_width=True )

with col52:
    st.plotly_chart(fig_id_fil,use_container_width=True )
    
st.markdown("-----------")    

#------------------------------------------------

st.write(":blue[_MATERNAL MORTALITY RATIO: Number of women who die from pregnancy-related causes while pregnant or within 42 days of pregnancy termination. The data are estimated with a regression model using information on the proportion of maternal deaths among non-AIDS deaths in women ages 15-49, fertility, birth attendants, and GDP.(per 100,000 live births.)_]")

#Grafico 27

df_gup = df.groupby(['Year'])['Maternal Mortality'].sum().reset_index()

fig_mm = px.line(df_gup, x=df_gup["Year"], y=df_gup['Maternal Mortality'], title='Maternal Mortality')
fig_mm.update_traces(line_color='#728C9F', line_width=3)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Maternal Mortality'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_mm_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Maternal Mortality'],  title=f'Maternal Mortality: {selected_pais}')
fig_mm_fil.update_traces(line_color='#ED80DD', line_width=3)



col53,col54 = st.columns(2)

with col53:
    st.plotly_chart(fig_mm,use_container_width=True )

with col54:
    st.plotly_chart(fig_mm_fil,use_container_width=True )
