#---------------------------------------------------------------------------#
print("Starting Pipeline:")
print("Loading libraries...")
#---------------------------------------------------------------------------#

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
print("Libraries successfully loaded.")
print("Loading Datasets:")
print("...loading 'Economy'. This may take a while...")
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

#---------------------------------------------------------------------------#
print("Successfully loaded 'Economy' dataset.")
print("...loading 'People'. This may take a while...")
#---------------------------------------------------------------------------#

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

#---------------------------------------------------------------------------#
print("Successfully loaded 'People' dataset.")
print("...loading 'Environment'. This may take a while...")
#---------------------------------------------------------------------------#

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

#---------------------------------------------------------------------------#
print("Successfully loaded 'Environment' dataset.")
print("...loading 'Poverty'. This may take a while...")
#---------------------------------------------------------------------------#

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

#---------------------------------------------------------------------------#
print("Successfully loaded 'Poverty' dataset.")
print("...loading 'States'. This may take a while...")
#---------------------------------------------------------------------------#

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

#---------------------------------------------------------------------------#
print("Successfully loaded 'States' dataset.")
print("...loading 'Demographic Indicators'. This may take a while...")
#---------------------------------------------------------------------------#

'''---------------Demographic Indicators---------------'''

mig_demo_url = 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_General/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx'
    # Storing the link in a variable to make the code cleaner.
mig_demo  = pd.read_excel(mig_demo_url, skiprows=15 , header=1 , index_col=False)
    # Importing the excel, indicating we want to skip the first 15 rows, keep row 16 as header, and removing the index column. 

#---------------------------------------------------------------------------#
print("Successfully loaded 'Demographic Indicators' dataset.")
print("Loading Pipelines...")
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
        X = X.reset_index(drop=True) # reset index
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
        X = X.reset_index(drop=True) # reset index
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
        X = X.reset_index(drop=True) # reset index
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
        X = X.reset_index(drop=True) # reset index
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
        'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City (Holy See)', 'Venezuela',
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
        X = X.reset_index(drop=True) # reset index
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
        X = X.reset_index(drop=True) # reset index
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
print("Successfully loaded Pipelines.")
print("Applying pipelines...")
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
print("Pipelines successfully applied.")
print("Merging datasets...")
#---------------------------------------------------------------------------#

'''Dropping [Vatican] since it presents problems'''
mig_demo = mig_demo.drop(mig_demo[mig_demo['Country Name'] == 'Vatican City (Holy See)'].index)

'''Changing type of data to float:'''
column_names = mig_demo.columns
for col in column_names[3:]:
    mig_demo[col] = mig_demo[col].astype('float64')

'''Renaming column [Value]'''
env_pop_density = env_pop_density.rename(columns={'Value': 'Population Density'})
pov_maternal_mortality = pov_maternal_mortality.rename(columns={'Value': 'Maternal Mortality'})
sta_gdp_percapita = sta_gdp_percapita.rename(columns={'Value': 'GDP per_capita'})

#---------------------------------------------------------------------------#

''' Merging all the datasets in one'''

merged = eco_complete.merge(peo_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(env_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(env_pop_density, on=['Country Code', 'Country Name', 'Year'],
                            how='outer').merge(pov_maternal_mortality, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(pov_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(sta_complete, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(sta_gdp_percapita, on=['Country Code', 'Country Name', 'Year'], 
                            how='outer').merge(mig_demo, on=['Country Code', 'Country Name', 'Year'], how='outer')

#---------------------------------------------------------------------------#
print("Datasets successfully merged.")
#---------------------------------------------------------------------------#

'''Applying pipeline to the merged dataset:'''

processed_merged = pipeline_FIN.fit_transform(merged) 

#---------------------------------------------------------------------------#

print("Pipeline successfully applied to the merged dataset.")
print("Loading Machine Learning module...")

#---------------------------------------------------------------------------#

#-----------------------------MACHINE LEARNING------------------------------#

#---------------------------------------------------------------------------#

# Neccessary Libraries:
import numpy as np

from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

import seaborn as sns
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------#

'''---------------Calculating VIF---------------'''

# Select the features and target variable
X = processed_merged.drop(['Country Code','Country Name', 'Year', 'Net Number of Migrants (thousands)'], axis=1)
y = processed_merged['Net Number of Migrants (thousands)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate the VIF for each feature
vif = pd.DataFrame()
vif["feature"] = X_train.columns
vif["VIF"] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]

# Remove any features with a VIF greater than 5
while vif["VIF"].max() > 5:
    feature_to_remove = vif.loc[vif["VIF"].idxmax(), "feature"]
    X_train.drop(feature_to_remove, axis=1, inplace=True)
    X_test.drop(feature_to_remove, axis=1, inplace=True)
    vif = pd.DataFrame()
    vif["feature"] = X_train.columns
    vif["VIF"] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]

# Fit the model again using the reduced feature set
model.fit(X_train, y_train)

# Make predictions on the testing set and calculate the mean squared error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Print the coefficients, VIF, MSE, and RMSE
coefficients = pd.DataFrame({'feature': X_train.columns, 'coefficient': model.coef_})
p_values = pd.DataFrame({'feature': X_train.columns, 'p_value': sm.OLS(model.predict(X_train), X_train).fit().pvalues})
results = pd.merge(coefficients, p_values, on="feature")
results["VIF"] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
results["MSE"] = mse
results["RMSE"] = rmse

# Print the dropped features
dropped_features = set(X.columns) - set(X_train.columns)

'''---------------Dividing and Classifying based on Net Migratory Flows---------------'''

# Sort the rows by net migration in descending order
df_sorted = processed_merged.sort_values(by=['Net Number of Migrants (thousands)'], ascending=False)
processed_merged = processed_merged.sort_values(by=['Net Number of Migrants (thousands)'], ascending=False)

# Calculate the number of countries in each group
num_countries = len(df_sorted)
group_size = num_countries // 5
last_group_size = num_countries - 4 * group_size

# Create a list with the group number for each register
group_numbers = [1] * group_size + [2] * group_size + [3] * group_size + [4] * group_size + [5] * last_group_size

# Add the column to the DF with the corresponding value to each register.
df_sorted['Group'] = group_numbers
processed_merged['Group'] = df_sorted['Group']
processed_merged = processed_merged.sort_values(['Country Name', 'Year'], ascending=[True, True])

'''---------------Creating new dataframes based on values---------------'''
df_sorted_1 = df_sorted.loc[df_sorted['Group'] == 1].copy()
df_sorted_3 = df_sorted.loc[df_sorted['Group'] == 3].copy()
df_sorted_5 = df_sorted.loc[df_sorted['Group'] == 5].copy()

# Columns that will not be used for training:
not_considered = ['Country Code',
                'Country Name', 
                'Year', 
                'Net Number of Migrants (thousands)',
                'Net Migration Rate (per 1,000 population)',
                'Access Elect.',
                'Crude Birth Rate (births per 1,000 population)',
                'Natural Change, Births minus Deaths (thousands)',
                'Population Growth Rate (percentage)',
                'Population Total',
                'Rate of Natural Change (per 1,000 population)']

#---------------------------------------------------------------------------#
print("Successfully loaded Machine Learning module.")
print("Training group 1...")
#---------------------------------------------------------------------------#

#----- Group #1 - High Positive Net Migration -----#

'''---------------5 most important features for group 1---------------'''

# Drop non-numeric columns and separate features and target variable
X = df_sorted_1.drop(not_considered, axis=1)
y = df_sorted_1['Net Number of Migrants (thousands)']

# Scale the df
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform feature selection
selector = SelectKBest(score_func=f_regression, k=5)
selector.fit(X_scaled, y)
selected_features_1 = X.columns[selector.get_support()]

# Print the selected features
SK_1 = selected_features_1.to_list()

'''---------------Ordinary Least Square Method Regression---------------'''

# Select the features and target variable
X = df_sorted_1[selected_features_1]
y = df_sorted_1['Net Number of Migrants (thousands)']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the linear regression model
model = sm.OLS(y, sm.add_constant(X_scaled))
results = model.fit()

# Print the coefficients and p-values for each feature
coefficients_1 = pd.DataFrame({'feature': X.columns, 'coefficient': results.params[1:], 'p-value': results.pvalues[1:]})

#---------------------------------------------------------------------------#
print("Successfully trained group 1.")
print("Training group 5...")
#---------------------------------------------------------------------------#

#----- Group #5 - High Negative Net Migration -----#

'''---------------5 most important features for group 5---------------'''

# Drop non-numeric columns and separate features and target variable
X = df_sorted_5.drop(not_considered, axis=1)
y = df_sorted_5['Net Number of Migrants (thousands)']

# Scale the df
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform feature selection
selector = SelectKBest(score_func=f_regression, k=5)
selector.fit(X_scaled, y)
selected_features_5 = X.columns[selector.get_support()]

# Print the selected features
SK_5 = selected_features_5.to_list()

'''---------------Ordinary Least Square Method Regression---------------'''

# Select the features and target variable
X = df_sorted_5[selected_features_5]
y = df_sorted_5['Net Number of Migrants (thousands)']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the linear regression model
model = sm.OLS(y, sm.add_constant(X_scaled))
results = model.fit()

# Print the coefficients for each feature
coefficients_5 = pd.DataFrame({'feature': X.columns, 'coefficient': results.params[1:], 'p-value': results.pvalues[1:]})

#---------------------------------------------------------------------------#
print("Successfully trained group 5.")
print("Loading KPI's module...")
#---------------------------------------------------------------------------#


#---------------------------------------------------------------------------#

#-----------------------------------KPI-------------------------------------#

#---------------------------------------------------------------------------#

#--------------- KPI #1

processed_merged['KPI_1'] = round((processed_merged['Net Number of Migrants (thousands)']*1000)/(processed_merged['Population Total']) * 100 , 2)

#---------------------------------------------------------------------------#
print("Success: KPI-1.")
#---------------------------------------------------------------------------#

#--------------- KPI #2

# Group the data by country
grouped = processed_merged.groupby('Country Name')

# Calculate the difference in 'Net Number of Migrants (thousands)' between consecutive years for each country
diff = grouped['Net Number of Migrants (thousands)'].diff()

# Add the difference as a new column to the original DataFrame
processed_merged['KPI_2'] = round(diff,2)

# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
processed_merged['KPI_2'].fillna(0, inplace=True)

#---------------------------------------------------------------------------#
print("Success: KPI-2.")
#---------------------------------------------------------------------------#

#--------------- KPI #3

# Create a new column 'KPI_3'
processed_merged['KPI_3'] = round((np.sign(processed_merged['KPI_2']) * abs(processed_merged['KPI_2'] / processed_merged['Net Number of Migrants (thousands)'].shift()) * 100) , 2)
# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
processed_merged['KPI_3'].fillna(0, inplace=True)

#---------------------------------------------------------------------------#
print("Success: KPI-3.")
#---------------------------------------------------------------------------#

#--------------- KPI #4

# Standardize the columns
processed_merged[SK_1] = (processed_merged[SK_1] - processed_merged[SK_1].mean()) / processed_merged[SK_1].std()

# Assign a negative sign for the features with negative coefficient
processed_merged['Exports of goods and services (PCT of GDP)'] = -processed_merged['Exports of goods and services (PCT of GDP)']
processed_merged['Infant Mortality Rate (infant deaths per 1,000 live births)'] = -processed_merged['Infant Mortality Rate (infant deaths per 1,000 live births)']

# Create the KPI column
processed_merged['KPI_4'] = processed_merged[SK_1].sum(axis=1)/5

#--- Year on Year KPI's percentual variation

processed_merged['VAR_KPI_4'] = round(processed_merged['KPI_4'].pct_change()*100,2)

# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
processed_merged['VAR_KPI_4'].fillna(0, inplace=True)

#---------------------------------------------------------------------------#
print("Success: KPI-4.")
#---------------------------------------------------------------------------#

#--------------- KPI #5

# Standardize the columns
processed_merged[SK_5] = (processed_merged[SK_5] - processed_merged[SK_5].mean()) / processed_merged[SK_5].std()

# Assign a negative sign for the features with negative coefficient
processed_merged['Imports of goods and services (PCT of GDP)'] = -processed_merged['Imports of goods and services (PCT of GDP)']

# Create the KPI column
processed_merged['KPI_5'] = -processed_merged[SK_5].sum(axis=1)/5

#--- Year on Year KPI's percentual variation

processed_merged['VAR_KPI_5'] = round(processed_merged['KPI_5'].pct_change()*100,2)

# Replace the NaN values with 0 (since the first row for each country will have a NaN value)
processed_merged['VAR_KPI_5'].fillna(0, inplace=True)

#---------------------------------------------------------------------------#
print("Success: KPI-5.")
print("Exporting finished dataset...")
#---------------------------------------------------------------------------#

#---------------------------------------------------------------------------#

'''---------------Exporting the final csv---------------'''

processed_merged.to_csv('Merged_Dataset_v03.csv', index = False)

print('Successfully exported Merged_Dataset_v03.csv')
print('End of Pipeline!')

#---------------------------------------------------------------------------#
