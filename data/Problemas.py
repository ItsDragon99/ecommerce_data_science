import pandas as pd


df = pd.read_csv('data/shopping_trends_updated.csv')

# 1.-
categoria_mas_popular_hombres = df[df['Gender'] == 'Male']['Category'].value_counts().idxmax()

# 2.- 
item_mas_popular_california = df[df['Location'] == 'California']['Item Purchased'].value_counts().idxmax()

# 3.- 
bins = list(range(0, 101, 10))
labels = [f'{i}-{i+9}' for i in bins[:-1]]
df['Age Range'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
rango_mas_gasto = df.groupby('Age Range')['Purchase Amount (USD)'].sum().idxmax()

# 4.- 
envio_preferido_mujeres = df[df['Gender'] == 'Female']['Shipping Type'].value_counts().idxmax()

print(f"1.- La categoria mas popular entre hombres es: {categoria_mas_popular_hombres}")
print(f"2.- El item mas popular en California es: {item_mas_popular_california}")
print(f"3.- El rango de edad que mas dinero gasta es: {rango_mas_gasto}")
print(f"4.- El tipo de envio preferido por las mujeres es: {envio_preferido_mujeres}")
