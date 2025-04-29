import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
df = pd.read_csv("./data/shopping_trends.csv")  # Asegúrate de poner la ruta correcta

# 1. Integridad de los Datos
print(" 1. Integridad de los Datos")
print("Total de registros:", df.shape[0])
print("Total de columnas:", df.shape[1])

valores_nulos = df.isnull().sum()
print("\nValores nulos por columna:")
print(valores_nulos[valores_nulos > 0] if valores_nulos.sum() > 0 else "Ninguna columna contiene valores nulos.")

registros_duplicados = df.duplicated().sum()
print("\nRegistros duplicados:", registros_duplicados)

# 2. Estadísticas Descriptivas para campos numéricos
print("\n 2. Estadísticas Descriptivas (Campos Numéricos)")
campos_numericos = ['Age', 'Purchase Amount (USD)', 'Previous Purchases']
if 'Rating' in df.columns:
    campos_numericos.append('Rating')

estadisticas = df[campos_numericos].describe().loc[['min', 'mean', 'max']]
print(estadisticas)

# 3. Consistencia en Campos Categóricos
print("\n 3. Consistencia en Campos Categóricos")

# Género
print("\n -Género:")
print(df['Gender'].value_counts())

# Talla
print("\n -Talla (Size):")
print(df['Size'].value_counts())

# Temporada
print("\n -Temporada (Season):")
print(df['Season'].value_counts())

# Métodos de Pago
print("\n -Método de Pago:")
print(df['Payment Method'].value_counts())

print("\n -Método de Pago Preferido:")
print(df['Preferred Payment Method'].value_counts())

# Ubicaciones
print("\n -Ubicaciones distintas:", df['Location'].nunique())

# Columnas binarias
columnas_binarias = ['Subscription Status', 'Discount Applied', 'Promo Code Used']
print("\n -Columnas Binarias:")
for columna in columnas_binarias:
    if columna in df.columns:
        print(f"{columna}:\n{df[columna].value_counts()}\n")


# Gráfica de barras para 'Gender'
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title('Distribución por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfica de barras para 'Size'
plt.figure(figsize=(6,4))
sns.countplot(x='Size', data=df, palette='muted')
plt.title('Distribución de Tallas')
plt.xlabel('Talla')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfica de barras para 'Season'
plt.figure(figsize=(6,4))
sns.countplot(x='Season', data=df, palette='cool')
plt.title('Distribución por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfica de pastel para 'Payment Method'
plt.figure(figsize=(6,6))
df['Payment Method'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('Método de Pago Usado')
plt.ylabel('')
plt.show()

# Histograma de 'Age'
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribución de Edad de los Clientes')
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
