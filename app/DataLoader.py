import pandas as pd
from tkinter import messagebox

class DataLoader:
    def load_csv(self, filepath):
        try:
            df = pd.read_csv(filepath)
            return df
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            return None
