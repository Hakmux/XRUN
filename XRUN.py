from tkinter import *
import os

root= Tk()
root.title("XRUN")
root.iconbitmap('1.ico')
root.geometry("300x260")
root.config(bg="black")
root.resizable(False,False)

def shutdown():
 os.system("shutdown /s /t 1")

def restart():
  os.system("shutdown /r /t 5")

def logout():
 os.system("shutdown /l")
 
Label(root, text= "XRUN", font=("arial" ,30,"bold"),bg="red",).pack(pady= 30)


btn0=Button(root, text= "SHUTDOWN",width=10, height=1,font=("arial" ,10,"bold"),bg="red", command=shutdown).pack(pady= 10)
btn1=Button(root, text= "RESTART",width=10, height=1,font=("arial" ,10,"bold"),bg="red", command=restart).pack(pady= 10)
btn2=Button(root, text= "LOGOUT",width=10, height=1,font=("arial" ,10,"bold"),bg="red", command=logout).pack(pady= 10)

root.mainloop()
