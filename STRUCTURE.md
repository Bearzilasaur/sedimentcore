# Structure of the Package

This package will be structured so that the ***Retrieval***, _**Data Wrangling**_ and _**Sythesis**_, ***Graphing***, and ***SQLite*** functions are stored in separate modules.

## Retrieval

This module will define a file select window object with methods which:


- [ ] Display a popup window which users can navigate the filesystem to select an appropriate folder within which the files are stored.
- [ ] Create a list with the filepaths of every *.csv file in that folder
- [ ] Display another window where the user can select an output folder for the raw data files, the synthesized raw data.

Additionally this class will be able to interface with user chosen SQLite files:

- [ ] User selects the appropriate SQLite .db file. 

## Data Wrangling and Synthesis

The output from the sediment analyzer is not typical of most .csv files. This module will retrieve the relevant data from the specified files and:

- [ ] Extract relevant raw data to a formatted pandas DataFrame
- [ ] Extract the sample depth and sample name metadata and attach that to DataFrame.metadata

```example
df.metadata = dict{'CoreName': 'CoreExample',
                   'SampleDepth': '10'}
```

Which can then be called with:

```ex2
df.metadata['CoreName']

CoreExample
```

### Sythensis

Once the data has been formatted, the DataFrame will be appended to a larger frame so that the output of this module is a large DataFrame which contains the formatted data from all sediment samples within a core.
- [ ] Synthesize the sample DataFrames into an aggregated core DataFrame.


## Graphing With Matlplotlib

Currently graphing is managed by an R script with ***ggplot2***. This can be implemented with the python library ***Rpy*** or something similar. However it would be good to implement a python module which uses ***Matplotlib*** to graph a proportional sediment distribution for the data as an option for the script. This module should:
- [ ] This section should create a plot where y axis = sample depth and x axis = proportional contribution of sediment classes.
  - [ ] The origin of the graph should start with the maximum depth of the core, such that the top of the graph is the top of the core.

## SQLite

Although ***SQLite*** is not appropriate for multiuser systems, the database files are readily transferable using usb as they are a single self contained file. There is no need to export to a .csv or other data format. Additionally, there ***SHOULD*** only be one person working on the file at one time _(me)_. This module should prompt the user to select an ***SQLite*** database file _(.db)_ and then use the ***PySQLite*** package to connect and then append the core to the database. 
- [ ] Popup window for user to select database file.
- [ ] Create a connection to the database file
- [ ] Append to the appropriate table
  - [ ] How do we get the user to select the appropriate table?

# Final Product

This set of modules should allow easy translation of the sediment datasets published by the Laser Diffraction Particle Sizer to .csv files and SQL tables. 

## Extras

- [ ] Write documentation for the package
- [ ] Add docstrings to each module
- [ ] Create a 'Sediment Sample' class which contains methods for determining the calculated statistics from the Laser Diff
  - [ ] create class variables which store the already calculated statistics (e.g. &phi;)
    - This can be used to create vectors of sample statistics for graphing etc. 
- [ ] Create a 'Core' class which contains a dict(?) of sampleName: sampleObject. This core can then contain methods for core-wide analysis. 
