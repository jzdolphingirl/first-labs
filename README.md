# Cemetery Lab Java Program

This repository now contains a Java implementation of the cemetery database lab.

How to run:

1. Open a terminal in this folder.
2. Compile:
   javac CemeteryLab.java
3. Run:
   java CemeteryLab

The program reads the cemetery data from `cemetery_orig.txt` and supports:
- search by last name
- search by street name or choose from a generated street list
- sorting by name, burial date, age at death, or address
- summary statistics: average age at death, highest mortality year, and oldest age at death

The data is parsed from the historical burial list, including inconsistent ages and address formats.

