import pandas as pd
from sklearn.tree import DecisionTreeRegressor

from sklearn import tree
import matplotlib.pyplot as plt
# Ruta del archivo CSV
# Asegúrate de que la ruta sea correcta
melbourne_file_path = 'csv/melb_data.csv'  

# Leer el archivo CSV en un DataFrame
melbourne_data = pd.read_csv(melbourne_file_path)

print('TABLA. Dataset Original \n', melbourne_data.describe())
                  #PARTE: MODELIZACIóN
# Eliminamos filas que tengan valores perdidos
melbourne_data = melbourne_data.dropna(axis=0)

#y será nuestra predicción
y = melbourne_data.Price

#las columnas de nuestro modelo se llaman "features" y son con las que haremos la predicción
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 
                      'Lattitude', 'Longtitude']

#por conveción, a la data en esas features, se la llama X
X = melbourne_data[melbourne_features]

#vista de los datos que utilizaremos en nuestro modelo
print("Datos del modelo- Subset\n")
print(X.describe())

melbourne_model = DecisionTreeRegressor(random_state=1, max_depth=3)

# Fit model
melbourne_model.fit(X, y)

print("Las predicciones se haran sobre las siguiente 5 casas:")
print(X.head())
print("Las predicciones son")
print(melbourne_model.predict(X.head()))

fig = plt.figure(figsize=(25,20))
tree.plot_tree(melbourne_model, feature_names=melbourne_features, class_names= y, filled=True)
plt.show()