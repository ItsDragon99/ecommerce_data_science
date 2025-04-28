import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('./data/shopping_trends.csv')

columnas_a_normalizar = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
scaler = MinMaxScaler()
df[columnas_a_normalizar] = scaler.fit_transform(df[columnas_a_normalizar])

output_dir = './results.oliver/normalizados'
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'datos_normalizados.csv')
df.to_csv(output_file, index=False)

for columna in columnas_a_normalizar:
    plt.figure()
    df[columna].plot(kind='line', title=f'Columna Normalizada: {columna}')
    plt.xlabel('Índice')
    plt.ylabel('Valor Normalizado')
    plt.grid()
    plt.savefig(os.path.join(output_dir, f'{columna}_normalizada.png'))
    plt.close()

print(f"normazalizado aqui merengues --->{output_file}")
print(f"graficos aca bien chidos  en ---> {output_dir}")
