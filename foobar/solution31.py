seen = {}

def findsteps(level, stepsleft, current):
    debug=0
    found=0
    savecurrent = current

    key = str(level) + ':' + str(stepsleft)

    donottake=0

    if key in seen:
        return seen[key]

    if debug:
        print("at level %i with %i steps left with path %s" % (level,stepsleft, current))
    if level==stepsleft:
        # ok, must be at least two steps so this is good
        found=found+1
        current = current + str(level)
        if debug:
            print('               ********  ', current, ' was the path found')
        donottake=1
    elif level <=1 or stepsleft <0:
        # impossible, give up
        return 0
    elif level > stepsleft:
        if debug:
            print('keep going, but do not take the step because level %i > steps %i, so the step would overshoot' % (level, stepsleft))
        donottake=1

    # ok now we have two options
    # take a step, first not take a step
    # so we should return the sum of these two options
 
    if not donottake:
        found = findsteps(level-1, stepsleft-level, savecurrent + str(level))
    notake =    findsteps(level-1, stepsleft,       savecurrent )

    seen[key] = found+notake
    return(found+notake)



def solution(n):
    #print("\n")
    #print "solving for ", n
    # at 1 = 0: impossible
    # at 2 = 0: impossible
    # at 3 = 1: one way: 2, 1
    # at 4 = 1: one way: 3, 1
    # at 5 = 2: 41, or 32
    # at 6 = 3: 51, 42, 321
    # at 7 = 4: 61, 52, 43, 421,  
    # at 8 = 5: 71, 62, 53, 521, 431
    # at 9 = 7: 81, 72, 63, 621, 54, 531, 432
    # at 10 = 9: 81, 72, 63, 621, 54, 531, 432
    # next 5 are: 11, 14, 17, 21, 26
    # at 200 = 487067745
    # ** n will be between 3 and 200 **
  
    # Params
    #  level
    #  number of steps left
    #  tracking of current solution
    ways = findsteps(n-1, n, '') 
    return ways

