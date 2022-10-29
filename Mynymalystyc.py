from tkinter import *
from PIL import Image
from os import *

def run():
    img = Image.new(mode="RGB", size=(1000, 1000), color=ent.get())
    img.save("bgi.jpg")
    img.show()
   

root = Tk()
root.title("Mynymalystyc")
root.geometry("500x200")
root.iconbitmap("icon.ico")
root.configure(bg="black")
root.resizable(0,0)


ttl = Label(root, text = "Mynymalystyc", font =("Consolas", 35),bg="black", fg = "white")
ttl.pack()

ent = Entry(root, width=25, font= ("Consolas", 25), bg="#111111", fg = "white", border = 0,insertbackground="white")
ent.pack()

btn = Button(root, text="GO", width= 25, font =("Consolas", 25), bg="#001122", fg= "white", border=0,command=run)
btn.pack(pady=10)

root.mainloop()