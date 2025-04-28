import pandas as pd

# 1. Carga el CSV
df = pd.read_csv('./data/shopping_trends_updated.csv')

# 2. Obtén el conteo por categoría
counts = df['Frequency of Purchases'].value_counts()

# 3. Mapea cada etiqueta a su intervalo medio en semanas
#    Asumimos 52 semanas al año, 12 meses, 4 trimestres...
interval_weeks = {
    'Weekly': 1,
    'Fortnightly': 2,
    'Bi-Weekly': 2,
    'Monthly': 52 / 12,       # ≈ 4.333 semanas
    'Quarterly': 52 / 4,      # 13 semanas
    'Every 3 Months': 52 / 4, # 13 semanas
    'Annually': 52            # 52 semanas
}

# 4. Construye un DataFrame con los resultados
df_counts = (
    counts
    .rename_axis('Frequency')     # pone el índice como columna 'Frequency'
    .reset_index(name='Count')    # convierte a DataFrame con columna 'Count'
)
df_counts['Interval_weeks'] = df_counts['Frequency'].map(interval_weeks)

# 5. Probabilidad de recompra en la próxima semana
df_counts['P_next_week'] = 1 / df_counts['Interval_weeks']

# 6. (Opcional) Normaliza para que la suma sea 1
df_counts['P_norm'] = df_counts['P_next_week'] / df_counts['P_next_week'].sum()

# 7. Muestra el resultado
print(df_counts)
