import pandas as pd

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
