import streamlit as st
import pandas as pd
from PIL import Image
import pandas as pd 
import numpy as np
import plotly.express as px


image = Image.open('./Stream_finalisimo_kpi_last3/images/kpiIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write('Key performance indicators, commonly known as KPIs, are (as their name supposes) key performance indicators used to assess the success of actions and/or processes carried out in order  to obtain certain objectives.  In this way it is possible to determine if the actions taken gave the expected results or if instead it is necessary to make corrections in the approach. ')
st.write('The importance of KPIs lies in their key characteristic of allowing real-time measurement of the operation of business, marketing or sales strategies, providing valuable information for strategic decision making.')
st.write('KPIs also play an important communicative role as they inform managers, employees and investors about the evolution of the company with respect to the established objectives, so that everyone can work with a general vision and goal in common.')
st.write('From the in-depth exploration of different variables and data obtained during the project, the  analysts team proposes the formulation of the following KPIs described here. The importance of tracking their values is determinant for Policy Makers regarding Migrations')
st.write('The methodology used for determining the KPIs follows the concept of the recognized SMART objectives. The acronym stands for "Specific", "Measurable", "Attainable", "Relevant" and "Time-bound".')
         
st.markdown("-----------")

st.header(":violet[KPI 1]")
st.markdown('This KPI shows us Interpretation:. Percentage of incidence of the migratory flow over the total population of the chosen country.')
st.markdown('A value of 1.2 implies that the migratory flow contributed to increase the population by 1.2%.')

code = '''df['KPI_1'] = (df['Net Number of Migrants (thousands)']*1000)/(df['Population Total']/1000)'''
st.code(code, language='python')

st.markdown("-----------")

st.header(":violet[KPI 2]")
st.markdown('This KPI shows the variation in the net flow of migrants with respect to the flow of the previous year.')
st.markdown('Positive values imply that more people immigrated or that fewer emigrated.')
st.markdown('Negative values imply that more people emigrated or that less immigrated.')
st.markdown('Values of zero imply that there were no changes in the annual flow, i.e. Net Migration was the same as the past year.')

code = '''# Group the data by country
grouped = df.groupby('Country Name')

# Calculate the difference in 'Net Number of Migrants (thousands)' between consecutive years for each country
diff = grouped['Net Number of Migrants (thousands)'].diff()

# Add the difference as a new column to the original DataFrame
df['KPI_2'] = round(diff,2)

# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
df['KPI_2'].fillna(0, inplace=True)
'''

st.code(code, language='python')

st.markdown("-----------")

st.header(":violet[KPI 3]")

st.markdown('This KPI shows the porcentual variation in the net flow of migrants with respect to the flow of the previous year.')
st.markdown('Positive value of 20.36 implies that net migration has increased in a 20.36% annnualy.')

code = '''# Create a new column 'KPI 3'
df['KPI_3'] = round((np.sign(df['KPI_2']) * abs(df['KPI_2'] / df['Net Number of Migrants (thousands)'].shift()) * 100) , 2)
# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
df['KPI_3'].fillna(0, inplace=True)
'''

st.code(code, language='python')


st.markdown('The following KPIs take for their measurement some specific features, which arise as a result of the implementation of the ML models that can be seen in the "Study of Features with ML" section.')
st.markdown('For this development, we take the "m = 5" most important features because in this way the authorities and policy makers will know concisely which features to direct their actions to maximize the result on the objective variable.')
st.markdown('These KPIs are precisely adapted to the characteristics of each group, and their utility and functionality is maximized by following the guidelines below.')
st.markdown('KPI_4 will be more useful for countries that have similar characteristics to the countries of Group 1, which are characterized by having a large and positive Net Migration Flow.')
st.markdown('KPI_5 is most useful for group 5 countries, which have a negative influx of migrants.')
st.markdown('Later we will explain the method so that each country has a point estimate of which group it belongs to.')

st.markdown("-----------")

st.header(":violet[KPI 4]")
st.markdown('This index is a basket of the characteristics that we consider most relevant accoirding to our ML model to explain the reception of migrants in the countries and years that receive the largest amount of net migration.')
st.markdown('This KPI is the weighted average of the "m" indicators chosen. It provides an estimate of the measure of the attractiveness of the country to receive migrants. Higher levels of KPI_4 are related to greater positive migratory flows.')
st.markdown('According to our ML model, the top features for Group 1 are:')

st.markdown('[Exports of goods and services (PCT of GDP)')
st.markdown('Gross Domestic Product')
st.markdown('Refugee population by country or territory of asylum')
st.markdown('Refugee population by country or territory of origin')
st.markdown('Infant Mortality Rate (infant deaths per 1,000 live births)]')


code = '''# List of the selected features
SK_4 = ['Exports of goods and services (PCT of GDP)',
 'Gross Domestic Product',
 'Refugee population by country or territory of asylum',
 'Refugee population by country or territory of origin',
 'Infant Mortality Rate (infant deaths per 1,000 live births)']

# Standardize the columns
df[SK_4] = (df[SK_4] - df[SK_4].mean()) / df[SK_4].std()

# Assign a negative sign for the features with negative coefficient
df['Exports of goods and services (PCT of GDP)'] = -df['Exports of goods and services (PCT of GDP)']
df['Infant Mortality Rate (infant deaths per 1,000 live births)'] = -df['Infant Mortality Rate (infant deaths per 1,000 live births)']


# Create the KPI column
df['KPI_4'] = df[SK_4].sum(axis=1)/5
'''

st.code(code, language='python')

st.markdown('Beyond the usefulness of KPI_4, the performance and effectiveness of the policies implemented in a given country can also be measured by evaluating the variation of KPI_4 between two consecutive periods.')
st.markdown('In this way, VAR_KPI_4 shows us the percentage variation of KPI_4 between the period n and period n-1. Provides an effective estimate of the variation in the degree of desirability of the country to receive FM between the current period and the next.')
st.markdown('In practical terms, it is a quick and and easy to understand indicator that allows us to assess at a glance the degree of effectiveness of the implemented policies.')
st.markdown('Ex: VAR_KPI_4 = 0.12 implies that the objective to be achieved is that there is a percentage increase 12% per year of KPI_4 from one year to the next.')

code = '''df['VAR_KPI_4'] = round(df['KPI_4'].pct_change()*100,2)

# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
df['VAR_KPI_4'].fillna(0, inplace=True)
'''

st.code(code, language='python')

st.markdown("-----------")

st.header(":violet[KPI 5]")
st.markdown('The logic is similar to that of KPI_4, except that this basket measures the features that most explain migratory flows in country where net migration es negative.')
st.markdown('As before, an increasing KPI over time is desirable because it indicates that the adverse conditions are less and net migration is increasing (or has a less negative number).')
st.markdown('According to our ML model, the top features for Group 5 are:.')

st.markdown('[Imports of goods and services (PCT of GDP),')
st.markdown('Population Density,')
st.markdown('Refugee population by country or territory of asylum,')
st.markdown('Labour force, total,')
st.markdown('Infant Deaths, under age 1 (thousands)]')

code = '''# List of the selected features
SK_5 = ['Imports of goods and services (PCT of GDP)',
 'Population Density',
 'Refugee population by country or territory of asylum',
 'Labour force, total',
 'Infant Deaths, under age 1 (thousands)']

# Standardize the columns
df[SK_5] = (df[SK_5] - df[SK_5].mean()) / df[SK_5].std()

# Assign a negative sign for the features with negative coefficient
df['Imports of goods and services (PCT of GDP)'] = -df['Imports of goods and services (PCT of GDP)']

# Create the KPI column
df['KPI_5'] = -df[SK_5].sum(axis=1)/5
'''

st.code(code, language='python')

st.markdown('As we saw in the previous section, in this case we present VAR_KPI_5, which shows us the percentage variation of KPI_5 between the period n and period n-1.')
st.markdown('Example: VAR_KPI_5 = 0.08 implies that the objective to be achieved is that there is a percentage increase of 8% year-on-year of the KPI_5.')



code = '''df['VAR_KPI_5'] = round(df['KPI_5'].pct_change()*100,2)


# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
df['VAR_KPI_5'].fillna(0, inplace=True)
'''

st.code(code, language='python')


st.markdown("In this section you can see the historical records of all the KPIs for each country. In this way, the performance of migration policies can be evaluated throughout the period studied.")




df = pd.read_csv('./Stream_finalisimo_kpi_last3/Merged_Dataset_v03 (2).csv')

KPIs = df[['Country Name','Year','Group','KPI_1','KPI_2','KPI_3','KPI_4','VAR_KPI_4','KPI_5','VAR_KPI_5']]

KPIs['Year'] = df['Year'].astype(int)

# Crear lista de países para el selectbox
paises = KPIs['Country Name'].unique()

selected_pais = st.sidebar.selectbox("Select a country:", paises, key='country_selector7')


# Filtrar datos por país seleccionado
df_filtered = KPIs[KPIs['Country Name'] == selected_pais]


# Imprimir parte del dataframe filtrado
st.write(f"Showing some data from the selected country  ({selected_pais}):")


st.write(df_filtered.iloc[:22]) # Muestra las primeras 10 filas del dataframe filtrado


st.write(round(KPIs[KPIs['Country Name'] == f'{selected_pais}']['Group'].mean(),2))


valor = (round(KPIs[KPIs['Country Name'] == f'{selected_pais}']['Group'].mean(),2))
st.write(f' The selected country has a value in the Group column of {valor}  \
 on average.In order to assess its net migratory flow in the medium term, it is recommended to consider the KPIs and the specific characteristics of the Group closest to that value.')





import pandas as pd
import streamlit as st
import plotly.express as px



KPIs = df[[ 'KPI_1', 'KPI_2', 'KPI_3', 'KPI_4', 'VAR_KPI_4', 'KPI_5', 'VAR_KPI_5']]
selected_kpi = st.selectbox("Selecciona un KPI:", KPIs.columns,key='country_selector9')
selected_country = st.selectbox("Selecciona un país:", df['Country Name'].unique())

# Convertir el índice en un objeto datetime y extraer los años
KPIs.index = pd.to_datetime(KPIs.index)
KPIs['Year'] = KPIs.index.year

# Filtrar los datos para mostrar solo el KPI y el país seleccionados por el usuario
df_filtered = df[(df['Country Name'] == selected_country)][['Country Name', 'Year', selected_kpi]].groupby(['Country Name', 'Year']).mean().reset_index()

# Crear figura usando plotly
fig = px.line(df_filtered, x='Year', y=selected_kpi, title=f"{selected_kpi} en {selected_country}")

# Mostrar gráfico en Streamlit
st.plotly_chart(fig)








