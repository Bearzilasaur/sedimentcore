# Selects and saves the raw data from the sediment grain size analyzer
# into separate files in a user specified folder.


import pandas as pd
import tkinter
from tkinter import filedialog
import xlrd
import RetrieveSediment


def rawdat(sedfilepath):
    print(sedfilepath)
    df = pd.read_csv(sedfilepath,
                     skiprows=74,
                     header=None,
                     names=['BinMaxSedDiameter',
                            'SedProp'],
                            engine='python')
    df2 = df.dropna()
    return df2


def simplify():
    paths = RetrieveSediment.getsedspaths()
    root = tkinter.Tk()
    root.withdraw()
    save_file = filedialog.askdirectory(title='Select save folder')
    for i in paths:
        try:
            df = pd.DataFrame(rawdat(i))
            _, filename = i.rsplit('/', 1)
            write_path = save_file + '/' + filename
            print(write_path)
            df.to_csv(write_path)
        except IsADirectoryError:
            pass
