import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('C:/Users\PC\Downloads\data.csv')
data=data.drop(index=0, axis=0)
a=pd.get_dummies(data)
c=data.to_numpy()
#data=data.head(100)
plt.scatter(data['Country'], data['Schooling'])
plt.xlabel('Country')
plt.ylabel('Schooling')
plt.colorbar()
plt.show()







