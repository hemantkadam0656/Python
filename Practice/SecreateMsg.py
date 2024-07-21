from tkinter import Tk
from tkinter import messagebox
import base64
import os


class message:
    def __init__(self,master):
        master.title("MessageBox")
        master.geometry("400x400")


root = Tk()
message(root)
root.mainloop()