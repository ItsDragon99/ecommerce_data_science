import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos (opcional si ya lo tienes cargado)
df = pd.read_csv('./data/shopping_trends_updated.csv')

# Crear columna de recompra
df['Recompra'] = df['Previous Purchases'] > 1

# Agrupar por categoría y frecuencia
grupo = df.groupby(['Category', 'Frequency of Purchases'])
resumen = grupo['Recompra'].agg(
    total_compras='count',
    recompras='sum'
)
resumen['probabilidad_recompra'] = resumen['recompras'] / resumen['total_compras']
resumen = resumen.reset_index()

# Ordenar los datos para graficar
resumen = resumen.sort_values(by='probabilidad_recompra', ascending=False)

# Crear el gráfico
plt.figure(figsize=(14, 8))
sns.barplot(
    data=resumen,
    x='probabilidad_recompra',
    y='Category',
    hue='Frequency of Purchases',
    palette='viridis'
)

plt.title('Probabilidad de Recompra por Categoría y Frecuencia', fontsize=16)
plt.xlabel('Probabilidad de Recompra', fontsize=14)
plt.ylabel('Categoría de Producto', fontsize=14)
plt.legend(title='Frecuencia de Compra', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlim(0.9, 1.0)  # Como todas son muy altas, hacemos zoom entre 90% y 100%
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
