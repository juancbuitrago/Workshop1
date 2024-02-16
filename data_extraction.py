import pandas as pd

# Lee el archivo CSV
data = pd.read_csv('candidates.csv', sep=';')

# Muestra los primeros registros para verificar que los datos se cargaron correctamente
name_list = data.columns.tolist()
print(name_list)
#data.info()