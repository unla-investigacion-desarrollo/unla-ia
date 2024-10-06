import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

# Función para obtener el MAE y entrenar el modelo con diferentes valores de max_leaf_nodes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae, model  # Devuelve el MAE y el modelo entrenado

# Ruta del archivo CSV
melbourne_file_path = 'csv/melb_data.csv'  
melbourne_data = pd.read_csv(melbourne_file_path)

# Eliminamos filas que tengan valores perdidos
melbourne_data = melbourne_data.dropna(axis=0)

# Definimos el target (lo que queremos predecir) y las características (features)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# Dividir los datos en conjunto de entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Probar diferentes valores de max_leaf_nodes y almacenar el que da mejor resultado
best_mae = float('inf')
best_model = None
best_leaf_nodes = None

for max_leaf_nodes in [5, 10, 20, 30]:  # Cambiar valores si prefieres menos computación
    mae, model = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {max_leaf_nodes} \t Mean Absolute Error: {mae}")
    
    if mae < best_mae:
        best_mae = mae
        best_model = model
        best_leaf_nodes = max_leaf_nodes

# Mostrar el mejor modelo con su MAE
print(f"\nMejor modelo con max_leaf_nodes = {best_leaf_nodes} tiene un MAE de {best_mae}")

# Visualizar el árbol del mejor modelo
fig = plt.figure(figsize=(25,20))
tree.plot_tree(best_model, feature_names=melbourne_features, filled=True)
plt.show()

