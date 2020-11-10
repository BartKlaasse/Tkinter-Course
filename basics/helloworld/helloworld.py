import tkinter as tk
# make the root widget
root = tk.Tk()

# creating a label widget
myLabel = tk.Label(root, text="Hello World")
# Shoving the widget onto the screen
myLabel.pack()


# event loop
root.mainloop()
