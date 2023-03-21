import streamlit as st
import pandas as pd
from PIL import Image
import pandas as pd 
import numpy as np

st.set_page_config(
    page_title='Study of Features with ML',
    layout='wide'
)

image = Image.open('./Stream_finalisimo_kpi_last3/images/predicciones.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.header(":violet[Hypothesis of work.]")
st.write('We are interested on finding out wich are the more important features when it comes to explain migratory phenomena, in order to provide Countries Policy Makers and third party interested individuals several KPIs, to monitor and measure the effect of migration within its frontiers.')   
st.write('Our hypothesis of work is that the features that explain Net Migration Flows are different for countries with positive and negative net migration. In order to test our hypothesis, we will run a ML model using SelectKBest features for different groupings of countries based on its Net Migration.')
st.write('We will run some tests on the data in order to study the realtionships between our variables and compare the results.')
st.write('First of all we will run the SelectKBest module of SciKitLearn. This function selects the top k features with the highest scores based on a scoring function that in this case will be "f_regression", which calculates the correlation between each feature and the target variable and returns an F-value and p-value for each feature. In our case study the variable we will consider as our target is Net Net Number of Migrants (thousands).')
st.write('SelectKBest then selects the top k features with the highest F-values, which indicates that they have the strongest linear relationship with the target variable. This means that the selected features are the ones that have more incidence in explaining the phenomenon of the numbers of migrants.')
st.write('But how can I understan further the impact of each feature in the phenomena of net migration? We can use the coefficients of the Linear Regression Model to understand the direction and the impact of each feature on the target variable.')
st.write('In the first place, we will apply the methodology to all countries, in order to have a broad overview of the idea.')

#LINEA VISIBLE DE CODIGO
code = '''# Select the 5 best characteristics to explain migration flows globally.
# Drop non-numeric columns and separate features and target variable
y = df['Net Number of Migrants (thousands)']

# Scale the df

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform feature selection

selector = SelectKBest(score_func=f_regression, k=5)
selector.fit(X_scaled, y)
selected_features_total = X.columns[selector.get_support()]

# Print the selected features

SKB_mundo = selected_features_total.to_list()
SKB_mundo
'''
st.code(code, language='python')



image = Image.open('./Stream_finalisimo_kpi_last3/images/population_totalIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write('------------------------')

#LINEA VISIBLE DE CODIGO
code = '''# Select the features and target variable

X = df[selected_features_total]
y = df['Net Number of Migrants (thousands)']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the linear regression model
model = sm.OLS(y, sm.add_constant(X_scaled))
results = model.fit()

# Print the coefficients and p-values for each feature
coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': results.params[1:], 'p-value': results.pvalues[1:]})
coefficients'''

st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/x_population_totalIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.write('------------------------')

st.write('The process gives us these 5 variables and their respective coefficients. This means that, considering all countries, Net Migration tends to be explained globally by these features.')
st.write('At first sight, all of them tend to be logic. We will delve into the more detailed analysis once we have the complete data to compare, infer patterns and draw conclusions.')
st.write('A p-value is a statistical measure of the evidence against the null hypothesis that the coefficient of the feature is zero. A p-value less than or equal to 5% significance level suggests that the coefficient for the feature is statistically significant at a 95% confidence level.')
st.write('This means that there is strong evidence of a relationship between each of these variables and "Net Number of Migrants (thousands)" in the population from where our sample was drawn. This means that there is less than a 5% probability that the observed relationship between the predictor and the response variable is due to chance.')
st.write('Based on the information we got from the tests, the p-values are very low (much less than 0.05), which indicates that the corresponding coefficients are statistically significant at a 95% confidence level. ')
st.write('Therefore, we can say that the features are likely to have a significant impact on the target variable.')

st.markdown("-----------")

st.header(":violet[Feature Selection.]")
         
st.write('Multicollinearity refers to a situation in which two or more independent variables in a regression model are highly correlated with each other. As a result, the coefficients of the variables in the model may become unstable and difficult to interpret, and the overall performance of the model may suffer. This effect can be a problem for a number of reasons, which we will not go into detail. ')
st.write('One way to check for multicollinearity is to calculate the variance inflation factor (VIF) for each feature. The VIF measures how much the variance of the estimated regression coefficient for a given feature is increased due to multicollinearity with the other features. A VIF value of 1 indicates no multicollinearity, while higher values indicate increasing levels of multicollinearity.')

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO
code = '''# Select the features and target variable
X = df.drop(['Country Code','Country Name', 'Year', 'Net Number of Migrants (thousands)'], axis=1)
y = df['Net Number of Migrants (thousands)']

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
dropped_features
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/access_electIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write(' We can see that these variables had a VIF > 5, so the features were removed and will not be taken into account for this analysis.')
st.write('Finally, we keep the rest ot the features to work with our ML model.')

st.markdown("-----------")

st.write('To test our hypothesis we will proceed to divide and classify our database based on net migratory flows.')
st.write('We will sort the DF by net migration in descending order and sort out all the registers into 5 categories, labelling them from 1 to 5, being 1 the group of registers with more positive Net Migration and 5 the group with more negative Net Migration . This will provide us a more profound understanding of migration in different scenarios y times.')
st.write('It is important to note that in this experiment we will have different years from different countries in each group. This is because we are not trying to study the behavior of migratory flows for a particular country. Here we are trying to understand migration as a social phenomenon inherent to the nature of the human being, regardless of the human political borders that are subject to constant modification.')

#LINEA VISIBLE DE CODIGO
code = '''# Sort the rows by net migration in descending order

df_sorted = df.sort_values(by=['Net Number of Migrants (thousands)'], ascending=False)

# Calculate the number of countries in each group
num_countries = len(df_sorted)
group_size = num_countries // 5
last_group_size = num_countries - 4 * group_size

# Create a list with the group number for each register
group_numbers = [1] * group_size + [2] * group_size + [3] * group_size + [4] * group_size + [5] * last_group_size

# Add the column to the DF with the corresponding value to each register.
df_sorted['Group'] = group_numbers
'''
st.code(code, language='python')

st.markdown("-----------")

st.write('Now we ll proceed to make 3 different DF for those countries with values 1, 3 and 5.')

#LINEA VISIBLE DE CODIGO
code = '''df_sorted_1 = df_sorted.loc[df_sorted['Group'] == 1].copy()
df_sorted_3 = df_sorted.loc[df_sorted['Group'] == 3].copy()
df_sorted_5 = df_sorted.loc[df_sorted['Group'] == 5].copy()
'''
st.code(code, language='python')

st.markdown("-----------")

st.write('Now for every group, we will select the 5 Best features and we will calculate the coefficients, check the p-values and some statistical data of relevance.')
st.write('We will do without the non numerical features, the Net Number of Migrants (thousands) target feature and Net Migration Rate (per 1,000 population).')
st.write('This last variable is highly correlated with the target, so we will remove it from the sample as we have strong reasons to believe it could bring to the model problems of endogeneity and autocorrelation.')

#LINEA VISIBLE DE CODIGO

code = '''not_considered = ['Country Code',
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
'''
st.code(code, language='python')


st.markdown("-----------")

st.write('***Group 1 High Positive Net Migration***')

#LINEA VISIBLE DE CODIGO

code = '''# 5 most important features for group 1

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
SK_1
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/export_ofIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Select the features and target variable
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
coefficients_1
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/x1 export.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Create a correlation matrix using pandas corr() method
SK_1.append('Net Number of Migrants (thousands)')
corr = df[SK_1].corr()

# Round the correlation values to two decimals
corr = corr.round(2)

# Create a heatmap using seaborn
sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"fontsize":14}, ax=ax)

# Set the plot title
ax.set_title('Correlation Matrix', fontsize=16)

# Show the plot
plt.show()
'''
st.code(code, language='python')

image = Image.open('./Stream_finalisimo_kpi_last3/images/grafico_1Ing.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.write('***Group 3 Tending to Neutral Net Migration***')

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# 5 most important features for group 3

# Drop non-numeric columns and separate features and target variable

X = df_sorted_3.drop(not_considered, axis=1)
y = df_sorted_3['Net Number of Migrants (thousands)']

# Scale the df

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform feature selection

selector = SelectKBest(score_func=f_regression, k=5)
selector.fit(X_scaled, y)
selected_features_3 = X.columns[selector.get_support()]

# Print the selected features

SK_3 = selected_features_3.to_list()
SK_3
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/gni_per_capita.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Select the features and target variable
X = df_sorted_3[selected_features_3]
y = df_sorted_3['Net Number of Migrants (thousands)']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit the linear regression model
model = sm.OLS(y, sm.add_constant(X_scaled))
results = model.fit()

# Print the coefficients for each feature
coefficients_3 = pd.DataFrame({'feature': X.columns, 'coefficient': results.params[1:], 'p-value': results.pvalues[1:]})
coefficients_3
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/x1_gni_per.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Create a correlation matrix using pandas corr() method
SK_3.append('Net Number of Migrants (thousands)')
corr = df[SK_3].corr()

# Round the correlation values to two decimals
corr = corr.round(2)

# Create a heatmap using seaborn
sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"fontsize":14}, ax=ax)

# Set the plot title
ax.set_title('Correlation Matrix', fontsize=16)

# Show the plot
plt.show()
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/grafico_2Ing.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write('***Group 5 High Negative Net Migration***')

#LINEA VISIBLE DE CODIGO

code = '''# 5 most important features for group 5

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
SK_5
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/import_ofIng.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Select the features and target variable
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
coefficients_5
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/x1 import.png')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

#LINEA VISIBLE DE CODIGO

code = '''# Create a correlation matrix using pandas corr() method
SK_5.append('Net Number of Migrants (thousands)')
corr = df[SK_5].corr()

# Round the correlation values to two decimals
corr = corr.round(2)

# Create a heatmap using seaborn
sns.set(font_scale=1.2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"fontsize":14}, ax=ax)

# Set the plot title
ax.set_title('Correlation Matrix', fontsize=16)

# Show the plot
plt.show()
'''
st.code(code, language='python')


image = Image.open('./Stream_finalisimo_kpi_last3/images/grafico_3Ing3.jpg')
st.image(image, caption=None, width=750, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("-----------")

st.write('Scaling the data doesnt change the interpretation of a linear regression model. The coefficients in the model still represent the change in the target variable for a one-unit change in the corresponding feature, after holding all other features constant. However, the interpretation of the coefficients in terms of their magnitude may change.')
st.write('When the data is scaled, the coefficients will be in terms of standard deviations instead of the original units of measurement. This means that a one-standard deviation increase in a particular feature will result in a beta coefficient increase (or decrease) of the target variable, rather than a one-unit increase in the feature.')
st.write('Overall, the interpretation of the coefficients will still be meaningful, but you will need to keep in mind that they are expressed in terms of standard deviations, rather than the original units of measurement.')



