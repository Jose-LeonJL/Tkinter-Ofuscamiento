import customtkinter
from tkinter import *

app = customtkinter.CTk()
login_Frame = customtkinter.CTkFrame(app)

def center_window(window,width,height):

    window.update_idletasks()
    width = width
    height = height
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
