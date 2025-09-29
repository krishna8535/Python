import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Greeting", "Hello from GUI!")

root = tk.Tk()
root.title("Sample GUI")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=20)

root.mainloop()

