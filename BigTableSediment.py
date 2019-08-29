

import os
from tkinter import filedialog
import RetrieveSediment
import TidySediment
import numpy as np
import pandas as pd


def synthesizeSedData(store=True, clean=False):
    files = RetrieveSediment.getsedspaths()  # list of paths to each sedtable file
    bigsedtable = TidySediment.bigtable(files)  # a large combined table of all data
    if clean is True:
        del bigsedtable[bigsedtable.icol[:,4]]
    if store is True:
        savepath = filedialog.asksaveasfilename(
            defaultextension=".csv")
        bigsedtable.to_csv(savepath, index=True, header=True)
    else:
        return bigsedtable
