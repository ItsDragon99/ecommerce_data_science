import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tkinter import messagebox, BOTH
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotManager:
    def __init__(self, frame_content):
        self.frame_content = frame_content

    def plot_data(self, df):
        if df is None or df.empty:
            messagebox.showerror("Error", "El DataFrame está vacío o no se pudo cargar el archivo CSV.")
            return

        fig = plt.figure(figsize=(10, 8), dpi=100)
        rows, cols = 2, 2

        if 'Gender' in df.columns:
            ax1 = fig.add_subplot(rows, cols, 1)
            df['Gender'].value_counts().plot(kind='bar', ax=ax1)
            ax1.set_title('Distribución por Género')
            ax1.set_xlabel('Género')
            ax1.set_ylabel('Cantidad')

        if 'Payment Method' in df.columns:
            ax2 = fig.add_subplot(rows, cols, 2)
            df['Payment Method'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
            ax2.set_ylabel('')
            ax2.set_title('Métodos de Pago')

        if 'Age' in df.columns:
            ax3 = fig.add_subplot(rows, cols, 3)
            df['Age'].plot(kind='hist', bins=10, ax=ax3)
            ax3.set_xlabel('Edad')
            ax3.set_ylabel('Frecuencia')
            ax3.set_title('Distribución de Edad')

        # Mostrar el gráfico en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame_content)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def normalize_and_save_data(self, input_file='./data/shopping_trends.csv', output_dir='./results/normalizados'):
        try:
            df = pd.read_csv(input_file)
            columnas_a_normalizar = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
            columnas_existentes = [col for col in columnas_a_normalizar if col in df.columns]

            if not columnas_existentes:
                messagebox.showwarning("Advertencia", "No se encontraron columnas para normalizar.")
                return

            # Normalizar
            scaler = MinMaxScaler()
            df[columnas_existentes] = scaler.fit_transform(df[columnas_existentes])

            # Crear carpeta si no existe
            os.makedirs(output_dir, exist_ok=True)

            # Guardar CSV
            output_file = os.path.join(output_dir, 'datos_normalizados.csv')
            df.to_csv(output_file, index=False)

            # Graficar cada columna normalizada
            for columna in columnas_existentes:
                self.plot_column(df, columna, output_dir)

            print(f"Archivo normalizado guardado en: {output_file}")
            print(f"Gráficos guardados en: {output_dir}")

        except FileNotFoundError:
            messagebox.showerror("Error", f"No se encontró el archivo: {input_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al normalizar los datos: {e}")

    def plot_column(self, df, columna, output_dir):
        """Método para graficar cada columna de manera individual."""
        try:
            plt.figure(figsize=(10, 6))  # Definir el tamaño de la gráfica
            df[columna].plot(kind='line', title=f'Columna Normalizada: {columna}')
            plt.xlabel('Índice')
            plt.ylabel('Valor Normalizado')
            plt.grid(True)  # Habilitar la cuadrícula para mejor lectura
            plt.tight_layout()  # Ajustar para evitar que los textos se salgan
            plt.savefig(os.path.join(output_dir, f'{columna}_normalizada.png'))
            plt.close()  # Cerrar la figura después de guardarla
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al graficar la columna {columna}: {e}")
