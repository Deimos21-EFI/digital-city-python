#
import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Hello, John! This is an information message.")

window = tk.Tk()
window.title("Message Box Example")
window.geometry("300x200")
button = tk.Button(window, text="Show Message", command=show_message)
button.pack()

window.mainloop()