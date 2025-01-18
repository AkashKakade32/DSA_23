'''

@author : Akash Kakade
@goal : 
    a) accept mass of two objects in kgs, distance between them in meters,
    b) do a validation check
    c) compute gravitational force of attraction
    d) print the result

    
'''

import sys

def main() -> None:
    '''
    
    @input None
    @output None
    @goal driver function of application

    
    '''

    m1 = float(input("Enter Mass Of Object 1 in Kgs : "))
    m2 = float(input("Enter Mass Of Object 2 in Kgs : "))
    r = float(input("Enter the distance between the two objects in meters : "))

    try:
        F = computeGravitionalForce(m1, m2, r)
    except:
        exc_name, exc_date, exc_tb = sys.exc_info()
        print(exc_name.__name__, exc_date, sep=':')
        sys.exit(-1)
    print(f'Force of attraction is :{F} Newton')
    sys.exit(-1)

main()