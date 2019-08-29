# takes the formatted file from Sedimend and organises it and adds the depth
# of each sample.
# bigtable takes a list of file paths and opens the .csv file, adds a
# depth measurement and then adds that table to a larger table.
# Essentially it joins all the tables together, ensuring the depth of
# sample is marked for each case.
import os
import numpy as np
import pandas as pd
import RetrieveSediment as sfg


def namecol(table, depth):
    dftable = pd.DataFrame(table)
    dftable["DepthMeasured"] = depth
    return dftable


def tableDepth(tablePath):
    filename = os.path.basename(tablePath)
    depth = filename[6:8]
    return depth


def SedClassif(table):
    print("table *****", table)
    def categorize(c):
        if c.iloc[2] > 2000:
            return 'Gravel'
        if c.iloc[2] <= 2000 & c.iloc[2] > 62.5:
            return 'Sand'
        if c.iloc[2] <= 62.5 & c.iloc[2] > 3.9:
            return 'Silt'
        if c.iloc[2] <= 3.9:
            return 'Clat'
    #
    #sedCategories = [
    #    (grainSize > 2000),
    #    (grainSize <= 2000) & (grainSize > 62.5),
    #    (grainSize <= 62.5) & (grainSize > 3.9),
    # #   (grainSize <= 3.9)
    #]
    #sedCatNames = [
    #    "Gravel",
    #    "Sand",
    #    "Silt",
    #    "Clay"
    #]
    #table["SedClass"] = np.select(sedCategories,
    #                              sedCatNames,
    #                              default="")
    table['SedClass'] = table.apply(categorize, axis = 1)
    return table


def bigtable(tablepathlist):  # takes a list of filepaths as input then
    sedData = pd.DataFrame()  # formats and appends to sedData and
    for i in tablepathlist:   # and returns sedData
        depth = tableDepth(i)
        table = pd.read_csv(i)
        table_w_depth = namecol(table, depth)
        table_complete = SedClassif(table_w_depth)
        sedData = pd.concat([sedData, table_complete], ignore_index=True)
    print(sedData)
    return sedData
