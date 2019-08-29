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
    table["SedClass"] = ""
    grainSize = table.iloc[:, 2]
    print("table *****", table)

    # detailSedClass = {"VF Sand": 125, # More detailed classify for
    #                  "F Sand": 250,   # Sandy sediments
    #                  "M Sand": 500,
    #                  "C Sand": 1000,
    #                  "VC Sand": 2000
    #                  }
    sedCategories = [
        (grainSize <= 3.9),
        (grainSize <= 62.5) & (grainSize > 3.9),
        (grainSize <= 2000) & (grainSize > 62.5),
        (grainSize > 2000)
    ]
    sedCatNames = [
        "Clay",
        "Silt",
        "Sand",
        "Gravel"
    ]
    table["SedClass"] = np.select(sedCategories,
                                  sedCatNames,
                                  default="")
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
