import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Dashboard import Dashboard

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
