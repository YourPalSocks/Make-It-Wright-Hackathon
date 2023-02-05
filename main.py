import os
import tkinter as tk
from tkinter import *

from PyToExcel import *
from CsvToPy import *

order_dict = {}

def find_csv_file():
    file = getFile()
    if file == -1:
        print("Uh oh")
    else:
        order_dict = readFile(file)
        print(order_dict["Case GTIN"])

def export_spreadsheet():
    # Element variables
    gtin = ""
    expiration = ""
    batch = ""
    serial = ""
    quantity = 0
    # Pull out GTIN and Expiration
    gtin = order_dict["Case GTIN"]
    expiration = format_expiration_date(order_dict["Expiration"])
    quantity = int(order_dict["Quantity"])
    # Generate Serial and Batch/Lot
    batch = "" # TODO: Generate random batch number
    for x in quantity:
        # Generate serial number
        print("Working on it")

def format_expiration_date(date):
    # Format MM-DD-YY into YYMMDD
    print("Working on it")


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.resizable(False, False)
    window.geometry("250x250")
    window.title("TITLE HERE")
    # Set up buttons
    input = Button(window, text="Input CSV", command=find_csv_file)
    export = Button(window, text="Output Spreadsheet", command=export_spreadsheet)
    # Pack
    input.pack(side=TOP, expand=1)
    export.pack(side=BOTTOM, expand=5)
    # Run loop
    window.mainloop()