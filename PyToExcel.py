import os
import tkinter as tk
from tkinter import filedialog
from pandas import *
import openpyxl

# Creates a spreadsheet formatted for a Bartender UNIT label
# Data expectation:
# GTIN: One flow of numbers (10810055939197)
# Serial: One flow of alphanumeric (string or int) ("1QH001005")
# Batch/Lot: One flow of alphanumeric (string or int) ("TRT001")
# Date: YYMMDD
def print_case_ss(gtin, serial, batch, expiration, sscc):
    # Vars Here
    bt_headers = ["GTIN", "Serial #", "Batch/Lot", "Expiration", "GS1 Element", "SSCC"]
    gs1_string = create_dsgtin_element_string(expiration, gtin, serial, batch)
    data_vals = [gtin, serial, batch, expiration, gs1_string, sscc]
    df = DataFrame([data_vals], columns=bt_headers)

    file_path = get_save_path()

    # Print if name obtained
    if file_path:
        df.to_excel(file_path, sheet_name= "Case Label Info")


# Open file dialogue and return valid path, return fail condition (-1) otherwise
def get_save_path():
    file_path = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension=".xlsx", initialdir=os.getcwd())
    return file_path

# Creates DSGTIN+ GS1 element string from date, gtin, serial, batch/lot
def create_dsgtin_element_string(date, gtin, serial, batch_lot):
    ret = ""
    ret += "(17)" + str(date) + "(01)" + str(gtin) + "(21)" + str(serial) + "(10)" + str(batch_lot)
    # Remove any new line codes
    if ret.__contains__("\n"):
        ret = ret.replace("\n", "")
    return ret