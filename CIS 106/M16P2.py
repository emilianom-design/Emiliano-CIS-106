import tkinter as tk
from tkinter import messagebox
import math
import os

room_paint_data = {}

def calculate_and_save():
    room = entry_room.get()
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter numeric values.")
        return

    area = 2 * height * (length + width)
    gallons = math.ceil(area / 50)
    room_paint_data[room] = gallons

    result_text = f"{'Room':<10} {'Gallons':>10}\n"
    for r, g in room_paint_data.items():
        result_text += f"{r:<10} {g:>10}\n"

    result_label.config(text=result_text)

    with open("paint_results.txt", "a") as file:
        file.write(f"{room},{gallons}\n")

root = tk.Tk()
root.title("Room Paint Estimator with Save")

tk.Label(root, text="Room Name:").grid(row=0, column=0)
tk.Label(root, text="Length (ft):").grid(row=1, column=0)
tk.Label(root, text="Width (ft):").grid(row=2, column=0)
tk.Label(root, text="Height (ft):").grid(row=3, column=0)

entry_room = tk.Entry(root)
entry_length = tk.Entry(root)
entry_width = tk.Entry(root)
entry_height = tk.Entry(root)

entry_room.grid(row=0, column=1)
entry_length.grid(row=1, column=1)
entry_width.grid(row=2, column=1)
entry_height.grid(row=3, column=1)

tk.Button(root, text="Calculate and Save", command=calculate_and_save).grid(row=4, columnspan=2)

result_label = tk.Label(root, text="", font=("Courier", 12), justify=tk.LEFT)
result_label.grid(row=5, columnspan=2)

root.mainloop()
