import pandas as pd

# Cargar los datos
df = pd.read_csv('./data/shopping_trends.csv')

# 1. Estado que más gasta
def estado_mayor_gasto(df):
    estado_gasto = df.groupby('Location')['Purchase Amount (USD)'].sum()
    return estado_gasto.idxmax(), estado_gasto.max()

# 2. Método de pago más popular en mujeres (ajustar si existen registros femeninos)
def metodo_pago_mujeres(df):
    mujeres_df = df[df['Gender'] == 'Female']
    if mujeres_df.empty:
        return "No hay registros de mujeres en el dataset"
    return mujeres_df['Payment Method'].mode()[0]
def metodo_pago_hombres(df):
    mujeres_df = df[df['Gender'] == 'Male']
    if mujeres_df.empty:
        return "No hay registros de hombres en el dataset"
    return mujeres_df['Payment Method'].mode()[0]

# 3. Tipo de envío más popular en Hawaii
def envio_popular_hawaii(df):
    hawaii_df = df[df['Location'] == 'Hawaii']
    return hawaii_df['Shipping Type'].mode()[0]

# 4. Color más popular por categoría
def color_popular_por_categoria(df):
    categorias = df['Category'].unique()
    resultados = {}
    for categoria in categorias:
        cat_df = df[df['Category'] == categoria]
        color_popular = cat_df['Color'].mode()[0]
        resultados[categoria] = color_popular
    return resultados

# Ejecutar las funciones
print("1. Estado que más gasta:")
estado, monto = estado_mayor_gasto(df)
print(f"{estado} - ${monto:,.2f}")

print("\n2. Método de pago más popular en mujeres:")
print(metodo_pago_mujeres(df))

print("\n2. Método de pago más popular en hombres:")
print(metodo_pago_hombres(df))

print("\n3. Tipo de envío más popular en Hawaii:")
print(envio_popular_hawaii(df))

print("\n4. Color más popular por categoría:")
colores = color_popular_por_categoria(df)
for categoria, color in colores.items():
    print(f"{categoria}: {color}")