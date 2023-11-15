import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re

#We used a class because the values are gonna get used often. (Also makes it look neat)
#I should try this often.
class currency_converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    #Since we're basing it on USD, we first convert it into USD if it isn't,
    #then convert it to target currency
    def convert(self, original_currency, target_currency, amount):
        initial_amount = amount

        #Convert it into USD if it isn't originally USD
        if original_currency != "USD":
            amount = amount / self.currencies[original_currency]

        #Converts the amout to the target currency, and
        #Rounds up the amount to the specified value
        amount = round(amount * self.currencies[target_currency], 4)

        return amount


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.converter_call = converter

        self.geometry("500x200")

        # Label
        self.intro_label = Label(self, text='Currency Converter', fg='blue', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)


        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("INR")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.converter_call.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.converter_call.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)


        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        # self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x=346, y=150)

        # Convert button
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)


    #Performs tasks on button press
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.converter_call.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))



    #Restricts the text box to only digits
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = currency_converter(url)

    App(converter)
    mainloop()

