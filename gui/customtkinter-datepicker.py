from datetime import date, datetime

import customtkinter as ctk

try:
    from tkcalendar import DateEntry
except ImportError as exc:
    raise SystemExit(
        "tkcalendar is required for the date picker. Install with: pip install tkcalendar"
    ) from exc


def main():
    # Appearance
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Main window
    app = ctk.CTk()
    app.title("CustomTkinter Date Picker")
    app.resizable(False, False)

    result_var = ctk.StringVar(value="")

    # Layout container
    frame = ctk.CTkFrame(app)
    frame.grid(padx=16, pady=16)

    ctk.CTkLabel(frame, text="Target date:").grid(
        row=0, column=0, padx=(0, 10), pady=8, sticky="e"
    )

    # tkcalendar DateEntry works inside a CustomTkinter window
    date_picker = DateEntry(frame, dateformat="%Y-%m-%d", width=16, background="#1F6AA5")
    date_picker.grid(row=0, column=1, pady=8)

    ctk.CTkLabel(frame, text="Days until:").grid(
        row=1, column=0, padx=(0, 10), pady=8, sticky="e"
    )

    ctk.CTkLabel(frame, textvariable=result_var, width=140, anchor="w").grid(
        row=1, column=1, pady=8, sticky="w"
    )

    def calculate_days():
        target = date_picker.get_date()
        if isinstance(target, datetime):
            target = target.date()
        delta = (target - date.today()).days
        result_var.set(f"{delta} day(s)")

    ctk.CTkButton(frame, text="Calculate", command=calculate_days).grid(
        row=2, column=0, padx=8, pady=(12, 0)
    )

    ctk.CTkButton(frame, text="Exit", command=app.destroy).grid(
        row=2, column=1, padx=8, pady=(12, 0)
    )

    app.mainloop()


if __name__ == "__main__":
    main()
