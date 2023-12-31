# -*- coding: utf-8 -*-
"""car price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FliUg5KWEXC33RdBbYDOM9UX_WDo3JXL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/CarPrice_Assignment.csv')

df.head()

df.info()

df.describe()

df.isnull().sum()

df.dtypes

sns.heatmap(df.corr())

cr = df.corr()

cr_df = cr['price'].sort_values(ascending=False)
cr_df

df.hist(bins=20, figsize =(15,10), color= 'blue', edgecolor='yellow')

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True, color='blue')
plt.title('Distribution of Target Variable')
plt.xlabel('Sales Price')
plt.ylabel('Density')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['boreratio'], df['price'], alpha=0.5,color='blue')
plt.title('Relationship between Boreratio and Sales Price')
plt.xlabel('Boreratio')
plt.ylabel('Sales Price')
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(df['horsepower'], df['price'], alpha=0.5,color='blue')
plt.title('Relationship between HorsePower and Sales Price')
plt.xlabel('horsepower')
plt.ylabel('Sales Price')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['enginesize'], df['price'], alpha=0.5,color='blue')
plt.title('Relationship between Enginesize and Sales Price')
plt.xlabel('enginesize')
plt.ylabel('Sales Price')
plt.show()

df['enginetype'].unique()



df['BRthreshold'] = df['boreratio'].apply(lambda x: 1 if x > 3.5 else 0)

df['EGthreshold'] = df['enginesize'].apply(lambda x: 2 if x > 150 else 0 if x < 100 else 1)

df['cylindernumber'].unique()

cylinder_map = {'four': 4,'five': 5,'three': 3,'six': 6,'two': 2,'eight': 8,'twelve': 12}
df['cylindernumber']= df['cylindernumber'].map(cylinder_map)

df.head()

df['CarName'].unique()

df['CarName']= df['CarName'].apply(lambda x: 'Alfa-romero' if 'alfa-romero'in x.lower() else
                                   ('Audi' if 'audi'in x.lower() else
                                   ("BMW" if 'bmw' in x.lower() else
                                   ('Chevrolet' if 'chevrolet'in x.lower() else
                                   ('Dodge' if 'dodge'in x.lower() else
                                   ('Honda' if 'honda'in x.lower() else
                                   ('Isuzu' if 'isuzu'in x.lower() else
                                   ('Jaguar' if 'jaguar'in x.lower() else
                                   ('Mazda' if 'maxda'in x.lower() or 'mazda'in x.lower() else
                                   ('Buick' if 'buick'in x.lower() else
                                   ('Mercury' if 'mercury'in x.lower() else
                                    ('Mitsubishi' if 'mitsubishi'in x.lower() else
                                    ('Nissan' if 'nissan' in x.lower() else
                                    ('Peugeot' if 'peugeot' in x.lower() else
                                    ('Plymouth'if 'plymouth' in x.lower() else
                                    ('Porsche' if 'porsche' in x.lower() else
                                    ('Renault' if 'renault' in x.lower() else
                                    ('Saab' if 'saab' in x.lower() else
                                    ('Subaru' if 'subaru' in x.lower() else
                                    ('Toyota' if 'toyota' in x.lower() else
                                    ('Volkswagen' if 'volkswagen' in x.lower() or 'vw' in x.lower() else
                                    ('Volvo' if 'volvo' in x.lower() else
                                      None))))))))))))))))))))))

print(df['CarName'].value_counts())

df.head()

avg_price= df.groupby('CarName')['price'].mean()
print(avg_price.sort_values(ascending=False))

high_end = ['Jaguar', 'Porsche', 'BMW', 'Buick','Audi']
mid_range = ['Toyota', 'Nissan', 'Mazda', 'Volvo', 'Volkswagen', 'Saab', 'Isuzu','Mercury', 'Peugeot','Alfa-romero']
budget = ['Plymouth', 'Renault','Chevrolet','Honda','Dodge','Mitsubishi','Subaru']

df['ExpensiveTier'] = df['CarName'].apply(lambda x: 2 if x in high_end else (1 if x in mid_range else 0))

df_1 = df.drop(columns=['symboling','car_ID','compressionratio','stroke','peakrpm','carheight','CarName','aspiration','doornumber','carlength','carlength','carwidth'], axis=1)

df_1.head()

df_1.shape

df_1.dtypes

df_1= pd.get_dummies(data= df_1, columns= ['fueltype'])

df_1= pd.get_dummies(data= df_1, columns= ['carbody'], drop_first= True)

df_1= pd.get_dummies(data= df_1, columns= ['drivewheel'], drop_first= True)

df_1= pd.get_dummies(data= df_1, columns= ['enginelocation'], drop_first= True)



df_1= pd.get_dummies(data= df_1, columns= ['fuelsystem'], drop_first= True)



df_1= pd.get_dummies(data= df_1, columns= ['enginetype'], drop_first= True)



df_1.columns

df_1.shape











from sklearn.model_selection import train_test_split

X= df_1.drop(columns=['price'])
y= df_1['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred= lr.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2_square = r2_score(y_test,y_pred)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

rf= RandomForestRegressor()
rf.fit(X_train, y_train)

y_pred2= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred2)
r2_square = r2_score(y_test,y_pred2)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

dt= DecisionTreeRegressor()
dt.fit(X_train, y_train)

y_pred3= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred3)
r2_square = r2_score(y_test,y_pred3)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

