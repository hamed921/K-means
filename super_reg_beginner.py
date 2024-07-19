# -*- coding: utf-8 -*-
"""SUPER_REG_BEGINNER.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y0ki1WC52FKf6uK5aU7FtSaZtfT9Qkm5

Importing Required libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

"""Loadig Dataset"""

url = 'https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'
df = pd.read_csv(url)
df.head()

"""Exploratory Data Analysis"""

df.shape

df.info()

df.describe()

plt.figure(figsize=(15,4))
sns.lineplot(data=df , x='Hours',y='Scores')
plt.title('Hours and Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

plt.figure(figsize=(15,4))
sns.scatterplot(data=df , x='Hours',y='Scores')
plt.title('Hours and Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

"""Splitting the Data"""

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values
x_train ,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=50)

"""Data Modelling"""

ridge_regression = LinearRegression()
ridge_regression.fit(x_train, y_train)
y_pred = ridge_regression.predict(x_test)
frame = {'Actual Values':y_test,'Predicted Values':y_pred}
frame = pd.DataFrame(frame)
frame

plt.figure(figsize=(15,4))
sns.regplot(data=df , x='Hours',y='Scores')
plt.xlabel('Number of Hours')
plt.ylabel('Score')
plt.show()

"""Evaluation"""

metrics.r2_score(y_test , y_pred)