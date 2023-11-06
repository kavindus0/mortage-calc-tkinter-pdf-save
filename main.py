import math
import time
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

import numpy as np
from fpdf import FPDF


def listOfReport(principalEntry, annualEntry, timeEntry):
    principalEntry = float(principalEntry.get())
    annualEntry = float(annualEntry.get())
    timeEntry = int(timeEntry.get())

    loanAmountForFinal = principalEntry

    monthlyInterest = annualEntry / 100 / 12
    numberOfPayments = timeEntry * 12
    mathPower = math.pow(1 + monthlyInterest, numberOfPayments)
    monthlyPayment = principalEntry * (monthlyInterest * mathPower / (mathPower - 1))
    finalAns = round(monthlyPayment, 2)
    term = 1
    store = []
    while term <= numberOfPayments:
        principalEntry -= finalAns
        if principalEntry < 0:
            break
        store.append(round(principalEntry, 2))
        term += 1

    # pdf Work

    pdf = FPDF()
    pdf.add_page()

    pdf.image('calc.png', 100, 180, 100, 100)

    # Set the font and text color

    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0, 0, 0)

    # Get current date and time

    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y   %H:%M:%S", named_tuple)
    time_string_for_name = time.strftime("%m_%d_%Y_%H_%M_%S", named_tuple)

    # Write header information

    pdf.cell(200, 10, 'Mortage Calculation'.upper(), 0, 1, 'C')
    pdf.cell(200, 10, time_string, 0, 1, 'C')
    pdf.cell(200, 10, '', 0, 1, 'C')
    pdf.cell(200, 10,
             f'Monthly Payment is Rs.{round(monthlyPayment, 2)}/= for your Rs.{round(loanAmountForFinal, 2)}/='.title(),
             0, 1, 'L')
    pdf.cell(200, 10, '', 0, 1, 'C')

    # Write table header
    pdf.cell(100, 10, 'Remaining Balance', 1, 1, 'C')
    np.arange(1, len(store) + 1)

    for index, row in enumerate(store):
        pdf.cell(100, 10, f'{index + 1}               Rs. {row}/=', 1, 0, 'L')
        pdf.ln(10)

    pdf.set_font('Arial', '', 10)

    # Save PDF file
    pdf.output(name=f'report_{time_string_for_name}.pdf')


class MortCalc:

    def __init__(self, top):
        self.top = top
        top.geometry('600x400')
        top.configure(background='#73877B')
        top.title('mortgage calculator'.upper())

        font0 = 'Raleway 30 bold'
        font1 = 'Raleway 20 bold'
        fontTextFeild = '{Rupee Foredian Regular} 20 '

        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%m/%d/%Y", named_tuple)

        self.Label1 = tk.Label(master=top, text='Mortage Calculator', background='#73877B', font=font0,
                               foreground='#F5E4D7')
        self.Label1.place(relx=0.5, rely=0.045, width=407, height=55, anchor=CENTER)

        self.Label2 = tk.Label(master=top, text=time_string, background='#73877B', font=font1, foreground='#F5E4D7')
        self.Label2.place(relx=0.5, rely=0.145, width=407, height=35, anchor=CENTER)

        seperator = ttk.Separator(root, orient='horizontal')
        seperator.place(relx=0.5, rely=0.2, anchor=CENTER, width=900, height=10)

        self.Label3 = tk.Label(master=top, text='Principal', background='#73877B', font=font1, foreground='#F5E4D7',
                               anchor='w')
        self.Label3.place(rely=0.3, relx=0.032, width=407, height=40)

        principalEntry = tk.Entry(root, background='#E5D1D0', font=fontTextFeild)
        principalEntry.place(relx=0.5, rely=0.3, width=290, height=38)

        self.Label3 = tk.Label(master=top, text='Annual Interest Rate', background='#73877B', font=font1,
                               foreground='#F5E4D7', anchor='w')
        self.Label3.place(rely=0.4, relx=0.032, width=407, height=40)

        annualEntry = tk.Entry(root, background='#E5D1D0', font=fontTextFeild)
        annualEntry.place(relx=0.5, rely=0.4, width=290, height=38)

        self.Label3 = tk.Label(master=top, text='Period (Years)', background='#73877B', font=font1,
                               foreground='#F5E4D7', anchor='w')
        self.Label3.place(rely=0.5, relx=0.032, width=407, height=40)

        timeEntry = tk.Entry(root, background='#E5D1D0', font=fontTextFeild)
        timeEntry.place(relx=0.5, rely=0.5, width=290, height=38)

        self.Button01 = tk.Button(height=2, width=20, command=lambda: [tkinter.messagebox.showinfo("Successfully",
                                                                                                   "View " + " Detailed " + "Payments.".title()),
                                                                       self.calculateF(principalEntry, annualEntry,
                                                                                       timeEntry),
                                                                       listOfReport(principalEntry, annualEntry,
                                                                                    timeEntry)], text='CALCULATE',
                                  font='{Swis721 Blk BT Black} 12', background='#BDBBB6')

        self.Button01.place(relx=0.3, rely=0.628)
        self.sum_label = tk.Label(root, background='#73877B')
        self.sum_label.place(rely=0.8, relx=0.1, width=507, height=40)

    def calculateF(self, principalEntry, annualEntry, timeEntry):

        try:
            principalEntry = float(principalEntry.get())
            annualEntry = float(annualEntry.get())
            timeEntry = int(timeEntry.get())

            monthlyInterest = annualEntry / 100 / 12
            numberOfPayments = timeEntry * 12
            mathPower = math.pow(1 + monthlyInterest, numberOfPayments)
            monthlyPayment = principalEntry * (monthlyInterest * mathPower / (mathPower - 1))

            finalAns = round(monthlyPayment, 2)
            self.sum_label.config(text="monthly payment: Rs".title() + str(finalAns) + '/=',
                                  font='{Swis721 Blk BT Black} 20')
        except:
            self.sum_label.config(text='Please Enter Valid Data', font='{Swis721 Blk BT Black} 22')


if __name__ == '__main__':
    root = tk.Tk()
    img = PhotoImage(file='calc.png')
    root.iconphoto(False, img)
    MortCalc(root)
    mainloop()
