### images.py

import tkinter
from PIL import Image,ImageTk

root = tkinter.Tk()

img = Image.open('sasha.jpg')
pix = ImageTk.PhotoImage(img)
label = tkinter.Label(root,image=pix)
label.pack(side='left')
root.title('Sasha')

root.mainloop()

