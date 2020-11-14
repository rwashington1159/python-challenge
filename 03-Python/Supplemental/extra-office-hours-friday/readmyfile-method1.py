# *********************************************
#  Method 1: Plain Reading of CSV files
# *********************************************

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# let's create our path to the location of our CSV file
hereismycsvpath = os.path.join('', 'Data', 'harry_potter.csv')

# Plain Reading of CSV files
#   It is good practice to use the with keyword when dealing with file objects. The #   advantage is that the file is properly closed after its suite finishes, even if #   an exception is raised at some point.


# get a reference to my file, and call the reference "myfile"
with open(hereismycsvpath, 'r') as myfile:
    #read the contents of my file, and assign that to my variable "getmemyrows"
    getmemyrows = myfile.read()

    # print the content of the 'getmemyrows' variable
    # (this should contain all lines from CSV)
    print(getmemyrows)

    # show me the type for the variable 'getmemyrows'
    print('\n') #THIS will print a new empty line on the console (COSMETIC)
    print('')  # THIS will print a new empty line on the console (COSMETIC) - same as line above
    print(f'The type for my variable "getmemyrows" at line(19) is: ', type(
        getmemyrows))
    print('')

    #
    # **************************
    # Understanding why is harder to work with a returned type of 'str'
    # **************************
    #

    # let's try to go over our content and find specifics about our content.

    # FIRST: let's get rid of the '\n' return character -
    #
    # this will return a LIST, where each line will be an item on our list
    geteachrow = getmemyrows.split('\n')

    print('')
    print(f'The type for my variable "geteachrow" at line (43) is :', type(geteachrow))
    print('')

    #let's print our variable, for us to see that indeed the return type is a 'list'
    print('>>>>>>>> here is my list, now sitting at "geteachrow" variable:\n ')
    print(geteachrow)
    print('*'*100)

    # SECOND: let's iterate over our 'list' and now get access to our items
    print('\n')
    for row in geteachrow:
        print(row.split(',')[0])
        # print(    int( row.split(',')[6] ) * 0.10    )
