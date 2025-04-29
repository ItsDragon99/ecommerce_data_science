import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear la carpeta si no existe
output_dir = './results.julian/distribuciones'
os.makedirs(output_dir, exist_ok=True)

# Cargar el dataset
data = pd.read_csv('./data/shopping_trends.csv')

# Visualizar distribuciones
# Ejemplo: Distribución de Edad
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], kde=True, bins=20, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig(f'{output_dir}/age_distribution.png')
plt.close()

# Ejemplo: Distribución del Monto de Compra
plt.figure(figsize=(8, 6))
sns.histplot(data['Purchase Amount (USD)'], kde=True, bins=20, color='green')
plt.title('Purchase Amount Distribution')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frequency')
plt.savefig(f'{output_dir}/purchase_amount_distribution.png')
plt.close()

# Visualizar dispersiones
# Ejemplo: Diagrama de dispersión Edad vs Monto de Compra
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['Age'], y=data['Purchase Amount (USD)'], hue=data['Gender'])
plt.title('Age vs Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Purchase Amount (USD)')
plt.legend(title='Gender')
plt.savefig(f'{output_dir}/age_vs_purchase_amount.png')
plt.close()

# Ejemplo: Diagrama de caja para Calificación de Reseñas por Género
plt.figure(figsize=(8, 6))
sns.boxplot(x=data['Gender'], y=data['Review Rating'], palette='Set2')
plt.title('Review Rating by Gender')
plt.xlabel('Gender')
plt.ylabel('Review Rating')
plt.savefig(f'{output_dir}/review_rating_by_gender.png')
plt.close()

# Ejemplo: Diagrama de conteo para Estado de Suscripción
plt.figure(figsize=(8, 6))
sns.countplot(x=data['Subscription Status'], palette='Set3')
plt.title('Subscription Status Count')
plt.xlabel('Subscription Status')
plt.ylabel('Count')
plt.savefig(f'{output_dir}/subscription_status_count.png')
plt.close()