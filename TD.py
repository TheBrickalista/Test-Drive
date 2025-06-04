import tkinter as tk

root = tk.Tk()
root.title("Test Drive")
root.configure(bg="#3498db")

label = tk.Label(
    root,
    text="Test Drive",
    font=("Helvetica", 24, "bold"),
    bg="#3498db",
    fg="white"
)
label.pack(expand=True)
root.geometry("400x200")
root.mainloop()
