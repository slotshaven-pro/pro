import customtkinter as ctk
from datetime import datetime, date

def calculate_days():
    try:
        target = datetime.strptime(date_entry.get(), "%Y-%m-%d").date()
        delta = (target - date.today()).days
        result_label.configure(text=f"{delta} day(s)")
    except ValueError:
        result_label.configure(text="Invalid date")

# Appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Main window
app = ctk.CTk()
app.title("Days Until")
app.resizable(False, False)

# Layout
ctk.CTkLabel(app, text="Target date (YYYY-MM-DD):").grid(
    row=0, column=0, padx=10, pady=10, sticky="e"
)

date_entry = ctk.CTkEntry(app, width=140)
date_entry.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(app, text="Days until:").grid(
    row=1, column=0, padx=10, pady=10, sticky="e"
)

result_label = ctk.CTkLabel(app, text="", width=140, anchor="w")
result_label.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(app, text="Calculate", command=calculate_days).grid(
    row=2, column=0, padx=10, pady=15
)

ctk.CTkButton(app, text="Exit", command=app.destroy).grid(
    row=2, column=1, padx=10, pady=15
)

# Event loop
app.mainloop()
