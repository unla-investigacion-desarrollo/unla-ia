import pandas as pd

# Ruta del archivo CSV
# Asegúrate de que la ruta sea correcta
melbourne_file_path = 'csv/melb_data.csv'  

# Leer el archivo CSV en un DataFrame
melbourne_data = pd.read_csv(melbourne_file_path)

# Imprimir un resumen de los datos
print(melbourne_data.describe())
