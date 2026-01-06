import tkinter as tk
from datetime import datetime, date

def calculate_days():
    try:
        target = datetime.strptime(date_entry.get(), "%Y-%m-%d").date()
        delta = (target - date.today()).days
        result_var.set(f"{delta} day(s)")
    except ValueError:
        result_var.set("Invalid date")

# Main window
root = tk.Tk()
root.title("Days Until2")
root.resizable(False, False)

# Variables
result_var = tk.StringVar(value="")

# Layout
tk.Label(root, text="Target date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(root, width=14)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Days until:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, textvariable=result_var, width=15, anchor="w").grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=calculate_days).grid(row=2, column=0, padx=5, pady=10)
tk.Button(root, text="Exit", command=root.destroy).grid(row=2, column=1, padx=5, pady=10)

# Event loop
root.mainloop()
