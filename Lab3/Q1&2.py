#Q1-------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv('hepatitis_csv.csv')
df2 = pd.read_csv('diabetes_csv.csv')
#df2 = df.dropna()

df = df.dropna(thresh=len(df)*0.75, axis = 1)
df = df.dropna(axis = 0)

df = pd.get_dummies(df)

df = df.fillna(df.median(numeric_only = True).round(1))
arr = df.to_numpy()

x = df['albumin'].to_numpy()
y = df['class_live'].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size = 0.25)

#Q2-------------------

model = LinearRegression().fit(x_train.reshape(-1,1), y_train)
pred = model.predict(x_test.reshape(-1,1))
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")
rmse = np.sqrt((pred - y_test) ** 2).mean()
print(rmse)
fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,.5,.5])
ax1.scatter(x_test,y_test,color='g')
ax1.plot(x_test,pred,color='b')

