import sys

path_name = 'Numbers.txt'

try:
    f_handle = open(path_name, 'r')
except:
    print("Error in opening a file")
    sys.exit()


# Read file line by line
# Remove leading and traling white spaces
# Covert a string into an integer
# If there is exception in format conversion 
# Exception will be thrown


for line in f_handle:
    print(line, type(line))
    line = line.strip()
    try:
        n = int(line)
    except:
        print("Error in Converting the string. Exiting the application")
        f_handle.close()
        sys.exit()
    print(n, type(n))

# relese the file handler
f_handle.close()




# for line in f_handle:
#     line = line.strip()
#     try:
#         n = int(line)
#         print(n)
#     except:
#         print("Invalid Input File. Exiting the application")
#         sys.exit()