import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('50_Startups.csv')
x=data.iloc[:,-1].values
y=data.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X=LabelEncoder()
x[: , 3] = labelencoder_X.fit_transform(x[: , 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
x=onehotencoder.fit_transform(x).toarray()

x=x[: , 1:]



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train  = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()


classifier.add(Dense(output_dim = 6 ,init= 'uniform' , activation = 'relu' , input_dim = 4))

classifier.add(Dense(output_dim = 6 ,init= 'uniform' , activation = 'relu'))

classifier.add(Dense(output_dim = 1 ,init= 'uniform' , activation = 'relu'))

classifier.compile(optimizer = 'adam' , loss = 'rms' , metrics = ['accuracy'])

classifier.fit(x_train , y_train , batch_size = 10 ,nb_epoch =100)

y_pred = classifier.predict(x_test)


print(y_pred)

