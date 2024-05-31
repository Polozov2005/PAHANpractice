import tkinter as tk
from tkinter import ttk
from ctypes import windll
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

equation_u_frame = ttk.Frame(conditions_frame)
equation_u_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)
equation_u_image = tk.PhotoImage(file='gfx/u.png')
equation_u_label = ttk.Label(equation_u_frame, image=equation_u_image)
equation_u_label.grid(
    row=0, column=0, sticky='nsew'
)

equation_U_frame = ttk.Frame(conditions_frame)
equation_U_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
equation_U_image = tk.PhotoImage(file='gfx/u_sqrt.png')
equation_U_label = ttk.Label(equation_U_frame, image=equation_U_image)
equation_U_label.grid(
    row=0, column=0, sticky='nsew'
)

f_frame = ttk.Frame(conditions_frame)
f_frame.grid(
    row=2, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
f_label = ttk.Label(f_frame, text="f = ")
f_label.grid(
    row=0, column=0, sticky='nsew'
)
f_var = tk.DoubleVar(value=50)
f_entry = ttk.Entry(f_frame, textvariable=f_var)
f_entry.grid(
    row=0, column=1, sticky='nsew'
)
f_unit_label = ttk.Label(f_frame, text="Гц")
f_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

U_frame = ttk.Frame(conditions_frame)
U_frame.grid(
    row=3, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
U_label = ttk.Label(U_frame, text="U = ")
U_label.grid(
    row=0, column=0, sticky='nsew'
)
U_var = tk.DoubleVar(value=220)
U_entry = ttk.Entry(U_frame, textvariable=U_var)
U_entry.grid(
    row=0, column=1, sticky='nsew'
)
U_unit_label = ttk.Label(U_frame, text="В")
U_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

optionmenu_frame = ttk.Frame(conditions_frame)
optionmenu_frame.grid(
    row=4, column=0, padx=10, pady=(20, 10), sticky='nsew'
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
    f = f_entry.get()
    U = U_entry.get()

    if optionmenu_var.get() == "Решение встроенной функцией":
        alpha = built_in_integration.alpha(f)

    if optionmenu_var.get() == "Решение реализованной функцией":
        alpha = my_integration.alpha(f)

    T = equation.T(f)

    U_0 = equation.U_0(alpha, U)

    y = lambda x: equation.u(x, f, U_0)
    fig = plotting.plotting(y, 0, T)
    graph_canvas = FigureCanvasTkAgg(fig, master = graph_frame)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().grid(row = 0, column = 0)

    T = round(T, 3)
    T_var.set(T)

    U_0 = round(U_0, 3)
    U_0_var.set(U_0)

solve_button = ttk.Button(
    solve_frame, text="Решить", style="Accent.TButton", command=solve_command
)
solve_button.config(width=30)
solve_button.grid(row=0, column=0, padx=(250, 0), sticky="nsew")

T_frame = ttk.Frame(answer_frame)
T_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
T_label = ttk.Label(T_frame, text="T = ")
T_label.grid(
    row=0, column=0, sticky='nsew'
)
T_var = tk.DoubleVar(value=0)
T_entry = ttk.Entry(T_frame, state="readonly", textvariable=T_var)
T_entry.grid(
    row=0, column=1, sticky='nsew'
)
T_unit_label = ttk.Label(T_frame, text="с")
T_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

U_0_frame = ttk.Frame(answer_frame)
U_0_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
U_0_label = ttk.Label(U_0_frame, text="U_0 = ")
U_0_label.grid(
    row=0, column=0, sticky='nsew'
)
U_0_var = tk.DoubleVar(value=0)
U_0_entry = ttk.Entry(U_0_frame, state="readonly", textvariable=U_0_var)
U_0_entry.grid(
    row=0, column=1, sticky='nsew'
)
U_0_unit_label = ttk.Label(U_0_frame, text="В")
U_0_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()