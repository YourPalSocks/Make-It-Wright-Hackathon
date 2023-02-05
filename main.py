import os
import random
import tkinter as tk
from tkinter import *
from datetime import date

from PyToExcel import *
from CsvToPy import *

order_dict = {}

def find_csv_file():
    global order_dict

    file = getFile()
    if file == -1:
        print("Uh oh")
    else:
        order_dict = readFile(file)
        export_spreadsheet(order_dict)

def export_spreadsheet(order_dict):
    today = date.today().strftime("%y%b")

    # Element variables
    gtin = ""
    expiration = ""
    batch = ""
    sscc = ""
    serial = "179CPM" # Constant used for serial, but can be replaced by whatever generation system

    # Pull out GTIN and Expiration
    gtin = order_dict["Case GTIN"]
    expiration = format_expiration_date(order_dict["Expiration"])
    sscc = order_dict["SSCC"]
    # Generate Serial and Batch/Lot
    batch = str(today) + expiration
    print_case_ss(gtin, serial, batch, expiration, sscc)
    

def format_expiration_date(date):
    # Format MM-DD-YY into YYMMDD
    broken_string = []
    result = ""

    # Remove any new line chars
    if date.__contains__("\n"):
        date = date.replace("\n", "")

    if date.__contains__("-"):
        broken_string = date.split("-")
    else: # Assuming using backslashes
        broken_string = date.split("/")
    result = broken_string[2] + broken_string[0] + broken_string[1]
    return result


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.resizable(False, False)
    window.geometry("250x250")
    window.title("TITLE HERE")
    # Set up button
    input = Button(window, text="CSV to Bartender Excel", command=find_csv_file)
    # Pack
    input.pack(expand=1)
    # Run loop
    window.mainloop()