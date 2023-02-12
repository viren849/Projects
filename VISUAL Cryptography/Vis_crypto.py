import aes
import simple_xor as simp

from tkinter import *
import tkinter as tk

from tkinter.filedialog import *
import tkinter.messagebox
from PIL import Image,ImageTk

import os
from pathlib import Path

def pass_alert():
   tkinter.messagebox.showinfo("Password Alert","Please enter a password and select a method")


def select_method(a,b,c,key,filename,file_path_e,method):
    if a == 1 and method == "enc":
        simp.encrypt(c,filename, key,file_path_e)
    elif a == 1 and method == "dec":
        simp.decrypt(c,filename, key,file_path_e,"")
    elif b == 1 and method == "enc":
        aes.aes_encrypt(c,key, file_path_e, filename,"")
    elif b == 1 and method == "dec":
        aes.aes_decrypt(c,key, file_path_e, filename)
    elif c == 1 and method == "enc":
        simp.encrypt(c,filename, key, file_path_e)
    else:
        aes.aes_decrypt(c,key, file_path_e, filename)

def func(method):
    a=var1.get()
    b=var2.get()
    c=var3.get()

    global file_path_e
    pas = passg.get()
    if pas == "" or (a == 0 and b == 0 and c == 0):
        pass_alert()
    else:
        # LOAD THE IMAGE
        filename = tkinter.filedialog.askopenfilename()
        file_path_e = os.path.dirname(filename)

        select_method(a,b,c,pas,filename,file_path_e,method)



parent=tk.Tk()
parent.geometry("800x500")

parent.resizable(0,0)

parent.title("Encryption/Decryption")

title="Image Encryption / Decryption"

msgtitle=Message(parent,text=title)
msgtitle.config(font=('helvetica',25,'bold'),width=600)
msgtitle.pack()

sp="-------------------------------------------------------------------------------------"
sp_title=Message(parent,text=sp)
sp_title.config(font=('arial',12,'bold'),width=650)
sp_title.pack()


passlabel = Label(parent, text="Enter Encryption/Decryption Key:")
passlabel.pack()

passg = Entry(parent, show="*", width=50)
passg.config(highlightthickness=2,highlightbackground="blue",)
passg.pack()

lbl = Label(text = "Choose Encryption/Decryption Methods :")
lbl.config(font=(13))
lbl.place(x=200,y=140)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
btn1 = Checkbutton(parent, text="XOR ", variable=var1, onvalue=1, offvalue=0, height=2,width=10)
btn2 = Checkbutton(parent, text="AES", variable=var2, onvalue=1, offvalue=0, height=2,width=10)
btn3 = Checkbutton(parent, text="Both", variable=var3, onvalue=1, offvalue=0, height=2,width=10)
btn1.place(x=300,y=200)
btn2.place(x=300,y=240)
btn3.place(x=300,y=290)

encrypt=Button(parent,text="ENCRYPT",width=20,height=3,command=lambda :func("enc"))
encrypt.place(x=60,y=350)
decrypt=Button(parent,text="DECRYPT",width=20,height=3,command=lambda :func("dec"))
decrypt.place(x=550,y=350)

name="Done by: Virender Kumar"
msg=Message(parent,text=name)
msg.config(font=('helvetica',20,'bold'),width=600)
msg.place(x=200,y=405)

parent.mainloop()
