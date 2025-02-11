def geh(is_tb=False, should_exit=False, exit_msg=None):
    from sys import exc_info,exit
    exc_name, exc_data, exc_tb = exc_info()
    print(exc_name.__name__, exc_data, sep=":")
    if is_tb == True:
        from traceback import print_tb
        print_tb(exc_tb)
    if should_exit == True:
        if exit_msg is not None:
            print(exit_msg)
        exit(-1)
