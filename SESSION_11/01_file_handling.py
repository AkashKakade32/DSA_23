import sys

try:
    f_handle = open("abc.txt", "r")
except:
    exe_name, exe_data, exe_tb = sys.exe_info()
    print(exe_name.__name__, exe_data)
    print("Existing Application...")
    sys.exit()

    