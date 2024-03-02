import pandas as pd

data = pd.read_csv('candidates.csv', sep=';')

name_list = data.columns.tolist()
print(name_list)
