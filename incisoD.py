import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# --- Preparar carpetas ---
output_folder = './results'
os.makedirs(output_folder, exist_ok=True)

# --- Leer datos ---
df = pd.read_csv('./data/shopping_trends_updated.csv')

# --- Resumen estadístico ---
summary = pd.DataFrame(columns=['media', 'mediana', 'moda', 'minimo', 'maximo', 'rango', 'Rango Intercuartílico'])

for col in df.columns:
    series = df[col]
    if pd.api.types.is_numeric_dtype(series):
        mean_val = series.mean()
        median_val = series.median()
        mode_val = series.mode().iloc[0] if not series.mode().empty else None
        min_val = series.min()
        max_val = series.max()
        range_val = max_val - min_val
        iqr_val = series.quantile(0.75) - series.quantile(0.25)
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

# Guardar resumen
summary.to_csv(os.path.join(output_folder, 'resumen_estadistico.csv'))
print(summary)

# --- Probabilidades ---
resultados_txt = []

if 'Gender' in df.columns:
    p_male = (df['Gender'] == 'Male').mean()
    resultados_txt.append(f"Probabilidad de que el comprador sea Hombre: {p_male:.2f}")

if 'Payment Method' in df.columns:
    p_credit_card = (df['Payment Method'] == 'Credit Card').mean()
    resultados_txt.append(f"Probabilidad de uso de Tarjeta de Crédito: {p_credit_card:.2f}")

# --- Prueba t de Student ---
if 'Gender' in df.columns and 'Purchase Amount (USD)' in df.columns:
    males = df[df['Gender'] == 'Male']['Purchase Amount (USD)'].dropna()
    females = df[df['Gender'] == 'Female']['Purchase Amount (USD)'].dropna()

    t_stat, p_value = stats.ttest_ind(males, females, equal_var=False)
    resultados_txt.append(f"Prueba t de Student entre Hombres y Mujeres:\nt = {t_stat:.4f}, p = {p_value:.4f}")
    if p_value < 0.05:
        resultados_txt.append("→ Rechazamos H0: Hay diferencia significativa en el gasto promedio.")
    else:
        resultados_txt.append("→ No se rechaza H0: No hay diferencia significativa en el gasto promedio.")

# --- Prueba U de Mann-Whitney ---
u_stat, p_value_mw = stats.mannwhitneyu(males, females, alternative='two-sided')
resultados_txt.append(f"\nPrueba U de Mann-Whitney:\nU = {u_stat:.4f}, p = {p_value_mw:.4f}")
if p_value_mw < 0.05:
    resultados_txt.append("→ Rechazamos H0: Hay diferencia significativa en el gasto promedio.")
else:
    resultados_txt.append("→ No se rechaza H0: No hay diferencia significativa en el gasto promedio.")

# --- Prueba de normalidad ---
shapiro_stat, shapiro_p = stats.shapiro(df['Purchase Amount (USD)'].dropna())
resultados_txt.append(f"\nPrueba de normalidad (Shapiro-Wilk):\nW = {shapiro_stat:.4f}, p = {shapiro_p:.4f}")
if shapiro_p < 0.05:
    resultados_txt.append("→ Los datos NO siguen una distribución normal.")
else:
    resultados_txt.append("→ Los datos podrían seguir una distribución normal.")

# Guardar resultados en txt
with open(os.path.join(output_folder, 'resultados.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(resultados_txt))

# --- Gráficas ---
sns.set(style="whitegrid")

# Histograma + KDE de 'Purchase Amount (USD)'
plt.figure(figsize=(8,6))
sns.histplot(df['Purchase Amount (USD)'].dropna(), kde=True, bins=30, color="blue")
plt.title('Distribución de Purchase Amount (USD)')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frecuencia')
plt.savefig(os.path.join(output_folder, 'histograma_purchase_amount.png'))
plt.close()

# Boxplot por 'Gender'
plt.figure(figsize=(8,6))
sns.boxplot(x='Gender', y='Purchase Amount (USD)', data=df, palette="Set2")
plt.title('Gasto según Género')
plt.xlabel('Género')
plt.ylabel('Purchase Amount (USD)')
plt.savefig(os.path.join(output_folder, 'boxplot_gender_purchase.png'))
plt.close()

# QQ-Plot para ver normalidad
from scipy.stats import probplot

plt.figure(figsize=(8,6))
probplot(df['Purchase Amount (USD)'].dropna(), dist="norm", plot=plt)
plt.title('QQ-Plot de Purchase Amount (USD)')
plt.savefig(os.path.join(output_folder, 'qqplot_purchase_amount.png'))
plt.close()

print("\nTodos los archivos fueron guardados en ./results/")

