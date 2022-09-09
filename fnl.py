from functools import partial
import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import func as fn



_script = sys.argv[0]
_location = os.path.dirname(_script)

import fnl_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1


class Toplevel1:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        top.geometry("644x428+558+242")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("SSH Tooler")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.517, rely=0.117, relheight=0.832
                , relwidth=0.425)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        data = fn.web_drivings
        M__ = self.txtOutput = tk.Text(self.Frame1)
        dta = data
        print(dta)
        # if str(dta) != str("<function web_drivings at"):
        #     M__.insert(END, data)
        # M__.insert(END, "")
         
        self.txtOutput.place(relx=0.036, rely=0.028, relheight=0.938
                , relwidth=0.927)
        self.txtOutput.configure(background="white")
        self.txtOutput.configure(font="TkTextFont")
        self.txtOutput.configure(foreground="black")
        self.txtOutput.configure(highlightbackground="#d9d9d9")
        self.txtOutput.configure(highlightcolor="black")
        self.txtOutput.configure(insertbackground="black")
        self.txtOutput.configure(selectbackground="#c4c4c4")
        self.txtOutput.configure(selectforeground="black")
        self.txtOutput.configure(wrap="word")

        self.Frame1_1 = tk.Frame(self.top)
        self.Frame1_1.place(relx=0.05, rely=0.117, relheight=0.834
                , relwidth=0.425)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")
        self.Frame1_1.configure(background="#d9d9d9")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")

        self.Label2 = tk.Label(self.Frame1_1)
        self.Label2.place(relx=0.077, rely=0.112, height=21, width=69)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='right')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(justify='right')
        self.Label2.configure(text='''Username:''')

        username__ = self.username = tk.Entry(self.Frame1_1)
        self.username.place(relx=0.401, rely=0.112, height=20, relwidth=0.489)
        self.username.configure(background="white")
        self.username.configure(disabledforeground="#a3a3a3")
        self.username.configure(font="TkFixedFont")
        self.username.configure(foreground="#000000")
        self.username.configure(insertbackground="black")

        password__ = self.password = tk.Entry(self.Frame1_1, show='*')
        self.password.place(relx=0.401, rely=0.196, height=20, relwidth=0.489)
        self.password.configure(background="white")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(font="TkFixedFont")
        self.password.configure(foreground="#000000")
        self.password.configure(insertbackground="black")

        self.Label3 = tk.Label(self.Frame1_1)
        self.Label3.place(relx=0.077, rely=0.196, height=21, width=69)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='right')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(justify='right')
        self.Label3.configure(text='''Password:''')

        _style_code()
        self.TSeparator1 = ttk.Separator(self.Frame1_1)
        self.TSeparator1.place(relx=-0.066, rely=0.482,  relwidth=1.12)
        
        usernm = username__
        passwd = password__
        btnD = partial(fn.cred, usernm, passwd)
        self.btnLogin = tk.Button(self.Frame1_1, command=btnD)
        self.btnLogin.place(relx=0.314, rely=0.336, height=24, width=87)
        self.btnLogin.configure(activebackground="beige")
        self.btnLogin.configure(activeforeground="black")
        self.btnLogin.configure(background="#d9d9d9")
        self.btnLogin.configure(compound='left')
        self.btnLogin.configure(disabledforeground="#a3a3a3")
        self.btnLogin.configure(foreground="#000000")
        self.btnLogin.configure(highlightbackground="#d9d9d9")
        self.btnLogin.configure(highlightcolor="black")
        self.btnLogin.configure(pady="0")
        self.btnLogin.configure(text='''Login''')

        self.Label4 = tk.Label(self.Frame1_1)
        self.Label4.place(relx=0.391, rely=0.616, height=41, width=2)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Copy Driver ->''')

        driver = self.btnDriver = tk.Button(self.Frame1_1, command=fn.copy_driver)
        # print(driver)
        # drM = ".!frame2.!button2"
        if (fn.copy_driver) != (True):
            messagebox.showerror(title=None, message="Driver installation error !")
        else:
            messagebox.showinfo(title=None, message="Driver installed !")

        self.btnDriver.place(relx=0.438, rely=0.644, height=24, width=57)
        self.btnDriver.configure(activebackground="beige")
        self.btnDriver.configure(activeforeground="black")
        self.btnDriver.configure(background="#d9d9d9")
        self.btnDriver.configure(compound='left')
        self.btnDriver.configure(disabledforeground="#a3a3a3")
        self.btnDriver.configure(foreground="#000000")
        self.btnDriver.configure(highlightbackground="#d9d9d9")
        self.btnDriver.configure(highlightcolor="black")
        self.btnDriver.configure(pady="0")
        self.btnDriver.configure(text='''Driver''')

        self.Label5 = tk.Label(self.Frame1_1)
        self.Label5.place(relx=0.073, rely=0.644, height=21, width=84)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(justify='right')
        self.Label5.configure(text='''Copy Driver ->''')

        self.Label6 = tk.Label(self.Frame1_1)
        self.Label6.place(relx=0.073, rely=0.56, height=21, width=84)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(justify='right')
        self.Label6.configure(text='''Save File ->''')
      
        sfM = fn.saveFile(data)
        saveFileM = self.btnSave = tk.Button(self.Frame1_1, command=sfM)
        self.btnSave.place(relx=0.438, rely=0.56, height=24, width=57)
        self.btnSave.configure(activebackground="beige")
        self.btnSave.configure(activeforeground="black")
        self.btnSave.configure(background="#d9d9d9")
        self.btnSave.configure(compound='left')
        self.btnSave.configure(disabledforeground="#a3a3a3")
        self.btnSave.configure(foreground="#000000")
        self.btnSave.configure(highlightbackground="#d9d9d9")
        self.btnSave.configure(highlightcolor="black")
        self.btnSave.configure(pady="0")
        self.btnSave.configure(text='''Save''')

        self.btnReset = tk.Button(self.Frame1_1)
        self.btnReset.place(relx=0.292, rely=0.84, height=24, width=107)
        self.btnReset.configure(activebackground="beige")
        self.btnReset.configure(activeforeground="black")
        self.btnReset.configure(background="#d9d9d9")
        self.btnReset.configure(compound='left')
        self.btnReset.configure(disabledforeground="#a3a3a3")
        self.btnReset.configure(foreground="#000000")
        self.btnReset.configure(highlightbackground="#d9d9d9")
        self.btnReset.configure(highlightcolor="black")
        self.btnReset.configure(pady="0")
        self.btnReset.configure(text='''Reset All''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.401, rely=0.023, height=31, width=122)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''SSH Tooler''')


def start_up():
    fnl_support.main()

if __name__ == '__main__':
    fnl_support.main()




