# sedimentcore

This is a bunch of python scripts for the processing and graphical display of the output of Beckham Coulter laser diffraction particle sizer. It is specifically designed to assemble a complete dataset for a sediment core by stripping the raw data out of the Beckham Coulter output for each sediment sample, and then combining the raw datas into a dataset for the whole sediment core. 

# How to use

 - The primary use of this package is to tidy and sort all of the relevant sediment output data into a table for visualisation with the R studio package ggplot2
 - Run the Sedimend module from a python interpreter, which will call the other modules for you.
 - Then select the appropriate folder or files from the file browser, and then choose an output forlder for the table to be stored in.
 - Lastly, open up RStudio and run the SedProcessing r script to select the newly created table and plot it using ggplot2. This will prompt you to select a folder in which to save the two output images in both .svg and .png.

This can be broken down into 3 steps:

  1. Cleaning raw .csv files.
  2. Combining cleaned .csv files into one table.
  3. Graphing the data.

## Cleaning raw .csv files

This step is performed by calling the simplify function from the Sedimend module:

```
  import Sedimend

  Sedimend.simplif()
```

This will prompt the user to select a folder which contains all of the raw .csv files from the Beckham Coulter laser diff. particle sizer. The user is then prompted to select (or create and then select) a folder for the output cleaned .csv files which contain only the raw data.

## Combining cleaned data

The next step is to combine the cleaned data into one large table. The synthesizeSedData method from the BigTableSediment module.
```
import BigTableSediment as bts

bts.synthesizeSedData()
```

### Options

The synthesizeSedData module comes with two options as follows:

```synthesizeSedData(store=True, clean=False)
```
The default setting store=True prompts the user to save the combined table as a .csv file. Setting this to store=False simply returns the combined data as a pandas DataFrame object. The clean=False setting is _deprecated_. 

## Graphing the Data

Graphing of the proportional contribution of sediment is carried out by R scripts located in the SedimentGraph directory. The method for this step is as follows:

1. Load the SedimentGraphFunction.R script into RStudio
	- Dependencies for packrat can be found in packrat/bundles
2. Load the big table from the last section into RStudio.
3. Call the sedGraph() function from SedGraphFunction.R on the bigtable.

```Example
sedGraph(table)
```

### Options

There are several options available for the sedGraph function:

```Options
sedGraph(table, format=TRUE, greys=TRUE, savefile=FALSE)

Format=TRUE:
	This takes the table input and classifies each row into Clay, Silt and Sand based upon the sediment grain size for the bin in that row. Does not happen if set to FALSE

greys=TRUE:
	Sets the colour of the output graph image files to greyscale. Set to FALSE to return colour graphs.

savefile=FALSE:
	This prevents saving the graphs to file by default and instead returns a ggplot2 plot as the output of the function. Set to TRUE to save graphs straight to file. However it is recommended that you do not do this, so that you can customize the resulting graphs. 
```

# TODO

The next step is to integrate all of these into a single callable function which will then let the user determine where the function ends, such as after raw extraction, big table creation, or simply return a graph. 

# Note
There is currently an issue where .DS_Store files or any dotfiles in the target directory with the raw Beckham Coulter files can break the function. It is important to make sure that the folder is clean, I am working on an implementation where the user will select the ***Files*** rather than the ***folder*** which the files reside in. 
