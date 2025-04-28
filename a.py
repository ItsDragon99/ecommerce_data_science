import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('data/shopping_trends_updated.csv')

# 1. Integridad de los Datos
print(" 1. Integridad de los Datos")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")
print()

# Verificar valores nulos
print("Valores nulos por columna:")
if df.isnull().sum().sum() == 0:
    print("Ninguna columna contiene valores nulos.")
else:
    print(df.isnull().sum())
print()

# Verificar duplicados
duplicados = df.duplicated().sum()
print(f"Registros duplicados: {duplicados}")
print()

# 2. Estadísticas Descriptivas
print(" 2. Estadísticas Descriptivas (Campos Numéricos)")
print(df[['Age', 'Purchase Amount (USD)', 'Previous Purchases']].describe().loc[['min', 'mean', 'max']])
print()

# 3. Consistencia en Campos Categóricos
print(" 3. Consistencia en Campos Categóricos")
print()

# Género
print(" -Género:")
print(df['Gender'].value_counts())
print()

# Talla
print(" -Talla (Size):")
print(df['Size'].value_counts())
print()

# Temporada
print(" -Temporada (Season):")
print(df['Season'].value_counts())
print()

# Método de Pago
print(" -Método de Pago:")
payment_counts = df['Payment Method'].value_counts()
print(payment_counts)
print()

# Análisis del método de pago preferido (basado en frecuencia)
print(" -Método de Pago Preferido (basado en frecuencia):")
preferred_payment = payment_counts.idxmax()
preferred_count = payment_counts.max()
preferred_percentage = (preferred_count / len(df)) * 100
print(f"El método de pago más utilizado (preferido) es: {preferred_payment}")
print(f"Utilizado en {preferred_count} transacciones ({preferred_percentage:.2f}% del total)")
print()

# Visualización de métodos de pago
plt.figure(figsize=(10, 6))
payment_counts.plot(kind='bar', color='skyblue')
plt.title('Métodos de Pago Utilizados')
plt.xlabel('Método de Pago')
plt.ylabel('Número de Transacciones')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('payment_methods.png')
print("Se ha guardado un grafico de métodos de pago como 'payment_methods.png'")
print()

# Ubicaciones
print(" -Ubicaciones distintas:", df['Location'].nunique())
print()

# Columnas binarias
print(" -Columnas Binarias:")
print("Subscription Status:")
print(df['Subscription Status'].value_counts())
print()

print("Discount Applied:")
print(df['Discount Applied'].value_counts())