import tkinter as tk
from DataLoader import DataLoader
from PlotManager import PlotManager

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard de Análisis de Datos de E-commerce")

        # Frame de contenido
        self.frame_content = tk.Frame(root, bg="white")
        self.frame_content.pack(expand=True, fill=tk.BOTH)

        # Inicializar componentes
        self.data_loader = DataLoader()
        self.plot_manager = PlotManager(self.frame_content)

        # Cargar y graficar
        self.df = self.data_loader.load_csv("./data/shopping_trends_updated.csv")
        self.plot_manager.plot_data(self.df)
        self.plot_manager.normalize_and_save_data()
