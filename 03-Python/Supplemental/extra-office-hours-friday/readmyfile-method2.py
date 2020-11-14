# *********************************************
#  Method 2: Improve reading of CSV files using the CSV module
# *********************************************

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Then, we import our module for reading CSV files
import csv

#let's create our path to the location of our CSV file
csvfilepath = os.path.join('', 'Data', 'harry_potter.csv')

# Method 2: Improved Reading using CSV module

with open(csvfilepath) as thisismyfile:
    # CSV reader specifies delimiter and variable that holds contents
    myfilecontent = csv.reader(thisismyfile, delimiter=',')
    # csv.reader will return an "iterator", like a cursor, a pointer
    # that can move from row to row
    # "iterable" - list, tuples - collections

    # print("What type are you?",type(myFile))
    # print(myFile)

    # Using the next() method, we will move our cursor to the first line in our CSV
    myExcelHeader = next(myfilecontent)
    print(myExcelHeader)
    print('\n')
    # # Read each row of data after the header
    for row in myfilecontent:
        # Every row will be a list
        print(row)
        #and we can even do calculations with our data
        commission = int(row[6]) * 0.10

        #we can now use "interpolation" and display info to our user...
        print(f'Here is 10% of our revenue : {commission:,.2f}')
        print('\n')

