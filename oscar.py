import pandas as pd

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
