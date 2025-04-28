import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

results_folder = './results.oliver/extra'
os.makedirs(results_folder, exist_ok=True)

file_path = './data/shopping_trends.csv'
data = pd.read_csv(file_path)

with open(os.path.join(results_folder, 'summary.txt'), 'w', encoding='utf-8') as f:
    f.write("Resumen de los datos:\n")
    f.write(str(data.info()) + "\n\n")
    f.write("Primeras filas del dataset:\n")
    f.write(str(data.head()) + "\n")

# Pregunta 1: ¿Hay más mujeres u hombres comprando?
gender_counts = data['Gender'].value_counts()
with open(os.path.join(results_folder, 'summary.txt'), 'a', encoding='utf-8') as f:
    f.write("\nCantidad de compras por género:\n")
    f.write(str(gender_counts) + "\n")

plt.figure(figsize=(6, 4))
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='viridis')
plt.title('Cantidad de Compras por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Compras')
plt.savefig(os.path.join(results_folder, 'compras_por_genero.png'))
plt.close()

# Pregunta 2: ¿Qué ciudades generan más compras?
city_counts = data['Location'].value_counts().head(10)
with open(os.path.join(results_folder, 'summary.txt'), 'a', encoding='utf-8') as f:
    f.write("\nTop 10 ciudades con más compras:\n")
    f.write(str(city_counts) + "\n")

plt.figure(figsize=(10, 6))
sns.barplot(x=city_counts.values, y=city_counts.index, palette='coolwarm')
plt.title('Top 10 Ciudades con Más Compras')
plt.xlabel('Cantidad de Compras')
plt.ylabel('Ciudad')
plt.savefig(os.path.join(results_folder, 'ciudades_mas_compras.png'))
plt.close()

# Pregunta 3: ¿Faltan edades? ¿Hay edades menores a 10 o mayores a 100?
missing_ages = data['Age'].isnull().sum()
out_of_range_ages = data[(data['Age'] < 10) | (data['Age'] > 100)]
with open(os.path.join(results_folder, 'summary.txt'), 'a', encoding='utf-8') as f:
    f.write(f"\nCantidad de edades faltantes: {missing_ages}\n")
    f.write(f"Cantidad de edades fuera del rango (menores a 10 o mayores a 100): {len(out_of_range_ages)}\n")

plt.figure(figsize=(8, 5))
sns.histplot(data['Age'].dropna(), bins=30, kde=True, color='skyblue')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.axvline(10, color='red', linestyle='--', label='Edad mínima (10)')
plt.axvline(100, color='red', linestyle='--', label='Edad máxima (100)')
plt.legend()
plt.savefig(os.path.join(results_folder, 'distribucion_edades.png'))
plt.close()

# Pregunta 4: ¿Cuál es el rango de montos de compra más común en las compras?
if 'Purchase Amount (USD)' in data.columns:
    amount_bins = pd.cut(data['Purchase Amount (USD)'], bins=[0, 50, 100, 200, 500, 1000, float('inf')], 
                         labels=['0-50', '51-100', '101-200', '201-500', '501-1000', '1000+'])
    amount_range_counts = amount_bins.value_counts().sort_index()
    with open(os.path.join(results_folder, 'summary.txt'), 'a', encoding='utf-8') as f:
        f.write("\nCantidad de compras por rango de montos:\n")
        f.write(str(amount_range_counts) + "\n")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=amount_range_counts.index, y=amount_range_counts.values, palette='magma')
    plt.title('Cantidad de Compras por Rango de Montos')
    plt.xlabel('Rango de Montos (USD)')
    plt.ylabel('Cantidad de Compras')
    plt.savefig(os.path.join(results_folder, 'compras_por_rango_montos.png'))
    plt.close()
else:
    with open(os.path.join(results_folder, 'summary.txt'), 'a', encoding='utf-8') as f:
        f.write("\nLa columna 'Purchase Amount (USD)' no existe en el dataset.\n")
