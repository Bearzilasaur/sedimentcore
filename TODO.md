# TODO

List of steps to take to make better code and store information better.

## Short Term

- [x] Use python to strip raw data out of output csv files
- [ ] Compress all functions into one file, and re-write it so that you only call one function.
  - i.e. only on def and only one .py
  - [ ] Save output option
  - [ ] Graph output option
- [ ] Collect the sample depth from the csv file
  - [ ] Create second/paired table with the metadata and use that to capture the sample depth and core name

## Long Term

- [ ] Restructure the conversion around Cores and Samples as classes
- [ ] Build an SQLite interpreter object which can be used to parse in/out the data from the SQLite database file.
- [ ] Extend these such that the other information stored by the sediment grain size analyzer is stored in another table in SQLite.
  - i.e. all of the statistics for each sample (e.g. Phi, &Phi;)
  - Use the core name as the keyword/identifier.
