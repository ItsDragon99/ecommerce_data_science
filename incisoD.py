import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Lee el archivo CSV
df = pd.read_csv('./data/shopping_trends_updated.csv')

# DataFrame para el resumen completo
summary = pd.DataFrame(columns=['media', 'mediana', 'moda', 'minimo', 'maximo', 'rango', 'Rango Intercuartílico'])

for col in df.columns:
    series = df[col]
    # Columnas numéricas
    if pd.api.types.is_numeric_dtype(series):
        mean_val = series.mean()
        median_val = series.median()
        mode_val = series.mode().iloc[0] if not series.mode().empty else None
        min_val = series.min()
        max_val = series.max()
        range_val = max_val - min_val
        iqr_val = series.quantile(0.75) - series.quantile(0.25)
    # Columnas no numéricas (convertidas a categorías)
    else:
        cat_series = series.astype('category')
        codes = cat_series.cat.codes
        mean_val = codes.mean()
        median_code = codes.median()
        try:
            median_val = cat_series.cat.categories[int(median_code)]
        except (IndexError, ValueError):
            median_val = None
        mode_val = series.mode().iloc[0] if not series.mode().empty else None
        min_val = cat_series.cat.categories[codes.min()] if len(cat_series.cat.categories) > 0 else None
        max_val = cat_series.cat.categories[codes.max()] if len(cat_series.cat.categories) > 0 else None
        range_val = codes.max() - codes.min()
        iqr_val = codes.quantile(0.75) - codes.quantile(0.25)
    
    summary.loc[col] = [mean_val, median_val, mode_val, min_val, max_val, range_val, iqr_val]

# Imprime el resumen
print(summary.to_string())
# --- 3. Probabilidades Básicas ---

# Probabilidad de que el comprador sea Hombre
if 'Gender' in df.columns:
    p_male = (df['Gender'] == 'Male').mean()
    print(f"\nProbabilidad de que el comprador sea Hombre: {p_male:.2f}")

# Probabilidad de que un comprador use tarjeta de crédito
if 'Payment Method' in df.columns:
    p_credit_card = (df['Payment Method'] == 'Credit Card').mean()
# --- 4. Prueba de Hipótesis (Test t de Student) ---

# Comparar gasto promedio entre Hombres y Mujeres
if 'Gender' in df.columns and 'Purchase Amount (USD)' in df.columns:
    males = df[df['Gender'] == 'Male']['Purchase Amount (USD)']
    females = df[df['Gender'] == 'Female']['Purchase Amount (USD)']

    # Prueba t para muestras independientes
    t_stat, p_value = stats.ttest_ind(males.dropna(), females.dropna(), equal_var=False)
    print("\nPrueba t de Student entre Hombres y Mujeres:")
    print(f"t = {t_stat:.4f}, p-value = {p_value:.4f}")
    if p_value < 0.05:
        print("\u2192 Rechazamos H0: Hay diferencia significativa en el gasto promedio.")
    else:
        print("\u2192 No se rechaza H0: No hay diferencia significativa en el gasto promedio.")

# --- Estadística Inferencial Avanzada ---

# 1. Prueba U de Mann-Whitney (no paramétrica)
# Comparar gasto entre Hombres y Mujeres sin suponer normalidad
if 'Gender' in df.columns and 'Purchase Amount (USD)' in df.columns:
    males = df[df['Gender'] == 'Male']['Purchase Amount (USD)'].dropna()
    females = df[df['Gender'] == 'Female']['Purchase Amount (USD)'].dropna()

    u_stat, p_value_mw = stats.mannwhitneyu(males, females, alternative='two-sided')

    print("\nPrueba U de Mann-Whitney entre Hombres y Mujeres:")
    print(f"U = {u_stat:.4f}, p-value = {p_value_mw:.4f}")

    if p_value_mw < 0.05:
        conclusion_mw = "\u2192 Rechazamos H0: Hay diferencia significativa en el gasto promedio."
    else:
        conclusion_mw = "\u2192 No se rechaza H0: No hay diferencia significativa en el gasto promedio."
    print(conclusion_mw)

# 2. Prueba de normalidad (Shapiro-Wilk)
print("\nPrueba de normalidad (Shapiro-Wilk) para 'Purchase Amount (USD)':")
shapiro_stat, shapiro_p = stats.shapiro(df['Purchase Amount (USD)'].dropna())
print(f"W = {shapiro_stat:.4f}, p-value = {shapiro_p:.4f}")

if shapiro_p < 0.05:
    conclusion_shapiro = "\u2192 Los datos no siguen una distribución normal."
else:
    conclusion_shapiro = "\u2192 No se rechaza la normalidad de los datos."
print(conclusion_shapiro)
