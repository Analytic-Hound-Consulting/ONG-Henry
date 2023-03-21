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
    page_title='Micro Indicators',
    layout='wide'
)


image = Image.open('./Stream_finalisimo_kpi_last3/images/microIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[ IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTANT VARIABLES ON THIS CATEGORY OF INDICATORS]")

st.markdown("-----------")

st.write(":blue[_FOREIGN DIRECT INVESTEMENT, NET INFLOWS: Net inflows of investment to acquire a lasting management interest (10% or more of voting stock) in an enterprise operating in an economy other than that of the investor. It is the sum of equity capital, reinvestment of earnings, other long-term capital, and short-term capital as shown in the balance of payments. This series shows net inflows (new investment inflows less disinvestment) in the reporting economy from foreign investors, and is divided by GDP (PCT of GDP)_]")

#Grafico 10 INICIO indicadores MICRO

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

df_gup = df.groupby(['Year'])['Foreign direct investment, net inflows (BoP, current US$)'].sum().reset_index()

fig_inver = px.line(df_gup, x=df_gup["Year"], y=df_gup['Foreign direct investment, net inflows (BoP, current US$)'], title="Foreign direct investment, net inflows (BoP, current US$)")
fig_inver.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Foreign direct investment, net inflows (BoP, current US$)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
selected_pais = st.sidebar.selectbox("Select a country :", paises, key='country_selector5')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_inver_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Foreign direct investment, net inflows (BoP, current US$)'],  title=f'Foreign direct investment, net inflows (BoP, current US$): {selected_pais}')
fig_inver_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col19,col20 = st.columns(2)

with col19:
    st.plotly_chart(fig_inver,use_container_width=True )

with col20:
    st.plotly_chart(fig_inver_fil,use_container_width=True )
st.markdown("-----------")

#------------------------------------------

st.write(":blue[_TOTAL TAX AND CONTRIBUTION RATE: Amount of taxes and mandatory contributions and exemptions as a share of commercial profits. Taxes withheld (such as personal income tax)  or collected and remitted to tax authorities (such as value added taxes, sales taxes or goods and service taxes) are excluded (PCT of profit)_]")


#Grafico 11 


df_gup = df.groupby(['Year'])['Total tax and contribution rate (PCT of profit)'].sum().reset_index()

fig_tax = px.line(df_gup, x=df_gup["Year"], y=df_gup['Total tax and contribution rate (PCT of profit)'], title="Total tax and contribution rate (PCT of profit)")
fig_tax.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Total tax and contribution rate (PCT of profit)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector6')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tax_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Total tax and contribution rate (PCT of profit)'],  title=f'Total tax and contribution rate (PCT of profit): {selected_pais}')
fig_tax_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col21,col22 = st.columns(2)

with col21:
    st.plotly_chart(fig_tax,use_container_width=True )

with col22:
    st.plotly_chart(fig_tax_fil,use_container_width=True )
st.markdown("-----------")
#------------------------------------------

st.write(":blue[_TIME REQUIRED TO START A BUSINESS: Number of calendar days needed to complete the procedures to legally operate a business (if a procedure can be speeded up at additional cost, the fastest procedure is chosen) (days)_]")

#Grafico 12


df_gup = df.groupby(['Year'])[ 'Time required to start a business (days)'].sum().reset_index()

fig_tax = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Time required to start a business (days)'], title="Time required to start a business (days)")
fig_tax.update_traces(line_color='#728C9F', line_width=3)

#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Time required to start a business (days)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_tax_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Time required to start a business (days)'],  title=f'Time required to start a business (days): {selected_pais}')
fig_tax_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col23,col24 = st.columns(2)

with col23:
    st.plotly_chart(fig_tax,use_container_width=True )

with col24:
    st.plotly_chart(fig_tax_fil,use_container_width=True )

st.markdown("-----------")
#------------------------------------------

st.write(":blue[_RESERACH AND DEVELOPMENT EXPENDITURE: Gloss domestic expenditure on research and development. Include capital and current expenditure in 4 main sectors: business enterprise, government, higher education and private non-profit. Covers basic research, applied research, and experimental development(PCT of GDP)_]")

#Grafico 12


df_gup = df.groupby(['Year'])['Research and development expenditure (PCT of GDP)'].sum().reset_index()

fig_desa = px.line(df_gup, x=df_gup["Year"], y=df_gup['Research and development expenditure (PCT of GDP)'], title="Research and development expenditure (PCT of GDP)")
fig_desa.update_traces(line_color='#728C9F', line_width=3)


#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])[ 'Research and development expenditure (PCT of GDP)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_desa_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered[ 'Research and development expenditure (PCT of GDP)'],  title=f'Research and development expenditure (PCT of GDP: {selected_pais}')
fig_desa_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col25,col26 = st.columns(2)

with col25:
    st.plotly_chart(fig_desa,use_container_width=True )

with col26:
    st.plotly_chart(fig_desa_fil,use_container_width=True )

#------------------------------------------



