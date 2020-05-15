# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
from Lib import pickle
from Lib.urllib import request

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
filename = 'finalized_model.sav'

pickle.dump(regressor,open(filename,'wb'))

# Predicting the Test set results
y_pred = regressor.predict(X_test)




def predictValueModel(experience):
    import pickle
    print(experience)
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(np.array([float(experience)]).reshape(1, 1))
    return result

