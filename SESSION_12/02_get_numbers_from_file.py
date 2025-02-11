import sys

def get_list_of_numbers_from_file(path_name:str)->[int]:
    #Type Checking

    if type(path_name) != str:
        print("Invalid Path Name. Exiting the app")
        sys.exit()

    try:
        f_handle = open(path_name, "r")
    except:
        print("Error opening the file. Exiting the app")
        f_handle.close()
        sys.exit()

    #Take and empty list and add the data in the empty list
    L = []

    for line in f_handle:
        line = line.strip()
        try:
            n = int(line)
            L.append(n)
        except:
            print("Bad Integer Format on file data. Exiting the app")
            sys.exit()
            f_handle.close()
    
    f_handle.close()
    
    return L


lst = get_list_of_numbers_from_file('Numbers.txt')
print(lst)
