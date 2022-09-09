from func import *
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def sm_cred():
    uname = input('Enter a username: ')
    passW = input('Enter a password: ')

    # if uname == "nk" and passW == "nk":
    #     Gui()
    # print("\ncheck cridentials! \n")
    Gui()
    # sm_cred()

if is_admin():
    sm_cred()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sm_cred()
