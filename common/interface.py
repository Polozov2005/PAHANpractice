import tkinter as tk
from tkinter import ttk
from ctypes import windll
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import equation
import built_in_integration
import my_integration
import plotting

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("")
root.geometry("1600x900")
root.resizable(False, False)

# Задание темы
root.tk.call("source", "common/azure.tcl")
root.tk.call("set_theme", "dark")

root.columnconfigure(index=0, weight=2)
root.columnconfigure(index=1, weight=1)
for index in [0, 2]:
    root.rowconfigure(index=index, weight=1)

graph_frame = ttk.Frame(root)
graph_frame.grid(
    row=0, column=0, sticky="nsew", rowspan=3
)

conditions_frame = ttk.LabelFrame(root, text="Начальные условия", padding=(20, 10))
conditions_frame.grid(
    row=0, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(5):
    conditions_frame.rowconfigure(index=index, weight=1)

solve_frame = ttk.Frame(root, padding=(0, 10))
solve_frame.grid(
    row=1, column=1, padx=0, pady=(20, 0), sticky="nsew"
)

answer_frame = ttk.LabelFrame(root, text="Ответ", padding=(20, 10))
answer_frame.grid(
    row=2, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(2):
    answer_frame.rowconfigure(index=index, weight=1)

def y(x):
    return 0 * x
fig = plotting.plotting(y, 0, 0)
graph_canvas = FigureCanvasTkAgg(fig, master = graph_frame)
graph_canvas.draw()
graph_canvas.get_tk_widget().grid(row = 0, column = 0)

equation_frame = ttk.Frame(conditions_frame)
equation_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)
equation_image = tk.PhotoImage(file='gfx/equation.png')
equation_label = ttk.Label(equation_frame, image=equation_image)
equation_label.grid(
    row=0, column=0, sticky='nsew'
)

phi_frame = ttk.Frame(conditions_frame)
phi_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
phi_label = ttk.Label(phi_frame, text="phi = ")
phi_label.grid(
    row=0, column=0, sticky='nsew'
)
phi_var = tk.DoubleVar(value=220)
phi_entry = ttk.Entry(phi_frame, textvariable=phi_var)
phi_entry.grid(
    row=0, column=1, sticky='nsew'
)
phi_unit_label = ttk.Label(phi_frame, text="В")
phi_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

optionmenu_frame = ttk.Frame(conditions_frame)
optionmenu_frame.grid(
    row=2, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
optionmenu_list = ["", "Решение встроенной функцией", "Решение реализованной функцией"]
optionmenu_var = tk.StringVar(value=optionmenu_list[1])
optionmenu = ttk.OptionMenu(
    optionmenu_frame, optionmenu_var, *optionmenu_list
)
optionmenu.config(width = 33)
optionmenu.grid(
    row=0, column=0, sticky='nsew'
)

def solve_command():
    phi = phi_entry.get()
    T = 1.7 * np.power(10.0, -6)

    if optionmenu_var.get() == "Решение встроенной функцией":
        alpha = built_in_integration.alpha()

    if optionmenu_var.get() == "Решение реализованной функцией":
        alpha = my_integration.alpha()

    I_m = equation.I_m(alpha, phi)

    y = lambda x: equation.i(x, I_m)
    fig = plotting.plotting(y, 0, T)
    graph_canvas = FigureCanvasTkAgg(fig, master = graph_frame)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().grid(row = 0, column = 0)

    I_m = round(I_m, 3)
    I_m_var.set(I_m)


solve_button = ttk.Button(
    solve_frame, text="Решить", style="Accent.TButton", command=solve_command
)
solve_button.config(width=30)
solve_button.grid(row=0, column=0, padx=(250, 0), sticky="nsew")

I_m_frame = ttk.Frame(answer_frame)
I_m_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
I_m_label = ttk.Label(I_m_frame, text="I_m = ")
I_m_label.grid(
    row=0, column=0, sticky='nsew'
)
I_m_var = tk.DoubleVar(value=0)
I_m_entry = ttk.Entry(I_m_frame, state="readonly", textvariable=I_m_var)
I_m_entry.grid(
    row=0, column=1, sticky='nsew'
)
I_m_unit_label = ttk.Label(I_m_frame, text="А")
I_m_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()