from tkinter import *
from tkinter import ttk

def convert_currency():
    amount = float(entry_amount.get())
    selected_currency = currency.get()

    if selected_currency == "USD":
        result = amount * 0.024
    elif selected_currency == "EUR":
        result = amount * 0.023
    elif selected_currency == "CZK":
        result = amount * 0.57
    else:
        label_result.config(text="Выберите валюту!")
        return

    label_result.config(text=f"Результат: {result:.2f} {selected_currency}")

root = Tk()
root.geometry('400x300')
root.title("Калькулятор валют")
Label(root, text="Сумма в гривнах:").pack()
entry_amount = Entry(root)
entry_amount.pack()
Label(root, text="Выберите валюту:").pack()
currency = ttk.Combobox(root, values=["USD", "EUR", "CZK"])
currency.pack()
Button(root, text="Конвертировать", command=convert_currency).pack()
label_result = Label(root, text="Результат: ")
label_result.pack()
root.mainloop()
