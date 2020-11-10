import tkinter as tk
# make the root widget
root = tk.Tk()

# creating a label widget
myLabel1 = tk.Label(root, text="Hello World")
myLabel2 = tk.Label(root, text="Blablablabla")
# showing it with the grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


# event loop
root.mainloop()
