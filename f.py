import pandas as pd

# Cargar el CSV
df = pd.read_csv('./data/shopping_trends_updated.csv')

# Crear una columna que indique si hubo recompra (Previous Purchases > 1)
df['Recompra'] = df['Previous Purchases'] > 1

# Agrupar por Category y Frequency of Purchases
grupo = df.groupby(['Category', 'Frequency of Purchases'])

# Calcular el número total de casos y el número de recompras
resumen = grupo['Recompra'].agg(
    total_compras='count',
    recompras='sum'
)

# Calcular la probabilidad condicional de recompra
resumen['probabilidad_recompra'] = resumen['recompras'] / resumen['total_compras']

# Ordenar de mayor a menor probabilidad
resumen = resumen.sort_values(by='probabilidad_recompra', ascending=False)

# Mostrar el resumen
print(resumen.reset_index())