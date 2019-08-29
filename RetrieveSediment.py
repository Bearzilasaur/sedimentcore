# Collects filenames for formatted files within a user selected folder
# and returns as a list.
# Author: Mitchell Baum
# ======================================================================

import tkinter as tk
from tkinter import filedialog
import os


def folderselect():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    return folder


def filelist(folderpath, path=True):
    files = []
    for i in os.listdir(folderpath):
        if path is not True:
            files.append(i)
        else:
            files.append(folderpath + '/' + i)
    return files


def getsedspaths():
    folder = folderselect()
    files = filelist(folder)
    return files
