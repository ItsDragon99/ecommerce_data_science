import pandas as pd

# Carga el CSV
df = pd.read_csv('./data/shopping_trends_updated.csv')

# 1. Definir indicador de recompra:
#    True si el cliente ha tenido al menos 1 compra previa
df['recompra'] = df['Previous Purchases'] > 0

# 2. Probabilidad global de recompra
prob_global = df['recompra'].mean()

# 3. Probabilidad de recompra por segmento
#    a) Por frecuencia de compra
prob_por_frecuencia = df.groupby('Frequency of Purchases')['recompra'].mean()

#    b) Por categoría de producto
prob_por_categoria = df.groupby('Category')['recompra'].mean()

#    c) Por método de pago
prob_por_pago = df.groupby('Payment Method')['recompra'].mean()

# Mostrar resultados
print(f"Probabilidad global de recompra: {prob_global:.2%}\n")

print("Probabilidad de recompra por frecuencia de compras:")
print(prob_por_frecuencia.to_string(), "\n")

print("Probabilidad de recompra por categoria de producto:")
print(prob_por_categoria.to_string(), "\n")

print("Probabilidad de recompra por metodo de pago:")
print(prob_por_pago.to_string())