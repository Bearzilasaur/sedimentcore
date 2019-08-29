# sedimentcore

This is a bunch of python scripts for the processing and graphical display of the output of Beckham Coulter laser diffraction particle sizer. It is specifically designed to assemble a complete dataset for a sediment core by stripping the raw data out of the Beckham Coulter output for each sediment sample, and then combining the raw datas into a dataset for the whole sediment core. 

# How to use

 - The primary use of this package is to tidy and sort all of the relevant sediment output data into a table for visualisation with the R studio package ggplot2
 - Run the Sedimend module from a python interpreter, which will call the other modules for you.
 - Then select the appropriate folder or files from the file browser, and then choose an output forlder for the table to be stored in.
 - Lastly, open up RStudio and run the SedProcessing r script to select the newly created table and plot it using ggplot2. This will prompt you to select a folder in which to save the two output images in both .svg and .png.
