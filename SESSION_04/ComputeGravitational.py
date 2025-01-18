'''

@author : Akash Kakade
@goal : 
    a) accept mass of two objects in kgs, distance between them in meters,
    b) do a validation check
    c) compute gravitational force of attraction
    d) print the result

    
'''

import sys

def computeGravitionalForce(m1:float, m2:float, r:float) -> float:
    '''

    m1: mass of m1 object
    m2: mass of m2 object
    r: distace betwenn two objects

    Output: Gravitional force of attraction
    '''

    if(type(m1) != int and type(m1) != float):
        raise TypeError('Bad Type For Mass Of Object 1')
    if(type(m2) != int and type(m2) != float):
        raise TypeError('Bad Type For Mass Of Object 2')
    if(type(r) != int and type(r) != float):
        raise TypeError('Bad Type For Distance')
    if(m1<=0.0 or m2<=0.0 or r<=0.0):
        raise ValueError('Magnitude of Mass and Distance Must Be Positive')
    
    G = 6.67 * (10**-11)
    F = (G*m1*m2)/(r*r)
    return F



def main() -> None:
    '''
    
    @input None
    @output None
    @goal driver function of application

    
    '''

    try:
        m1 = float(input("Enter Mass Of Object 1 in Kgs : "))
        m2 = float(input("Enter Mass Of Object 2 in Kgs : "))
        r = float(input("Enter the distance between the two objects in meters : "))

        F = computeGravitionalForce(m1, m2, r)
        
        print(f'Force of attraction is :{F} Newton')
    except:
        exc_name, exc_date, exc_tb = sys.exc_info()
        print(exc_name.__name__, exc_date, sep=':')
        sys.exit(-1)
    
    sys.exit(0)

main()