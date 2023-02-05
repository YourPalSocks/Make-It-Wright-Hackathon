"""
Prompt user for a file, read the file,
then parse and return data.
"""

import io
import tkinter
from tkinter import filedialog
import os


def readFile(file: io.TextIOWrapper):
    """
    :param file:
    create text file with given csv file
    """

    with open(file.name, 'r') as f:
        with open("order.txt", "w") as w:
            for line in f:
                info = line.split(",")
                # strip values of newlines, etc...
                w.write(f"{info[0]} : {info[1]}")


def getFile():
    """
    :return: file object selected by user
    """
    # create window for file searching
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currDir = os.getcwd()
    currFile = filedialog.askopenfile(parent=root, initialdir=currDir, title='Please select a file.')

    if currFile:
        print(f"You chose {currFile}")

    return currFile


file = getFile()
data = readFile(file)
