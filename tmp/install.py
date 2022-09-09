import subprocess, shutil
import os

# to = "./tmp"
# file = "msedgedriver.exe"
# process = "cp ..{} ..{}".format(to,file)
# subprocess.run(process, shell=True)

# to = "/tmp/"
# file = "/msedgedriver.exe"
# process = "copy .{} .{}".format(file, to)
# print(process)
# prnt = os.system(process)
# print(prnt)


# path = 'D:/NK/Python Programe/web auto filler and submitter'

# print("Before copying file:")
# print(os.listdir(path))

# def copy_driver():
#     source = "./msedgedriver.exe"

#     destination = "C:/Program Files (x86)/"

#     dest = shutil.copy(source, destination)
#     if dest != '':
#         print("Destination path -> ", dest)


import time
from tkinter import *  
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import partial
import subprocess, shutil
import os


# class files_cop:
#     def file_handle_read(path, name):
#         f = open(str(name) , 'r')
#         print(f.readlines())
#         f.close()
#     def file_handle_write(name, data):
#         f = open(str(name) , 'w')
#         f.writelines(data)
#         f.close()
# # files_cop.file_handle_read('','')

# parent = Tk()
# parent.title('SSH-cridentials gene')
# parent.geometry('500x300')

# def valdLogin(uname, passW):
#     print("username entered :", uname.get())
#     print("password entered :", passW.get())
#     return

# Label(parent, text="Username: ").grid(row=0, column=0)
# username = StringVar()
# username = Entry(parent).grid(row=0, column=1)

# Label(parent, text="Password: ").grid(row=1, column=0)
# password = Entry(parent).grid(row=1, column=1)

# validateLogin = partial(valdLogin, username, password)
# submit = Button(parent, text = "Submit", command=validateLogin).grid(row = 4, column = 0)  

# parent.mainloop()

def copy_driver():
    source = "./msedgedriver.exe"

    destination = "C:/Program Files (x86)/"

    dest = shutil.copy(source, destination)
    if dest != '':
        print("Destination path -> ", dest)
        return True
    return False    

def Gui():
    parent = Tk()
    parent.title('SSH-cridentials gene')
    parent.geometry('500x300')
    def valdLogin(uname, passw):
        print("username entered :", uname.get())
        print("password entered :", passw.get())
        return

    Label(parent, text="Username: ").grid(row=0, column=0)
    username = StringVar()
    username = Entry(parent).grid(row=0, column=1)

    Label(parent, text="Password: ").grid(row=1, column=0)
    password = StringVar()
    password = Entry(parent, show='*').grid(row=1, column=1)

    validateLogin = partial(valdLogin, username, password)
    submit = Button(parent, text = "Submit", command=validateLogin).grid(row = 4, column = 0)  
    submitCp = Button(parent, text = "Copy Drivers", command=copy_driver).grid(row = 6, column = 0) 
    # print(submit, submitCp)
    parent.mainloop()

Gui()
