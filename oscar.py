import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el CSV
df = pd.read_csv('./data/shopping_trends_updated.csv')


# 1. En qué estación del año suelen comprar más los hombres
hombres = df[df['Gender'] == 'Male']
estacion_mas_comprada_hombres = hombres['Season'].value_counts().idxmax()
print(f"1. Estación donde compran más los hombres: {estacion_mas_comprada_hombres}")

# 2. Qué artículo suelen comprar más los hombres
articulo_mas_comprado_hombres = hombres['Item Purchased'].value_counts().idxmax()
print(f"2. Artículo más comprado por los hombres: {articulo_mas_comprado_hombres}")

# 3. Qué artículo suelen comprar más las mujeres
mujeres = df[df['Gender'] == 'Female']
articulo_mas_comprado_mujeres = mujeres['Item Purchased'].value_counts().idxmax()
print(f"3. Artículo más comprado por las mujeres: {articulo_mas_comprado_mujeres}")

# 4. En qué categoría compran más las personas de diferentes edades
def categoria_edad(edad):
    if 18 <= edad <= 25:
        return '18-25'
    elif 26 <= edad <= 35:
        return '26-35'
    elif 36 <= edad <= 45:
        return '36-45'
    elif 46 <= edad <= 55:
        return '46-55'
    elif 56 <= edad <= 65:
        return '56-65'
    else:
        return '66+'

# Crear una nueva columna de rango de edad
df['Rango Edad'] = df['Age'].apply(categoria_edad)

# Para cada rango de edad, sacar la categoría más comprada
rango_edades = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']

print("4. Categoría más comprada por rango de edad:")
for rango in rango_edades:
    subset = df[df['Rango Edad'] == rango]
    if not subset.empty:
        categoria_mas_comprada = subset['Category'].value_counts().idxmax()
        print(f"   - {rango}: {categoria_mas_comprada}")
    else:
        print(f"   - {rango}: No hay datos")



# Filtrar hombres
hombres = df[df['Gender'] == 'Male']

# Conteo de compras por estación
compras_hombres_estacion = hombres['Season'].value_counts()

# Gráfica
plt.figure(figsize=(6,4))
sns.barplot(x=compras_hombres_estacion.index, y=compras_hombres_estacion.values, palette='Blues')
plt.title('Compras de Hombres por Estación')
plt.xlabel('Estación')
plt.ylabel('Cantidad de Compras')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Conteo artículos hombres y mujeres
top_hombres = hombres['Item Purchased'].value_counts().head(5)
mujeres = df[df['Gender'] == 'Female']
top_mujeres = mujeres['Item Purchased'].value_counts().head(5)

# Juntar en un DataFrame
articulos = pd.DataFrame({
    'Hombres': top_hombres,
    'Mujeres': top_mujeres
}).fillna(0)

# Gráfica
articulos.plot(kind='bar', figsize=(10,6), color=['steelblue', 'pink'])
plt.title('Top 5 Artículos Comprados por Género')
plt.xlabel('Artículo')
plt.ylabel('Cantidad de Compras')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# Crear columna de rango de edad (si no se ha creado aún)
df['Rango Edad'] = df['Age'].apply(categoria_edad)

# Conteo de categorías por rango
tabla_categoria_rango = pd.crosstab(df['Rango Edad'], df['Category'])

# Gráfica
plt.figure(figsize=(12,6))
sns.heatmap(tabla_categoria_rango, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Compras por Categoría y Rango de Edad')
plt.xlabel('Categoría de Producto')
plt.ylabel('Rango de Edad')
plt.show()
