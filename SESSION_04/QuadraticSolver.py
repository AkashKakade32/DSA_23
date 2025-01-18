'''
@Author : Akash Avinash Kakade
@Date : 12/01/2025
@Goal:
    1) To accept the coefficient of quadratic equation
    2) TO check if real roots are possible
    3) If yes then compute and return

'''

import sys

def q_solver(a:float, b:float, c:float) -> tuple[float]:
    '''
    a: CF of x^2, CF of x, c: Constant of equation
    '''

    if a==0.0:
        raise ValueError("CF of X^2 cannot be 0")
    if b**2 < 4*a*c:
        raise ValueError("Equation do not have real roots")
    
    r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    T = (r1, r2)
    return T

def main() -> None:
    try:
        a = float(input("Enter CF of x^2: "))
        b = float(input("Enter CHF of X: "))
        c = float(input("Enter constant of eqn: "))
        r1, r2 = q_solver(a,b,c)
        print(f'Root 1: {r1}, Root 2: {r2}')
    except:
        exc_name, exc_date, exc_tb = sys.exc_info()
        print(exc_name.__name__, exc_date, sep=':')
        sys.exit(-1)
    sys.exit(0)

main()
