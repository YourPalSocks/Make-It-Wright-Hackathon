import tkinter as tk
from tkinter import *

def main():
    root = tk.Tk()
    root.title("Order Information")

    t = Text(root)
    with open("order.txt", "r") as f:
        for line in f:
            info = line.split(":")
            info[0], info[1] = info[0].strip(), info[1].strip()

            if info[0] == "Customer":
                t.insert(END, "\n")
            t.insert(END, f"{info[0]} : {info[1]}\n")

    t.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
