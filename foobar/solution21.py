import numpy as np
from fractions import Fraction


def solution(pegs):
    # ok just thinking out loud
    # so for 4, 30, 50
    # we are solving for X, such that X <= 30-4
    # that means there's a Y, such that Y = 30-X-4
    # e.g. if X was 12, Y = 30-16 = 14
    # then lastly we have Z, such that 50-30-Y = Z, but Z must = X/2
    # so since Y was 14, Z =6
    
    # say pegs was 4, 30, 50
    # X = b - a - Y,  X + Y = b - a  (X + Y = 26)
    # Y = c - b - Z,  Y + Z = c - b  (Y + Z = 20)
    # X = Z*2,    X- 2Z = 0
    # solution would be X = 12, Y = 14, Z = 6
 
    # OOOOOH BUT this only solves for 3, problem  said at least 2 no more than 20    
    # (a,b,c) = pegs
    # diff1 = b-a
    # diff2 = c-b
    #a = np.array([[1,1,0], [0,1,1], [1,0,-2]])
    #b = np.array([diff1, diff2, 0])
    
    # Rewrite to handle > 1 dimensions
    list1 = []
    list2 = []
    for i in range(len(pegs)):
        # e.g.
        # need 1, 1, 0, 0, 0
        # need 0, 1, 1, 0, 0
        # need 0, 0, 1, 1, 0
        # need 0, 0, 0, 1, 1
        # need 1, 0, 0, 0, -2

        initlist = [0 for j in range(len(pegs))]
        if i < len(pegs)-1:
            initlist[i] = 1
            initlist[i+1] = 1
            list2.append(pegs[i+1]-pegs[i])
        else:
            initlist[0] = 1
            initlist[i] = -2
            list2.append(0)

        list1.append(initlist)

    a = np.array(list1)
    b = np.array(list2)

    x = np.linalg.solve(a, b)

    # problem said radius >=1
    if any(i <1 for i in x):
        return (-1,-1)

    # curse python's floating pt errors
    #(n, d) = x[0].as_integer_ratio()
    #x[0] = '1.2758620689'
    #x[0] = '72.4117647058'

    # would still cause floating point miscalculations without limiting denominator
    frac = Fraction(str(x[0])).limit_denominator(max_denominator=10000)
    #frac = Fraction(str(x[0]))

    n = frac.numerator
    d = frac.denominator

    if n > 0 and n >=d:
        return (n,d)
    else:
        return (-1,-1)



