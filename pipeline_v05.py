#Libraries to work on the databases:
from pandas_datareader import wb
import wbgapi as wb
import datetime
import datapackage 

#Libraries to work on the pipeline:
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

#---------------------------------------------------------------------------#

today = datetime.date.today()
year = today.year

#---------------------------------------------------------------------------#

'''Loading datasets'''


'''---------------Economy---------------'''

economy_worldbank_series = ['NY.GDP.MKTP.CD', 'NY.GDP.MKTP.KD.ZG', 'NE.CON.TOTL.KD.ZG', 'NY.GNP.PCAP.CD', 'NY.GNS.ICTR.ZS', 'FP.CPI.TOTL', 
                            'FI.RES.TOTL.CD', 'BX.KLT.DINV.CD.WD', 'IC.TAX.TOTL.CP.ZS', 'IC.REG.DURS', 'NE.EXP.GNFS.ZS', 'NE.IMP.GNFS.ZS']
                                # We indicate which data from the economy series we want.
eco_complete = wb.data.DataFrame((economy_worldbank_series), labels = True, time=range(2000, year), skipBlanks=True, columns='series').reset_index()
                                # We indicate the range of years we want and various details to have a clean database.
eco_complete.rename(columns={'NY.GDP.MKTP.CD': 'Gross Domestic Product', 
                             'NY.GDP.MKTP.KD.ZG': 'GDP Growth', 
                             'NE.CON.TOTL.KD.ZG': 'Final Consumption Expenditure',
                             'NY.GNP.PCAP.CD': 'GNI Per Capita', 
                             'NY.GNS.ICTR.ZS': 'Gross Savings', 
                             'FP.CPI.TOTL': 'Consumer Price', 
                             'FI.RES.TOTL.CD' : 'Total reserves (gold + US$)', 
                             'BX.KLT.DINV.CD.WD' : 'Foreign direct investment, net inflows (BoP, current US$)', 
                             'IC.TAX.TOTL.CP.ZS' : 'Total tax and contribution rate (PCT of profit)', 
                             'IC.REG.DURS' : 'Time required to start a business (days)', 
                             'NE.EXP.GNFS.ZS' : 'Exports of goods and services (PCT of GDP)', 
                             'NE.IMP.GNFS.ZS' : 'Imports of goods and services (PCT of GDP)'}, inplace=True)
                                # In this stage, we can rename the columns with what those values represent.


'''---------------People---------------'''

people_worldbank_series = ['SE.XPD.TOTL.GD.ZS', 'SL.UEM.TOTL.ZS', 'SE.PRM.CMPT.ZS', 'VC.IHR.PSRC.P5', 'VC.IHR.PSRC.P5']
                                # We indicate which data from the people series we want.
peo_complete = wb.data.DataFrame((people_worldbank_series), labels = True, time=range(2000, year), skipBlanks=True, columns='series').reset_index()
                                # We indicate the range of years we want and various details to have a clean database.
peo_complete.rename(columns={'SE.XPD.TOTL.GD.ZS': 'Expenditure Education', 
                             'SL.UEM.TOTL.ZS': 'Unemployment', 
                             'SE.PRM.CMPT.ZS' : 'Primary completion rate, total (PCT of relevant age group)', 
                             'VC.IHR.PSRC.P5' : 'Intentional homicides (per 100,000 people)'}, inplace=True)
                                # In this stage, we can rename the columns with what those values represent.


'''---------------Environment---------------'''

enviroment_worldbank_series = ['EG.ELC.ACCS.ZS', 'SH.STA.BASS.UR.ZS']
                                # We indicate which data from the environment series we want.
env_complete = wb.data.DataFrame((enviroment_worldbank_series), labels = True, time=range(2000, year), skipBlanks=True, columns='series').reset_index()
                                # We indicate the range of years we want and various details to have a clean database.
env_complete.rename(columns={'EG.ELC.ACCS.ZS': 'Access Elect.', 'SH.STA.BASS.UR.ZS': 'Basic Sanitation'}, inplace=True)
                                # In this stage, we can rename the columns with what those values represent.


#Population Density
data_url = 'https://datahub.io/world-bank/en.pop.dnst/datapackage.json'     # Storing the dataset into a generic variable:
package = datapackage.Package(data_url)                                     # Loading Data Package into storage
resources = package.resources
for resource in resources:
    if resource.tabular:
        env_pop_density = pd.read_csv(resource.descriptor['path'])          # Loading only tabular data

'''---------------Poverty---------------'''

#Maternal Mortality Ratio
data_url = 'https://datahub.io/world-bank/sh.sta.mmrt/datapackage.json'     # Storing the dataset into a generic variable
package = datapackage.Package(data_url)                                     # Loading Data Package into storage
resources = package.resources
for resource in resources:
    if resource.tabular:
        pov_maternal_mortality = pd.read_csv(resource.descriptor['path'])   # Loading only tabular data


poverty_worldbank_series = ['SM.POP.REFG.OR', 'SM.POP.REFG']                
                                # We indicate which data from the environment series we want.
pov_complete = wb.data.DataFrame((poverty_worldbank_series), labels = True, time=range(2000, year), skipBlanks=True, columns='series').reset_index()
                                # We indicate the range of years we want and various details to have a clean database.
pov_complete.rename(columns={'SM.POP.REFG.OR': 'Refugee population by country or territory of origin', 
                             'SM.POP.REFG': 'Refugee population by country or territory of asylum'}, inplace=True)
                                # In this stage, we can rename the columns with what those values represent.

'''---------------States---------------'''

states_worldbank_series = ['IT.CEL.SETS.P2', 'SP.POP.TOTL', 'GB.XPD.RSDV.GD.ZS', 'SL.TLF.TOTL.IN']
                            # We indicate which data from the environment series we want.
sta_complete = wb.data.DataFrame((states_worldbank_series), labels = True, time=range(2000, year), skipBlanks=True, columns='series').reset_index()
                            # We indicate the range of years we want and various details to have a clean database.
sta_complete.rename(columns={'IT.CEL.SETS.P2': 'Mobile Subs.', 
                             'SP.POP.TOTL': 'Population Total', 
                             'GB.XPD.RSDV.GD.ZS' : 'Research and development expenditure (PCT of GDP)', 
                             'SL.TLF.TOTL.IN': 'Labour force, total'}, inplace=True)
                            # In this stage, we can rename the columns with what those values represent.

#GDP per capita
data_url = 'https://datahub.io/world-bank/ny.gdp.pcap.pp.cd/datapackage.json'   # Storing the dataset into a generic variable
package = datapackage.Package(data_url)                                         # Loading Data Package into storage
resources = package.resources
for resource in resources:
    if resource.tabular:
        sta_gdp_percapita = pd.read_csv(resource.descriptor['path'])            # Loading only tabular data

'''---------------Demographic Indicators---------------'''

mig_demo_url = 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_General/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx'
    # Storing the link in a variable to make the code cleaner.
mig_demo  = pd.read_excel(mig_demo_url, skiprows=15 , header=1 , index_col=False)
    # Importing the excel, indicating we want to skip the first 15 rows, keep row 16 as header, and removing the index column. 

#---------------------------------------------------------------------------#

'''PIPELINES'''

'''---------------World Bank---------------'''
# Dropping columns:
class DropColumn(BaseEstimator, TransformerMixin):
    def __init__(self, columns=['time']):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.drop(columns=self.columns)
        return X

# Renaming columns:
class ColumnRenamer(BaseEstimator, TransformerMixin):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.rename(columns={self.old_name: self.new_name})
        return X

# Filling null values with country mean: 
class ImputeWithCountryMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X.groupby('Country Name')[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the same country.
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X
    
# Filling remaning null values with world mean:
class ImputeWithWorldMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the whole column.
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X

    
# Changing 'Year' type of data:
class ChangeDataType(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['Year'] = X['Year'].astype(str)
        return X

#Defining the pipeline:
processes_WB = [
    ('drop_columns', DropColumn(columns=['time'])), 
    ('rename_economy_column', ColumnRenamer(old_name='economy', new_name='Country Code')),
    ('rename_time_column', ColumnRenamer(old_name='Time', new_name='Year')),
    ('rename_country_column', ColumnRenamer(old_name='Country', new_name='Country Name')),
    ('fill_null_mean', ImputeWithCountryMean()), 
    ('fill_null_world_mean', ImputeWithWorldMean()),
    ('change_data_type', ChangeDataType())]

pipeline_WB = Pipeline(processes_WB)


'''---------------Datahub---------------'''

# Dropping rows which year is prior to 2000:
class DropRowsBefore2000(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X[X['Year'] >= 2000]
        return X
    
# Checking if there are countries and years duplicated:
class DropDuplicates(BaseEstimator, TransformerMixin):
    def __init__(self, columns=["Country Code", "Year"]):
        self.columns = columns
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.drop_duplicates(subset=self.columns)
        return X

# Filling null values with country mean: 
class ImputeWithCountryMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X.groupby('Country Name')[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the whole column.
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X
    
# Filling remaning null values with world mean:
class ImputeWithWorldMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the whole column.
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X

# Changing 'Year' type of data:
class ChangeDataType(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['Year'] = X['Year'].astype(str)
        return X

# Organizing the columns:
class ColumnOrganizer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X[['Country Code', 'Country Name', 'Year', 'Value']]
        return X

#Defining the pipeline:
processes_DH = [            
    ('drop_rows_before_2000', DropRowsBefore2000()),        
    ('drop_duplicates', DropDuplicates(columns=["Country Code", "Year"])),
    ('fill_null_mean', ImputeWithCountryMean()), 
    ('fill_null_world_mean', ImputeWithWorldMean()),
    ('change_data_type', ChangeDataType()),
    ('organize_columns', ColumnOrganizer())]

pipeline_DH = Pipeline(processes_DH)


'''---------------United Nations---------------'''
# Keeping only selected columns and renaming them:
class ColumnSelectorRenamer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X[['Region, subregion, country or area *', 'ISO3 Alpha-code', 'Year', 'Natural Change, Births minus Deaths (thousands)', 'Rate of Natural Change (per 1,000 population)',
               'Population Growth Rate (percentage)', 'Crude Birth Rate (births per 1,000 population)', 'Median Age, as of 1 July (years)', 'Life Expectancy at Birth, both sexes (years)',
               'Net Number of Migrants (thousands)', 'Net Migration Rate (per 1,000 population)','Infant Mortality Rate (infant deaths per 1,000 live births)', 'Infant Deaths, under age 1 (thousands)']]
        X.columns = ['Country Name', 'Country Code'] + list(X.columns[2:])
        return X[['Country Name', 'Country Code', 'Year', 'Natural Change, Births minus Deaths (thousands)', 'Rate of Natural Change (per 1,000 population)',
                  'Population Growth Rate (percentage)', 'Crude Birth Rate (births per 1,000 population)', 'Median Age, as of 1 July (years)', 'Life Expectancy at Birth, both sexes (years)',
                  'Net Number of Migrants (thousands)', 'Net Migration Rate (per 1,000 population)', 'Infant Mortality Rate (infant deaths per 1,000 live births)', 'Infant Deaths, under age 1 (thousands)']]

# Dropping rows which year is prior to 2000:
class DropRowsBefore2000(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X[X['Year'] >= 2000]
        return X

# Changing 'Year' type of data:
class ChangeYearDataType(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['Year'] = X['Year'].astype(int)
        X['Year'] = X['Year'].astype(str)
        X['Year'] = X['Year'].str.replace('.', '')
        return X
    
# Normalizing countries' names:
class RenameCountries(BaseEstimator, TransformerMixin):
    def __init__(self):
       pass

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        self.country_dict = {'Bolivia (Plurinational State of)': 'Bolivia', 'Brunei Darussalam': 'Brunei', 'Congo': 'Congo, Republic of the', 'Democratic Republic of the Congo': 'Congo, Democratic Republic of the',
                             "Côte d'Ivoire": "Cote d'Ivoire", 'Czechia': 'Czech Republic (Czechia)', 'Eswatini': 'Eswatini (formerly Swaziland)', 'Iran (Islamic Republic of)': 'Iran', 
                             'Kosovo (under UNSC res. 1244)': 'Kosovo', "Lao People's Democratic Republic": 'Laos', 'Republic of Moldova': 'Moldova', 'Myanmar': 'Myanmar (formerly Burma)', 
                             'North Macedonia': 'North Macedonia (formerly Macedonia)', 'Russian Federation': 'Russia', "Dem. People's Republic of Korea": 'North Korea', 'Republic of Korea': 'South Korea',
                             'Syrian Arab Republic': 'Syria', 'Taiwan Province of China': 'Taiwan', 'United Republic of Tanzania': 'Tanzania', 'Turks and Caicos Islands': 'Turkey', 'United States of America': 'United States',
                             'Holy See': 'Vatican City (Holy See)', 'Venezuela (Bolivarian Republic of)': 'Venezuela', 'Viet Nam': 'Vietnam'}
        X['Country Name'] = X['Country Name'].replace(self.country_dict)
        return X

# Defining the pipeline:
processes_UN = [    
    ('column_selector_renamer', ColumnSelectorRenamer()),
    ('drop_rows_before_2000', DropRowsBefore2000()),          
    ('change_year_data_type', ChangeYearDataType()), 
    ('change_country_names', RenameCountries())
    ]

pipeline_UN = Pipeline(processes_UN)


'''---------------Finishing Touches---------------'''
# Changing 'Year' type of data back to INT:
class ChangeYearDataType(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X['Year'] = X['Year'].astype(int)
        return X

# Removing the rows that are not countries:
class RemoveRows(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        country_list = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
        'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
        'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
        'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic',
        'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Republic of the', 'Congo, Democratic Republic of the',
        'Costa Rica', 'Cote d\'Ivoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti',
        'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
        'Eswatini (formerly Swaziland)', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
        'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
        'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
        'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan',
        'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
        'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania',
        'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
        'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
        'Nigeria', 'North Korea', 'North Macedonia (formerly Macedonia)', 'Norway', 'Oman', 'Pakistan', 'Palau',
        'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
        'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
        'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone',
        'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
        'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
        'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia',
        'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
        'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City (Holy See)', 'Venezuela',
        'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        mask = X['Country Name'].isin(country_list)
        X = X[mask]
        return X

# Filling null values with country mean: 
class ImputeWithCountryMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X.groupby('Country Name')[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the whole column.
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X
    
# Filling remaning null values with world mean:
class ImputeWithWorldMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        cols_to_impute = X.columns[3:]  
            # We select the columns starting from the fourth onwards.
        self.means = X[cols_to_impute].apply(lambda x: x.fillna(x.mean()))  
            # We calculate the mean of the whole column
        X[cols_to_impute] = X[cols_to_impute].fillna(self.means)  
            # We fill in the null values with the calculated mean.
        return X

# Dropping duplicated registries:
class DropDuplicates(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.drop_duplicates()
        return X

# Sorting the dataset by alphabetical and cronological order:
class SortDataset(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.sort_values(['Country Name', 'Year']).reset_index(drop=True)
        return X
    
processes_FIN = [    
    ('change_year_data_type', ChangeYearDataType()),
    ('remove_unnecessary_rows', RemoveRows()),           
    ('fill_null_mean', ImputeWithCountryMean()), 
    ('fill_null_world_mean', ImputeWithWorldMean()),
    ('drop_duplicates', DropDuplicates()),
    ('sort_dataset', SortDataset())
    ]

pipeline_FIN = Pipeline(processes_FIN)


#---------------------------------------------------------------------------#

'''First application of Pipelines'''

# Economy
eco_complete = pipeline_WB.fit_transform(eco_complete)

# People
peo_complete= pipeline_WB.fit_transform(peo_complete)

# Environment
env_complete = pipeline_WB.fit_transform(env_complete)
env_pop_density = pipeline_DH.fit_transform(env_pop_density)

# Poverty
pov_maternal_mortality = pipeline_DH.fit_transform(pov_maternal_mortality)
pov_complete = pipeline_WB.fit_transform(pov_complete)

# States
sta_complete = pipeline_WB.fit_transform(sta_complete)
sta_gdp_percapita = pipeline_DH.fit_transform(sta_gdp_percapita)

# Migration
mig_demo = pipeline_UN.fit_transform(mig_demo)

#---------------------------------------------------------------------------#
# Obtener el nombre de las columnas
column_names = mig_demo.columns
# Iterar a través de las columnas a partir de la cuarta
for col in column_names[3:]:
    mig_demo[col] = mig_demo[col].astype('float64')

mig_demo = mig_demo.drop(mig_demo[mig_demo['Country Name'] == 'Vatican City (Holy See)'].index)
#---------------------------------------------------------------------------#

'''Renaming column [Value]'''

env_pop_density = env_pop_density.rename(columns={'Value': 'Population Density'})
pov_maternal_mortality = pov_maternal_mortality.rename(columns={'Value': 'Maternal Mortality'})
sta_gdp_percapita = sta_gdp_percapita.rename(columns={'Value': 'GDP per_capita'})

''' Merging all the datasets in one'''

merged = eco_complete.merge(peo_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(env_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(env_pop_density, on=['Country Code', 'Country Name', 'Year'],
                            how='outer').merge(pov_maternal_mortality, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(pov_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(sta_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(sta_gdp_percapita, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(mig_demo, on=['Country Code', 'Country Name', 'Year'], how='outer')


'''Applying pipeline to the merged dataset:'''

processed_merged = pipeline_FIN.fit_transform(merged) 

#---------------------------------------------------------------------------#

'''---------------Exporting the final csv---------------'''

processed_merged.to_csv('Merged_Dataset_v03.csv', index = False)

#---------------------------------------------------------------------------#