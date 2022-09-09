from msilib.schema import ListBox
from tkinter import messagebox
import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import *
import tkinter as tk
from functools import partial

# uname = input('Enter a username: ')
# passW = input('Enter a password: ')

# PATH = 'C:\Program Files (x86)\msedgedriver.exe'
# web = webdriver.Edge(PATH)
# url = 'https://www.clientam.com/sso/Login'
# web.get(url)

# time.sleep(2)

# username = web.find_element(By.XPATH, '//*[@id="user_name"]')
# username.send_keys(uname)

# password = web.find_element(By.XPATH, '//*[@id="password"]')
# password.send_keys(passW)

# logBtn = web.find_element(By.XPATH, '//*[@id="submitForm"]')
# logBtn.click()

# time.sleep(2)

# info = web.find_element(By.XPATH, '//*[@id="ERRORMSG"]').text

# if info != "":
#     print(info)

# # if info != "":
# #     getInf = web.find_element_by_xpath('//*[@id="report"]/b')
# #     getInfo = getInf.text
# #     print(getInfo)

# # print(info)

# open the file for write operation
# f = open('hello.txt' , 'w')
# #writes the new content
# f.write('Tutorialspoint')
# #close the file
# f.close()
# # again open the file for read
# f = open('hello.txt' , 'r')
# #reads the file content and prints in console
# print(f.read())
# #close the file
# f.close()

# info = ('please support our site. if you think this site is useful for you. We are Provider Premium SSH Account Dropbear port 443,143,80, and SSH SSL 443. SSH or Secure Shell is a network protocol that allows the exchange of data via a secure channel between two network devices. Many')
# for data in info:
#     newData = [data]
# if info != "":
#     print(info)
#     time.sleep(1)
#     checker = (info[0:66])
#     print(checker, "\n", newData)
#     if checker == 'please support our site. if you think this site is useful for you.':
#         file = open('ssh-creds.txt', 'w') 
#         # data = [info]
#         file.write(str(info))
#         file.close()

parent = Tk()
parent.geometry("300x200")
parent.title('SSH-creadentials builder tool.')

def valdLogin(uname, passW):
    print("username entered :", uname.get())
    print("password entered :", passW.get())
    return

Label(parent, text="Username: ").grid(row=0, column=0)
username = StringVar()
username = Entry(parent).grid(row=0, column=1)

Label(parent, text="Password: ").grid(row=1, column=0)
password = Entry(parent).grid(row=1, column=1)

validateLogin = partial(valdLogin, username, password)
submit = Button(parent, text = "Submit", command=validateLogin).grid(row = 4, column = 0)  

# if submit != "":
#     print(submit)

parent.mainloop()


# window
# tkWindow = Tk()  
# tkWindow.geometry('400x150')  
# tkWindow.title('Tkinter Login Form - pythonexamples.org')

# def validateLogin(username, password):
# 	# print("username entered :", username.get())
# 	# print("password entered :", password.get())
#     listBx = Listbox(tkWindow)
#     listBx.insert(1, ("username entered :"))
#     listBx.insert(2, ("password entered :"))
#     return

# #username label and text entry box
# usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = StringVar()
# usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

# validateLogin = partial(validateLogin, username, password)

# #login button
# loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

# tkWindow.mainloop()

# window = tk.Tk()
# window.title('My Window')
 
# window.geometry('500x300')
 
# var1 = tk.StringVar()
# l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=var1)
# l.pack()
 
# def print_selection():
#     value = lb.get(lb.curselection())   
#     var1.set(value)  
 
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
 
# var2 = tk.StringVar()
# var2.set((1,2,3,4))
# lb = tk.Listbox(window, listvariable=var2)

# list_items = [11,22,33,44]
# for item in list_items:
#     lb.insert('end', item)
# lb.insert(1, 'first')
# lb.insert(2, 'second')
# lb.delete(2)
# lb.pack()
 
# window.mainloop()