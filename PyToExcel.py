import os
import tkinter as tk
from tkinter import filedialog
from pandas import *
import openpyxl

# Globals
DEFAULT_PATH = ""

# Creates a spreadsheet formatted for a Bartender UNIT label
def print_case_ss(gtin, serial, batch, expiration):
    # Vars Here
    bt_headers = ["GTIN", "Serial #", "Batch/Lot", "Expiration"]
    data_vals = [gtin, serial, batch, expiration]
    df = DataFrame([data_vals], columns=bt_headers)

    file_path = get_save_path()

    # Print if name obtained
    if file_path:
        df.to_excel(file_path, sheet_name= "Case Label Info")

# Open file dialogue and return valid path, return fail condition (-1) otherwise
def get_save_path():
    file_path = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension=".xlsx")
    return file_path