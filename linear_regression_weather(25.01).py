import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('C://Users//DELL//Desktop//Yeni klasör//rdu-weather-history.csv')

print(dataset.shape)
print(dataset.describe())

dataset.plot(x='temperaturemin', y='temperaturemax',style='o')
plt.title("temp")
plt.xlabel("min")
plt.ylabel("max")
plt.show()

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['temperaturemax'])
plt.show()

x = dataset['temperaturemin'].values.reshape(-1,1)
y = dataset['temperaturemax'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)

print('intercept:', regressor.intercept_)
print('coefficient:', regressor.coef_)

y_pred = regressor.predict(x_test)
df = pd.DataFrame({ 'Gercek' :y_test.flatten(), 'Tahmin': y_pred.flatten() })
print(df)

df1 = df.head(50)
df1.plot(kind='bar', figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='red')
plt.show()

plt.scatter(x_test, y_test, color='gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.show()

print('mean absolute', metrics.mean_absolute_error(y_test,y_pred))
print('mean squared', metrics.mean_squared_error(y_test,y_pred))
print('root squared', np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#111001

