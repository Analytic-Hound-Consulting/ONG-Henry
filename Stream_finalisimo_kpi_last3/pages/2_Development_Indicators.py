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

#------------------------------------------

st.set_page_config(
    page_title='Development Indicators',
    layout='wide'
)


image = Image.open('./Stream_finalisimo_kpi_last3/images/desarrolloIng.jpg')
st.image(image, caption=None, width=750 , use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write(":violet[IN THIS SECTION YOU CAN CONSULT THE MOST IMPORTANT VARIABLES ON THIS CATEGORY OF INDICATORS.]")

st.markdown("-----------")


df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")


#Grafico 13

st.write(":blue[_GOVERMENT EXPENDITURE ON EDUCATION: General government expenditure on education expressed as a percentage of GDP. total (% of GDP)_]")

df_gup = df.groupby(['Year'])['Expenditure Education'].sum().reset_index()

fig_edu = px.line(df_gup, x=df_gup["Year"], y=df_gup['Expenditure Education'] , title="Expenditure Education ")
fig_edu.update_traces(line_color='#728C9F', line_width=3)

#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Expenditure Education'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
selected_pais = st.sidebar.selectbox("Select a country:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_edu_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Expenditure Education'],  title=f'Expenditure Education: {selected_pais}')
fig_edu_fil.update_traces(line_color='#ED80DD', line_width=3)

# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col27,col28 = st.columns(2)

with col27:
    st.plotly_chart(fig_edu, use_container_width=True )

with col28:
    st.plotly_chart(fig_edu_fil, use_container_width=True )

st.markdown("-----------")

#------------------------------------------

#Grafico 14

st.write(":blue[_INTENTIONAL HOMICIDES: Unlawful homicides purposely inflicted as a result of domestic disputes, interpersonal violence, violet conflicts over land resources, intergang violence over turf or control, and predatory violence and killing by armed groups.(per 100,000 people)_]")

df_gup = df.groupby(['Year'])['Intentional homicides (per 100,000 people)'].sum().reset_index()

fig_hom= px.line(df_gup, x=df_gup["Year"], y=df_gup['Intentional homicides (per 100,000 people)'], title="Intentional homicides (per 100,000 people) ")
fig_hom.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Intentional homicides (per 100,000 people)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_hom_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Intentional homicides (per 100,000 people)'],  title=f'Intentional homicides (per 100,000 people): {selected_pais}')
fig_hom_fil.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col27,col28 = st.columns(2)

with col27:
    st.plotly_chart(fig_hom,use_container_width=True )

with col28:
    st.plotly_chart(fig_hom_fil,use_container_width=True )

st.markdown("-----------")

#------------------------------------------



#Grafico 15

st.write(":blue[_PRIMARY COMPLETION RATE, TOTAL: Number of new entrants (enrollments minus repeaters) in the last grade of primary education, regardless of age, divided by the population at the entrance age for the las grade of primary education.(PCT of relevant age group)_]")

df_gup = df.groupby(['Year'])['Primary completion rate, total (PCT of relevant age group)'].sum().reset_index()

fig_edupf = px.line(df_gup, x=df_gup["Year"], y=df_gup['Primary completion rate, total (PCT of relevant age group)'], title="Primary completion rate, total (PCT of relevant age group) ")
fig_edupf.update_traces(line_color='#728C9F', line_width=3)
#st.plotly_chart(fig_expor)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Primary completion rate, total (PCT of relevant age group)'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_edupf_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Primary completion rate, total (PCT of relevant age group)'],  title=f'Primary completion rate, total (PCT of relevant age group): {selected_pais}')
fig_edupf_fil.update_traces(line_color='#ED80DD', line_width=3)
# Mostrar gráfico en Streamlit
#st.plotly_chart(fig_expor_fil)


col29,col30 = st.columns(2)

with col29:
    st.plotly_chart(fig_edupf,use_container_width=True )

with col30:
    st.plotly_chart(fig_edupf_fil,use_container_width=True )
    
st.markdown("-----------")    

df = pd.read_csv("./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv")

#Grafico 16

st.write(":blue[_ACCESS TO ELECTRICITY: Percentage of population with access to electricity. Electrificacion data is collected from industry, national surveys, and international sources.(% of population)_]")

df_gup = df.groupby(['Year'])[ 'Access Elect.'].sum().reset_index()

fig_acc = px.line(df_gup, x=df_gup["Year"], y=df_gup[ 'Access Elect.'], title="Access to electricity")
fig_acc.update_traces(line_color='#728C9F', line_width=3)

#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Access Elect.'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Añadir selectbox para filtrar por país
#selected_pais = st.sidebar.selectbox("Selecciona un país:", paises, key='country_selector7')

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_acc_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Access Elect.'],  title=f'Access to electricity: {selected_pais}')
fig_acc_fil.update_traces(line_color='#ED80DD', line_width=3)

col31,col32 = st.columns(2)

with col31:
    st.plotly_chart(fig_acc, use_container_width=True )

with col32:
    st.plotly_chart(fig_acc_fil, use_container_width=True )     
                     
st.markdown("-----------")

#------------------------------------------------

#Grafico 17

st.write(":blue[_PEPOPLE USING AT LEAST BASIC SANITATION SERVICES IN URBAN AREAS: Improved sanitation facilities that are not shared with other households. This indicator encompasses both people using basic sanitation services as well as those using safely managed sanitation services._]")

df_gup = df.groupby(['Year'])['Basic Sanitation'].sum().reset_index()

fig_sa = px.line(df_gup, x=df_gup["Year"], y=df_gup['Basic Sanitation'], title="basic sanitation services")
fig_sa.update_traces(line_color='#728C9F', line_width=3)


#------------------------------------------------

# Gráfico de barras FILTRADO


df_gup = df.groupby(['Year','Country Name'])['Basic Sanitation'].sum().reset_index()

# Crear lista de países para el selectbox
paises = df['Country Name'].unique()

# Filtrar datos por país seleccionado
df_filtered = df_gup[df_gup['Country Name'] == selected_pais]

# Crear gráfico de barras
fig_sa_fil = px.line(df_filtered, x=df_filtered['Year'], y=df_filtered['Basic Sanitation'],  title=f'basic sanitation services: {selected_pais}')
fig_sa_fil.update_traces(line_color='#ED80DD', line_width=3)

col33,col34 = st.columns(2)

with col33:
    st.plotly_chart(fig_sa, use_container_width=True )

with col34:
    st.plotly_chart(fig_sa_fil, use_container_width=True )


#------------------------------------------------




















