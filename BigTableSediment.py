

import os
from tkinter import *
import sedfilegrab
from sedfilegrab import *
import sedfilecleanandjoin
from sedfilecleanandjoin import *
import numpy as np
import pandas as pd


def synthesizeSedData(store=True, clean=False):
    files = getsedspaths()  # list of paths to each sedtable file
    bigsedtable = bigtable(files)  # a large combined table of all data
    if clean is True:
        del bigsedtable[bigsedtable.columns[4]]
    if store is True:
        savepath = tk.filedialog.asksaveasfilename(
            defaultextension=".csv")
        bigsedtable.to_csv(savepath, index=None, header=True)
    else:
        return bigsedtable
