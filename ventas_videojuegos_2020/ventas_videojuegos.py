import pandas as pd

videojuegos = pd.read_csv("ventas_videojuegos_2020.csv")
print(videojuegos.info())

df_sin_nulos = videojuegos.dropna(how='any')
df_sin_nulos.loc[:, 'Year'] = df_sin_nulos['Year'].round().astype(int)
print(df_sin_nulos.info())


df_sin_nulos.to_csv("ventas_videojuegos_2024.csv", index=False)