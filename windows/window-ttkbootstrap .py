from ttkbootstrap import Window
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from datetime import datetime, date

def calculate_days():
    try:
        target = datetime.strptime(date_entry.get(), "%Y-%m-%d").date()
        delta = (target - date.today()).days
        result_var.set(f"{delta} day(s)")
    except ValueError:
        result_var.set("Invalid date")

# Main window
app = Window(themename="litera")
app.title("Days Until")
app.resizable(False, False)

# Variables
result_var = ttk.StringVar(value="")

# Layout
ttk.Label(app, text="Target date (YYYY-MM-DD):").grid(
    row=0, column=0, padx=10, pady=10, sticky=E
)

date_entry = ttk.Entry(app, width=14)
date_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(app, text="Days until:").grid(
    row=1, column=0, padx=10, pady=10, sticky=E
)

ttk.Label(app, textvariable=result_var, width=15, anchor=W).grid(
    row=1, column=1, padx=10, pady=10
)

ttk.Button(app, text="Calculate", bootstyle=PRIMARY, command=calculate_days).grid(
    row=2, column=0, padx=10, pady=15
)

ttk.Button(app, text="Exit", bootstyle=SECONDARY, command=app.destroy).grid(
    row=2, column=1, padx=10, pady=15
)

# Event loop
app.mainloop()
