import tkinter as tk
import os
# pip install PIL
from PIL import ImageTk, Image

# config
dirname = os.path.dirname(__file__)
iconPath = os.path.join(dirname, 'icon.ico')
imagePath = os.path.join(dirname, 'examplekaart.png')

# make the root widget
root = tk.Tk()
root.title('Super awesome app')
# program icon on titlebar
root.iconbitmap(iconPath)

my_img = ImageTk.PhotoImage(Image.open(imagePath))
my_label = tk.Label(image=my_img)
my_label.pack()


button_quit = tk.Button(root, text="Exit program", command=root.quit)
button_quit.pack()

# event loop
root.mainloop()
