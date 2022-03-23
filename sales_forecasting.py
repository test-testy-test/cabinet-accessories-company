#Import libraries

#basic packages
import os
import math
import pandas as pd
import numpy as np
import seaborn as sns
import catboost as cat
import matplotlib.pyplot as plt
%matplotlib inline

#load our data

df = pd.read_excel(r'C:\Users\zachw\Desktop\projects\internal_audit_analytics\cabinet_accessories.xlsx')
df.head()

#delete erroneous rows with cols 'Centrall' and 'Midwess'

df = df[df.region != 'Centrall']
df = df[df.region != 'Midwess']

#use sklearns to split training and test data

training_data, testing_data = train_test_split(df, test_size=0.2, random_state=25)

print(f"No. of training examples: {training_data.shape[0]}")
print(f"No. of testing examples: {testing_data.shape[0]}")

#No. of training examples: 39869
#No. of testing examples: 9968

train = training_data
test = testing_data

#first three rows of training data

print(train.head())

#shape of training data

print(train.shape)

#display general info about training data

train.info()

#training data description of numerical values

train.describe().transpose()

#percentage of missing values

train.isna().sum()/len(train)*100

#no missing values!

#correlation matrix

plt.figure(figsize=(15,10))
sns.heatmap(train.corr(), annot=True, cmap='mako')

#nothing here is unexpected. price and cost are naturally going to perfectly correlated
#sales revenue, total cost, and gross profits are all going to be perfectly correlated too

#Since our models are going to be forecasting gross profit as a function of the other variables
##we should visualize the distribution of gross profit as the dependent variable

plt.figure(figsize=(20,5))
sns.distplot(train['gross_profit'], bins=40, kde=True, color='blue')
plt.title('Gross Profit Distribution')
plt.show()

#distribution map shows that virtually all instances of sales yield gross profits between $0-5000, with some outliers
##above and below, reflecting unusually high or low (negative) gross profits

#gross profits as a function of individual variables

fig, ax = plt.subplots(2, 2, figsize= (20,20))
ax[0,0].scatter(train['list_price'], train['gross_profit'])
ax[0,0].set_title('Gross Profits by Price')
ax[0,1].scatter(train['cost'], train['gross_profit'])
ax[0,1].set_title('Gross Profits by Cost')
ax[1,0].scatter(train['date_of_sale'], train['gross_profit'])
ax[1,0].set_title('Gross Profits by Date')
ax[1,1].scatter(train['region'], train['gross_profit'])
ax[1,1].set_title('Gross Profits by Region')
plt.show()

#obviously, profits are likely to be higher when items are sold at a higher listed price
#the same pattern is is seen with costs, as higher costs tend to be reflected in listed price
#the four years are roughly similar, with 2018 having a higher share of very expensive sales
#the midwest region appears to perform distinctively well

#with catboost, we will build a regression model for gross profits as a function of our categorical features region,
##brand, and collection

#create categorical features and pass them over to the model and fit the model on the training dataset

import catboost as cat
cat_feat = ['region','brand', 'collection']
features = list(set(train.columns)-set(['gross_profit']))
target = 'gross_profit'
model = cat.CatBoostRegressor(random_state=100,cat_features=cat_feat,verbose=0)
model.fit(train[features],train[target])

#now, used the fitted model, we test its accuracy on the test dataset

y_true = pd.DataFrame(data=test[target], columns=['gross_profit'])
test_temp = test.drop(columns=[target])

#now, run the trained model on the test dataset to get model predictions and check accuracy

y_pred = model.predict(test_temp[features])
from sklearn.metrics import mean_squared_error
from math import sqrt

rmse = sqrt(mean_squared_error(y_true, y_pred))
print(rmse)

#RMSE Output: ~276.25 is not good! It looks like our categorical features are not the best predictors of success!

#save model locally

import pickle
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
