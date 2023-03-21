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
    page_title='Macro Indicators',
    layout='wide'
)


#GRAFICO 4 ---------------------------

image = Image.open('./Stream_finalisimo_kpi_last3/images/macroIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTANT VARIABLES ON THIS CATEGORY OF INDICATORS.]")

st.markdown("-----------")




# Gráfico de barras FIJO

st.write(":blue[_GROSS DOMESTIC PRODUCT (GDP): Total gross value added by all resident producers in the economy of each country in U$D.(U$D)_]")

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

df_gup = df.groupby(['Year'])["Gross Domestic Product"].sum().reset_index()

fig_15123 = px.line(df_gup, x=df_gup["Year"], y=df_gup["Gross Domestic Product"], title="Gross Domestic Product por año")
fig_15123.update_traces(line_color='#728C9F', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_15123)

#------------------------------------------------

# Gráfico de barras FILTRADO TEST

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

# Agrupar por año y país
df_gup = df.groupby(['Year', 'Country Name'])["Gross Domestic Product"].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
selected_pais = st.sidebar.selectbox("Select a country:", paises, key='country_selector')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_gross = px.line(df_filtered, x='Year', y='Gross Domestic Product',  title=f'Gross Domestic Product for year: {selected_pais}')
fig_gross.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig)

col7,col8 = st.columns(2)

with col7:
    st.plotly_chart(fig_15123,use_container_width=True )

with col8:
    st.plotly_chart(fig_gross,use_container_width=True )
st.markdown("-----------")

#------------------------------------------

st.write(":blue[_GDP GROWTH: Annual percentage growth rate of GDP.(annualy %)_]")

#Grafico 5

#SI DEJO ESTE FUNCIONA BIEN VOY A SACAR LOS DE ARRIBA

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

df_gup = df.groupby(['Year'])['GDP Growth'].sum().reset_index()

fig_gdp = px.line(df_gup, x=df_gup["Year"], y=df_gup["GDP Growth"], title="GDP Growth")
fig_gdp.update_traces(line_color='#728C9F', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_gdp)

#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['GDP Growth'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_gdp_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['GDP Growth'],  title=f'GDP Growth: {selected_pais}')
fig_gdp_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_gdp_fil)


col9,col10 = st.columns(2)

with col9:
    st.plotly_chart(fig_gdp,use_container_width=True )

with col10:
    st.plotly_chart(fig_gdp_fil,use_container_width=True )

st.markdown("-----------")

#------------------------------------------

st.write(":blue[_TOTAL RESERVES:  Comprise holdings of monetary gold, special drawing rights, reserves of IMF members held by the IMF, and holdings of foreign exchange under the control of monetary authorities.(gold + US$)_]")

#Grafico 6

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

df_gup = df.groupby(['Year'])['Total reserves (gold + US$)'].sum().reset_index()

fig_total = px.line(df_gup, x=df_gup["Year"], y=df_gup['Total reserves (gold + US$)'], title="Total reserves (gold + US$)")
fig_total.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_total)

#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['Total reserves (gold + US$)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector1')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_total_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Total reserves (gold + US$)'],  title=f'Total reserves (gold + US$) del pais: {selected_pais}')
fig_total_fil.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_total_fil)


col11,col12 = st.columns(2)

with col11:
    st.plotly_chart(fig_total,use_container_width=True )

with col12:
    st.plotly_chart(fig_total_fil,use_container_width=True )
st.markdown("-----------")

#------------------------------------------
st.write(":blue[_UNEMPLOYMENT,TOTAL: Share of the labor force that is without work but available for and seeking employment.(% of total labor force)_]")

#Grafico 7


df_gup = df.groupby(['Year'])['Unemployment'].sum().reset_index()

fig_desempleo = px.line(df_gup, x=df_gup["Year"], y=df_gup['Unemployment'], title="Unemployment")
fig_desempleo.update_traces(line_color='#728C9F', line_width=3)
#------------------------------------------------

# Gráfico de barras FILTRADO

df_gup = df.groupby(['Year','Country Name'])['Unemployment'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector2')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_desempleo_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Unemployment'],  title=f'Unemployment: {selected_pais}')
fig_desempleo_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_desempleo_fil)


col13,col14 = st.columns(2)

with col13:
    st.plotly_chart(fig_desempleo,use_container_width=True )

with col14:
    st.plotly_chart(fig_desempleo_fil,use_container_width=True )
st.markdown("-----------")

#------------------------------------------

st.write(":blue[_EXPORTS OF GOODS AND SERVICES: Value of all goods and other market services provided to the rest of the world. (Exclude: compensation of employees and investment income and transfer payments)_]")

#Grafico 8

df_gup = df.groupby(['Year'])['Exports of goods and services (PCT of GDP)'].sum().reset_index()

fig_expor = px.line(df_gup, x=df_gup["Year"], y=df_gup['Exports of goods and services (PCT of GDP)'], title="Exports of goods and services (PCT of GDP)")
fig_expor.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Exports of goods and services (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector3')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_expor_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Exports of goods and services (PCT of GDP)'],  title=f'Exports of goods and services (PCT of GDP): {selected_pais}')
fig_expor_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col15,col16 = st.columns(2)

with col15:
    st.plotly_chart(fig_expor,use_container_width=True )

with col16:
    st.plotly_chart(fig_expor_fil,use_container_width=True )


st.markdown("-----------")

#------------------------------------------
st.write(":blue[_IMPORTS OF GOODS AND SERVICES: Value of all goods and other market services provided from the rest of the world. (Exclude: compensation of employees and investment income and transfer payments)_]")

#Grafico 9

df_gup = df.groupby(['Year'])['Imports of goods and services (PCT of GDP)'].sum().reset_index()

fig_impor = px.line(df_gup, x=df_gup["Year"], y=df_gup['Imports of goods and services (PCT of GDP)'], title="Imports of goods and services (PCT of GDP)")
fig_impor.update_traces(line_color='#728C9F', line_width=3)

#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Imports of goods and services (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector4')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_impor_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Imports of goods and services (PCT of GDP)'],  title=f'Imports of goods and services (PCT of GDP): {selected_pais}')
fig_impor_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col17,col18 = st.columns(2)

with col17:
    st.plotly_chart(fig_impor,use_container_width=True )

with col18:
    st.plotly_chart(fig_impor_fil,use_container_width=True )
