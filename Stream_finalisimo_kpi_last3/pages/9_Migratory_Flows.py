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
import requests
import streamlit as st

# Load the data
filtered_df_can = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

# Create the Streamlit app
st.title('Flows between countries')

# Select base and target countries
base_country = st.selectbox('Select a base country', filtered_df_can['base_country_name'].unique(),key='country_selector27')
target_country = st.selectbox('Select a target country', filtered_df_can['target_country_name'].unique(),key='country_selector25')

# Filter the data based on the selected countries
filtered_df = filtered_df_can[(filtered_df_can['base_country_name'] == base_country) & (filtered_df_can['target_country_name'] == target_country)]

# Check if there is data for the selected countries
if filtered_df.empty:
    st.write("Por favor utilice los dos filtros")
else:
    # Create a list of colors for the lines based on the year
    colors = ['rgb(255, 0, 0)', 'rgb(255, 128, 0)', 'rgb(255, 255, 0)', 'rgb(0, 255, 0)', 'rgb(0, 0, 255)']

    # Create a list of line thicknesses for the lines based on the flow value
    sizes = [1, 2, 4, 8, 16]

    # Create a list of Scattergeo traces for each year of data
    traces = []
    for i, year in enumerate(filtered_df.columns[-5:]):
        # Check if there is data for the selected year
        if filtered_df[year].sum() == 0:
            continue
        trace = go.Scattergeo(
            lon=[filtered_df['base_long'].iloc[0], filtered_df['target_long'].iloc[0]],
            lat=[filtered_df['base_lat'].iloc[0], filtered_df['target_lat'].iloc[0]],
            mode='lines',
            line=dict(
                color=colors[i],
                width=sizes[i],
            ),
            name=year
        )
        traces.append(trace)

    # Create a layout for the map
    layout = go.Layout(
        title=f"{base_country} to {target_country} Flows",
        geo=dict(
            showcountries=True,
            showland=True,
            showocean=True,
            countrywidth=0.5,
            landcolor='rgb(230, 230, 230)',
            oceancolor='rgb(0, 204, 204)',
            projection_type='orthographic'
        ),
        legend=dict(
            x=0,
            y=1.2,
            orientation='h'
        )
    )

    # Create a figure for the map
    fig = go.Figure(data=traces, layout=layout)

    # Show the map in Streamlit
    st.plotly_chart(fig)



df = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

dest_country = st.selectbox('Selecciona el país de destino:', df['target_country_name'].unique())

dest_df = df.loc[df['target_country_name'] == dest_country]

fig, ax = plt.subplots()
dest_df.sort_values(by='2019', ascending=False).head(5).set_index('base_country_name')['2019'].plot(kind='barh', ax=ax)

ax.set_xlabel('Número de inmigrantes')
ax.set_ylabel('País de origen')
plt.title(f'Top 5 países de origen con más inmigrantes a {dest_country.upper()}')

fig.canvas.draw()  # Dibuja la figura antes de mostrarla

st.pyplot(fig)




# Lectura de datos
df = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

# Lista de años de interés
years = list(map(str, range(2015, 2020)))

# Selección del país de destino
dest_country = st.selectbox('Selecciona el país de destino:', df['target_country_name'].unique(), key='country251')

# Selección de los datos correspondientes al país de destino
dest_df = df.loc[df['target_country_name'] == dest_country]

if dest_df.empty:
    st.warning(f"No se encontraron datos para {dest_country}")
else:
    # Selección de los 5 países con más inmigrantes en 2019
    top5 = dest_df.loc[:, ['base_country_name', '2015', '2016', '2017', '2018', '2019']].sort_values(by='2019', ascending=False).head(5)

    top5.set_index('base_country_name', inplace=True)

    # Crear el gráfico de área
    top5.index = top5.index.map(str)
    top5.index.name = 'Country'
    top5.columns = top5.columns.map(int)
    top5.plot(kind='area', stacked=False, figsize=(20, 10))
    fig, ax = plt.subplots()
    top5.plot(kind='area', stacked=False, figsize=(20, 10), ax=ax)

    ax.set_title(f'Immigration Trend of Top 5 Countries to {dest_country}')
    ax.set_ylabel('Number of Immigrants')
    ax.set_xlabel('Years')

    st.pyplot(fig)



# Lectura de datos
df = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

# Lista de años de interés
years = list(map(str, range(2015, 2020)))

# Selección del país de destino
dest_country = st.selectbox('Selecciona el país de destino:', df['target_country_name'].unique(), key='country2')

# Selección de los datos correspondientes al país de destino
dest_df = df.loc[df['target_country_name'] == dest_country]

if dest_df.empty:
    st.warning(f"No se encontraron datos para {dest_country}")
else:
    # Selección de los 5 países con más inmigrantes en 2019
    top5 = dest_df.loc[:, ['base_country_name', '2015', '2016', '2017', '2018', '2019']].sort_values(by='2019', ascending=False).head(5)

    top5.set_index('base_country_name', inplace=True)

    # Crear el gráfico de área
    fig, ax = plt.subplots(figsize=(20, 10))

    for country in top5.index:
        ax.plot(top5.columns, top5.loc[country], alpha=0.35, label=country)

    ax.set_title(f'Immigration Trend of Top 5 Countries to {dest_country}')
    ax.set_ylabel('Number of Immigrants')
    ax.set_xlabel('Years')
    ax.legend()

    st.pyplot(fig)


#----------------------------------------------------------------------------------------------
#OPCION1

# Lectura de datos
df = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

# Lista de años de interés
years = list(map(str, range(2015, 2020)))

# Selección del país de destino
dest_country = st.selectbox('Selecciona el país de destino:', df['target_country_name'].unique(), key='country12')

# Selección de los datos correspondientes al país de destino
dest_df = df.loc[df['target_country_name'] == dest_country]

if dest_df.empty:
    st.warning(f"No se encontraron datos para {dest_country}")
else:
    # Selección de los 5 países con más inmigrantes en 2019
    top5 = dest_df.loc[:, ['base_country_name', '2015', '2016', '2017', '2018', '2019']].sort_values(by='2019', ascending=False).head(5)

    top5.set_index('base_country_name', inplace=True)

    # Crear el gráfico de área
fig, ax = plt.subplots(figsize=(20, 10))

bottom = np.zeros(len(years))
for country in top5.index:
    ax.bar(years, top5.loc[country], bottom=bottom, label=country)
    bottom += top5.loc[country]

    ax.set_title(f'Immigration Trend of Top 5 Countries to {dest_country}')
    ax.set_ylabel('Number of Immigrants')
    ax.set_xlabel('Years')
    ax.legend()

    st.pyplot(fig)


 
#----------------------------------------------------------------------------------------------
#OPCION2 

# Lectura de datos
df = pd.read_csv("./Stream_finalisimo_kpi_last3/df_can.csv", header=0)

# Lista de años de interés
years = list(map(str, range(2015, 2020)))

# Selección del país de destino
dest_country = st.selectbox('Selecciona el país de destino:', df['target_country_name'].unique(), key='country122')

# Selección de los datos correspondientes al país de destino
dest_df = df.loc[df['target_country_name'] == dest_country]

if dest_df.empty:
    st.warning(f"No se encontraron datos para {dest_country}")
else:
    # Selección de los 5 países con más inmigrantes en 2019
    top5 = dest_df.loc[:, ['base_country_name', '2015', '2016', '2017', '2018', '2019']].sort_values(by='2019', ascending=False).head(5)

    top5.set_index('base_country_name', inplace=True)

    # Crear el gráfico de área
fig, ax = plt.subplots(figsize=(20, 10))

width = 0.15
x = np.arange(len(years))

for i, country in enumerate(top5.index):
    ax.bar(x + i*width, top5.loc[country], width, label=country)

ax.set_title(f'Immigration Trend of Top 5 Countries to {dest_country}')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')
ax.set_xticks(x + width*(len(top5.index)-1)/2)
ax.set_xticklabels(years)
ax.legend()

st.pyplot(fig)
