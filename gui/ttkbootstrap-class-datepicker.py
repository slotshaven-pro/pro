from ttkbootstrap import Window
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.widgets import DateEntry
from datetime import date, datetime


class App(Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Days Until")
        self.resizable(False, False)

        self._create_variables()
        self._create_widgets()
        self._layout_widgets()

    def _create_variables(self):
        self.result = ttk.StringVar(value="")

    def _create_widgets(self):
        self.label_date = ttk.Label(self, text="Target date:")
        self.date_picker = DateEntry(
            self,
            bootstyle=PRIMARY,
            dateformat="%Y-%m-%d",
            width=14,
        )

        self.label_result = ttk.Label(self, text="Days until:")
        self.result_label = ttk.Label(
            self,
            textvariable=self.result,
            width=16,
            anchor=W,
        )

        self.btn_calc = ttk.Button(
            self,
            text="Calculate",
            bootstyle=SUCCESS,
            command=self.calculate_days,
        )

        self.btn_exit = ttk.Button(
            self,
            text="Exit",
            bootstyle=SECONDARY,
            command=self.destroy,
        )

    def _layout_widgets(self):
        pad = dict(padx=10, pady=8)

        self.label_date.grid(row=0, column=0, sticky=E, **pad)
        self.date_picker.grid(row=0, column=1, **pad)

        self.label_result.grid(row=1, column=0, sticky=E, **pad)
        self.result_label.grid(row=1, column=1, **pad)

        self.btn_calc.grid(row=2, column=0, **pad)
        self.btn_exit.grid(row=2, column=1, **pad)

    def calculate_days(self):
        target = self.date_picker.get_date()
        if isinstance(target, datetime):
            target = target.date()
        delta = (target - date.today()).days
        self.result.set(f"{delta} day(s)")


if __name__ == "__main__":
    app = App()
    app.mainloop()
