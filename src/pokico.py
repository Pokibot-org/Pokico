import numpy as np
import matplotlib.pyplot as plt
import control

#from ui import *

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Initialisation
s = control.tf('s')


class IdentificationFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)


class FreqAnalysisFrame(ttk.Frame):

    PLOT_OPTIONS = ['Bode', 'Nyquist']

    def __init__(self, master):
        # parent init
        ttk.Frame.__init__(self, master)

        # instance variables
        self.tf_sys = control.tf(1 , 1)

        # widget declaration
        self.bode_fig = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.bode_fig, master=self)
        self.plot_combo = ttk.Combobox(self, values = self.PLOT_OPTIONS,
                state = 'readonly')

        # widget customization
        self.plot_combo.current(0)

        # place
        self.plot_combo.pack(side=tk.TOP, fill=tk.BOTH)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)

        # event bindng
        self.plot_combo.bind("<<ComboboxSelected>>", self.refreshPlot)

        # init
        self.refreshPlot()

    def refreshPlot(self, event=None):
        selected_plot = self.plot_combo.get()
        plt.figure(self.bode_fig.number)
        self.bode_fig.clf()
        if selected_plot == 'Bode':
            control.bode(self.tf_sys)
        elif selected_plot == 'Nyquist':
            control.nyquist(self.tf_sys)
        self.canvas.draw()

    def setTfSys(self, tf_sys):
        self.tf_sys = tf_sys
        self.refreshPlot()


class PokicoUI(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill = tk.BOTH, expand = True)

        self.freq_analysis_frame = FreqAnalysisFrame(self.notebook)

        self.notebook.add(ttk.Frame(), text = "Identification")
        self.notebook.add(self.freq_analysis_frame, text = "Frequency Analysis")
        self.notebook.add(ttk.Frame(), text = "PID tuning")
        self.notebook.add(ttk.Frame(), text = "Discrete domain")


# System
tf_sys = (4255) / (s**2 + 11.06*s + 38.53)

# Graph
bode_fig = plt.figure()
control.bode(tf_sys)
#plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pokico")
    PokicoUI(root).pack(side = "top", fill="both", expand = True)
    root.mainloop()
