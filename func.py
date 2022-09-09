from distutils.command.config import config
from distutils.log import info
import time
from tkinter import *  
from selenium import webdriver
from selenium.webdriver.common.by import By
from functools import partial
import subprocess, shutil
import os
import fnl_support as GuiFnl
import fnl as Fnl


class files_cop:
    def file_handle_read(path, name):
        f = open(str(name) , 'r')
        print(f.readlines())
        f.close()
    def file_handle_write(name, data):
        f = open(str(name) , 'w')
        f.writelines(data)
        f.close()
# files_cop.file_handle_read('','')

def copy_driver():
    source = "./msedgedriver.exe"
    destination = "C:/Program Files (x86)/"
    dest = shutil.copy(source, destination)
    print(dest)
    if dest != '':
        conf = str(dest[0:22])
        if conf == "C:/Program Files (x86)/":
            print("Destination path -> ", dest)
            return True
        return False
    return False    

def cred(usn, psw):
   username = usn.get() 
   password = psw.get()
   print(username, password)
    #web_drivings(username, password)
   return username, password

def saveFile(data):
    file = open('ssh-creds.txt', 'w')
    file.writelines(str(data))
    file.close()

def Gui():
    GuiFnl.main()
    # Fnl.Toplevel1.cred()

def web_drivings(uname, passW):
    PATH = 'C:\Program Files (x86)\msedgedriver.exe'
    web = webdriver.Edge(PATH)
    url = 'https://www.speedssh.com/create-ssh-server-30-days/132/ssh-server-sg-2-30-days'
    web.get(url)

    time.sleep(2)

    username = web.find_element(By.XPATH, '//*[@id="user"]')
    username.send_keys(uname)
 
    password = web.find_element(By.XPATH, '//*[@id="pass"]')
    password.send_keys(passW)

    regBtn = web.find_element(By.XPATH, '//*[@id="submit"]')
    regBtn.click()

    time.sleep(2)
    info = web.find_element(By.XPATH, '//*[@id="report"]').text
    if info != "":
        return info

def saveF(info):
    if info != "":
        print(info)
        time.sleep(1)
        checker = (info[0:44])
        if checker == 'Your Account has been successfully created !':
            data = [info]
            file = open('ssh-creds.txt', 'w')
            file.writelines(str(info))
            file.close()
            return data
    