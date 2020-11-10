import tkinter as tk
# make the root widget
root = tk.Tk()


def myClick():
    myLabel = tk.Label(root, text="hey i clicked")
    myLabel.pack()


myButton = tk.Button(root, text="click me", padx="50",
                     pady="50", state="active", command=myClick, fg="blue", bg="red")
myButton.pack()

# event loop
root.mainloop()
