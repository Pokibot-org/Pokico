import tkinter as tk
from tkinter import ttk

class IdentificationFrame(ttk.Frame):
    pass

class FreqAnalysisFrame(ttk.Frame):
    pass

class PokicoUI(ttk.Frame):


    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill = "both", expand = True)

        self.freq_analysis_frame = ttk.Frame(self.notebook)

        self.notebook.add(ttk.Frame(), text = "Identification")
        self.notebook.add(self.freq_analysis_frame, text = "Frequency Analysis")
        self.notebook.add(ttk.Frame(), text = "PID tuning")
        self.notebook.add(ttk.Frame(), text = "Discrete domain")

