import tkinter as tk
# make the root widget
root = tk.Tk()

e = tk.Entry(root, width=50, borderwidth=10)
e.pack()
e.insert(0, "Enter your name")


def myClick():
    myLabel = tk.Label(root, text=e.get())
    myLabel.pack()


myButton = tk.Button(root, text="Enter your name", padx="50",
                     pady="50", state="active", command=myClick)
myButton.pack()

# event loop
root.mainloop()
