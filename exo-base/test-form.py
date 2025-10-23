#
import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "Hello, John! This is an information message.")

def click():
    messagebox.showwarning("Warning", "Warning: You have not clicked the button yet.")

window = tk.Tk()
window.title("Message Box Example")
window.geometry("300x200")
button = tk.Button(window, text="Show Message", command=show_message)
button2 = tk.Button(window, text="Click", command=click)
label = tk.Label(window, text="Hello, World!")


button.pack()
button2.pack()
label.pack()
window.mainloop()