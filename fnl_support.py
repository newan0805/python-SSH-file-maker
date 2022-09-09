import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import fnl

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = fnl.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    fnl.start_up()