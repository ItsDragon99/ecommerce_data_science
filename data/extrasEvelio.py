# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo subido
df = pd.read_csv('data\shopping_trends.csv')

# 1.- Categoría más popular entre hombres
categoria_hombres = df[df['Gender'] == 'Male']['Category'].value_counts()

# 2.- Ítem más popular en California
item_california = df[df['Location'] == 'California']['Item Purchased'].value_counts()

# 3.- Rango de edad que más gasta
bins = list(range(0, 101, 10))
labels = [f'{i}-{i+9}' for i in bins[:-1]]
df['Age Range'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
gasto_por_rango = df.groupby('Age Range')['Purchase Amount (USD)'].sum()

# 4.- Tipo de envío preferido por mujeres
envio_mujeres = df[df['Gender'] == 'Female']['Shipping Type'].value_counts()

# Estilo de los gráficos
sns.set(style="whitegrid")

# Crear subplots
fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Análisis de Compras', fontsize=20, y=1.02)

# 1. Categoría más popular entre hombres
sns.barplot(x=categoria_hombres.values, y=categoria_hombres.index, ax=axes[0,0], palette="Blues_r")
axes[0,0].set_title('Categorías más populares entre Hombres')
axes[0,0].set_xlabel('Cantidad')

# 2. Ítem más popular en California
sns.barplot(x=item_california.values, y=item_california.index, ax=axes[0,1], palette="Greens_r")
axes[0,1].set_title('Items más populares en California')
axes[0,1].set_xlabel('Cantidad')

# 3. Gasto por rango de edad
sns.barplot(x=gasto_por_rango.values, y=gasto_por_rango.index, ax=axes[1,0], palette="Purples_r")
axes[1,0].set_title('Gasto Total por Rango de Edad')
axes[1,0].set_xlabel('Monto Total (USD)')

# 4. Tipo de envío preferido por mujeres
sns.barplot(x=envio_mujeres.values, y=envio_mujeres.index, ax=axes[1,1], palette="Oranges_r")
axes[1,1].set_title('Tipos de Envío preferidos por Mujeres')
axes[1,1].set_xlabel('Cantidad')

plt.tight_layout()
plt.show()
