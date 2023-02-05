import io
import tkinter
from tkinter import filedialog
import os
import sys

def readFile(file: io.TextIOWrapper):
    order_dict = {}
    """
    :param file:
    :return: dictionary with all keys and values read in
    """
    for line in file:
        spl_line = line.split(",")
        order_dict.update({spl_line[0] : spl_line[1]})
    return order_dict



def getFile():
    """
    :return: file object selected by user
    """
    # create window for file searching
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currDir = os.getcwd()
    currFile = filedialog.askopenfile(parent=root, initialdir=currDir, title='Please select a file.', filetypes=[("CSV files", "*.csv")])

    # Check for empty input
    if currFile:
        return currFile
    else:
        return -1